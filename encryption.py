import random
from os import startfile
from tkinter import *
from tkinter.filedialog import askopenfilename


class Data:
    def __init__(self):
        self.dataWin = Tk()
        self.dataWin.title("Data")
        self.dataA = []
        self.dataB = []
        self.data1 = StringVar()
        self.data2 = StringVar()
        self.var = BooleanVar()

        labelPad = Label(self.dataWin, text="\t\t")
        labelPad.grid(row=0, column=1)

        label1 = Label(self.dataWin, text="Select Data:")
        label1.grid(row=0, column=0)

        buttonDef1 = Button(self.dataWin, text="Default 1",
                            font="Arial 12", padx=5, pady=5,
                            width=10,
                            command=lambda: self.premadeData("1"))
        buttonDef1.grid(row=0, column=1)

        buttonDef2 = Button(self.dataWin, text="Default 2",
                            font="Arial 12", padx=5, pady=5,
                            width=10,
                            command=lambda: self.premadeData("2"))
        buttonDef2.grid(row=1, column=1)

        buttonDef3 = Button(self.dataWin, text="Default 3",
                            font="Arial 12", padx=5, pady=5,
                            width=10,
                            command=lambda: self.premadeData("3"))
        buttonDef3.grid(row=2, column=1)

        buttonData1 = Button(self.dataWin, text="Create Data",
                             font="Arial 12", padx=5, pady=5,
                             width=10,
                             command=self.getData)
        buttonData1.grid(row=3, column=1)

    def premadeData(self, opt):
        if opt == "1":
            self.dataa = [1, 4, 6, 24, 54, 14, 2, 23, 1, 2, 32, 2, 43, 76]
            self.dataB = [2, 5, 74, 12, 23, 54, 76, 98, 23, 65, 1, 32, 5, 9]

        elif opt == "2":
            self.dataA = [10, 40, 60, 24, 54, 14, 20, 23, 10, 20, 32, 20, 43, 76]
            self.dataB = [20, 50, 74, 12, 23, 54, 76, 98, 23, 65, 10, 32, 50, 90]

        elif opt == "3":
            self.dataA = [10, 40, 60, 2, 5, 1, 20, 3, 10, 20, 3, 20, 4, 7]
            self.dataB = [20, 50, 7, 12, 3, 5, 7, 9, 23, 6, 10, 3, 50, 90]

        self.analysis()

    def getData(self):
        self.getWin = Toplevel()
        self.getWin.title("Get Data")

        labelData1 = Label(self.getWin, text="Data 1: ")
        labelData1.grid(row=0, column=0)

        labelData2 = Label(self.getWin, text="Data 2: ")
        labelData2.grid(row=1, column=0)

        userInputEntry1 = Entry(self.getWin, textvariable=self.data1,
                                width=10, relief=RAISED)
        userInputEntry1.grid(row=0, column=1)
        userInputEntry1.bind("<Return>", lambda event: self.addData("1"))

        userInputEntry2 = Entry(self.getWin, textvariable=self.data2,
                                width=10, relief=RAISED)
        userInputEntry2.grid(row=1, column=1)
        userInputEntry2.bind("<Return>", lambda event: self.addData("2"))

        buttonDone = Button(self.getWin, text="Done",
                            command=self.quitAndAnalyze)
        buttonDone.grid(row=2, column=0)

        return

    def quitAndAnalyze(self):
        self.getWin.destroy()
        self.analysis()

    def addData(self, opt):
        if opt == "1":
            self.dataA.append(int(self.data1.get()))
            self.data1.set("")
        elif opt == "2":
            self.dataB.append(int(self.data2.get()))
            self.data2.set("")

        return

    def Regression(self):
        return

    def analysis(self):
        self.analysisWin = Toplevel()
        self.analysisWin.title("Analysis")

        buttonTtest = Button(self.analysisWin, text="T-Test", command=self.Ttest)
        buttonTtest.grid(row=0, column=0)

        buttonRegression = Button(self.analysisWin, text="Linear Regression", command=self.Regression)
        buttonRegression.grid(row=0, column=1)

        buttonRegression = Button(self.analysisWin, text="Linear Regression", command=self.Regression)
        buttonRegression.grid(row=0, column=1)

    def Ttest(self):
        return

    def Regression(self):
        return

    def go(self):
        self.dataWin.mainloop()
        return


