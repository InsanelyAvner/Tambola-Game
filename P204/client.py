import socket
from tkinter import *
from threading import Thread
import random

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    PORT = 6000
    IP_ADDRESS = '127.0.0.1'
    SERVER = socket.socket (socket. AF_INET, socket.SOCK STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=receivedMsg)
    thread.start()

det askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow = Tk()
    nameWindow.title("Tanbola Family Fun") 
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nanetindow, width = 500,height = 580)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.create_text(screen_width/4.5, screen_height/8,
                        text="Enter Your Name",
                        font={'Chlakboard SE, 60'},
                        fill="black")
    
    nameEntry = Entry(nameWindow, width=15, justify="center", font={"Chalkboard SE", 30}, bd=5, bg="white")
    nameEntry.place(x=screen_width/7, y=screen_height/5.5)

    button = Button(nameWindow, text="Save", font={"Chalkboard SE", 30}, width=11, command=saveName, height=2, bg="50deea", bd=3)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry
    
    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())