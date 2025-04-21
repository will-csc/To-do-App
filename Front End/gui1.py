from functions import relative_to_assets, get_name, search_file, circular_image, file_content, set_placeholder, createimage_button, update_last_folder, open_calendar
from tkinter import Tk, Canvas, Entry, Button
from changewindows import open_gui,centralize_window
from pathlib import Path
import os
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "default"
config_image = ASSETS_PATH / "config3.png"

# Obtém a pasta onde o arquivo está
caminho_atual = os.path.abspath(__file__)
pasta_atual = os.path.dirname(caminho_atual)
pasta_pai = os.path.dirname(pasta_atual)

# Caminho dinâmico para a pasta "Back End"
backend_path = os.path.join(pasta_pai, "Back End")
sys.path.append(backend_path)
from database_functions import your_files

# ------------------- Dados Principais -------------------
window = Tk()

window.geometry("1051x682")
window.configure(bg = "#0A3A40")

canvas = Canvas(
    window,
    bg = "#0A3A40",
    height = 682,
    width = 1051,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
centralize_window(window,1051,682)

canvas.place(x = 0, y = 0)

# ------------------- Retângulos e Textos -------------------
rantangulo_image = relative_to_assets("image_1.png")
retangulo = canvas.create_image(
    645.0,
    410,
    image=rantangulo_image
)

canvas.create_text(
    101.0,
    24.0,
    anchor="nw",
    text="Minhas Tarefas/Notas",
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

# ------------------- Procurar Arquivo -------------------
search_image_1 = relative_to_assets("search.png")
search_1 = Button(
    image=search_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: search_file(window,find_1.get()),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
search_1.place(
    x=380.0,
    y=14.0,
    width=42.0,
    height=40.0
)

# ------------------- Alterar informações pessoais -------------------
config_image_2 = relative_to_assets(circular_image())
config_2 = Button(
    image=config_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,3),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
config_2.place(
    x=859.0,
    y=10.0,
    width=60.0,
    height=59.0
)

canvas.create_text(
    750,
    19,
    anchor="nw",
    text=get_name(),
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

#------------------------ Adicionar/Criar novo arquivo ---------------
add_image_5 = relative_to_assets("add.png")
add_5 = Button(
    image=add_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: file_content(window,"model.json"),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
add_5.place(
    x=62.0,
    y=106.0,
    width=71.0,
    height=18.0
)

add_image_11 = relative_to_assets("add2.png")
add_11 = Button(
    image=add_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: file_content(window,"model.json"),
    relief="flat",
    bg="#0A3A40"
)
add_11.place(
    x=17.0,
    y=95.0,
    width=34.986785888671875,
    height=38.0
)

#------------------------- Calendario ------------------------------
calendar_image_6 = relative_to_assets("calendar.png")
calendar_6 = Button(
    image=calendar_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_calendar(window),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
calendar_6.place(
    x=62.0,
    y=154.0,
    width=81.0,
    height=18.0
)
calendar_image_9 = relative_to_assets("calendar2.png")
calendar_9 = Button(
    image=calendar_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_calendar(window),
    relief="flat",
    bg="#0A3A40"
)
calendar_9.place(
    x=16.0,
    y=144.0,
    width=37.0,
    height=37.0
)

#------------------------- Files ------------------------------
files_image_7 = relative_to_assets("files.png")
files_7 = Button(
    image=files_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,7),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
files_7.place(
    x=62.0,
    y=208.0,
    width=67.0,
    height=18.0
)
files_image_10 = relative_to_assets("files2.png")
files_10 = Button(
    image=files_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,7),
    relief="flat",
    bg="#0A3A40"
)
files_10.place(
    x=16.0,
    y=198.0,
    width=37.0,
    height=37.0
)

#----------------- Abrir mais arquivos --------------------------
files_image_15 = relative_to_assets("more.png")
files_15 = Button(
    image=files_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,7),
    relief="flat",
    bg="#F6F8D5"
)
files_15.place(
    x=1008.0,
    y=510.0,
    width=36.0,
    height=36.0
)

#----------------- Lixeira -----------------
trash_image_8 = relative_to_assets("trash.png")
trash_8 = Button(
    image=trash_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_last_folder(window=window),
    relief="flat",
    bg="#0A3A40"
)
trash_8.place(
    x=17.0,
    y=256.0,
    width=36.0,
    height=36.0
)
trash_image_18 = relative_to_assets("trash2.png")
trash_18 = Button(
    image=trash_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_last_folder(window=window),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
trash_18.place(
    x=62,
    y=265,
    width=49,
    height=18
)

#------------------ Textos e retângulo -----------------
canvas.create_text(
    12.0,
    381.0,
    anchor="nw",
    text="Visite e apoie nossos\nDesenvolvedores",
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    85.0,
    495.0,
    anchor="center",
    text="William ->\ngithub.com/will-csc\nhttps://www.linkedin.com/in/william-cesar-7b7b89202/\n\nJoao\nMatheus\nEduardo",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1),
    width=144  # quebra o texto quando passar de 144px
)

canvas.create_text(
    210.0,
    100.0,
    anchor="nw",
    text="Arquivos Recentes",
    fill="#092B81",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    210.0,
    350.0,
    anchor="nw",
    text="Tarefas Pendentes",
    fill="#092B81",
    font=("Inter Bold", 20 * -1)
)

# ------------------ Input arquivo a procurar ------------------
find_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 15)
)
find_1.place(
    x=440.0,
    y=23.0,
    width=280.0,
    height=25.0
)
set_placeholder(find_1,"Digite o nome do arquivo")
find_1.bind("<Return>", lambda event: search_file(window,find_1.get()))

find_retangle = relative_to_assets("search2.png")
canvas.create_image(
    580,
    35,
    image=find_retangle
)

#------------------- Botão de Sair --------------------
exit_image_17 = relative_to_assets("exit.png")
exit_17 = Button(
    image=exit_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,0),
    relief="flat",
    bg="#0A3A40",  # Garante que o fundo do botão combina com o fundo
    activebackground="#0A3A40"
)
exit_17.place(
    x=949.0,
    y=27.0,
    width=81.0,
    height=24.0
)
exit_image_16 = relative_to_assets("exit2.png")
exit_16 = Button(
    image=exit_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,0),
    relief="flat",
    bg="#8D0E0E",  # Garante que o fundo do botão combina com o fundo
    activebackground="#8D0E0E"
)
exit_16.place(
    x=975.0,
    y=30.0,
    width=29.0,
    height=18.0
)

#------------------- Arquivos Recentes --------------------
displayed_files = your_files(1)
mutable_x = 210

for file in displayed_files:
    createimage_button(
        root=window,
        nome=file.name,
        deadline=file.deadline,
        imagem_base_path=ASSETS_PATH / "horizontal_note.png",
        comando=lambda path=file.path: file_content(window, path),
        x=mutable_x,
        y=150,
        font_size=20,
        type=1
    )
    mutable_x += 264
    
#------------------- Arquivos Recentes --------------------
displayed_files = your_files(0)
mutable_x = 196

for file in displayed_files:
    createimage_button(
        root=window,
        nome=file.name,
        deadline=file.deadline,
        imagem_base_path=ASSETS_PATH / "vertical_note.png",
        comando=lambda path=file.path: file_content(window, path),
        x=mutable_x,
        y=387,
        font_size=16,
        type=0
    )
    mutable_x += 133

window.resizable(False, False)
window.mainloop()
