import datetime
import os.path
import sqlite3
from tkinter import *
from tkinter import messagebox, PhotoImage
from passlib.hash import pbkdf2_sha256

print("[INFO]: Import von Systemmodulen erfolgreich")

# Designeinstellungen
mainbg = "#0b0c16"
mainfg = "white"
font_body = "Fixedsys", 20, "bold"

# ----- LOADER -----
user = {}
char = {}

if os.path.exists("data.db"):
    # noinspection PyGlobalUndefined
    global connection
    # noinspection PyGlobalUndefined
    global cursor
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
else:
    print("[WARN]: Datenbank existiert nicht")
    print("[INFO]: Datenbank wird angelegt")

    connection_startup = sqlite3.connect("data.db")
    cursor_startup = connection_startup.cursor()
    cursor_startup.execute("""CREATE TABLE credentials(
            id          INTEGER     PRIMARY KEY      AUTOINCREMENT,
            user        TEXT        NOT NULL,
            password    TEXT        NOT NULL)
            """)
    cursor_startup.execute("""CREATE TABLE gamedata(
            id          INTEGER     PRIMARY KEY      AUTOINCREMENT,
            user        TEXT        NOT NULL,
            character   TEXT        NOT NULL,
            progress    TEXT        NOT NULL)
            """)
    connection_startup.close()
    print("[INFO]: Datenbank erfolgreich angelegt")
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

if os.path.exists("graphics/transparent.ico"):
    loadico = True
    print("[INFO]: Systemgrafiken komplett")
else:
    print("[WARN]: Transparent.ico not found!")
    loadico = False


def golog():  # Login Funktion
    name_cache = username.get()  # Speichert die Username Eingabe in ()
    pass_cache = password.get()  # Speichert die Passwort Eingabe in ()

    valid = pbkdf2_sha256.verify(pass_cache, user[name_cache])  # Vergleicht Eingabe mit Hash und setzt Wert in Valid

    if name_cache in user.keys():  # Login Abfrage (Wenn Benutzername == registriert)
        if valid:  # Wenn valid == True führe fort
            output = "Anmeldung von " + name_cache + " erfolgt!"
            message.config(text="\n" + output)
            print("[INFO]: Anmeldung von ", name_cache, "erfolgt")  # DEBUG CONSOLE

            if "NONE" in char[name_cache]:  # Wenn Benutzer kein Character gewählt hat führe fort
                print("nothing")
                # Programmende (alle Instanzen geschlossen)
                # Übergabe von sämtlichen Parametern hier!
        else:
            message.config(text="\nFalsches Passwort !")
    else:
        message.config(text="\nUnbekannter Benutzername !")


def importdata():
    with connection:
        import_cur = connection.cursor()
        import_cur2 = connection.cursor()
        import_cur3 = connection.cursor()
        import_cur4 = connection.cursor()
        import_cur5 = connection.cursor()
        import_cur.execute("SELECT user FROM credentials")
        import_cur2.execute("SELECT password FROM credentials")
        import_cur3.execute("SELECT user FROM gamedata")
        import_cur4.execute("SELECT character FROM gamedata")
        import_cur5.execute("SELECT progress FROM gamedata")

        while True:
            importeduser = import_cur.fetchone()
            importedpassword = import_cur2.fetchone()
            importeduserchar = import_cur3.fetchone()
            importedchar = import_cur4.fetchone()
            importedprogress = import_cur5.fetchone()

            if importeduser is None:
                break

            user[importeduser[0]] = importedpassword[0]

            if importedchar is None:
                break

            char[importeduserchar[0]] = importedchar[0], importedprogress[0]
        print("[DEBUG]: USERS:", user, "CHARACTERS:", char)


importdata()
print("[INFO]: Datenbank erfolgreich ausgelesen")

root_load = Tk()
root_load.configure(bg=mainbg)
root_load.overrideredirect(1)
root_load.geometry("600x350")

if loadico:
    root_load.iconbitmap(default='graphics/transparent.ico')


# noinspection PyStringFormat,PyTypeChecker
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


center(root_load)

label = Label(bg=mainbg)
label.place(x=150, y=170, width=100, height=100)
info = Label(text="", bg=mainbg, fg=mainfg, font=font_body)
info.place(x=100, y=120, width=400, height=60)
info.after(100, lambda: info.config(text="Laden..."))
info.after(1000, lambda: root_load.destroy())
root_load.mainloop()

