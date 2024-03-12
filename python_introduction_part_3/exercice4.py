# Fontion fournie ne pas modifier
import copy

clearConsole = lambda: print('\n' * 10)

def print_table(table):
    # Dimension 1 = ligne
    # Dimension 2 = colonne
    clearConsole()
    for i, row in enumerate(table):
        row_str = "{:>2}" * len(row)
        row_str = row_str.format(*row)
        print("{:^20}".format(row_str), '\n')

# ________________________________________________________________

# Partie 1
def init_maze(nb_row, nb_col, player_pos, end_pos, walls):
    maze = [["_" for col in range(nb_col)] for row in range(nb_row)]# TODO Générer un labyrinthe vide -> rempli de "_"
    # TODO Placer le joueur "O" la sortie "X" les murs "W"
    maze[player_pos[0]][player_pos[1]]='O'
    maze[end_pos[0]][end_pos[1]]='X'
    for position in walls:
        maze[position[0]][position[1]]='W'
    return maze




# Partie 2
def validate_move(maze, new_player_pos):
    result = False
    # TODO Vérifier si la position est valide -> dans le labyrinthe et pas sur un mur
    for row in maze:
        colonne=len(row)
    if 0<=new_player_pos[0]<len(maze) and 0<=new_player_pos[1]< colonne and (maze[new_player_pos[0]][new_player_pos[1]]=='_' or maze[new_player_pos[0]][new_player_pos[1]]=='X' or maze[new_player_pos[0]][new_player_pos[1]]=='O'):
        result=True
    return result

#Partie 3
def move(key_pressed, maze, player_pos):
    move_dic = {"w": [-1,0], "a": [0,-1],"s":[1,0], "d":[0,1]} # TODO Créer le dictionnaire d'équivalence entre la touche appuyée et la direction ("up", "left", "down", "right")

    # TODO Vérifier si la touche appuyée est dans le dictionnaire
    if key_pressed in move_dic.keys() :
        move = move_dic[key_pressed]# TODO Récupérer la direction du mouvement


        # TODO Générer la position potentielle du joueur en fonction de la direction
        new_player_pos=[player_pos[0]+move[0],player_pos[1]+move[1]]


        if validate_move(maze, new_player_pos):
            # TODO Changer réellement la position du joueur
            maze[new_player_pos[0]][new_player_pos[1]]='O'
            maze[player_pos[0]][player_pos[1]]='_'
            player_pos=new_player_pos
    return maze, player_pos


if __name__ == '__main__':
    nb_row = 4
    nb_col = 7
    player_pos = [0,0] # TODO Définir la position ligne, colonne sur en haut à gauche
    end_pos = [3,6] # TODO Définir la position ligne, colonne sur en bas à droite
    # Coordoné sous la forme (ligne, colone)
    walls = [[0, 1],[1, 1], [1, 2], [1, 3], [1, 5], [2, 1], [2, 5], [3, 3], [3, 5]]
    maze = init_maze(nb_row, nb_col, player_pos, end_pos, walls)

    print_table(maze)

    # TODO Décommenter pour tester votre code en Partie 2
    test_pos = [3,5] #changez les valeurs pour tester tous les cas possibles
    valid = validate_move(maze, test_pos)
    print(valid)


    # TODO Décommenter pour tester votre code en Partie 3
    while player_pos != end_pos:
         key_pressed = input("mouvement : ")
         maze, player_pos = move(key_pressed, maze, player_pos)
         print_table(maze)
    print("Vous avez gagnez !")
