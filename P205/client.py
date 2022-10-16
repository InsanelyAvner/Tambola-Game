import socket
from tkinter import *
from  threading import Thread
import random
from PIL import ImageTk, Image
import platform

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None
playerName = None

canvas1 = None

nameEntry = None
nameWindow = None


def createTicket():
    global gameWindow()
    global ticketGrid

    mainLabel = Label(gameWindow, width=65, height=16, relief="ridge", borderwidth=5, bg="white")
    mainLabel.place(x=95, y=119)

    xPos = 105
    yPos = 130

    for row in range(0, 3):
        rowList = []

        for col in range(0, 9):
            if platform.system() == "Darwin":
                boxButton = Button(gameWindow,
                                    font={"Chalboard SE", 18},
                                    borderwidth=3,
                                    pady=23,
                                    padx=22,
                                    bg="#FFF176",
                                    highlightbackgrounds="#FFF176",
                                    activebackground="#C5ELA5")

                boxButton.place(x=xPos, y=yPos)
            else:
                boxButton = tk.Button(gameWindow, font={"Chalkboard SE", 30}, width=3, height=2, borderwidth=5, bg="#FFF176")
                boxButton.place(x=xPos, y=yPos)

            rowList.append(boxButton)
            xPos += 64
        
    ticketGrid.append(rowList)
    yPos = 105
    yPos += 82

def placeNumbers():
    global ticketGrid
    global currentNumberList

    for row in range(0, 3):
        randomColList = []
        counter = 0

        while counter <= 4:
            randomCol = random.randint(0, 8)
            if randomCol not in randomColList:
                randomColList.append(randomCol)
                counter += 1
    
    numberContainer = {
        "0": [i for i in range(1, 10)],
        "1": [i for i in range(10, 20)],
        "2": [i for i in range(20, 30)],
        "3": [i for i in range(30, 40)],
        "4": [i for i in range(40, 50)],
        "5": [i for i in range(50, 60)],
        "6": [i for i in range(60, 70)],
        "7": [i for i in range(70, 80)],
        "8": [i for i in range(80, 91)]
    }

    counter = 0
    while (counter < len(randomColList)):
        colNum = randomColList[counter]
        numbersListByIndex = numberContainer[str(colNum)]
        randomNumber = random.choice(numbersListByyIndex)

        if randomNumber not in currentNumberList:
            numberBox = ticketGrid[row][colNum]
            numberBox.configure(text=randomNumber, fg="black")
            
            currentNumberList.append(randomNumber)

            counter += 1

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

    
def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow  = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/4.5,screen_height/8, text = "Enter Name", font=("Chalkboard SE",60), fill="black")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 30), bd=5, bg='white')
    nameEntry.place(x = screen_width/7, y=screen_height/5.5 )

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=11, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/6, y=screen_height/4)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def recivedMsg():
    pass


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=recivedMsg)
    thread.start()

    askPlayerName()



setup()