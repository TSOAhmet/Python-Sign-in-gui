from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from PIL import ImageTk
import PIL
import sys
import tkinter.filedialog
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x600")
window.configure(bg = "#3A7FF6")


canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file=relative_to_assets("background.png"))
canvas.create_image(10, 10, image = image, anchor = NW)
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    339.9999999999999,
    78.0,
    459.9999999999999,
    121.0,
    fill="#000000",
    outline="")

canvas.create_text(
    369.9999999999999,
    86.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    369.9999999999999,
    126.0,
    429.9999999999999,
    131.0,
    fill="#FCFCFC",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    399.4999999999999,
    196.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.place(
    x=238.9999999999999,
    y=166.0,
    width=321.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    399.4999999999999,
    301.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_2.place(
    x=238.9999999999999,
    y=271.0,
    width=321.0,
    height=59.0
)

canvas.create_text(
    235.9999999999999,
    247.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Roboto Bold", 18 * -1)
)

canvas.create_text(
    235.9999999999999,
    142.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Roboto Bold", 18 * -1)
)

def loginfos():
    usname = entry_1.get()
    pasword = entry_2.get()
    scriptedinfos = (usname,pasword)
    stringscript = ''.join(scriptedinfos)
    print(usname, pasword)
    print("giriş deneniyor")
    f = open(stringscript,"r") 
    contents =f.read()
    print("sonuc:")
    if contents == stringscript:
        print("giriş başarılı") 
        os.system("mainpage.py")
    else:print("giriş yapılamadı")
button_image_1 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=loginfos,
    relief="flat"
)
button_1.place(
    x=311.9999999999999,
    y=367.0,
    width=180.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()
