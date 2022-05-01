import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk, Image

# print('hi')

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 6000

playerName = None
nameEntry = None
nameWindow = None

# print('hi2')


def receiveMsg():
    print('receiveMsg')


def setup():
    # print('hi3')
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=receiveMsg)
    thread.start()

    askPlayerName()


def askPlayerName():
    print('hi')
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow = Tk()
    nameWindow.title('Tambola')
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="./assets/bg.jpg")

    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.create_text(screen_width/4.5, screen_height/8,
                        text="Enter Name", font=("Chalkboard SE", 60), fill="black")

    nameEntry = Entry(nameWindow, width=15, justify='center',
                      font=('Chalkboard SE', 30), bd=5, bg='white', fg='black')
    nameEntry.place(x=screen_width/7, y=screen_height/5.5)

    button = Button(nameWindow, text="Save", font=(
        "Chalkboard SE", 30), width=11, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x=screen_width/6, y=screen_height/4)

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


setup()
