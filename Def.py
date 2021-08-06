def MonAge():
    while True:
        Age = input('Mon age est  :  ')
        if Age == '3.9':
            break
        else:
            print("!!!! Erreur, il faut réessayer !!!!")

def LieuDeCrime():
    while True:
        Lieu = input('Le lieu de crime est  :   ')
        if Lieu == 'TRIESTE':
            break
        else:
            print("!!!! Erreur, il faut réessayer !!!!")

def ArmeDeCrime():
    while True:
        Arme = input('L\'arme de crime est  :  ')
        if Arme == 'ADMIN+PASSWORD':
            break
        else:
            print("!!!! Erreur, il faut réessayer !!!!")
