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



position_joueur = [2, 1]
position_precedente_joueur = [2, 1]
sortie = [0, 4]
tresors_collectes = 0
ennemis_vaincus = 0

dialogue_case_vide = ["Il n'y a rien de spécial sur cette case. Le joueur continue son chemin, sans s'attarder !",
                      "Oh la la, le joueur arrive sur une case vide, pas de trésor en vue!",
                      "La case est vide, il n y'a rien de captivant ici.",
                      "Rien de palpitant, passons!",
                      "Le joueur explore une case vide. Pas grand chose d'excitant ici, on continue !"]
dialogue_case_ennemi = ["Oh le joueur est attaqué par un Dragon! Il faut se défendre et montrer à cet ennemi de quoi on est capable !"
                      "Un fantome surgit de nulle part. Le joueur doit se défendre !",
                      "Attention, ça devient dangereux ! Un Gobelin se trouve sur cette case, il va falloir se préparer pour le combat !",
                      "La case est prise d'assaut par un des bandit! Allons nous battre !",
                      "L'ennemi bloque le passage du joueur, mais ne t'inquiète pas on va trouver une solution.",]
dialogue_case_tresor = ["Hourra ! Un coffre se cache ici ! C'est excellent!",
                      "Le joueur met la main sur une Pierre De L'Aventure. Quelle merveille !",
                      "La case renferme un une amulette inestimable. Le joueur est aux anges !",
                      "Waouh ! Le joueur a mis la mais sur un fruit magique ! Quelle chance !",
                      "Le joueur découvre une rose enchanté  sur cette case. Quelle aventure incroyable !"]
def il_y_a_un_mur ( x : int , y : int ) -> bool :
    """
        Description :
        --------- ----
        La fonction vérifie la présence d'un mur.
        Parametres :
        ------------
        x (int) : coordonnées correspondant à l'abcisse de la case.
        y (int) : coordonnées correspondant à l'ordonnée de la case.
        Retours :
        ---------
        ( None )
        """
    # on recupere la valeur a la position x,y du tableau et on verifie si il y a un 1.
    return murs[x][y] == 1


def il_y_a_un_ennemi(x: int, y: int) -> bool:
    """
        Description :
        --------- ----
        La fonction vérifie la présence d'un ennemi.
        Parametres :
        ------------
        x (int) : coordonnées correspondant à l'abcisse de la case.
        y (int) : coordonnées correspondant à l'ordonnée de la case.
        Retours :
        ---------
        ( None )
        """
    return ennemis[x][y] == 1


def il_y_a_un_tresor(x: int, y: int ) -> bool:
    """
        Description :
        --------- ----
        La fonction vérifie la présence d'un tresor.
        Parametres :
        ------------
        x (int) : coordonnées correspondant à l'abcisse de la case.
        y (int) : coordonnées correspondant à l'ordonnée de la case.
        Retours :
        ---------
        ( None )
        """
    return tresors[x][y] == 1


def obtenir_position_joueur() -> List[int] :
    """
        Description :
        --------- ----
        La fonction permet d'obtenir la position du joueur.
        Parametres :
        ------------

        Retours :
        ---------
        (List[int]): la position du joueur
        """
    global position_joueur
    return position_joueur


def deplacer_joueur ( x : int , y : int ) -> None :
    """
        Description :
        --------- ----
        La fonction permet de déplacer le joueur sur la carte.
        Parametres :
        ------------
        x (int) : coordonnées correspondant à l'abcisse de la nouvelle coordonnées.
        y (int) : coordonnées correspondant à l'ordonnée de la nouvelle coordonnées.
        Retours :
        ---------
        ( None )
         """
    global position_joueur
    global position_precedente_joueur
    position_precedente_joueur = position_joueur
    position_joueur = [x, y]
    arriver_case()


