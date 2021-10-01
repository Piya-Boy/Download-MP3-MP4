from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x600")
root.title("YouTube Video Downloader")
root.resizable(False, False)

img_icon = PhotoImage(file="Images/youtube.png")
root.iconphoto(False, img_icon)

Label(root, text="YouTube Video Downloader", font="arial 20 bold").pack(padx=5, pady=50)

link = StringVar()

Label(root, text="Paste your link here:", font="arial 15 bold").place(x=160, y=100)
link_enter = Entry(root, width=43, font=30, textvariable=link, bd=5).place(x=10, y=190)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()

    Label(root, text="DOWNLOAD COMPLETED", font="arial 15", fg="white", bg="red").place(x=100, y=300)
    Label(root, text="CHECK YOUR CURRENT FILE FOR THE VIDEO", font="arial 15").place(x=10, y=350)

Button(root, text="DOWNLOAD", font="arial 15 bold", bg="lightblue", padx=2, command=Downloader).place(x=170, y=250)


root.mainloop()
