# pip install youtube_dl
# pip install pafy

from tkinter import*
from tkinter import messagebox
import pafy

def Error():
    messagebox.showwarning('', 'Something went wrong, please check again.')

def Download_MP3():
    try:
        video = pafy.new(url.get())
        audiostreams = video.audiostreams
        for x in audiostreams:
            x.get_filesize()
            text1.set(video.title)
            text2.set('Download Successful !')

        audiostreams[3].download(filepath='C:/Users\Acer\Downloads\Music')
    except:
        Error()
        
def Download_MP4():
    try:
        video = pafy.new(url.get())
        video.audiostreams
        text1.set(video.title)
        text2.set('Download Successful !')
        best_video = video.getbest()
        best_video.download(filepath='C:/Users\Acer\Downloads\Video')
    except:
        Error()

win = Tk()
win.title('Download.com')
win.configure(bg='#CCFFFF')
win.geometry('360x300')
win.resizable(False, False)

url = StringVar()
text1 = StringVar()
text2 = StringVar()

photo_mp3 = PhotoImage(file='Images\mp3.png').subsample(13)
photo_mp4 = PhotoImage(file='Images\mp4.png').subsample(13)

Label(win, text='Please insert a valid video URL', font='Time 17', bg='#CCFFFF').pack(pady=10)
Entry(win, textvariable=url, width=46, bd=5).pack(pady=10, padx=30)

Button(win, command=Download_MP3, text="mp3".upper(), image=photo_mp3, compound=LEFT, padx=15, font="Tahoma 16", bd=5, bg='forest green').pack(pady=10)
Button(win, command=Download_MP4, text="mp4".upper(), image=photo_mp4, compound=LEFT, padx=15, font="Tahoma 16", bd=5, bg='forest green').pack()

Label(win, textvariable=text1, bg='#CCFFFF').pack(pady=5)
Label(win, textvariable=text2, fg='green', bg='#CCFFFF').pack()

Label(win, bg='#F7DC6F').pack(fill=X)

mainloop()
