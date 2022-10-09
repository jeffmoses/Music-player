
from pygame import mixer
from tkinter import*


wd=Tk()
wd.geometry("600x300")
wd['bg']='grey'

mixer.init()
mixer.music.load("congo_muchana_kanda_bongo_man_lyrics_aac_75446.mp3")


def pause():
    mixer.music.pause()

def play():
    mixer.music.play()

def resume():
    mixer.music.unpause()


Label(wd,text="JMO MUSIC PLAYER",font="lucidia 30 bold").pack()
Button(text="play",command=play).place(x=300,y=200)
Button(text="pause",command=pause).place(x=350,y=200)
Button(text="resume",command=resume).place(x=450,y=200)
Button(text="quit",command=quit).place(x=510,y=200)
wd.mainloop()
