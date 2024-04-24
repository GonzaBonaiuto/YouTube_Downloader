from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Downloader de YouTube by Gonza")
root.configure(bg="#AACDE2")

Label(root, text="Descargá tus videos", font="arial 20 bold", bg="#AACDE2").place(x=90, y=30)

link = StringVar()
Label(root, text="Pega el link acá", font="arial 12", bg="#AACDE2").place(x=190, y=90)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=120)

complete_label = Label(root, text="", font="arial 13 bold", bg="#AACDE2")

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    complete_label.config(text="Descarga completa")
    complete_label.place(x=180, y=240)

Button(root, text="DESCARGAR", font="arial 13 bold italic", bg="#B57199", padx=2, command=downloader).place(x=180, y=180)

root.mainloop()
