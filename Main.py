from File import *
from tkinter import *
from tkinter import messagebox

import tkinter as tk

def monAge(age):

    if age == '3.9':
        label_reponse.configure(text="Bravo", font=("Arial,40"),bg='#ADD8E6', fg='green')
        messagebox.showinfo("Bravo", "vous avez lancer le jeu, 1er étape vous devez trouver le lieu de crime\n"
                                     "Pour cela, un fichier sera généré dans le même répertoire pour vous aider à trouver le 1er indice")
        CreatImage()
        window_age.destroy()
    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')
def lieuDeCrime(lieu):
    if lieu == 'TRIESTE':
        label_reponse.configure(text="Bravo", font=("Arial,40"),bg='#ADD8E6', fg='green')
        messagebox.showinfo("Bravo", "Félicitation, vous avez trouvez le lieu de crime\n"
                                     "Un autre fichier sera généré dans le même répertoire pour vous aider à trouver l’arme de crime")
        CreatExe()
        window_lieu.destroy()
    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')
def armeDeCrime(arme):
    if arme == 'ADMIN+PASSWORD':
        label_reponse.configure(text="#################################################\n"
                                    "Félicitation vous avez trouvez les 3 indices \n l’assassin est « AMAL LARZAK »\n"
                                    "##################################################",
                                font=("Arial,40"), bg='green', fg='white')
    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')
def centerWindow(windowName):
    # set center screen window with following coordination
    MyLeftPos = (windowName.winfo_screenwidth() - 500) / 2
    myTopPos = (windowName.winfo_screenheight() - 300) / 2
    windowName.geometry("%dx%d+%d+%d" % (500, 300, MyLeftPos, myTopPos))


#pour l'age
window_age = Tk()
window_age.title("Jeu d'Assassin - Etape 1")
centerWindow(window_age)
window_age.config(background='#ADD8E6')

label_title = Label(window_age, text="\n\nBienvenue sur l'application", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_title.pack()
#code texte
entry=Entry(window_age, font=("Arial,40"), bg='white', fg='#ADD8E6')
entry.pack()
#code button enter
button=Button(window_age, text="Entrer" , font=("Arial,40"), bg='white', fg='#ADD8E6', command=lambda : monAge(entry.get()))
button.pack()
#code label
label_reponse = Label(window_age, text="", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_reponse.pack()
window_age.mainloop()

#pour le lieu
window_lieu = Tk()
window_lieu.title("Jeu d'Assassin - Etape 2")
centerWindow(window_lieu)
window_lieu.config(background='#ADD8E6')

label_title = Label(window_lieu, text="\n\nBienvenue sur l'application", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_title.pack()
#code texte
entry=Entry(window_lieu, font=("Arial,40"), bg='white', fg='#ADD8E6')
entry.pack()
#code button enter
button=Button(window_lieu, text="Entrer" , font=("Arial,40"), bg='white', fg='#ADD8E6', command=lambda : lieuDeCrime(entry.get()))
button.pack()
#code label
label_reponse = Label(window_lieu, text="", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_reponse.pack()
window_lieu.mainloop()

#pour l'arme
window_arme = Tk()
window_arme.title("Jeu d'Assassin - Etape 3")
centerWindow(window_arme)
window_arme.config(background='#ADD8E6')

label_title = Label(window_arme, text="\n\nBienvenue sur l'application", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_title.pack()
#code texte
entry=Entry(window_arme, font=("Arial,40"), bg='white', fg='#ADD8E6')
entry.pack()
#code button enter
button=Button(window_arme, text="Entrer" , font=("Arial,40"), bg='white', fg='#ADD8E6', command=lambda : armeDeCrime(entry.get()))
button.pack()
#code label
label_reponse = Label(window_arme, text="", font=("Arial,40"), bg='#ADD8E6', fg='white')
label_reponse.pack()
window_arme.mainloop()

