from tkinter import Tk, Canvas, Button, Entry
from functions import relative_to_assets, search_file, get_name, circular_image, file_content, search_file, set_placeholder, createimage_button, update_last_folder
from changewindows import open_gui,centralize_window
from pathlib import Path
from datetime import datetime
import locale
import sys
import os

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

window.geometry("1107x682")
window.configure(bg = "#0A3A40")

canvas = Canvas(
    window,
    bg = "#0A3A40",
    height = 682,
    width = 1107,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
centralize_window(window,1107,682)

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

#------------------- Fundo --------------------
canvas.create_rectangle(
    720.0,
    90.0,
    1291.0,
    790.0,
    fill="#F6F8D5",
    outline="")

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
    1061.0,
    690.0,
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

week_image_13 = relative_to_assets("week_marked.png")
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

month_image_14 = relative_to_assets("month.png")
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

#---------------- Retângulo Azul ----------------
canvas.create_rectangle(
    111.0,
    214.0,
    1085.0,
    682.0,
    fill="#6DBFBF",
    outline=""
)

#--------------- Dias da Semana ----------------
canvas.create_text(
    149.0,
    232.0,
    anchor="nw",
    text="Segunda",
    fill="#092B81",
    font=("Inter SemiBoldItalic", 15 * -1)
)
canvas.create_text(
    309.0,
    232.0,
    anchor="nw",
    text="Terça",
    fill="#092B81",
    font=("Inter SemiBoldItalic", 15 * -1)
)

canvas.create_text(
    435.0,
    232.0,
    anchor="nw",
    text="Quarta",
    fill="#092B81",
    font=("Inter SemiBoldItalic", 15 * -1)
)

canvas.create_text(
    581.0,
    232.0,
    anchor="nw",
    text="Quinta",
    fill="#092B81",
    font=("Inter SemiBoldItalic", 15 * -1)
)

canvas.create_text(
    718.0,
    232.0,
    anchor="nw",
    text="Sexta",
    fill="#092B81",
    font=("Inter SemiBoldItalic", 15 * -1)
)

canvas.create_text(
    837.0,
    232.0,
    anchor="nw",
    text="Sábado",
    fill="#092B81",
    font=("Inter SemiBoldItalic", 15 * -1)
)

canvas.create_text(
    974.0,
    232.0,
    anchor="nw",
    text="Domingo",
    fill="#092B81",
    font=("Inter SemiBoldItalic", 15 * -1)
)

#---------------- Botão + para dias da semana ------------
moremonday_image_9 = relative_to_assets("more.png")
moremonday = Button(
    image=moremonday_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,8),
    relief="flat",
    bg="#6DBFBF"
)
moremonday.place(
    x=174,
    y=630,
    width=36,
    height=36
)

moretuesday_image_9 = relative_to_assets("more.png")
moretuesday = Button(
    image=moretuesday_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,8),
    relief="flat",
    bg="#6DBFBF"
)
moretuesday.place(
    x=314,
    y=630,
    width=36,
    height=36
)

morewednesday_image_9 = relative_to_assets("more.png")
morewednesday = Button(
    image=morewednesday_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,8),
    relief="flat",
    bg="#6DBFBF"
)
morewednesday.place(
    x=445,
    y=630,
    width=36,
    height=36
)

morethursday_image_9 = relative_to_assets("more.png")
morethursday = Button(
    image=morethursday_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,8),
    relief="flat",
    bg="#6DBFBF"
)
morethursday.place(
    x=592,
    y=630,
    width=36,
    height=36
)

morefriday_image_9 = relative_to_assets("more.png")
morefriday = Button(
    image=morefriday_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,8),
    relief="flat",
    bg="#6DBFBF"
)
morefriday.place(
    x=723,
    y=630,
    width=36,
    height=36
)

moresaturday_image_9 = relative_to_assets("more.png")
moresaturday = Button(
    image=moresaturday_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,8),
    relief="flat",
    bg="#6DBFBF"
)
moresaturday.place(
    x=847,
    y=630,
    width=36,
    height=36
)

moresunday_image_9 = relative_to_assets("more.png")
moresunday = Button(
    image=moresunday_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui(window,8),
    relief="flat",
    bg="#6DBFBF"
)
moresunday.place(
    x=984,
    y=630,
    width=36,
    height=36
)

#----------------------- Logica dos Botões -----------------

# Dias da semana (segunda=0 até sábado=5)
dias_semana = {
    'segunda-feira': 0,
    'terça-feira': 1,
    'quarta-feira': 2,
    'quinta-feira': 3,
    'sexta-feira': 4,
    'sábado': 5,
    'domingo':6
}

# Inicializa a lista com listas vazias (máx 6 slots por dia)
semana_files = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
position_x = {0: 127, 1: 275, 2: 408, 3: 550, 4: 683, 5: 810, 6: 952}

# Preenche a lista nos dias corretos
displayed_files = your_files(3)
for file in displayed_files:
    idx = dias_semana.get(file.week_day.lower())
    if idx is not None and len(semana_files[idx]) < 6:
        semana_files[idx].append(file)

# Posição inicial
mutable_x = 127

# Cria os botões para cada dia da semana, até 6 por dia
for dia in range(7):  # de 0 a 5 (segunda a sábado)
    arquivos = semana_files[dia]
    
    for file in arquivos:
        createimage_button(
                root=window,
                nome=file.name,
                deadline=file.deadline,
                imagem_base_path=ASSETS_PATH / "smallnote.png",
                comando=lambda path=file.path: file_content(window, path),
                x=position_x[dia],
                y=mutable_y,
                font_size=16,
                type=3
            )
        mutable_y += 67

    # Após cada dia, reseta x e move para nova linha
    mutable_y = 266


window.resizable(False, False)
window.mainloop()