from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button
from functions import relative_to_assets, circular_image
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
from database_functions import login, send_code

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\login")

circular_image(Path(r".\assets\user_profile\config.png"))

#------------------- Dados da janela ----------------------
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

#------------------- Bloco --------------------
canvas.place(x = 0, y = 0)

bloco_image = relative_to_assets("image_2.png",ASSETS_PATH)
bloco = canvas.create_image(
    265.0,
    326.0,
    image=bloco_image
)

canvas.create_text(
    107.0,
    96.0,
    anchor="nw",
    text="Seja bem-vindo!",
    fill="#FFFFFF",
    font=("Inter SemiBoldItalic", 40 * -1)
)

#---------------- Imagem para input ----------------------
imagem_input = relative_to_assets("image_3.png",ASSETS_PATH)
email_image = canvas.create_image(
    265.0,
    326.0,
    image=imagem_input
)

password_image = canvas.create_image(
    265.0,
    240.0,
    image=imagem_input
)

# ------------------ Login ------------------
login_image_1 = relative_to_assets("button_1.png",ASSETS_PATH)
login_1 = Button(
    image=login_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login(email.get(),password.get(),window),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
login_1.place(
    x=145.0,
    y=433.0,
    width=214.0,
    height=49.0
)

login_image_3 = relative_to_assets("button_3.png",ASSETS_PATH)
login_3 = Button(
    image=login_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login(email.get(),password.get(),window),
    relief="flat",
    bg="#042326",  # Garante que o fundo do botão combina com o fundo
    activebackground="#042326"
)
login_3.place(
    x=204.0,
    y=442.5,
    width=95.0,
    height=30.0
)

#---------------- Linhas e "OU" ----------------------
canvas.create_rectangle(
    70.0,
    506.0,
    162.0054931640625,
    507.0,
    fill="#424242",
    outline="")

canvas.create_rectangle(
    358.0,
    506.0,
    450.0054931640625,
    507.0,
    fill="#424242",
    outline="")

canvas.create_text(
    239.0,
    495.0,
    anchor="nw",
    text="Ou",
    fill="#FFFFFF",
    font=("Inter SemiBoldItalic", 20 * -1)
)

# ------------------ Esqueceu a Senha ------------------
forgetpassw_image_2 = relative_to_assets("button_2.png",ASSETS_PATH)
forgetpassw_2 = Button(
    image=forgetpassw_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: send_code(email.get(),window),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
forgetpassw_2.place(
    x=271.0,
    y=363.0,
    width=189.0,
    height=24.0
)

# --------------- Cadastre-se --------------
cadastrar_image_4 = relative_to_assets("button_1.png",ASSETS_PATH)
cadastrar_4 = Button(
    image=cadastrar_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,11),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
cadastrar_4.place(
    x=148.0,
    y=536.0,
    width=218.0,
    height=42.0
)

cadastrar_image_5 = relative_to_assets("button_5.png",ASSETS_PATH)
cadastrar_5 = Button(
    image=cadastrar_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,11),
    relief="flat",
    bg="#042326",  # Garante que o fundo do botão combina com o fundo
    activebackground="#042326"
)
cadastrar_5.place(
    x=179.0,
    y=542.0,
    width=153.0,
    height=30.0
)

# ------------------- Retângulos e Textos ---------------------
canvas.create_text(
    92.0,
    198.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 25 * -1)
)

canvas.create_text(
    92.0,
    282.0,
    anchor="nw",
    text="Senha",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 25 * -1)
)


#--------------- Imagem principal --------------------
image_image_1 = relative_to_assets("image_1.png",ASSETS_PATH)
image_1 = canvas.create_image(
    753.0,
    345.0,
    image=image_image_1,
)

#------------------ Input e-mail e senha ----------------------
email = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 15)
)
email.place(
    x=88.0,
    y=229.0,
    width=362.0,
    height=20.0
)

password = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 15),
    show="*"
)
password.place(
    x=88.0,
    y=315.0,
    width=362.0,
    height=20.0
)

password.bind("<Return>", lambda event: login(email.get(), password.get(), window))
email.bind("<Return>", lambda event: login(email.get(), password.get(), window))

#-------------------- Inicia ----------------
window.resizable(False, False)
window.mainloop()
