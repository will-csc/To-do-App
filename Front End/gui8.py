from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button
from functions import relative_to_assets, get_name, circular_image, file_content, set_placeholder, search_file, update_last_folder
from changewindows import open_gui, centralize_window
from pathlib import Path
import os
import json

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "user_profile"
config_image = ASSETS_PATH / "config3.png"

#----------------- Lógica dos Arquivos ----------------
index_start = 0  # Índice da primeira pasta exibida

with open('dados_login.json', 'r') as json_file:
    data = json.load(json_file)

# Obtém a pasta onde o arquivo está
caminho_atual = os.path.abspath(__file__)
pasta_atual = os.path.dirname(caminho_atual)
pasta_pai = os.path.dirname(pasta_atual)
docs_path = os.path.join(pasta_pai, "Docs")

with open('data_file.json', 'r') as json_file:
    data = json.load(json_file)
    
if data.get("files_found"):
    files_list = data["files_found"]
    data["files_found"] = ""
        
    with open('data_file.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
else:
    try:
        with open('dados_login.json', 'r') as json_file:
            data = json.load(json_file)
        files_list = [
            {"name": file, "path": os.path.join(data["last_folder"],file)}
            for file in os.listdir(data["last_folder"])
        ]
    except:
        with open('dados_login.json', 'r') as json_file:
                data = json.load(json_file)
        new_path = os.path.join(docs_path,data["username"],"trash")
        files_list = [
            {"name": file, "path": new_path}
            for file in os.listdir(new_path)
        ]

# Função para atualizar as pastas no canvas
def update_files():
    global index_start

    # Limpa os elementos do canvas
    canvas.delete("files")  
    canvas.delete("files_text")

    # Define os limites para exibição
    max_display = 12  # Número máximo de pastas a serem exibidas
    displayed_files = files_list[index_start:index_start + max_display]

    mutable_x = 185
    mutable_y = 150
    cont = 0

    for file in displayed_files:
        cont += 1

        if ".ini" in file["path"]:
            continue

        # Criar a imagem da pasta
        file_button = Button(
            image=file_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda path=file["path"]: file_content(window,path),
            relief="flat",
            bg="#FFFFFF"
        )
        file_button.place(
            x=mutable_x-30,
            y=mutable_y-30,
            width=76,
            height=76
        )

        # Criar o nome da pasta dinamicamente
        canvas.create_text(
            mutable_x + 55,
            mutable_y - 10,
            anchor="nw",
            text=file["name"],
            fill="#000000",
            font=("Inter Bold", 25 * -1),
            tags="files_text"
        )

        # Mover para a segunda coluna
        if mutable_y < 504:
            mutable_y += 84
        else:
            mutable_y = 150

        if cont == 6:
            mutable_x += 369

# Função para avançar (Next)
def next_page():
    global index_start

    if index_start + 12 < len(files_list):  # Se houver mais pastas para exibir
        index_start += 1
        update_files()

# Função para voltar (Back)
def back_page():
    global index_start

    if index_start > 0:  # Se houver pastas anteriores para exibir
        index_start -= 1
        update_files()


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

#---------------- Botão de Voltar ----------------------
back_image_1 = relative_to_assets("back.png")
back_1 = Button(
    image=back_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,1),
    relief="flat",
    bg="#0A3A40"
)
back_1.place(
    x=19.0,
    y=15.0,
    width=59.0,
    height=59.0
)

# ------------------- Retângulos e Textos -------------------
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
calendar_image_9 = relative_to_assets("calendar2.png")
calendar_9 = Button(
    image=calendar_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,4),
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

#---------------- Fundo Branco ------------------
background_image_1 = relative_to_assets("fundobranco.png")
background_1 = canvas.create_image(
    607.0,
    417.0,
    image=background_image_1
)

#--------------- Pastas ------------------------
next_image_16 = relative_to_assets("next_y.png")
next = Button(
    image=next_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=next_page,
    relief="flat",
    bg="#FFFFFF"
)
next.place(x=984.0, y=607.0, width=58.0, height=58.0)

back_image_16 = relative_to_assets("back_y.png")
back_y = Button(
    image=back_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=back_page,
    relief="flat",
    bg="#FFFFFF"
)
back_y.place(x=984.0, y=108.5, width=58.0, height=58.0)

file_image_1 = relative_to_assets("openfile.png")
update_files()

window.resizable(False, False)
window.mainloop()