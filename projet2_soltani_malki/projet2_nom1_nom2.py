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

toto = "exemple2"

def il_y_a_un_mur ( x : int , y : int ) -> bool :
    # on recupere la valeur a la position x,y du tableau et on verifie si il y a un 1.
    return murs[x][y] == 1

def il_y_a_un_ennemi(x: int, y: int) -> bool :
    return ennemis[x][y] == 1

def il_y_a_un_tresor(x: int, y: int ) -> bool :
    return tresor[x][y] == 1


def obtenir_position_joueur() -> List[int]:
    return position_joueur

def deplacer_joueur ( x : int , y : int ) -> None :
    global position_joueur
    global position_precedente_joueur
    position_precedente_joueur = position_joueur
    position_joueur = [x, y]
    arriver_case()

def arriver_case () -> None :
    position_joueur[0]
    position_joueur[1]


    if (il_y_a_un_mur()) :
        print("il y a un mur")

    if (il_y_a_un_ennemi()) :
        print("il y a un ennemi")

    if (il_y_a_un_tresor()) :
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
    deplacer(x, y)


jouer()