def arriver_case() -> None :
    """
        Description :
        --------- ----
        La fonction permet de gérer l'arrivée du joueur dans une case .
        Parametres :
        ------------
        Retours :
        ---------
        ( None )
        """
    global position_joueur
    global murs
    global ennemis
    global tresors
    pygame_min.afficher_jeu(murs, ennemis, tresors, position_joueur)
    xPositionJoueur = position_joueur[0]
    yPositionJoueur = position_joueur[1]

    if (il_y_a_un_mur(xPositionJoueur, yPositionJoueur )) :
        print("il y a un mur")
        reponse = input("souhaitez-vous détruire le mur ?")
        reponse = reponse.lower()
        if (reponse == "oui"):
            detruire_mur(xPositionJoueur, yPositionJoueur)
        else:
            reculer()
            pygame_min.afficher_jeu(murs, ennemis, tresors, position_joueur)
        deplacement()
    elif (il_y_a_un_ennemi(xPositionJoueur, yPositionJoueur)) :
        affichePhrase(2)
        reponse = input("souhaitez-vous affronter l'ennemi ?")
        reponse = reponse.lower()
        if (reponse == "oui") :
            if(affronter_ennemi(xPositionJoueur, yPositionJoueur) == False ) :
                reculer()
                pygame_min.afficher_jeu(murs, ennemis, tresors, position_joueur)
        else:
            reculer()
            pygame_min.afficher_jeu(murs, ennemis, tresors, position_joueur)
    elif (il_y_a_un_tresor(xPositionJoueur, yPositionJoueur)) :
        affichePhrase(3)
        reponse = input("souhaitez-vous ramasser le trésor ?")
        reponse = reponse.lower()
        if (reponse == "oui") :
            ramasser_tresor(xPositionJoueur, yPositionJoueur)
            pygame_min.afficher_jeu(murs, ennemis, tresors, position_joueur)
        else:
            reculer()
            pygame_min.afficher_jeu(murs, ennemis, tresors, position_joueur)
        deplacement()

    else:
        affichePhrase(1)


def jouer() -> None:
    afficher_histoire()
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
    global murs
    pygame_min.initialiser_jeu(len(murs))
    # On fait le lien avec les variables globales
    position_joueur = obtenir_position_joueur()
    # On deplace le joueur sur sa position initiale
    x = position_joueur[0]
    y = position_joueur[1]
    deplacer_joueur(x, y)
    finDeplacement = False
    # continue d'appeler deplacement() tant que la fonction ne renvoie pas true
    while(finDeplacement == False):
        finDeplacement = deplacement()
    pygame_min.quitter_jeu()
def sortir () -> None :
    """
         Description :
         --------- ----
         La fonction affiche un message de sorti.
         Parametres :
         ------------

         Retours :
         ---------
         ( None )
                       """
    global ennemis_vaincus
    global tresors_collectes
    print("le nombre d'ennemi(s) vaincu(s) est de :", ennemis_vaincus)
    print("le nombre de tresor(s) collecté(s) est de :", tresors_collectes)
    print("le jeu est terminé")


def deplacement () -> bool:
    """
        Description :
        Permet de gérer le déplacement du joueur.

        Parametres :
        ------------
        Retours :
        ---------
        (bool)
        """
    position_joueur = obtenir_position_joueur()
    finDeplacement = False
    #on defini x et y afin de pouvoir les utuliser dans la condition .
    x = position_joueur[0]
    y = position_joueur[1]
    # on donne à direction la direction entrée par l'utilisateur
    direction = input("Dans quelle direction voulez-vous aller?")
    # si l'utilisateur a rentré Nord alors on rentre dans le if
    print("direction choisie est :", direction)
    direction = direction.lower()
    if(direction == "nord"):
        print("le joueur va au nord")
        # comme la direction choisie est le nord, on fait y = -1
        y -= 1
        #condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
        if(y >= 0) and (sortie != [x, y]) :
            deplacer_joueur(x, y)
            #est ce que x et y sont = a la sortie
        elif (sortie == [x, y]) :
            sortir()
            finDeplacement = True

        else :
            deplacement()
    elif (direction == "sud"):
         print("le joueur va au Sud")
         # comme la direction choisie est le Sud, on fait y = -1
         y += 1
         # condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
         if (y<len(murs)) and (sortie != [x, y]):
            deplacer_joueur(x, y)
            # est ce que x et y sont = a la sortie
         elif (sortie == [x, y]):
            sortir()
            finDeplacement = True
         else :
            deplacement()
    elif (direction == "ouest"):
        print("le joueur va a l'Ouest")
        # comme la direction choisie est l'Ouest, on fait x = -1
        x -= 1
        #condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
        if (x >= 0) and (sortie != [x, y]):
            deplacer_joueur(x, y)
            # est ce que x et y sont = a la sortie
        elif (sortie == [x, y]):
            sortir()
            finDeplacement = True
        else :
            deplacement()
    elif (direction == "est"):
        print("le joueur va à  Est")
        # comme la direction choisie est l'Est, on fait x = -1
        x += 1
        # condition pour savoir si on ne sort pas du tableau et que l'on ne se trouve pas a la sortie.
        if (x < len(murs)) and (sortie != [x, y]):
            deplacer_joueur(x, y)
            # est ce que x et y sont = a la sortie
        elif (sortie == [x, y]):
            sortir()
            finDeplacement = True
        else:
                deplacement()
    elif (direction == "useralg213"):
        tueToutLesEnnemis()
    else:
        print("direction non reconnu, les directions possibles sont: Nord, Sud, Est, Ouest")
    return finDeplacement



