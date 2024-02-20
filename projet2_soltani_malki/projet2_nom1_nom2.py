import pygame_min
from typing import List
from random import randint

murs = [[1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1] , \
[1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1] , \
[1 , 0 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 1] , \
[1 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 1] , \
[1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 1] , \
[1 , 0 , 1 , 0 , 1 , 0 , 0 , 1 , 0 , 1] , \
[1 , 0 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 1] , \
[1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 1] , \
[1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1] , \
[1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1]]

ennemis = [[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]]

tresors = [[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0] , \
[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]]

position_joueur = [5, 5]
position_precedente_joueur = [0, 4]
sortie = [0, 4]

def il_y_a_un_mur ( x : int , y : int ) -> bool :
    # on recupere la valeur a la position x,y du tableau et on verifie si il y a un 1.
    return murs[x][y] == 1


def il_y_a_un_ennemi(x: int, y: int) -> bool :
    return ennemis[x][y] == 1


def il_y_a_un_tresor(x: int, y: int ) -> bool :
    return tresors[x][y] == 1


def obtenir_position_joueur() -> List[int] :
    return position_joueur


def deplacer_joueur ( x : int , y : int ) -> None :
    global position_joueur
    global position_precedente_joueur
    position_precedente_joueur = position_joueur
    position_joueur = [x, y]
    arriver_case()


def arriver_case() -> None :
    global position_joueur
    xPositionJoueur = position_joueur[0]
    yPositionJoueur = position_joueur[1]

    if (il_y_a_un_mur(xPositionJoueur, yPositionJoueur )) :
        print("il y a un mur")

    if (il_y_a_un_ennemi(xPositionJoueur, yPositionJoueur)) :
        print("il y a un ennemi")

    if (il_y_a_un_tresor(xPositionJoueur, yPositionJoueur)) :
        print("il y a un tresor")

def jouer() -> None:
    """
    Description :
    --------- ----
    Cette fonction est la fonction principale de votre RPG .
    Parametres :
    ------------
    Retours :
    ---------
    ( None )
    """

    # On fait le lien avec les variables globales
    global position_joueur
    # On deplace le joueur sur sa position initiale
    x = position_joueur[0]
    y = position_joueur[1]
    deplacer_joueur(x, y)

def sortir () -> None :
    print("le jeu es terminé")


def deplacement () -> None :
    global position_joueur
    #on defini x et y afin de pouvoir les utuliser dans la condition .
    x = position_joueur[0]
    y = position_joueur[1]
    # on donne à direction la direction entrée par l'utilisateur
    direction = input("Dans quelle direction voulez-vous aller?")
    # si l'utilisateur a rentré Nord alors on rentre dans le if
    print("direction choisie est :", direction)
    if(direction == "Nord"):
        print("le joueur va au nord")
        # comme la direction choisie est le nord, on fait y = -1
        y -= 1
        #condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
        if(y >= 0) and (sortie != [x, y]) :
            deplacer_joueur(x, y)
            #est ce que x et y sont = a la sortie
        elif (sortie == [x, y]) :
            sortir()

        else :
            deplacement()


    if (direction == "Sud"):
         print("le joueur va au Sud")
         # comme la direction choisie est le Sud, on fait y = -1
         y += 1
         # condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
         if (y<=len(murs)) and (sortie != [x, y]):
            deplacer_joueur(x, y)
             # est ce que x et y sont = a la sortie
         elif (sortie == [x, y]):
              sortir()

         else :
            deplacement()

    if (direction == "Ouest"):
        print("le joueur va a l'Ouest")
        # comme la direction choisie est l'Ouest, on fait x = -1
        x -= 1
        #condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
        if (x >= 0) and (sortie != [x, y]):
            deplacer_joueur(x, y)
            # est ce que x et y sont = a la sortie
        elif (sortie == [x, y]):
            sortir()

        else :
            deplacement()

        if (direction == "Est"):
            print("le joueur va au Est")
            # comme la direction choisie est l'Est, on fait x = -1
            x += 1
            # condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
            if (x <= len(murs)) and (sortie != [x, y]):
                deplacer_joueur(x, y)
                # est ce que x et y sont = a la sortie
            elif (sortie == [x, y]):
                sortir()

            else:
                deplacement()
    print("fin de la fonction déplacement")

def reculer () -> None :
    global position_precedente_joueur
    global position_joueur
    position_precedente_joueur = position_joueur

def detruire_mur ( x : int , y : int ) -> None :
    global murs
    murs[x][y] = 0





jouer()





