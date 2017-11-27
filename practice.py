from tkinter import *


class Encryption():
    def __init__(self):
        self.encryptWin = Tk()
        self.input = StringVar()
        self.var = BooleanVar()

        button = Button(self.encryptWin, text="Caesar",
                        command=self.key)
        button.grid(row=0, column=0)

    def key(self):
        self.keyWin = Toplevel()

        button = Button(self.keyWin, text="Key:",
                        command=self.respond)
        button.grid(row=0, column=0)

        userInputEntry = Entry(self.keyWin, textvariable=self.input,
                               width=10, relief=RAISED)
        userInputEntry.grid(row=0, column=3)

        userInputEntry.bind("<Return>", self.respond)
        userInputEntry.bind("<Tab>", self.respond)

    def respond(self, event):
        self.input = self.input.get()
        self.keyWin.destroy()
        self.var.set(1)

    def wait(self):
        self.encryptWin.wait_variable(self.var)

class Hi():
    def __init__(self):
        self.win = Tk()
        self.key = StringVar()
        self.text = StringVar()
        self.text.set("Hi")

        x = 0

        self.createKeyEntries()

    def update(self, x):
        self.text.set("Bye")
        self.key.set("Hello")
        x = 1
        return x

    def printf(self, x):
        print(x)

    def go(self):
        self.win.mainloop()


    def createKeyEntries(self):
        entriesleft = []

        for i in range(13):
            entriesleft.append(Entry(self.win, width=10))
            entriesleft[i].grid(row=i, column=1)

        entriesright = []
        for i in range(13):
            entriesright.append(Entry(self.win, width=10))
            entriesright[i].grid(row=i, column=3)
            entriesright[i].bind("<Return>", lambda event, entry = entriesright[i]: self.respond(entry))

    def respond(self, entry):
        print(entry.get())
        entry['bg'] = "Light Green"

hi = Hi()
hi.go()