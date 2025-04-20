from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button
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
from database_functions import forget_password

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\forget")

#-------------------- Dados Gerais ---------------------
window = Tk()

window.geometry("1035x682")
window.configure(bg = "#1D7373")


canvas = Canvas(
    window,
    bg = "#1D7373",
    height = 682,
    width = 1035,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
centralize_window(window,1035,682)

canvas.place(x = 0, y = 0)

canvas.create_text(
    50.0,
    140.0,
    anchor="nw",
    text="Esqueceu a sua senha?",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 40 * -1)
)
canvas.create_text(
    48.0,
    200.0,
    anchor="nw",
    text="Utilize o código enviado no seu e-mail ou telefone",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 20 * -1)
)

#--------------------- Imagem Principal ----------------------
main_image_1 = relative_to_assets("image_1.png",ASSETS_PATH)
main_1 = canvas.create_image(
    263.0,
    421.0,
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

#------------------ Textos e Retângulo ------------------
retangulo_imagem = relative_to_assets("image_2.png",ASSETS_PATH)
retangulo_main = canvas.create_image(
    791.0,
    361.0,
    image=retangulo_imagem
)

canvas.create_text(
    603.0,
    122.0,
    anchor="nw",
    text="Digite o código enviado no email",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 25 * -1)
)

canvas.create_text(
    603.0,
    258.0,
    anchor="nw",
    text="Digite a nova senha",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 25 * -1)
)

canvas.create_text(
    603.0,
    386.0,
    anchor="nw",
    text="Redigite a nova senha",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 25 * -1)
)

retangulo_input = relative_to_assets("image_4.png",ASSETS_PATH)
y = 194
for i in range(3):
    retangulo = canvas.create_image(
        790.0,
        y,
        image=retangulo_input
    )
    y += 128

#---------------------- Botão Atualizar -----------------------
update_image_2 = relative_to_assets("button_2.png",ASSETS_PATH)
update_2 = Button(
    image=update_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: forget_password(code.get(),new_password.get(),new_password2.get(),window),
    relief="flat",
    bg="#0A3A40"
)
update_2.place(
    x=650.0,
    y=528.0,
    width=291.0,
    height=65.0
)

update_image_3 = relative_to_assets("button_3.png",ASSETS_PATH)
update_3 = Button(
    image=update_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: forget_password(code.get(),new_password.get(),new_password2.get(),window),
    relief="flat",
    bg="#042326"
)
update_3.place(
    x=699.0,
    y=545.0,
    width=184.0,
    height=31.0
)


# ---------------- Input's -------------------
code = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 25)
)
code.place(
    x=604.0,
    y=173.0,
    width=374.0,
    height=40.0
)

new_password = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 25)
)
new_password.place(
    x=604.0,
    y=300.0,
    width=374.0,
    height=40.0
)

new_password2 = Entry(
    bd=0,
    bg="#042326",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 25)
)
new_password2.place(
    x=604.0,
    y=427.0,
    width=374.0,
    height=40.0
)

window.resizable(False, False)
window.mainloop()
