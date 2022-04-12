from cProfile import label
import random
import os
import json
from tkinter import *
from turtle import clear, color

passwordTab = []
serviceTab = []
labelTab = []

def generatePassword(e):
    global labelTab
    if(serviceInput.get()):
        serviceChoice = serviceInput.get()
        listOfCaracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&-?./+%*_#'
        password=''
        for i in range(0,16):
            password+=listOfCaracteres[random.randint(0,len(listOfCaracteres)-1)]
        if(len(passwordTab) == 0 and len(serviceTab) == 0):
            passwordTab.append(password)
            serviceTab.append(serviceChoice)
            var = StringVar()
            var.set(password)
            passwordGenerated.config(textvariable=var)
            labelTab.append(Label(root,text=serviceChoice+' : '+password, justify=CENTER).pack())
        if(passwordTab[len(passwordTab)-1] != password and 
        serviceTab[len(serviceTab)-1] != serviceChoice):
            passwordTab.append(password)
            serviceTab.append(serviceChoice)
            var = StringVar()
            var.set(password)
            passwordGenerated.config(textvariable=var)
            labelTab.append(Label(root,text=serviceChoice+' : '+password, justify=CENTER).pack())

def generatePasswordButton():
    if(serviceInput.get()):
        serviceChoice = serviceInput.get()
        listOfCaracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&-?./+%*_#'
        password=''
        for i in range(0,16):
            password+=listOfCaracteres[random.randint(0,len(listOfCaracteres)-1)]
        if(len(passwordTab) == 0 and len(serviceTab) == 0):
            passwordTab.append(password)
            serviceTab.append(serviceChoice)
            var = StringVar()
            var.set(password)
            passwordGenerated.config(textvariable=var)
            labelTab.append(Label(root,text=serviceChoice+' : '+password, justify=CENTER).pack())
        if(passwordTab[len(passwordTab)-1] != password and 
        serviceTab[len(serviceTab)-1] != serviceChoice):
            passwordTab.append(password)
            serviceTab.append(serviceChoice)
            var = StringVar()
            var.set(password)
            passwordGenerated.config(textvariable=var)
            labelTab.append(Label(root,text=serviceChoice+' : '+password, justify=CENTER).pack())
    
def getService():
    global pathToSave
    serviceChoice = serviceInput.get()
    password = passwordGenerated.get()
    result = ''
    path = pathToSave.get()
    os.chdir(path)
    print(path)
    for i in range(len(passwordTab)):
        result += serviceTab[i] + ' : ' + passwordTab[i] + '\n'
    if(result):
        os.system('echo '+ str(json.dumps(result)) + ' > password.txt')
        os.system('open password.txt')
        print('Le fichier password.txt a été créé dans le chemin ',path,' .')


def windows():
    ##########
    global root, passwordGenerated, serviceInput, pathToSave
    root = Tk()
    widgetFrame1 = Frame(root)
    root.geometry('400x700')
    root.resizable(False, False)
    root.title("GMDP")
    titleName = Label(root, text="Gestionnaire de mot de passe", justify=CENTER,font=('Arial', 25)).pack(pady=20)
    ##########
    serviceLabel = Label(root, text='Service à utiliser : ').pack()
    serviceInput = Entry(root, justify=CENTER)
    passwordGenerated = Entry(root, state='readonly', justify=CENTER)
    generateButton = Button(widgetFrame1,text="Générer", command=generatePasswordButton).pack(side=LEFT)
    listOfPassword = Label(root, text='Liste de mot de passe généré : ', justify=CENTER)
    savePass = Button(root, justify=CENTER, text='Enregistrer en .txt', command=getService)
    pathToSave = Entry(root,justify=CENTER)
    pathToSaveLabel = Label(root, text='Chemin complet pour enregistrer le fichier : (/Users/...)', justify=CENTER)

    ##########
    close = Button(widgetFrame1,text="Quitter", command=root.destroy).pack(side=LEFT)
    serviceInput.pack(pady=5)
    widgetFrame1.pack()
    passwordGenerated.pack(pady=10)
    savePass.pack(side=BOTTOM, pady=20)
    pathToSave.pack(side=BOTTOM)
    pathToSaveLabel.pack(side=BOTTOM, pady=10)
    listOfPassword.pack(pady=10)
    root.bind('<Return>', generatePassword)
    root.mainloop()

windows()
