import mysql.connector
import sys
import os
from tkinter import messagebox
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client
import json
from tkinter import messagebox
from datetime import datetime,date

# Obtém a pasta onde o arquivo está
caminho_atual = os.path.abspath(__file__)
pasta_atual = os.path.dirname(caminho_atual)
pasta_pai = os.path.dirname(pasta_atual)
# Caminho dinâmico para a pasta "Front End" e "Docs"
frontend_path = os.path.join(pasta_pai, "Front End")
sys.path.append(frontend_path)
docs_path = os.path.join(pasta_pai, "Docs")
sys.path.append(docs_path)

from changewindows import open_gui

#----------------- Classe Documento -------------
class Document:
    def __init__(self, name, path, deadline="",week_day=""):
        self.name = name
        self.path = path
        self.deadline = deadline
        self.week_day = week_day

#----------------- Conexão MySQL ----------------

def connection():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sny-301mv",
        database="todo_app"
    )
    return conexao, conexao.cursor()

"""
users -> id_user, username, e_mail, phone, userpassword, image, retrieve_code
documents -> id_docs, id_user, doc_name, deadline
"""

#-------------------------------------------------

def salvar_dados(usuario):
    caminho_atual = os.path.abspath(__file__)
    pasta_atual = os.path.dirname(caminho_atual)
    pasta_pai = os.path.dirname(pasta_atual)
    docs_path = os.path.join(pasta_pai, "Docs")
    """Salva as informações do usuário em um arquivo JSON."""
    dados = {
        "username": usuario[0],
        "user_rank": usuario[2],
        "last_folder": os.path.join(docs_path,usuario[0],"trash"),
        "user_id":usuario[3]
    }
    
    with open("dados_login.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def login(email,password,window):
    conexao, cursor = connection()
    query = "SELECT username, userpassword, user_rank,id_user FROM users WHERE e_mail = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user:
        stored_password = user[1]  
        if password == stored_password:
            salvar_dados(user)
            mkdir(user[0])
            open_gui(window,1)
        else:
            messagebox.showerror("Erro", "Senha incorreta!")
        turn_off(cursor,conexao)
    else:
        messagebox.showerror("Erro", "Email incorreto!")
        turn_off(cursor,conexao)

def mkdir(username):
    user_folder = os.path.join(docs_path, username)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
        os.makedirs(os.path.join(user_folder,"trash"))

def sign_up(name,email,phone,password,window,rank=1):
    conexao, cursor = connection()
    query = "SELECT * FROM users WHERE e_mail = %s"
    cursor.execute(query, (email,))
    existing_user = cursor.fetchone() # Verifica se o usuario ja existe

    if existing_user:
        messagebox.showerror("Erro", "Usuario já existe!")
        return
    
    # Inserir novo usuário no banco de dados
    insert_query = """
    INSERT INTO users (username, e_mail, phone, userpassword,retrieve_code,user_rank)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (name, email, phone, password, r.randint(999999999,1999999999), rank))
    conexao.commit()
    messagebox.showinfo("Sucesso","Usuario cadastrado com sucesso!")
    turn_off(cursor,conexao)
    open_gui(window,0)

def forget_password(user_code,new_password,new_password2,window):
    conexao, cursor = connection()

    query = "SELECT retrieve_code,id_user FROM users WHERE retrieve_code = %s"
    cursor.execute(query, (user_code,))
    user = cursor.fetchone()

    if not user:
        messagebox.showerror("Erro", "Código de recuperação inválido.")
        turn_off(cursor, conexao)
        return
    if new_password != new_password2:
        messagebox.showerror("Erro", "As senhas informadas divergem.")
        turn_off(cursor, conexao)
        return
    if len(new_password) < 6:
        messagebox.showerror("Erro", "A senha precisa ser maior que 6 dígitos")
        turn_off(cursor, conexao)
        return

    # Atualizar os dados do usuário no banco de dados
    insert_query = """
    UPDATE users SET userpassword = %s WHERE id_user = %s
    """
    cursor.execute(insert_query, (new_password,user[1]))
    conexao.commit()

    messagebox.showinfo("Sucesso","Usuario atualizado com sucesso!")

    # Atualiza o código do usuário
    insert_query = """
    UPDATE users SET retrieve_code = %s WHERE id_user = %s
    """
    cursor.execute(insert_query, (r.randint(999999999,1999999999),user[1]))
    conexao.commit()

    turn_off(cursor,conexao)
    open_gui(window,0)

def send_code(email,window):
    if "@" not in email or len(email) < 10:
        messagebox.showerror("Erro", "E-mail digitado está fora do padrão!")
        return

    # Codigo de verificação
    conexao, cursor = connection()
    query = "SELECT retrieve_code FROM users WHERE e_mail = %s"
    cursor.execute(query, (email,))
    retrive_code = cursor.fetchone()

    if not retrive_code:
        messagebox.showerror("Erro", "E-mail não consta no banco de dados")
        turn_off(cursor, conexao)
        return

    query = "SELECT phone FROM users WHERE e_mail = %s"
    cursor.execute(query, (email,))
    phone = cursor.fetchone()

    # Informações do email
    sender_email = "semestretrabalhofecaf@gmail.com"
    receiver_email = email
    password = "upzg yebt cdrg sgzz"

    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Seu código do melhor App da Fecaf!!!"

    body = f"Seu código é: {retrive_code}."
    msg.attach(MIMEText(body, 'plain'))

    # Enviar o e-mail e sms
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        send_smscode(phone,retrive_code)
    except Exception as e:
        messagebox.showerror("Error", "Foi encaminhado apenas no SMS")
    open_gui(window,12)

def send_smscode(phone,retrive_code):
    account_sid = "ACb3b0b4578fe40c2a4231eadaab836e2a"
    auth_token = "36f3aa532241e6957cdfe4e807ab1f3d"

    client = Client(account_sid,auth_token)

    try:
        message = client.messages.create(
            from_="+13802701309",
            to=f"+55{str(phone)}",
            body=f"Seu código é {retrive_code}."
        )

    except TwilioRestException as e:
        print(f"Erro ao enviar SMS: {e}")

def update_rank(code):
    conexao, cursor = connection()
    with open("dados_login.json", "r") as arquivo:
        dados = json.load(arquivo)  # Carrega o JSON como um dicionário

    # Pegando o username (certifique-se de que a chave "username" existe)
    username = dados.get("username", "Usuário não encontrado")

    #Testa se o código informado é igual ao do banco de dados
    if code == 12345:
        query = "UPDATE users SET user_rank = 2 WHERE username = %s"
        cursor.execute(query, (username,))
        conexao.commit()
        dados["user_rank"] = 2
        with open("dados_login.json", "w") as arquivo:
                json.dump(dados, arquivo, indent=4)
                
        messagebox.showinfo("Success","Seu level foi atualizado com sucesso")
    else:
        messagebox.showerror("Error","Código errado")

def turn_off(cursor,conexao):
    cursor.close()
    conexao.close()

def update_information(window,e_mail, name, phone, password):
    conexao, cursor = connection()

    # Lê o id_user do JSON
    with open("dados_login.json", "r") as file:
        dados = json.load(file)
        id_user = dados.get("id_user")
    
    campos = []
    valores = []

    # Validação do e-mail
    if e_mail.strip() and not("Digite" in e_mail):
        if "@" not in e_mail or len(e_mail) < 6:
            messagebox.showerror("Erro", "O e-mail informado é inválido.")
            return
        campos.append("email = %s")
        valores.append(e_mail)

    # Validação do nome
    if name.strip() and not("Digite" in name):
        if len(name) < 3:
            messagebox.showerror("Erro", "Digite um nome com pelo menos 3 caracteres.")
            return
        # Verifica se o nome já existe no banco de dados
        cursor.execute("SELECT id_user FROM users WHERE username = %s AND id_user != %s", (name, id_user))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showerror("Erro", "Este nome de usuário já está em uso. Escolha outro.")
            return

        campos.append("username = %s")
        valores.append(name)

        # Atualiza o nome no JSON
        with open("dados_login.json", "r") as file:
            dados = json.load(file)

        old_username = dados.get("username")
        dados["username"] = name  # Atualiza o nome no JSON

        # Caminhos das pastas
        caminho_atual = os.path.abspath(__file__)
        pasta_atual = os.path.dirname(caminho_atual)
        pasta_pai = os.path.dirname(pasta_atual)
        docs_path = os.path.join(pasta_pai, "Docs")

        old_folder_path = os.path.join(docs_path, old_username)
        new_folder_path = os.path.join(docs_path, name)

        # Renomeia a pasta se ela existir
        if os.path.exists(old_folder_path):
            os.rename(old_folder_path, new_folder_path)

        # Atualiza a referência da pasta no JSON
        dados["last_folder"] = os.path.join(new_folder_path, "trash")

        with open("dados_login.json", "w") as file:
            json.dump(dados, file, indent=4)
        
        # Caminho da pasta onde estão as imagens de perfil
        user_profile_path = os.path.join("..\Front End", "assets", "user_profile")

        # Procura e renomeia os arquivos que contenham o nome antigo
        for filename in os.listdir(user_profile_path):
            if old_username in filename:
                old_file = os.path.join(user_profile_path, filename)
                new_filename = filename.replace(old_username, name)
                new_file = os.path.join(user_profile_path, new_filename)

                # Se o novo nome já existir, remove antes
                if os.path.exists(new_file):
                    os.remove(new_file)

                os.rename(old_file, new_file)
                
    turn_off(cursor,conexao)


    # Validação do telefone
    if phone.strip() and not("Digite" in phone):
        if not phone.isdigit() or len(phone) != 11:
            messagebox.showerror("Erro", "Digite um telefone válido com exatamente 11 dígitos numéricos.")
            return
        campos.append("phone = %s")
        valores.append(phone)

    # Validação da senha
    if password.strip() and not("Digite" in password):
        if len(password) < 6:
            messagebox.showerror("Erro", "A senha deve conter no mínimo 6 caracteres.")
            return
        campos.append("userpassword = %s")
        valores.append(password)

    # Nenhum campo preenchido
    if not campos:
        messagebox.showwarning("Aviso", "Nenhum campo foi preenchido para atualizar.")
        return

    # Montar e executar query
    query = f"UPDATE users SET {', '.join(campos)} WHERE id_user = %s"
    valores.append(id_user)

    cursor.execute(query, tuple(valores))
    conexao.commit()
    open_gui(window,1)

def insert_docs(file_path,deadline):
    conexao, cursor = connection()
    
    # Abrir arquivo JSON corretamente
    with open("dados_login.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    query = (
        "INSERT INTO documents (id_user, doc_name,doc_path, deadline) "
        "VALUES (%s, %s, %s, %s)"
    )

    file_name = os.path.basename(file_path)
    deadline = datetime.strptime(deadline, "%d%m%Y").date()

    cursor.execute(query, (data["user_id"], file_name, file_path, deadline))
    conexao.commit()
    turn_off(cursor,conexao)
    
def delete_docs(file_path):
    conexao, cursor = connection()

    # Abrir arquivo JSON com os dados do usuário
    with open("dados_login.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Preparar e executar o DELETE
    query = (
        "DELETE FROM documents "
        "WHERE id_user = %s AND doc_path = %s"
    )

    cursor.execute(query, (data["user_id"], file_path))
    conexao.commit()

    turn_off(cursor,conexao)
    
def your_files(type,today=date.today()):
    conexao, cursor = connection()

    # Abrir arquivo JSON corretamente
    with open("dados_login.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
                         
    if type == 1:
        query = (
            "SELECT doc_name, doc_path, deadline FROM documents "
            "WHERE id_user = %s ORDER BY id_docs DESC LIMIT 3;"
        )
    elif type == 0:
        query = (
            "SELECT doc_name, doc_path, deadline FROM documents "
            "WHERE id_user = %s ORDER BY deadline LIMIT 6;"
        )
    elif type == 2:
        query = (
            "SELECT doc_name, doc_path, deadline FROM documents "
            "WHERE id_user = %s AND deadline = %s ORDER BY deadline LIMIT 10;"
        )
    elif type == 3:
        query = (
            "SELECT doc_name, doc_path, week_day FROM documents "
            "WHERE id_user = %s "
            "AND DATE(deadline) BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) + 1 DAY) "
            "AND DATE_ADD(CURDATE(), INTERVAL 6 - WEEKDAY(CURDATE()) DAY);"
        )
    elif type == 4:
        query = (
            "SELECT doc_name, doc_path, deadline FROM documents"
            " WHERE deadline BETWEEN %s AND DATE_ADD(%s, INTERVAL 21 DAY)"
            " AND id_user = %s;"
        )

    if type == 4:
        cursor.execute(query, (today, today, data["user_id"]))
    elif type != 2:
        cursor.execute(query, (data["user_id"],))
    elif type == 2:
        cursor.execute(query, (data["user_id"],date.today()))
    resultados = cursor.fetchall()

    if type != 3:
        arquivos = [Document(nome, caminho, deadline) for nome, caminho, deadline in resultados]
    else:
        arquivos = [Document(nome, caminho, week_day=week_day) for nome, caminho, week_day in resultados]

    turn_off(cursor, conexao)
    return arquivos
