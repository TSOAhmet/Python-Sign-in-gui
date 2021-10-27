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

window.geometry("400x500")
window.configure(bg = "#3A7FF6")

canvas = Canvas(
    window,
    bg = "#DCDCE4",
    height = 500,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file=relative_to_assets("backgroundgui.png"))
canvas.create_image(0, 0, image = image, anchor = NW)
canvas.create_rectangle(
    140.0,
    65.0,
    260.0,
    108.0,
    fill="#DCDCE4",
    outline="")

canvas.create_text(
    170.0,
    73.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    170.0,
    113.0,
    230.0,
    118.0,
    fill="#FCFCFC",
    outline="")

def register():
    os.system("python register.py")

def login():
    os.system("login.py")
def exit():
    sys.exit(0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=register,
    relief="flat"
)
button_1.place(
    x=110.0,
    y=191.0,
    width=180.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_2.place(
    x=110.0,
    y=305.0,
    width=180.0,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=exit,
    relief="flat"
)
button_3.place(
    x=328.0,
    y=440.0,
    width=67.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()