class Cipher:
    def __init__(self):
        self.rootWin = Tk()
        self.rootWin.title("Cipher")

        self.key = StringVar()
        self.var = BooleanVar()

        welcome = Label(self.rootWin,
                        text="Welcome to Cipher!",
                        font="Arial 15", padx=5, pady=5)
        welcome.grid(row=0, column=1)

        buttonEncrypt = Button(self.rootWin, text="Encrypt",
                               font="Arial 12", padx=5, pady=5,
                               width=20,
                               command=self.encrypt)
        buttonEncrypt.grid(row=1, column=0)

        buttonEncrypt = Button(self.rootWin, text="Open File",
                               font="Arial 11", padx=5, pady=5,
                               command=self.openFile)
        buttonEncrypt.grid(row=1, column=1)

        buttonDecrypt = Button(self.rootWin, text="Decrypt",
                               font="Arial 12", padx=5, pady=5,
                               width=20,
                               command=self.decrypt)
        buttonDecrypt.grid(row=1, column=2)

        buttonQuit = Button(self.rootWin, text="Quit",
                            font="Arial 10", padx=5, pady=5,
                            command=self.quit)
        buttonQuit.grid(row=2, column=1)

    def encrypt(self):
        file = open(pickAFile())
        encryption = Encryption(file)
        encryption.wait()
        print("Encrypted")
        return

    def openFile(self):
        file = pickAFile()
        startfile(file)

    def decrypt(self):
        file = open(pickAFile())
        opt = file.read(1)
        key = file.readline()[:-1]

        if opt == "c":
            decryptCaesar(file, key)
        elif opt == "v":
            decryptVigenere(file, key)
        elif opt == "u":
            decryptCustom(file, key)
        elif opt == "r":
            decryptCustom(file, key)
        else:
            print("Invalid Selection")

        print("Decrypted")

    def go(self):
        self.rootWin.mainloop()

    def quit(self):
        self.rootWin.destroy()


