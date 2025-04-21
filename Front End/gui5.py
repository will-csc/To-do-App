from functions import relative_to_assets
from tkinter import Tk, Canvas, Entry, Button
from changewindows import open_gui, centralize_window
from pathlib import Path
import os
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "raise_rank"

# Obtém a pasta onde o arquivo está
caminho_atual = os.path.abspath(__file__)
pasta_atual = os.path.dirname(caminho_atual)
pasta_pai = os.path.dirname(pasta_atual)

# Caminho dinâmico para a pasta "Back End"
backend_path = os.path.join(pasta_pai, "Back End")
sys.path.append(backend_path)
from database_functions import update_rank

#-------------------- Detalhes Principais ------------------
window = Tk()

window.geometry("1051x619")
window.configure(bg = "#0A3A40")

canvas = Canvas(
    window,
    bg = "#0A3A40",
    height = 619,
    width = 1051,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
centralize_window(window,1051,619)
canvas.place(x=0,y=0)

#---------------- Botão de Voltar ----------------------
back_image_1 = relative_to_assets("back.png")
back_1 = Button(
    image=back_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,3),
    relief="flat",
    bg="#0A3A40"
)
back_1.place(
    x=19.0,
    y=15.0,
    width=59.0,
    height=59.0
)

#------------------ Fundo Branco ------------------
background_image = relative_to_assets("background.png",ASSETS_PATH)
background = canvas.create_image(
    557.0,
    316.0,
    image=background_image
)

#----------------- Textos -------------------------
canvas.create_text(
    220.0,
    60.0,
    anchor="nw",
    text="Faça um Pix de 1$, para elevar o nível da sua conta",
    fill="#000000",
    font=("Inter", 30 * -1)
)
canvas.create_text(
    214.0,
    446.0,
    anchor="nw",
    text="Digite o código de autorização enviado após o pagamento",
    fill="#000000",
    font=("Inter", 25 * -1)
)

#----------------- Qr Code -------------------
qrcode_image_2 = relative_to_assets("qrcode.png",ASSETS_PATH)
qrcode = canvas.create_image(
    558.0,
    281.0,
    image=qrcode_image_2
)

#----------------- Retângulo para Input ---------------
input_image_3 = relative_to_assets("input.png",ASSETS_PATH)
input_3 = canvas.create_image(
    558.0,
    521.0,
    image=input_image_3
)

#----------------- Input -------------------
code = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Arial",20)
)
code.place(
    x=236.0,
    y=507.0,
    width=618.0,
    height=28.0
)
code.bind("<Return>",lambda event: update_rank(int(code.get()),window))

#----------------- Botão Update -----------------
update_image_2 = relative_to_assets("update_button.png",ASSETS_PATH)
update_button = Button(
    image=update_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_rank(int(code.get()),window),
    relief="flat"
)
update_button.place(
    x=881.0,
    y=492.0,
    width=59.0,
    height=59.0
)

window.resizable(False, False)
window.mainloop()
