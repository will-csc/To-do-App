from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, messagebox
from functions import relative_to_assets
from changewindows import open_gui, centralize_window
import sys
import os

# Obtém a pasta onde o arquivo está
caminho_atual = os.path.abspath(__file__)
pasta_atual = os.path.dirname(caminho_atual)
pasta_pai = os.path.dirname(pasta_atual)

# Caminho dinâmico para a pasta "Back End"
backend_path = os.path.join(pasta_pai, "Back End")
sys.path.append(backend_path)
from database_functions import sign_up

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\signup")

#---------------- Verificação ----------------------
def fix_values():
    try:
        call_function = True

        global email, nome, phone, password

        # Possíveis erros na entrada do email
        email_value = str(email.get()).strip()
        if "@" not in email_value or len(email_value) < 10:
            messagebox.showerror("Erro", "E-mail digitado está fora do padrão!")
            call_function = False

        # Possíveis erros na entrada do nome
        nome_value = str(nome.get()).strip()
        if len(nome_value) < 5:
            messagebox.showerror("Erro", "O nome precisa ser maior que 5 caracteres")
            call_function = False

        # Possíveis erros na entrada do telefone
        phone_value = str(phone.get()).strip()
        if len(phone_value) != 11:
            messagebox.showerror("Erro", "O telefone deve conter o DDD e ter exatos 11 dígitos")
            call_function = False
        else:
            try:
                phone_value = int(phone_value)  # Certifique-se de que o telefone seja um número
            except ValueError:
                messagebox.showerror("Erro", "O telefone deve ser um número válido!")
                call_function = False

        # Possíveis erros na entrada da senha
        password_value = str(password.get()).strip()
        if len(password_value) < 6:
            messagebox.showerror("Erro", "A senha precisa ser maior que 6 dígitos")
            call_function = False

        if call_function:
            sign_up(nome.get(),email.get(),phone.get(),password.get(),window)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

#---------------- Detalhes Principais -------------------
window = Tk()

window.geometry("1051x682")
window.configure(bg = "#1D7373")

canvas = Canvas(
    window,
    bg = "#1D7373",
    height = 682,
    width = 1051,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
centralize_window(window,1051,682)

canvas.place(x = 0, y = 0)

#--------------------- Bloco Principal ----------------------
main_image_1 = relative_to_assets("main.png",ASSETS_PATH)
main_1 = canvas.create_image(
    290.0,
    433.0,
    image=main_image_1
)

#---------------- Botão de Voltar ----------------------
back_image_1 = relative_to_assets("back.png")
back_1 = Button(
    image=back_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,0),
    relief="flat",
    bg="#1D7373"
)
back_1.place(
    x=19.0,
    y=15.0,
    width=59.0,
    height=59.0
)

#-------------------- Bloco com os dados ---------------------
retangulo_image_2 = relative_to_assets("image_1.png",ASSETS_PATH)
retangulo_2 = canvas.create_image(
    806.0,
    334.0,
    image=retangulo_image_2
)

canvas.create_text(
    119.0,
    120.0,
    anchor="nw",
    text="Abrace a organização!",
    fill="#FFFFFF",
    font=("Inter SemiBoldItalic", 36 * -1)
)

canvas.create_text(
    811.0,
    124.0,
    anchor="center",
    text="Preencha os\ndados abaixo",
    fill="#FFFFFF",
    font=("Inter SemiBoldItalic", 40 * -1)
)
#----------------------- Blocos para Input ---------------------
image_2 = relative_to_assets("image_2.png",ASSETS_PATH)
x = 805
y = 150

for i in range(4):
    y += 72
    image = canvas.create_image(
        805.0,
        y,
        image=image_2
    )

#----------------------- Botão p/ Cadastrar --------------------
signup_image_2 = relative_to_assets("button_2.png",ASSETS_PATH)
signup_2 = Button(
    image=signup_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fix_values(),
    relief="flat",
    bg="#0A3A40"
)
signup_2.place(
    x=658.0,
    y=486.0,
    width=296.0,
    height=51.0
)

signup_image_3 = relative_to_assets("button_3.png",ASSETS_PATH)
signup_3 = Button(
    image=signup_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fix_values(),
    relief="flat",
    bg="#042326"
)
signup_3.place(
    x=660.0,
    y=496.0,
    width=291.0,
    height=27.0
)

#------------------- Textos ---------------------
canvas.create_text(
    656.0,
    404.0,
    anchor="nw",
    text="Senha",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

canvas.create_text(
    654.0,
    334.0,
    anchor="nw",
    text="Telefone",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

canvas.create_text(
    656.0,
    262.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

canvas.create_text(
    656.0,
    194.0,
    anchor="nw",
    text="Nome",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

#------------------- Textos ---------------------
nome = Entry(
    bd=0, 
    bg="#093439",
    fg="#D5CECE",
    highlightthickness=0,
    font=("Inter", 13)
)
nome.place(
    x=654.0,
    y=215.0,
    width=292.0,
    height=20.0
)

email = Entry(
    bd=0, 
    bg="#093439",
    fg="#D5CECE",
    highlightthickness=0,
    font=("Inter", 13)
)
email.place(
    x=654.0,
    y=289.0,
    width=292.0,
    height=20.0
)

phone = Entry(
    bd=0,  
    bg="#093439",
    fg="#D5CECE",
    highlightthickness=0,
    font=("Inter", 13)
)
phone.place(
    x=654.0,
    y=357.0,
    width=292.0,
    height=20.0
)

password = Entry(
    bd=0, 
    bg="#093439",
    fg="#D5CECE",
    highlightthickness=0,
    font=("Inter", 13)
)
password.place(
    x=654.0,
    y=428.0,
    width=292.0,
    height=20.0
)
nome.bind("<Return>", lambda event: fix_values())
email.bind("<Return>", lambda event: fix_values())
phone.bind("<Return>", lambda event: fix_values())
password.bind("<Return>", lambda event: fix_values())

window.resizable(False, False)
window.mainloop()
