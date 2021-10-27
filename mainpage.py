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

window.geometry("1300x900")
window.configure(bg = "#1A1A1A")


canvas = Canvas(
    window,
    bg = "#1A1A1A",
    height = 900,
    width = 1300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)



logolow = PhotoImage(
    file=relative_to_assets("logolow.png"))

canvas.create_image(
    75.0,
    60.0,
    image=logolow,
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("socialshare.png"))
entry_bg_1 = canvas.create_image(
    628.5,
    245.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D3D3D3",
    highlightthickness=0
)
entry_1.place(
    x=379.0,
    y=204.0,
    width=499.0,
    height=81.0
)

canvas.create_text(
    347.0,
    119.0,
    anchor="nw",
    text="Write Something About You !",
    fill="#FFFFFF",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    347.0,
    429.0,
    984.0,
    622.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    347.0,
    693.0,
    984.0,
    886.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1018.0,
    0.0,
    1328.0,
    769.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("home.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("home clicked"),
    relief="flat"
)
button_1.place(
    x=10.0,
    y=141.0,
    width=121.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("trends.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("trends clicked"),
    relief="flat"
)
button_2.place(
    x=10.0,
    y=221.0,
    width=121.0,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("profile.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("profile clicked"),
    relief="flat"
)
button_3.place(
    x=10.0,
    y=301.0,
    width=121.0,
    height=55.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("settings.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("settings clicked"),
    relief="flat"
)
button_4.place(
    x=10.0,
    y=381.0,
    width=121.0,
    height=55.0
)
def exit():
    sys.exit(0)


button_image_5 = PhotoImage(
    file=relative_to_assets("exit.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=exit,
    relief="flat"
)
button_5.place(
    x=1219.0,
    y=831.0,
    width=67.0,
    height=55.0
)


n1=6
n2=4

def send():
    global n1
    global n2
    text1 = entry_1.get()
    textscript = (text1)
    stringtext = ''.join(textscript)
    print(text1, "paylaşılıyor")
    f = open(stringtext,"w+")
    f.write(stringtext)
    contents =f.read()
    print(n1, n2)
    if n1>n2:
        canvas.create_text(
        352.0,
        435.0,
        anchor="nw",
        text=stringtext,
        fill="#FFFFFF",
        font=("Roboto Bold", 24 * -1)
)
        n1=n1-5
        print(n1, n2)
    elif n2>n1:
        canvas.create_text(
        352.0,
        700.0,
        anchor="nw",
        text=stringtext,
        fill="#FFFFFF",
        font=("Roboto Bold", 24 * -1)
)
        print(n1, n2)

    

    print("sonuc:paylasim yapildi")

button_image_6 = PhotoImage(
    file=relative_to_assets("send.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=send,
    relief="flat"
)
button_6.place(
    x=835.0,
    y=313.0,
    width=110.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()
