from tkinter import *
import os

def open_gui(window,n: int):
    window.destroy()
    if n == 0:
        os.system(f"python gui.py")
    else:
        os.system(f"python gui{n}.py")

def centralize_window(window, largura, altura):
    window.update_idletasks()  # Garante que a geometria da janela seja atualizada
    largura_tela = window.winfo_screenwidth()
    altura_tela = window.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    window.geometry(f"{largura}x{altura}+{x}+{y}")