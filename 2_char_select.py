# import section
from tkinter import *
import sqlite3

# definitions
width = 800
height = 400
a = b = c = x = 0

color = ['#6B430E', '#60695C', '#16281E', '#2A324B', '#EA526F']
hero = ['Javius', 'Onisu', 'Dashi', 'Rohan']
comment = ['Höhere\nGeschwindigkeit beim\nAngriff', 'Resistent\ngegen jede Form\nvon Hitze', 'Trägt schwerere\nWaffen für mehr\nAngriffsschaden', 'Gelehrt\nin\nZauberei']

geometry = {}
hero_symbol = {}

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


def charsel(d):
    if d == 0:
        print("Javius")
    elif d == 1:
        print("Onisu")
    elif d == 2:
        print('Dashi')
    elif d == 3:
        print('Rohan')
    else:
        print('Error')

# windows settings
root = Tk()
root.geometry('{}x{}'.format(width, height))
root.resizable(width=False, height=False)
# root.title('notitle')

# tk elements
while True:
    for i in range(0, 16):
        if i >= 12:
            geometry[i] = Label(geometry[i - 12], text=comment[c], font='Fixedsys 10 bold', bg='{}'.format(color[c]), fg='#ffffff')
            c += 1
        elif i >= 8:
            geometry[i] = Label(geometry[i - 8], text=hero[b], font='Fixedsys 20 bold', bg='{}'.format(color[b]), fg='#ffffff')
            b += 1
        elif i >= 4:
            hero_symbol[i] = PhotoImage(file='graphics/heroes/hero_{}_transparent.png'.format(hero[a].lower()))
            geometry[i] = Button(geometry[i - 4], image=hero_symbol[i], bg='{}'.format(color[a]), bd=7)
            a += 1
        else:
            geometry[i] = Label(root, bg='{}'.format(color[i]))

    for i in range(0, 16):
        if i >= 12:
            geometry[i].place(width=170, x=15, rely=0.7, bordermode=OUTSIDE)
        elif i >= 8:
            geometry[i].place(width=170, heigh=50, x=15, rely=0.55, bordermode=OUTSIDE)
        elif i >= 4:
            geometry[i].place(width=170, heigh=170, x=15, y=30, bordermode=OUTSIDE)
        else:
            geometry[i].place(x=x, y=50, width=200, height=400, bordermode=OUTSIDE)
            x += 200

    geometry[4].config(command=lambda: charsel(0))
    geometry[5].config(command=lambda: charsel(1))
    geometry[6].config(command=lambda: charsel(2))
    geometry[7].config(command=lambda: charsel(3))
    Label(root, text='Wähle deinen Helden:', font='Fixedsys 30 bold', bg='#000000', fg='#ffffff').place(x=0, y=0, width=800)
    break

# mainloop
root.mainloop()