def reculer () -> None :
    """
        Description :
        Cette fonction permet de reculer sur la carte .

        Parametres :

        Retours :
        ---------
        ( None )
        """
    global position_precedente_joueur
    global position_joueur
    position_joueur = position_precedente_joueur



def detruire_mur ( x : int , y : int ) -> None :
    """
        Description :
        Cette fonction permet de detruire les murs presents sur la carte.

        Parametres :
        x (int) : coordonnées correspondant à l'abcisse du mur à détruire.
        y (int) : coordonnées correspondant à l'ordonnée du mur à détruire.

        Retours :
        ---------
        ( None )
        """
    global murs
    #on enleve le mur aux coordonnées x,y, il faut donc mettre à 0
    murs[x][y] = 0
    print("vous avez detrui un mur !")

def ramasser_tresor ( x : int , y : int ) -> None :
    """
        Description :
        Fonction qui permet de ramasser les tresors présents sur la carte.

        Parametres :
         x (int) : coordonnées correspondant à l'abcisse de la case du trésor à récupérer.
         y (int) : coordonnées correspondant à l'ordonnée de la case du trésor à récupérer.

        Retours :
        ( None )
        """
    global tresors_collectes
    global tresors
    tresors_collectes += 1
    #on enleve le trésor aux coordonnées x,y, il faut donc mettre à 0
    tresors[x][y] = 0
    print("vous venez d'acquerir un nouveau tresor : Bravo! ")
    print("le nombre de tresors collectés jusqu'à présent est de :", tresors_collectes)

def affronter_ennemi ( x : int , y : int ) -> bool :
    """
        Description :
        Fonction qui permet d'affronter l'ennemi à la nouvelle position du joueur

        Parametres :
         x (int) : coordonnées correspondant à l'abcisse .
         y (int) : coordonnées correspondant à l'ordonnée .

        Retours :
        ( bool )
    """
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
    """
        Description :
        Fonction qui permet de tuer tout les ennemis présents sur la carte.

        Parametres :

        Retours :
        ( None )
    """

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


def afficher_histoire() -> None  :
    """
        Description :
        cette fonction permet d'afficher l'histoire du jeu.

        Parametres :

        Retours :

        ( None )
    """
    print("Alors que vous partez à la recherche de la légendaire pierre philosophique, un groupe de bandit vous tend une embuscade et vous capture. Après vous avoir amené dans leur cave fortifiée contenant tous les trésors volés, vous réussissez à vous libérer. Vous devez maintenant trouver la sortie.")

def affichePhrase(categorie: int) -> None :
    """
        Description :
        cette fonction permet de tirer au sort une phrase parmis plusieurs selon la bonne catégorie (case vide
        case avec un ennemi, case avec un trésor) et de l'afficher.

        Parametres :

        categorie: (int) categorie 1 = case vide categorie 2 = ennemi categorie 3 = tresor

        Retours :

    ( None )
    """
    #si la categorie = 1 alors on a une phrase de type dialogue case vide .
    if (categorie == 1):
        global dialogue_case_vide
        #sert a prendre une phrase a une certaine position .
        position = randint(0, 4)
        print(dialogue_case_vide[position])
    elif (categorie == 2) :
        global dialogue_case_ennemi
        position = randint(0, 4)
        print(dialogue_case_ennemi[position])
    elif (categorie == 3):
        global dialogue_case_tresor
        position = randint(0, 4)
        print(dialogue_case_tresor[position])


jouer()





