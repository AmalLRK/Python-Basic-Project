from File import *
from tkinter import *
from tkinter import messagebox
from File import *
def main():
    main_window = Tk()
    app = first_level(main_window)
    main_window.mainloop()

def centerWindow(windowName):
    # set center screen window with following coordination
    MyLeftPos = (windowName.winfo_screenwidth() - 500) / 2
    myTopPos = (windowName.winfo_screenheight() - 300) / 2
    windowName.geometry("%dx%d+%d+%d" % (500, 300, MyLeftPos, myTopPos))


class first_level:
    def __init__(self, root):
        CreatImage()
        self.root = root
        self.root.title("Jeu d'Assassin - Etape 1")
        centerWindow(self.root)
        self.root.config(background='#ADD8E6')
        label_title = Label(self.root, text="\n\nBienvenue sur l'application", font=("Arial,40"), bg='#ADD8E6',
                            fg='white')
        label_title.pack()
        entry = Entry(self.root, font=("Arial,40"), bg='white', fg='#ADD8E6')
        entry.pack()
        button = Button(self.root, text="Entrer", font=("Arial,40"), bg='white', fg='#ADD8E6',
                        command=lambda : self.second_window(entry.get()))
        button.pack()

    def second_window(self, age):
        if age == '3.9':
            messagebox.showinfo("Bravo", "vous avez lancer le jeu, 1er étape vous devez trouver le lieu de crime\n"
                                         "Pour cela, un fichier sera généré dans le même répertoire pour vous aider à trouver le 1er indice")
            CreatImage()
            self.new_window = Tk()
            self.app = second_level(self.new_window)
            self.root.destroy()
        else:
            messagebox.showerror("Erreur", "!!!! Erreur, il faut réessayer !!!!")


class second_level:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu d'Assassin - Etape 2")
        centerWindow(self.root)
        self.root.config(background='#ADD8E6')

        label_title = Label(self.root, text="\n\nBienvenue sur l'application", font=("Arial,40"), bg='#ADD8E6',
                            fg='white')
        label_title.pack()
        # code texte
        entry = Entry(self.root, font=("Arial,40"), bg='white', fg='#ADD8E6')
        entry.pack()
        # code button enter
        button = Button(self.root, text="Entrer", font=("Arial,40"), bg='white', fg='#ADD8E6',
                        command=lambda : self.third_window(entry.get()))
        button.pack()

    def third_window(self, lieu):
        if lieu == 'TRIESTE':
            messagebox.showinfo("Bravo", "Félicitation, vous avez trouvez le lieu de crime\n"
                                         "Un autre fichier sera généré dans le même répertoire pour vous aider à trouver l’arme de crime")
            CreatExe()
            self.new_window = Tk()
            self.app = third_level(self.new_window)
            self.root.destroy()
        else:
            messagebox.showerror("Erreur", "!!!! Erreur, il faut réessayer !!!!")


class third_level:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu d'Assassin - Etape 3")
        centerWindow(self.root)
        self.root.config(background='#ADD8E6')

        label_title = Label(self.root, text="\n\nBienvenue sur l'application", font=("Arial,40"), bg='#ADD8E6',
                            fg='white')
        label_title.pack()
        # code texte
        entry = Entry(self.root, font=("Arial,40"), bg='white', fg='#ADD8E6')
        entry.pack()
        # code button enter
        button = Button(self.root, text="Entrer", font=("Arial,40"), bg='white', fg='#ADD8E6',
                        command=lambda : self.final_window(entry.get()))
        button.pack()

    def final_window(self, arme):
        if arme == 'ADMIN+PASSWORD':
            messagebox.showinfo("Bravo", "#################################################\n"
                                         "Félicitation vous avez trouvez les 3 indices \n l’assassin est « AMAL LARZAK »\n"
                                         "##################################################")
        else:
            messagebox.showerror("Erreur", "!!!! Erreur, il faut réessayer !!!!")
if __name__ == '__main__':
    main()