class Encryption:
    def encryptButtons(self, file):
        buttonCaesar = Button(self.encryptWin, text="Caesar",
                              font="Arial 12", padx=5, pady=5,
                              width=10,
                              command=lambda: self.selectEncryption("1", file))
        buttonCaesar.grid(row=0, column=1)

        buttonVigenere = Button(self.encryptWin, text="Vigenere",
                                font="Arial 12", padx=5, pady=5,
                                width=10,
                                command=lambda: self.selectEncryption("2", file))
        buttonVigenere.grid(row=1, column=1)

        buttonCustom = Button(self.encryptWin, text="Custom",
                              font="Arial 12", padx=5, pady=5,
                              width=10,
                              command=lambda: self.selectEncryption("3", file))
        buttonCustom.grid(row=2, column=1)

        buttonRandom = Button(self.encryptWin, text="Random",
                              font="Arial 12", padx=5, pady=5,
                              width=10,
                              command=lambda: self.selectEncryption("4", file))
        buttonRandom.grid(row=3, column=1)

    def __init__(self, file):
        self.encryptWin = Tk()
        self.encryptWin.title("Encryption")

        self.key = StringVar()
        self.var = BooleanVar()

        label1 = Label(self.encryptWin,
                       text="Encryption:",
                       padx=5, pady=5)
        label1.grid(row=0, column=0)

        self.encryptButtons(file)

    def getKey(self):
        self.keyWin = Toplevel()
        self.keyWin.title("Key")

        keyLabel = Label(self.keyWin, text="Key:",
                         padx=5, pady=5)
        keyLabel.grid(row=0, column=0)

        userInputEntry = Entry(self.keyWin, textvariable=self.key,
                               width=10, relief=RAISED)
        userInputEntry.grid(row=0, column=3)

        userInputEntry.bind("<Return>", self.regKey)
        userInputEntry.bind("<Tab>", self.regKey)

    def getCustomKey(self):
        self.customKeyWin = Toplevel()

        labelKey = Label(self.customKeyWin, text="Select a key:",
                         padx=5, pady=5)
        labelKey.grid(row=0, column=0)

        button1 = Button(self.customKeyWin, text="Key #1",
                         font="Arial 12", padx=5, pady=5,
                         width=10,
                         command=lambda: self.premadeKey("1"))
        button1.grid(row=0, column=1)

        button2 = Button(self.customKeyWin, text="Key #2",
                         font="Arial 12", padx=5, pady=5,
                         width=10,
                         command=lambda: self.premadeKey("2"))
        button2.grid(row=1, column=1)

        button3 = Button(self.customKeyWin, text="Key #3",
                         font="Arial 12", padx=5, pady=5,
                         width=10,
                         command=lambda: self.premadeKey("3"))
        button3.grid(row=2, column=1)

        buttonCreate = Button(self.customKeyWin, text="Create a key",
                              font="Arial 12", padx=5, pady=5,
                              width=10,
                              command=self.createKey)
        buttonCreate.grid(row=3, column=1)

    def premadeKey(self, opt):
        global customKey
        if opt == "1":
            customKey = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v',
                         'j': 'w',
                         'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f',
                         't': 'g',
                         'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
                         '0': '6', '1': '9', '2': '5', '3': '2', '4': '7', '5': '0', '6': '8', '7': '3', '8': '4',
                         '9': '1'}

        elif opt == "2":
            customKey = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o',
                         'j': 'p',
                         'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l',
                         't': 'z',
                         'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm',
                         '0': '1', '1': '0', '2': '2', '3': '9', '4': '3', '5': '8', '6': '4', '7': '7', '8': '5',
                         '9': '6'}

        elif opt == "3":
            customKey = {'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z', 'h': 'l', 'i': 'k',
                         'j': 'j',
                         'k': 'h', 'l': 'g', 'm': 'f', 'n': 'd', 'o': 's', 'p': 'a', 'q': 'p', 'r': 'o', 's': 'i',
                         't': 'u',
                         'u': 'y', 'v': 't', 'w': 'r', 'x': 'e', 'y': 'w', 'z': 'q',
                         '0': '5', '1': '6', '2': '4', '3': '7', '4': '3', '5': '8', '6': '2', '7': '9', '8': '1',
                         '9': '0'}

        self.customKeyWin.destroy()

    def createKeyEntries(self):
        charLeft = []
        charRight = []
        numLeft = []
        numRight = []
        self.entries = 36

        for i in range(13):
            charLeft.append(Entry(self.inputKey, width=10))
            charLeft[i].grid(row=i, column=1)
            charLeft[i].bind("<Return>",
                             lambda event, entry=charLeft[i], char=chr(i + 97): self.cusKey(entry, char))
            charLeft[i].bind("<Tab>",
                             lambda event, entry=charLeft[i], char=chr(i + 97): self.cusKey(entry, char))

        for i in range(13):
            charRight.append(Entry(self.inputKey, width=10))
            charRight[i].grid(row=i, column=3)
            charRight[i].bind("<Return>",
                              lambda event, entry=charRight[i], char=chr(i + 110): self.cusKey(entry, char))
            charRight[i].bind("<Tab>",
                              lambda event, entry=charRight[i], char=chr(i + 110): self.cusKey(entry, char))

        for i in range(5):
            numLeft.append(Entry(self.inputKey, width=10))
            numLeft[i].grid(row=i + 14, column=1)
            numLeft[i].bind("<Return>",
                            lambda event, entry=numLeft[i], char=chr(i + 48): self.cusKey(entry, char))
            numLeft[i].bind("<Tab>",
                            lambda event, entry=numLeft[i], char=chr(i + 48): self.cusKey(entry, char))

        for i in range(5):
            numRight.append(Entry(self.inputKey, width=10))
            numRight[i].grid(row=i + 14, column=3)
            numRight[i].bind("<Return>",
                             lambda event, entry=numRight[i], char=chr(i + 53): self.cusKey(entry, char))
            numRight[i].bind("<Tab>",
                             lambda event, entry=numRight[i], char=chr(i + 53): self.cusKey(entry, char))

    def createKeyLabels(self):
        charLeft = []
        charRight = []
        numLeft = []
        numRight = []

        for i in range(13):
            charLeft.append(Label(self.inputKey, text=chr(i + 97) + ":", padx=5, pady=5))
            charLeft[i].grid(row=i, column=0)

        for i in range(13):
            charRight.append(Label(self.inputKey, text=chr(i + 110) + ":", padx=5, pady=5))
            charRight[i].grid(row=i, column=2)

        for i in range(5):
            numLeft.append(Label(self.inputKey, text=chr(i + 48) + ":", padx=5, pady=5))
            numLeft[i].grid(row=i + 14, column=0)

        for i in range(5):
            numRight.append(Label(self.inputKey, text=chr(i + 53) + ":", padx=5, pady=5))
            numRight[i].grid(row=i + 14, column=2)

    def createKey(self):
        global customKey
        customKey = {}

        self.entriesLeft = StringVar()

        self.inputKey = Toplevel()
        self.inputKey.title("Create Key")

        self.createKeyLabels()

        self.createKeyEntries()

        self.buttonDone = Button(self.inputKey, text="Done",
                                 state=DISABLED,
                                 command=self.inputKey.destroy)
        self.buttonDone.grid(row=20, column=0)

        labelLeft = Label(self.inputKey, text="Entries Left: ", textvariable=self.entriesLeft)
        labelLeft.grid(row=20, column=3)
        self.entriesLeft.set(str(self.entries))

        self.inputKey.wait_window(self.inputKey)

        self.customKeyWin.destroy()

    def regKey(self, event):
        self.key = self.key.get()
        self.keyWin.destroy()

    def cusKey(self, entry, char):
        j = 0
        key = entry.get()

        if key.isalnum() and len(key) == 1:
            if key.isalpha():
                key = key.lower()

            for i in customKey:
                if customKey[i] == key:
                    j = 1

            customKey[char] = key
        else:
            j = 1

        if j == 0:
            entry['bg'] = "Light Green"
            self.entries -= 1
            if self.entries == 0:
                self.buttonDone['state'] = NORMAL
        elif entry['bg'] != "Red":
            if entry['bg'] == "Light Green":
                self.entries += 1
            entry['bg'] = "Red"
            customKey[char] = ""

            if self.entries != 0:
                self.buttonDone['state'] = DISABLED

        self.entriesLeft.set(str(self.entries))

    def selectEncryption(self, opt, file):
        if opt == "1":
            self.getKey()
            self.keyWin.wait_window(self.keyWin)
            encryptCaesar(file, self.key)
            self.encryptWin.destroy()
        elif opt == "2":
            self.getKey()
            self.keyWin.wait_window(self.keyWin)
            encryptVigenere(file, self.key)
            self.encryptWin.destroy()
        elif opt == "3":
            self.getCustomKey()
            self.customKeyWin.wait_window(self.customKeyWin)
            encryptCustom(file, customKey)
            self.encryptWin.destroy()
        elif opt == "4":
            encryptRandom(file)
            self.encryptWin.destroy()

    def wait(self):
        self.encryptWin.wait_window(self.encryptWin)


