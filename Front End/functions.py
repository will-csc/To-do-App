from PIL import Image,ImageTk, ImageDraw, ImageFont, ImageTk
from pathlib import Path
import json
import sys
import os
from tkinter import messagebox, filedialog, Button
from PIL import Image, ImageDraw
import shutil
from changewindows import open_gui
from datetime import date, timedelta

# Obtém a pasta onde o arquivo está
caminho_atual = os.path.abspath(__file__)
pasta_atual = os.path.dirname(caminho_atual)
pasta_pai = os.path.dirname(pasta_atual)
# Caminho dinâmico para a pasta "Docs"
frontend_path = os.path.join(pasta_pai, "Front End")
sys.path.append(frontend_path)
docs_path = os.path.join(pasta_pai, "Docs")
sys.path.append(docs_path)
backend_path = os.path.join(pasta_pai, "Back End")
sys.path.append(backend_path)

from database_functions import insert_docs, delete_docs

DEFAULT_ASSETS_PATH = r".\assets\default"

def open_calendar(window):
    with open("dados_login.json",'r') as json_file:
        dados = json.load(json_file)
    
    if dados["user_rank"] != 2:
        messagebox.showerror("Error","Seu usuário não tem nível suficiente para acessar este recurso")
        return
    
    open_gui(window,4)

