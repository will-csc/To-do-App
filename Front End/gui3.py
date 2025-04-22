from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button
from changewindows import open_gui, centralize_window
from functions import relative_to_assets, circular_image, get_name, get_newphoto, set_placeholder
import os
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\config")

# Obtém a pasta onde o arquivo está
caminho_atual = os.path.abspath(__file__)
pasta_atual = os.path.dirname(caminho_atual)
pasta_pai = os.path.dirname(pasta_atual)

# Caminho dinâmico para a pasta "Back End"
backend_path = os.path.join(pasta_pai, "Back End")
sys.path.append(backend_path)
from database_functions import update_information

#----------------- Dados princiais ------------------
window = Tk()

window.geometry("1051x619")
window.configure(bg = "#1D7373")

canvas = Canvas(
    window,
    bg = "#1D7373",
    height = 619,
    width = 1051,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
centralize_window(window,1051,619)

canvas.place(x = 0, y = 0)

#---------------- Botão de Voltar ----------------------
back_image_1 = relative_to_assets("back.png")
back_1 = Button(
    image=back_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,1),
    relief="flat",
    bg="#1D7373"
)
back_1.place(
    x=19.0,
    y=15.0,
    width=59.0,
    height=59.0
)

#-------------------- Imagem do usuario -------------------------
button_image = os.path.join(ASSETS_PATH, "button_2.png")
user_image = circular_image(size=(212,211),second_image_path=button_image,
                            height_image=80,width_image=80,
                            pos_second_image=1)

config_image_2 = relative_to_assets(user_image)
button_2 = Button(
    image=config_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_newphoto(window),
    relief="flat",
    bg="#1D7373",  # Garante que o fundo do botão combina com o fundo
    activebackground="#1D7373"
)
button_2.place(
    x=95.0,
    y=136.0,
    width=212.0,
    height=211.0
)

canvas.create_text(
    100,
    346,
    anchor="nw",
    text=get_name(),
    fill="#FFFFFF",
    font=("Inter Bold", 35 * -1)
)

#------------------- Retângulo Principal ---------------
image_image_2 = relative_to_assets("image_2.png",ASSETS_PATH)
image_2 = canvas.create_image(
    710.0,
    310.0,
    image=image_image_2
)

canvas.create_text(
    480.0,
    77.0,
    anchor="nw",
    text="Altere suas informações abaixo",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

#------------------- Retângulo dos Input --------------
image_2 = relative_to_assets("image_3.png",ASSETS_PATH)
y = 165

for i in range(4):
    image = canvas.create_image(
        725.0,
        y,
        image=image_2
    )
    y += 88


#------------------- Salvar Informações ---------------
button_image_3 = relative_to_assets("button_3.png",ASSETS_PATH)
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_information(window,e_mail_2.get(),nome_1.get(),phone_3.get(),password_4.get()),
    relief="flat",
    bg="#0A3A40"
)
button_3.place(
    x=673.0,
    y=498.0,
    width=294.0,
    height=51.0
)

button_image_5 = relative_to_assets("button_5.png",ASSETS_PATH)
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_information(window,e_mail_2.get(),nome_1.get(),phone_3.get(),password_4.get()),
    relief="flat",
    bg="#107361"
)
button_5.place(
    x=703.0,
    y=508.0,
    width=234.0,
    height=31.0
)

#------------------- Sair ---------------
button_image_4 = relative_to_assets("button_4.png",ASSETS_PATH)
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,1),
    relief="flat",
    bg="#0A3A40"
)
button_4.place(
    x=450.0,
    y=498.0,
    width=178.0,
    height=51.0
)

button_image_6 = relative_to_assets("button_6.png",ASSETS_PATH)
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,1),
    relief="flat",
    bg="#8D0E0E"
)
button_6.place(
    x=513.0,
    y=508.0,
    width=51.0,
    height=31.0
)

#------------------- Nome dos Campos ------------------
canvas.create_text(
    457.0,
    126.0,
    anchor="nw",
    text="Nome",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

canvas.create_text(
    456.0,
    215.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

canvas.create_text(
    456.0,
    304.0,
    anchor="nw",
    text="Telefone",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

canvas.create_text(
    456.0,
    393.0,
    anchor="nw",
    text="Senha",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

#------------------- Texto p/ o Usuario ------------------
nome_1 = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 20)
)
nome_1.place(
    x=457.0,
    y=156.0,
    width=510.0,
    height=30.0
)

e_mail_2 = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 20)
)
e_mail_2.place(
    x=456.0,
    y=245.0,
    width=510.0,
    height=30.0
)

phone_3 = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 20)
)
phone_3.place(
    x=457.0,
    y=336.0,
    width=510.0,
    height=30.0
)

password_4 = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 20)
)
password_4.place(
    x=456.0,
    y=422.0,
    width=510.0,
    height=22.0
)

set_placeholder(nome_1, "Digite seu nome",text_color="#FFFFFF")
nome_1.bind("<Return>",lambda event:update_information(window,e_mail_2.get(),nome_1.get(),phone_3.get(),password_4.get()))
set_placeholder(e_mail_2, "Digite seu e-mail",text_color="#FFFFFF")
e_mail_2.bind("<Return>",lambda event:update_information(window,e_mail_2.get(),nome_1.get(),phone_3.get(),password_4.get()))
set_placeholder(phone_3, "Digite seu telefone",text_color="#FFFFFF")
phone_3.bind("<Return>",lambda event:update_information(window,e_mail_2.get(),nome_1.get(),phone_3.get(),password_4.get()))
set_placeholder(password_4, "Digite sua senha",text_color="#FFFFFF")
password_4.bind("<Return>",lambda event:update_information(window,e_mail_2.get(),nome_1.get(),phone_3.get(),password_4.get()))

#----------------- Botão de Elevar nível -----------------
rankbutton_image_5 = relative_to_assets("button_7.png",ASSETS_PATH)
rankbutton = Button(
    image=rankbutton_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,5),
    relief="flat",
    bg="#1D7373"
)
rankbutton.place(
    x=52.0,
    y=498.0,
    width=301.0,
    height=51.0
)

rankbutton_image_6 = relative_to_assets("button_8.png",ASSETS_PATH)
rankbutton_6 = Button(
    image=rankbutton_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,5),
    relief="flat",
    bg="#0A3A40"
)
rankbutton_6.place(
    x=70.0,
    y=508.0,
    width=270.0,
    height=31.0
)

window.resizable(False, False)
window.mainloop()
