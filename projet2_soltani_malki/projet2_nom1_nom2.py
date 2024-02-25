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
tresors_collectes = 0
ennemis_vaincus = 0
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
        detruireMur = input("souhaitez-vous détruire le mur ?")
        if (detruireMur == "Oui") :
            detruire_mur(xPositionJoueur, yPositionJoueur)
        else:
            reculer()
        deplacement()

    if (il_y_a_un_ennemi(xPositionJoueur, yPositionJoueur)) :
        print("il y a un ennemi")
        reponse = input("souhaitez-vous affronter l'ennemi ?")
        if (reponse == "Oui") :
            if(affronter_ennemi(xPositionJoueur, yPositionJoueur) == False ) :
                reculer()
        else:
            reculer()
    if (il_y_a_un_tresor(xPositionJoueur, yPositionJoueur)) :
        reponse = input("souhaitez-vous ramasser le trésor ?")
        if (reponse == "Oui") :
            ramasser_tresor(xPositionJoueur, yPositionJoueur)
        deplacement()


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
    deplacement()
def sortir () -> None :
    global ennemis_vaincus
    global tresors_collectes
    print("le nombre d'ennemi(s) vaincu(s) est de :", ennemis_vaincus)
    print("le nombre de tresor(s) collecté(s) est de :", tresors_collectes)
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
    elif (direction == "Sud"):
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
    elif (direction == "Ouest"):
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
    elif (direction == "Est"):
        print("le joueur va à  Est")
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
    elif (direction == "useralg213"):
        tueToutLesEnnemis()
    print("fin de la fonction déplacement")



def reculer () -> None :
    global position_precedente_joueur
    global position_joueur
    print("vous allez reculer voila l'ancienne position du joueur:",position_joueur)
    position_joueur = position_precedente_joueur
    print("vous avez reculer voici votre position actuel :", position_joueur)


def detruire_mur ( x : int , y : int ) -> None :
    global murs
    #on enleve le mur donc les coordonées doivent etre egales à 0 .
    murs[x][y] = 0
    print("vous avez detrui un mur !")

def ramasser_tresor ( x : int , y : int ) -> None :
    global tresors_collectes
    tresors_collectes += 1
    print("vous venez d'acquerir un nouveau tresor : Bravo! ")
    print("le nombre de tresors collectés jusqu'à présent est de :", tresors_collectes)

def affronter_ennemi ( x : int , y : int ) -> bool :
    global ennemis_vaincus
    global ennemis
    #Pour savoir si il y a un ennemi.
    vaincreLennemi = randint(0,1)
    if (vaincreLennemi == 1) :
        ennemis[x][y] = 0
        ennemis_vaincus += 1
        print("félicitation vous avez vaincus l'ennemi !!!")
        return True
    else:
        print("l'ennemi n'est pas vaincu")
        return False




def tueToutLesEnnemis()-> None :
    global ennemis_vaincus
    global ennemis
    #stock colonne dans ennemis.
    for x, colonne in enumerate(ennemis):
        #en plus de stocker la position il stock chaques cases  dans colonne .
        for y, case in enumerate(colonne):
            #si  il y a un 1 dans ennemi, alors on le transforme en 0.
            if (case == 1):
                ennemis[x][y] = 0
                ennemis_vaincus += 1
    print("félicitation,vous avez vaincu tout les ennemis !!!")






jouer()