# ----- END - LOADER -----


def characterselect():
    width = 800
    height = 400
    a = b = c = x = 0

    color = ['#6B430E', '#60695C', '#16281E', '#2A324B', '#EA526F']
    hero = ['Javius', 'Onisu', 'Dashi', 'Rohan']
    comment = ['Höhere\nGeschwindigkeit beim\nAngriff', 'Resistent\ngegen jede Form\nvon Hitze',
               'Trägt schwerere\nWaffen für mehr\nAngriffsschaden', 'Gelehrt\nin\nZauberei']

    geometry = {}
    hero_symbol = {}

    def charsel(d):
        if d == 0:
            cursor.execute("INSERT INTO credentials VALUES (NULL, ?, ?)",
                           (user_register, password_register))
            connection.commit()
            cursor.execute("INSERT INTO gamedata VALUES (NULL, ?, ?, ?)",
                           (user_register, "Javius", "0"))
            connection.commit()
        elif d == 1:
            cursor.execute("INSERT INTO credentials VALUES (NULL, ?, ?)",
                           (user_register, password_register))
            connection.commit()
            cursor.execute("INSERT INTO gamedata VALUES (NULL, ?, ?, ?)",
                           (user_register, "Onisu", "0"))
            connection.commit()
        elif d == 2:
            cursor.execute("INSERT INTO credentials VALUES (NULL, ?, ?)",
                           (user_register, password_register))
            connection.commit()
            cursor.execute("INSERT INTO gamedata VALUES (NULL, ?, ?, ?)",
                           (user_register, "Dashi", "0"))
            connection.commit()
        elif d == 3:
            cursor.execute("INSERT INTO credentials VALUES (NULL, ?, ?)",
                           (user_register, password_register))
            connection.commit()
            cursor.execute("INSERT INTO gamedata VALUES (NULL, ?, ?, ?)",
                           (user_register, "Rohan", "0"))
            connection.commit()

        else:
            print('Error')
        rootc.destroy()
        importdata()
        mainroot()

    # windows settings
    rootc = Tk()
    rootc.geometry('{}x{}'.format(width, height))
    rootc.resizable(width=False, height=False)
    rootc.title('Charakterauswahl')

    # tk elements
    while True:
        for i in range(0, 16):
            if i >= 12:
                geometry[i] = Label(geometry[i - 12], text=comment[c], font='Fixedsys 10 bold',
                                    bg='{}'.format(color[c]), fg='#ffffff')
                c += 1
            elif i >= 8:
                geometry[i] = Label(geometry[i - 8], text=hero[b], font='Fixedsys 20 bold',
                                    bg='{}'.format(color[b]), fg='#ffffff')
                b += 1
            elif i >= 4:
                hero_symbol[i] = PhotoImage(
                    file='graphics/heroes/hero_{}_transparent.png'.format(hero[a].lower()))
                geometry[i] = Button(geometry[i - 4], image=hero_symbol[i], bg='{}'.format(color[a]),
                                     bd=7)
                a += 1
            else:
                geometry[i] = Label(rootc, bg='{}'.format(color[i]))

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
        Label(rootc, text='Wähle deinen Helden:', font='Fixedsys 30 bold',
              bg='#000000', fg='#ffffff').place(
            x=0, y=0, width=800)
        break
    rootc.mainloop()


def show_info():
    info_msg = "\
******************************************\n\
Autoren: Jonas, Jaime, Joseph, Niklas\n\
Datum: 18.06.17\n\
Version: 0.8\n\
******************************************"
    messagebox.showinfo("Informationen", info_msg)


# noinspection PyGlobalUndefined
def gotodata():  # wird verwendet von <goregister>
    # ----- REGISTRIEREN -----
    global user_register
    global password_register
    user_register = username_register.get()
    password_register_cache = passwort_register1.get()
    password_register_recall_cache = passwort_register2.get()
    password_register = pbkdf2_sha256.encrypt(password_register_cache, rounds=200000, salt_size=16)
    valid = pbkdf2_sha256.verify(password_register_recall_cache, password_register)

    if len(user_register) > 0:
        if len(password_register_cache) > 0:
            if user_register not in user:

                if valid:
                    nroot.destroy()
                    root.destroy()
                    characterselect()
                    print("[INFO]:", user_register, "erfolgreich zur Datenbank hinzugeüft")
                    importdata()

                else:
                    information.config(text="Die Passwörter stimmen nicht überein!")
                    print("[WARN]: Die eingegebenen Passwörter stimmen nicht überein!")
            else:
                information.config(text="Dieser Benutzername ist bereits vorhanden!")
                print("[WARN]: Dieser Benutzername ist bereits vorhanden!")
        else:
            information.config(text="Ungültiges Passwort!")
            print("[WARN]: TypeFailure")
    else:
        information.config(text="Ungültiger Benutzername!")
        print("[WARN]: TypeFailure")


