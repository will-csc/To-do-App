from functions import relative_to_assets, save_file, get_name,search_file,delete_file, circular_image, file_content, set_placeholder, update_last_folder, open_calendar
from tkinter import Tk, Canvas, Entry, Button, Text, messagebox
from changewindows import open_gui, centralize_window
import re
import tkinter as tk
from datetime import datetime
from pathlib import Path
import json

def apply_markdown(event=None):
    """Renderiza Markdown dentro do user_input a cada atualização"""
    content = user_input.get("1.0", tk.END)
    
    # Remover todas as tags antes de aplicar novas
    for tag in ["bold", "italic", "code", "header", "list"]:
        user_input.tag_remove(tag, "1.0", tk.END)

    # **Negrito**
    for match in re.finditer(r"\*\*(.*?)\*\*", content):
        user_input.tag_add("bold", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")

    # *Itálico*
    for match in re.finditer(r"\*(.*?)\*", content):
        user_input.tag_add("italic", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")

    # `Código`
    for match in re.finditer(r"`(.*?)`", content):
        user_input.tag_add("code", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")

    # # Cabeçalhos
    for match in re.finditer(r"^# (.*?)$", content, re.MULTILINE):
        user_input.tag_add("header", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")

    # Listas
    for match in re.finditer(r"^- (.*?)$", content, re.MULTILINE):
        user_input.tag_add("list", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")

def save_newfile(day,month,year):
    global filename, user_input

    try:
        date = datetime(int(year), int(month), int(day))
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        
        if date < today:
            messagebox.showerror("Error","Digite uma data igual ou maior que a de hoje")
            return
        
        file_name = filename.get()
        if "[Nome do arquivo]" in file_name:
            messagebox.showerror("Error","Digite o nome de arquivo")
            return

    except ValueError:
        messagebox.showerror("Error","Data inválida. Verifique os valores informados.")
        return

    save_file(file_name + ".md",date,get_name(), user_input.get("1.0", "end-1c"))

def update_content():
    with open("data_file.json", 'r', encoding='utf-8') as file:
        content = json.load(file)

    set_placeholder(filename,content["file_name"],placeholder_color="#FFFFFF",text_color="#FFFFFF")
    set_placeholder(deadlineday,content["date"][:2],placeholder_color="#FFFFFF",text_color="#FFFFFF")
    set_placeholder(deadlinemonth,content["date"][2:4],placeholder_color="#FFFFFF",text_color="#FFFFFF")
    set_placeholder(deadlineyear,content["date"][4:9],placeholder_color="#FFFFFF",text_color="#FFFFFF")
    user_input.insert("1.0",content["content"])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "user_profile"
config_image = ASSETS_PATH / "config3.png"

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

# ------------------- Retângulo para o Texto -------------------
retangulo_image_2 =relative_to_assets("textarea.png")
retangulo_2 = canvas.create_image(
    605.0,
    408.0,
    image=retangulo_image_2
)

#------------------- Nome do Arquivo ------------------
filename_image_3 = relative_to_assets("filename.png")
filename_3 = canvas.create_image(
    222.0,
    93.0,
    image=filename_image_3
)

filename = Entry(
    bd=0,
    bg="#1D7373",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 15)
)
filename.place(
    x=114.0,
    y=82.0,
    width=230.0,
    height=22.0
)

#-------------------- Data Limite ------------------------
deadlineimage = relative_to_assets("deadline.png")
deadline = canvas.create_image(
    490.0,
    93.0,
    image=deadlineimage
)

def limitar_entry(texto):
    return len(texto) <= 2
vcmd = window.register(limitar_entry)

# Dia
deadlineday = Entry(
    bd=0,
    bg="#1C54E3",
    fg="#FFFBFB",
    highlightthickness=0,
    font=("Inter", 15),
    validate="key",
    validatecommand=(vcmd, "%P")
)
deadlineday.place(
    x=402.0,
    y=85.0,
    width=29.0,
    height=22.0
)

# Semana
deadlinemonth = Entry(
    bd=0,
    bg="#1C54E3",
    fg="#FFFBFB",
    highlightthickness=0,
    font=("Inter", 15),
    validate="key",
    validatecommand=(vcmd, "%P")
)
deadlinemonth.place(
    x=439.0,
    y=85.0,
    width=29.0,
    height=22.0
)
# Mês

# Ano (4 caracteres)
def limitar_ano(texto):
    return len(texto) <= 4

vcmd_ano = window.register(limitar_ano)

deadlineyear = Entry(
    bd=0,
    bg="#1C54E3",
    fg="#FFFBFB",
    highlightthickness=0,
    font=("Inter", 15),
    validate="key",
    validatecommand=(vcmd_ano, "%P")
)
deadlineyear.place(
    x=478.0,
    y=85.0,
    width=55.0,
    height=22.0
)

# *** Barras ***
canvas.create_text(
    431.0,
    82.0,
    anchor="nw",
    text="/",
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    469.0,
    82.0,
    anchor="nw",
    text="/",
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

# *** Texto ***
canvas.create_text(
    400.0,
    72.0,
    anchor="nw",
    text="Data Limite",
    fill="#FFFFFF",
    font=("Inter Bold", 11 * -1)
)

#-------------------- Entrada do usuário -----------------
user_input = Text(
    bd=0,
    bg="#F6F8D5",
    fg="#000000",
    highlightthickness=0,
    font=("Inter", 15),
    wrap="word"
)
user_input.place(
    x=114.0,
    y=133.0,
    width=860.0,
    height=515.0
)

# Aplicar Markdown a cada tecla pressionada
user_input.bind("<KeyRelease>", apply_markdown)

# Criar estilos de formatação
user_input.tag_configure("bold", font=("Inter", 15, "bold"))
user_input.tag_configure("italic", font=("Inter", 15, "italic"))
user_input.tag_configure("code", font=("Courier", 15), background="#eaeaea")
user_input.tag_configure("header", font=("Inter", 20, "bold"), foreground="black")
user_input.tag_configure("list", foreground="blue")

# ------------------- Botão de Deletar -------------------
delete_image_7 = relative_to_assets("delete.png")
delete_7 = Button(
    image=delete_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: delete_file(filename.get()),
    relief="flat"
)
delete_7.place(
    x=871.0,
    y=72.0,
    width=161.0,
    height=30.0
)
delete_image_9 = relative_to_assets("delete2.png")
delete_9 = Button(
    image=delete_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: delete_file(filename.get()),
    relief="flat",
    bg="#F02626"
)
delete_9.place(
    x=899.0,
    y=75.0,
    width=108.0,
    height=22.0
)

# ------------------- Botão de Salvar -------------------
save_image_9 = relative_to_assets("save.png")
save_9 = Button(
    image=save_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_newfile(deadlineday.get(),deadlinemonth.get(),deadlineyear.get()),
    relief="flat",
    bg="#1D7373"
)
save_9.place(
    x=633.0,
    y=72.0,
    width=211.0,
    height=30.0
)

save_image_8 = relative_to_assets("save2.png")
save_8 = Button(
    image=save_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_newfile(deadlineday.get(),deadlinemonth.get(),deadlineyear.get()),
    relief="flat",
    bg="#1D7373"
)
save_8.place(
    x=658.0,
    y=75.0,
    width=162.0,
    height=22.0
)

update_content()
window.resizable(False, False)
window.mainloop()