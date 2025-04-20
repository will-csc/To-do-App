from tkinter import Tk, Canvas, Entry, Button
from functions import relative_to_assets, set_placeholder, get_name, circular_image, file_content, search_file,month_days, createimage_button, update_last_folder
from changewindows import open_gui, centralize_window
from pathlib import Path
from datetime import datetime, date
import locale
import os
import sys

locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')

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

window.geometry("1107x739")
window.configure(bg = "#0A3A40")

canvas = Canvas(
    window,
    bg = "#0A3A40",
    height = 739,
    width = 1107,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
centralize_window(window,1107,739)

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

#---------------- Fundo ------------------
rantangulo_image = relative_to_assets("image_1.png")
retangulo = canvas.create_image(
    560.0,
    417,
    image=rantangulo_image
)
canvas.create_rectangle(
    720.0,
    90.0,
    1291.0,
    790.0,
    fill="#F6F8D5",
    outline="")

canvas.create_rectangle(
    84.0,
    218.0,
    200.0,
    900.0,
    fill="#F6F8D5",
    outline="")

#---------------- Data ------------------
# Obter a data atual formatada
data_atual = datetime.now()
dia_semana = data_atual.strftime("%A").upper()  # Pega as 5 primeiras letras do dia (ex: "Wednesday" vira "Wedne")
data_formatada = data_atual.strftime("%d/%m/%Y")

canvas.create_text(
    850.0,
    116.0,
    anchor="center",
    text=f"{dia_semana} {data_formatada}",
    fill="#092B81",
    font=("Inter Bold", 30 * -1)
)

#--------------- Texto ---------------
canvas.create_text(
    125.0,
    179.0,
    anchor="nw",
    text="Tarefas Pendentes",
    fill="#092B81",
    font=("Inter Bold", 20 * -1)
)

#------------------- Fundo --------------------
canvas.create_rectangle(
    111.0,
    214.0,
    1100.0,
    865.0,
    fill="#6DC8C8",
    outline="")

# ------------------ Calendario/Hoje/Week/Month ------------------
today_image_12 = relative_to_assets("today.png")
today_12 = Button(
    image=today_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,4),
    relief="flat",
    bg="#F6F8D5"
)
today_12.place(
    x=150.0,
    y=133.0,
    width=34.0,
    height=18.0
)

week_image_13 = relative_to_assets("week.png")
week_13 = Button(
    image=week_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,9),
    relief="flat",
    bg="#F6F8D5"
)
week_13.place(
    x=230.0,
    y=133.0,
    width=97.0,
    height=18.0
)

month_image_14 = relative_to_assets("month_marked.png")
month_14 = Button(
    image=month_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,10),
    relief="flat",
    bg="#F6F8D5"
)
month_14.place(
    x=370.0,
    y=133.0,
    width=69.0,
    height=18.0
)

#---------------- Nome do Mês ------------------
image_image_2 = relative_to_assets("filename.png")
image_2 = canvas.create_image(
    308.0,
    94.0,
    image=image_image_2
)

mes_atual = datetime.now().strftime('%B').capitalize()
canvas.create_text(
    294.0,
    91.0,
    anchor="center",
    text=mes_atual,
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

#-------------- Inserir documentos dos dias --------------
days_dict = month_days()
displayed_files = your_files(4)

position_x = {}
x = 164

for day in days_dict.keys():
    position_x[day] = x
    if x > 952:
        x = 164
    else:
        x += 144

for file in displayed_files:
    month_day = file.deadline.day  # Pegando apenas o número do dia
    if month_day in days_dict:
        days_dict[month_day].append(file)

#Inserir botões no canvas
mutable_y = 266
row_count = 1

more_image = relative_to_assets("more.png")

# Nomes dos dias em português
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

# Obter o dia da semana atual (0 = segunda, ..., 6 = domingo)
hoje = datetime.today().weekday()
today_idx = datetime.today().day

# Gerar ordem a partir do dia atual
ordem_dias = [(hoje + i) % 7 for i in range(7)]

# Criar cabeçalho com nomes dos dias da semana

for idx, dia_index in enumerate(ordem_dias):
    dia_semana = dias_semana[dia_index]

    canvas.create_text(
        position_x[today_idx]-10,
        232,  # posição Y do cabeçalho
        anchor="nw",
        text=dia_semana,
        fill="#092C82",
        font=("Inter Bold", 15)
    )
    today_idx += 1

for day, lista in days_dict.items():
    if day < date.today().day:
        color = "#425079"
    else:
        color = "#092C82"
        
    canvas.create_text(
        position_x[day],
        mutable_y,
        anchor="nw",
        text=str(day),
        fill=color,
        font=("Inter Bold", 30 * -1)
    )
    
    if lista:
        for i in range(len(lista)):
            if i == 3:
                break
            
            createimage_button(
                    root=window,
                    nome=lista[i].name,
                    deadline=lista[i].deadline,
                    imagem_base_path=ASSETS_PATH / "tinynote.png",
                    comando=lambda path=lista[i].path: file_content(window, path),
                    x=position_x[day]-25,
                    y=mutable_y+35,
                    font_size=16,
                    type=4
                )
            mutable_y += 28
        
    if len(lista) > 3:
        arquivo_path = Path(lista[i].path)
        pasta_pai = str(arquivo_path.parent)
        
        more_button = Button(
            image=more_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda path=pasta_pai: update_last_folder(path,window),
            relief="flat",
            bg="#6DC8C8"
        )
        more_button.place(
            x=position_x[day]+10,
            y=mutable_y+35,
            width=26.25,
            height=26.25
        )
    
    row_count += 1
    if row_count > 14:
        mutable_y = 590
    elif row_count > 7:
        mutable_y = 430
    else:
        mutable_y = 266

window.resizable(False, False)
window.mainloop()