def resource_path(relative_path):
    """Retorna o caminho correto, seja no modo normal ou empacotado"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def createimage_button(root, nome, deadline, imagem_base_path, comando, x, y,font_size,type):
    imagem_base = Image.open(imagem_base_path).convert("RGBA")
    draw = ImageDraw.Draw(imagem_base)

    try:
        fonte = ImageFont.truetype("arial.ttf", font_size)
    except:
        fonte = ImageFont.load_default()

    largura, altura = imagem_base.size
    if type == 1 or type == 2:
        texto_nome = nome[:15] + "\n" + nome[15:25]  # Trunca nome se for muito grande
        if len(nome) >= 15: 
            texto_nome + "..." # Trunca nome se for muito grande
            offset = 25
        elif len(nome) > 10:
            offset = 20
        else:
            offset = 10
            
        texto_deadline = f"Prazo:\n{deadline}" if deadline else ""
        draw.text((largura // 2, altura // 2 - offset), texto_nome, fill="black", font=fonte, anchor="mm")
        draw.text((largura // 2, altura // 2 + offset), texto_deadline, fill="red", font=fonte, anchor="mm")
    elif type == 0:
        texto_nome = nome[:10] + "\n" + nome[10:17]
        if len(nome) >= 17: 
            texto_nome + "..." # Trunca nome se for muito grande
            offset = 20
        elif len(nome) > 10:
            offset = 20
        else:
            offset = 10
            
        draw.text((largura // 2, altura // 2 - offset), texto_nome, fill="black", font=fonte, anchor="mm")
        
        texto_deadline = f"Prazo:\n{deadline}" if deadline else ""
        draw.text((largura // 2, altura // 2 + 15), texto_deadline, fill="red", font=fonte, anchor="mm")
    elif type == 4:
        texto_nome = nome[:8]
        if len(nome) >= 5: 
            texto_nome += "..." # Trunca nome se for muito grande
            
        draw.text((largura // 2, altura // 2), texto_nome, fill="black", font=fonte, anchor="mm")
    else:
        texto_nome = nome[:8]
        if len(nome) >= 5: 
            texto_nome += "..." # Trunca nome se for muito grande
            
        draw.text((largura // 2, altura // 2 - 5), texto_nome, fill="black", font=fonte, anchor="mm")
        
    imagem_tk = ImageTk.PhotoImage(imagem_base)

    color = "#F6F8D5"
    if type > 2:
        color = "#6DBFBF"        

    botao = Button(root, image=imagem_tk, command=comando, borderwidth=0, highlightthickness=0, relief="flat", bg=color)
    botao.image = imagem_tk  # Referência necessária
    
    if type == 1:
        botao.place(x=x, y=y, width=213, height=145)
    elif type == 0:
        botao.place(x=x, y=y, width=103, height=282)
    elif type == 2:
        botao.place(x=x, y=y, width=143, height=202)
    elif type == 3:
        botao.place(x=x, y=y, width=109, height=49)
    else:
        botao.place(x=x, y=y, width=109, height=22)

    return botao

def relative_to_assets(path: str,ASSETS_PATH=DEFAULT_ASSETS_PATH) -> ImageTk.PhotoImage:
    img = Image.open(ASSETS_PATH / Path(path))
    img = img.convert("RGBA")  # Garante que tem canal de transparência
    return ImageTk.PhotoImage(img)

def get_name():
    try:
        with open("dados_login.json", "r") as arquivo:
            dados = json.load(arquivo)
            nome = dados.get("username", "Nome não encontrado")  # Pega o nome salvo
            
            if len(nome) < 14:
                return "Olá \n"+nome.strip()+"!"  # Insere no Text
            else:
                return "Olá \n"+nome[:13]+"!"
            
    except FileNotFoundError:
        return "*Error*"
    
def save_file(nome_arquivo,data,user_name, conteudo):
    date_formated = data.strftime("%d%m%Y")
    new_name = user_name.replace('Olá ', '').replace('!', '').replace("\n","")
    folder = os.path.join(docs_path,new_name,date_formated)
    if not os.path.exists(folder):
        os.makedirs(folder)

    full_path = os.path.join(docs_path,new_name,date_formated, nome_arquivo)
    with open(full_path, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    messagebox.showinfo("Success","Arquivo salvo com sucesso!")
    insert_docs(full_path,date_formated)

def find_file(file_name):
    name = get_name().replace('Olá ', '').replace('!', '').replace("\n","")
    full_path = os.path.join(docs_path,name)
    
    for root, dirs, files in os.walk(full_path):  # Caminha recursivamente pela pasta
        if file_name + ".md" in files:
            return os.path.join(root, file_name + ".md")  # Retorna o caminho completo
    return "_"

def search_file(window,name):
    if not(name):
        return
            
    # Obtém a pasta onde o arquivo está
    caminho_atual = os.path.abspath(__file__)
    pasta_atual = os.path.dirname(caminho_atual)
    pasta_pai = os.path.dirname(pasta_atual)
    docs_path = os.path.join(pasta_pai, "Docs")
    
    with open('dados_login.json', 'r') as json_file:
        data = json.load(json_file)
    user_path = os.path.join(docs_path,data["username"])
    
    
    files_list = []

    for root, _, files in os.walk(user_path):
        for file in files:
            if name.lower() in file.lower():
                files_list.append({
                    "name": file,
                    "path": os.path.join(root, file)
                })
    
    with open('data_file.json', 'r') as json_file:
        data = json.load(json_file)
    if files_list:
        data["files_found"] = files_list
    else:
        data["files_found"] = user_path
        messagebox.showerror("Error","Não foram encontrados arquivos com esse nome")
        return
    
    with open('data_file.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)  # Salva corretamente
        
    open_gui(window,8)

def delete_file(file_name):
    file_path = find_file(file_name)  # Encontra o caminho do arquivo

    if not file_path or not os.path.exists(file_path):
        messagebox.showerror("Erro", "Arquivo não encontrado!")
        return

    # Caminho da pasta 'trash' (um nível acima)
    trash_folder = os.path.abspath(os.path.join(os.path.dirname(file_path), "..", "trash"))
    os.makedirs(trash_folder, exist_ok=True)  # Garante que a pasta 'trash' exista

    trash_path = os.path.join(trash_folder, os.path.basename(file_path))  # Caminho do arquivo na 'trash'

    if os.path.dirname(file_path) == trash_folder:
        # Se o arquivo já está na pasta 'trash', exclui permanentemente
        os.remove(file_path)
        messagebox.showinfo("Sucesso", "Arquivo deletado permanentemente!")

        # Remove a pasta original se estiver vazia
        original_folder = os.path.dirname(file_path)
        if not os.listdir(original_folder) and original_folder != "trash":
            os.rmdir(original_folder)

    else:
        # Move para a pasta 'trash'
        shutil.move(file_path, trash_path)
        delete_docs(file_path)
        messagebox.showinfo("Sucesso", f"Arquivo movido para a lixeira: {trash_path}")

        # Remove a pasta original se estiver vazia
        original_folder = os.path.dirname(file_path)
        if not os.listdir(original_folder) and original_folder != "trash":
            os.rmdir(original_folder)
    
    os.makedirs(trash_folder, exist_ok=True)  # Garante que a pasta 'trash' exista

def circular_image(image_path="", size=(60, 59),
                   second_image_path="",height_image="",width_image="",
                   pos_second_image=0.9):
    json_path = "dados_login.json"

    with open(json_path, "r") as arquivo:
        dados = json.load(arquivo)

    username = dados.get("username", "default_user")
    user_image_path = os.path.join(frontend_path, "assets", "user_profile", f"{username}.png")
    if not(second_image_path):
        second_image_path = os.path.join(frontend_path, "assets", "default", "config3.png")
        height_image = 30
        width_image = 30

    # Carregar a imagem correta
    if os.path.exists(image_path):
        img = Image.open(image_path).convert("RGBA")
        size = (37, 34)
    elif not os.path.exists(user_image_path):
        user_image_path = os.path.join(frontend_path, "assets", "user_profile", "config.png")
        img = Image.open(user_image_path).convert("RGBA")
    else:
        img = Image.open(user_image_path).convert("RGBA")

    img = img.resize(size, Image.LANCZOS)

    # Criar máscara circular
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    # Aplicar máscara
    circular_img = Image.new("RGBA", size, (0, 0, 0, 0))
    circular_img.paste(img, (0, 0), mask)

    # Adicionar outra imagem
    second_image = Image.open(second_image_path).convert("RGBA")
    second_image = second_image.resize((height_image, width_image), Image.LANCZOS)
    
    offset_x = int(size[0] - second_image.width * pos_second_image)
    offset_y = int(size[1] - second_image.height * pos_second_image)
    pos = (offset_x, offset_y)
    
    circular_img.paste(second_image, pos, second_image)

    # Salvar imagem final
    final_path = os.path.join(frontend_path, "assets", "user_profile", f"{username}_merged.png")
    circular_img.save(final_path)

    return final_path

def get_newphoto(window):
    # Pegar nome de usuário do JSON
    json_path = "dados_login.json"
    
    with open(json_path, "r") as arquivo:
        dados = json.load(arquivo)

    rank = dados.get("user_rank", "1")  # Obtém o rank do usuário
    user_name = dados.get("username", "config")  # Obtém o nome de usuário ou usa um padrão

    # Verifica se o usuário tem permissão
    if int(rank) != 2:
        messagebox.showerror("Erro", "O seu usuário não tem nível suficiente para colocar fotos")
        return

    # Abre a janela para selecionar um arquivo PNG
    arquivo_png = filedialog.askopenfilename(
        title="Selecione uma nova foto",
        filetypes=[("Imagens PNG", "*.png")]
    )

    if not arquivo_png:  # Se o usuário não selecionar nada, sai da função
        return

    # Define o diretório de destino (onde a imagem será salva)
    destino = os.path.join(r".\assets\user_profile", f"{user_name}.png")

    # Copia o arquivo para o diretório de destino
    shutil.copy(arquivo_png, destino)

    # Atualiza o JSON com o caminho da nova imagem
    with open(json_path, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    messagebox.showinfo("Sucesso", "Foto de perfil atualizada!")
    open_gui(window,3)

def directorys_profile():
    with open("dados_login.json", "r") as arquivo:
        dados = json.load(arquivo)

    profile_path = os.path.join(docs_path,f"{dados['username']}")

    folders_list = [
        {"name": pasta, "path": os.path.join(profile_path, pasta)}
        for pasta in os.listdir(profile_path)
        if os.path.isdir(os.path.join(profile_path, pasta))
    ]
    return folders_list

def files_folder(folder_path,window):
    # Adiciona o caminho apertado
    with open('dados_login.json', 'r') as json_file:
        data = json.load(json_file)
    data["last_folder"] = folder_path

    # Salva o arquivo
    with open('dados_login.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
    open_gui(window,8)

def file_content(window,file_path="model.json"):
    # Extrai nome do arquivo e nome da pasta (última pasta no caminho)
    file_name = os.path.basename(file_path)
    folder_name = os.path.basename(os.path.dirname(file_path))

    if file_name == "model.json" or ".ini" in file_name:
        data = {
            "date": "00000000",
            "file_name": "[Nome do arquivo]",
            "content": ""
        }
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        data = {
            "date": folder_name,
            "file_name": file_name.replace(".md",""),
            "content": content
        }

    # Salva os dados no JSON
    try:
        with open('data_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
    except Exception as e:
        return
    
    open_gui(window,2)

def set_placeholder(entry_widget, placeholder_text, placeholder_color="gray", text_color="#000716"):
    def on_focus_in(event):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, "end")
            entry_widget.config(fg=text_color)

    def on_focus_out(event):
        if entry_widget.get() == "":
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg=placeholder_color)

    entry_widget.insert(0, placeholder_text)
    entry_widget.config(fg=placeholder_color)
    entry_widget.bind("<FocusIn>", on_focus_in)
    entry_widget.bind("<FocusOut>", on_focus_out)

def month_days(today=""):
    if not(today):
        today = date.today()
    days_dict = {}
    current_day = today

    while len(days_dict) < 21:
        day_number = current_day.day
        
        # Adiciona apenas se o dia ainda não foi incluído
        if day_number not in days_dict:
            days_dict[day_number] = []

        current_day += timedelta(days=1)

    return days_dict

def update_last_folder(path="", window=None):
    with open("dados_login.json", "r") as arquivo:
        dados = json.load(arquivo)

    if not path:
        last_path = Path(dados["last_folder"])
        user_folder = last_path.parent
        path = str(user_folder / "trash")

    dados["last_folder"] = path

    with open("dados_login.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
        arquivo.flush()  # força o sistema a gravar imediatamente

    open_gui(window, 8)