# noinspection PyGlobalUndefined
def goregister():  # Wird aufgerufen von "root" und ruft selbst <gotodata> auf
    global nroot
    nroot = Tk()
    nroot.configure(bg=mainbg)
    nroot.title("Registrieren")
    nroot.geometry("800x400")
    nroot.resizable(0, 0)

    # Elements Definitions für nroot (Registrierungs Fenster)
    global username_register
    global passwort_register1
    global passwort_register2
    global information
    username_register = Entry(nroot, width=20, font=font_body)
    username_register_label = Label(nroot, text="Benutzername", font=font_body, bg=mainbg, fg=mainfg)
    passwort_register1 = Entry(nroot, width=20, font=font_body, show="*")
    passwort_register2 = Entry(nroot, width=20, font=font_body, show="*")
    passwort_register_label1 = Label(nroot, text="Passwort", font=font_body, bg=mainbg, fg=mainfg)
    passwort_register_label2 = Label(nroot, text="Passwort Wiederholen", font=font_body, bg=mainbg, fg=mainfg)
    register_button = Button(nroot, text="Weiter...", font=font_body, bg=mainbg, fg=mainfg, command=gotodata)
    information = Label(nroot, text="Bitte Daten eingeben!", font=font_body, bg=mainbg, fg=mainfg)

    # Place Elements für nroot (Registrierungs Fenster)
    username_register.place(x=450, y=60, width=250, height=40)
    username_register_label.place(x=50, y=60, width=320, height=50)
    passwort_register1.place(x=450, y=120, width=250, height=40)
    passwort_register2.place(x=450, y=180, width=250, height=40)
    passwort_register_label1.place(x=50, y=120, width=320, height=50)
    passwort_register_label2.place(x=50, y=180, width=350, height=50)
    register_button.place(x=480, y=240, width=200, height=60)
    information.place(x=10, y=320, width=800, height=50)


# ----- LOGIN -----
# noinspection PyGlobalUndefined
def mainroot():
    global root
    root = Tk()
    root.configure(bg=mainbg)
    root.title("Launcher")
    root.geometry("800x400")
    root.resizable(0, 0)

    # Elements Definitions für root (Login Fenster)
    global username
    global password
    global login
    global register
    global message
    global date
    global func_button
    username = Entry(root, width=20, font=font_body)
    user_label = Label(root, text="Benutzername", font=font_body, bg=mainbg, fg=mainfg)
    password = Entry(root, show="*", width=20, font=font_body)
    password_label = Label(root, text="Passwort", font=font_body, bg=mainbg, fg=mainfg)
    login = Button(root, text="Anmelden", command=golog, font=font_body, bg=mainbg, fg=mainfg)
    register = Button(root, text="Registrieren", font=font_body, bg=mainbg, fg=mainfg, command=goregister)
    message = Label(root, text="\nBitte Anmelden oder Registrieren!", font=font_body, bg=mainbg, fg=mainfg)
    date = Label(root, text="{:%d. %b %Y}".format(datetime.date.today()),
                 bg=mainbg, fg=mainfg, font=("Fixedsys", 17, "bold"))
    func_button = Button(root, text="Info", command=show_info, font=font_body, bg=mainbg, fg=mainfg)

    # Place root (Login Fenster) Elements
    date.place(x=200, y=10, width=500, height=35)
    user_label.place(x=80, y=60, width=200, height=50)
    password_label.place(x=80, y=120, width=200, height=50)
    username.place(x=320, y=60, width=250, height=40)
    password.place(x=320, y=120, width=250, height=40)
    login.place(x=320, y=180, width=250, height=60)
    message.place(x=50, y=320, width=700, height=60)
    register.place(x=320, y=260, width=250, height=60)
    func_button.place(x=700, y=0, width=100, height=60)
    root.mainloop()

mainroot()