def encryptCaesar(file, key):
    numKey = (ord(key) % 32) % 10
    chrKey = ord(key) % 32
    newText = "c" + key + "\n"
    textToEncrypt = file.read()

    for letter in textToEncrypt:
        if letter.isnumeric():
            newLetter = ord(letter) + numKey
            if newLetter > 57:
                newLetter -= 10

            newText += str(chr(newLetter))

        elif letter.isalpha():
            newLetter = ord(letter) + chrKey
            if (letter.islower() and newLetter > 122) or (letter.isupper() and newLetter > 90):
                newLetter -= 26

            newText += str(chr(newLetter))

        else:
            newText += letter

    createFile(file, newText, "CaesarEncrypted.txt")

    return


def decryptCaesar(file, key):
    numKey = (ord(key) % 32) % 10
    chrKey = ord(key) % 32
    newText = ""
    textToEncrypt = file.read()

    for letter in textToEncrypt:
        if letter.isnumeric():
            newLetter = ord(letter) - numKey
            if newLetter < 48:
                newLetter += 10

            newText += str(chr(newLetter))

        elif letter.isalpha():
            newLetter = ord(letter) - chrKey
            if (letter.islower() and newLetter < 97) or (letter.isupper() and newLetter < 65):
                newLetter += 26

            newText += str(chr(newLetter))

        else:
            newText += letter

    createFile(file, newText, "Decrypted.txt")

    return


