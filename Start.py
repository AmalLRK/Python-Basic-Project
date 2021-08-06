import base64
from File import *
from Def import *

#CreatImage()uhze
#CreatExe()


print("Bonjour et bienvenue dans mon univer")
print("jJe m'appelle ADMIL, et l'objectif de jeux et de trouver l'assassin ")
print("Vous avez trois indices pour le trouvez")
print("C'est parti, 1er question pour ouvrir les portes !!!!!!!")

MonAge()

print("Bravo, vous avez lancer le jeu, 1er étape vous devez trouver le lieu de crime")
print("Pour cela, un fichier sera généré dans le même répertoire pour vous aider à trouver le 1er indice")

CreatImage()
LieuDeCrime()

print("Félicitation, vous avez trouvez le lieu de crime")
print("Un autre fichier sera généré dans le même répertoire pour vous aider à trouver l’arme de crime")

CreatExe()
ArmeDeCrime()

print("##############################################################################")
print("Félicitation vous avez trouvez les 3 indices => l’assassin est « AMAL LARZAK »")
print("##############################################################################")