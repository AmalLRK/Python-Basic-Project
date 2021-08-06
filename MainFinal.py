from File import *
from tkinter import *
from tkinter import messagebox

import tkinter as tk
level = 0
def checkAnswer(var):
    global level
    if level == 0:
        monAge(var)
    else :
        if level == 1:
            lieuDeCrime(var)
        else :
            if level == 2:
                armeDeCrime(var)
def initFormul():
    global window, entry
    #mettre à jour le niveau du jeu
    window.title("Jeu d'Assassin - Etape "+str(level+1))
    #vider le texte et le label de reponse
    entry.delete(0, tk.END)
    entry.insert(0, "")
    label_reponse.configure(text="", font=("Arial,40"), bg='#ADD8E6', fg='#ADD8E6')
def monAge(age):

    if age == '3.9':
        messagebox.showinfo("Bravo", "vous avez lancer le jeu, 1er étape vous devez trouver le lieu de crime\n"
                                     "Pour cela, un fichier sera généré dans le même répertoire pour vous aider à trouver le 1er indice")
        CreatImage()
        global level
        level = 1
        initFormul()

    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')
def lieuDeCrime(lieu):
    if lieu == 'TRIESTE':
        messagebox.showinfo("Bravo", "Félicitation, vous avez trouvez le lieu de crime\n"
                                     "Un autre fichier sera généré dans le même répertoire pour vous aider à trouver l’arme de crime")
        CreatExe()
        global level
        level = 2
        initFormul()
    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')
def armeDeCrime(arme):
    if arme == 'arme':
        label_reponse.configure(text="#################################################\n"
                                    "Félicitation vous avez trouvez les 3 indices \n l’assassin est « AMAL LARZAK »\n"
                                    "##################################################",
                                font=("Arial,40"), bg='green', fg='white')
    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')
def centerWindow(windowName):
    # set center screen window with following coordination
    MyLeftPos = (windowName.winfo_screenwidth() - 500) / 2
    myTopPos = (windowName.winfo_screenheight() - 350) / 2
    windowName.geometry("%dx%d+%d+%d" % (500, 350, MyLeftPos, myTopPos))


#pour l'affichage
window = Tk()
window.title("Jeu d'Assassin - Etape 1")
centerWindow(window)
window.config(background='#ADD8E6')

#pour l'icon
window.iconbitmap('C:\\Users\\Amal\\OneDrive\\Documents\\Projet python\\Assassin-V1\\Assassin-V1\\ninja.ico')

label_title = Label(window, text="\n\nBienvenue sur l'application\n", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_title.pack()

#code texte
entry=Entry(window, font=("Arial,40"), bg='white', fg='#ADD8E6')
entry.pack()

#pour sauter la ligne
label = Label(window, text='\n', bg='#ADD8E6', fg='#ADD8E6')
label.pack()

#code button enter
button=Button(window, text="Entrer" , font=("Arial,40"), bg='white', fg='#ADD8E6', command=lambda : checkAnswer(entry.get()))
button.pack()

#pour sauter la ligne
label = Label(window, text='\n', bg='#ADD8E6', fg='#ADD8E6')
label.pack()

#code label de reponse
label_reponse = Label(window, text="", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_reponse.pack()
#window.bind('<Return>', checkAnswer(entry.get()))
window.mainloop()