def encryptVigenere(file, key):
    i = 0
    keyLen = len(key)
    newText = "v" + key + "\n"
    textToEncrypt = file.read()

    for letter in textToEncrypt:
        if letter.isnumeric():
            newLetter = ord(letter) + ((ord(key[i]) % 32) % 10)
            if newLetter > 57:
                newLetter -= 10

            i += 1
            if i == keyLen:
                i = 0

            newText += str(chr(newLetter))

        elif letter.isalpha():
            newLetter = ord(letter) + (ord(key[i]) % 32)
            if (letter.islower() and newLetter > 122) or (letter.isupper() and newLetter > 90):
                newLetter -= 26

            i += 1
            if i == keyLen:
                i = 0

            newText += str(chr(newLetter))

        else:
            newText += letter

    createFile(file, newText, "VigenereEncrypted.txt")

    return


def decryptVigenere(file, key):
    i = 0
    keyLen = len(key)
    newText = ""
    textToDecrypt = file.read()

    for letter in textToDecrypt:
        if letter.isnumeric():
            newLetter = ord(letter) - ((ord(key[i]) % 32) % 10)
            if newLetter < 48:
                newLetter += 10

            i += 1
            if i == keyLen:
                i = 0

            newText += str(chr(newLetter))

        elif letter.isalpha():
            newLetter = ord(letter) - (ord(key[i]) % 32)
            if (letter.islower() and newLetter < 97) or (letter.isupper() and newLetter < 65):
                newLetter += 26

            i += 1
            if i == keyLen:
                i = 0

            newText += str(chr(newLetter))

        else:
            newText += letter

    createFile(file, newText, "Decrypted.txt")

    return


def encryptCustom(file, key):
    newText = "u"
    for i in key:
        newText += i + key[i]
    newText += "\n"
    textToEncrypt = file.read()

    for letter in textToEncrypt:
        if letter.isalnum():
            if letter.isupper():
                newText += key[letter.lower()].upper()
            else:
                newText += key[letter]
        else:
            newText += letter

    createFile(file, newText, "CustomEncrypted.txt")

    return


def encryptRandom(file):
    key = {}

    numList = list(range(0, 26))
    for i in range(26):
        num = random.randrange(0, 26 - i)
        key[chr(i + 97)] = chr(numList[num] + 97)
        del numList[num]

    numList = list(range(0, 10))
    for i in range(10):
        num = random.randrange(0, 10 - i)
        key[chr(i + 48)] = chr(numList[num] + 48)
        del numList[num]

    newText = "r"
    for i in key:
        newText += i + key[i]
    newText += "\n"

    textToEncrypt = file.read()

    for letter in textToEncrypt:
        if letter.isalnum():
            if letter.isupper():
                newText += key[letter.lower()].upper()
            else:
                newText += key[letter]
        else:
            newText += letter

    createFile(file, newText, "RandomEncrypted.txt")

    return


def decryptCustom(file, key):
    decryptKey = {}
    length = len(key)
    for i in range(0, length, 2):
        decryptKey[key[i + 1]] = key[i]

    newText = ""
    textToDecrypt = file.read()

    for letter in textToDecrypt:
        if letter.isalnum():
            if letter.isupper():
                newText += decryptKey[letter.lower()].upper()
            else:
                newText += decryptKey[letter]
        else:
            newText += letter

    createFile(file, newText, "Decrypted.txt")

    return


def createFile(file, newText, name):
    nameFile = file.name[:-4] + name
    newFile = open(nameFile, "w")
    newFile.write(newText)
    newFile.close()


def pickAFile():
    file = askopenfilename()
    if file == None:
        print("No File Selected")
        return ""
    else:
        return file


cipher = Cipher()
cipher.go()
