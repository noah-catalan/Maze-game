import readchar
import os
from random import randint

POS_X = 0
POS_Y = 1

# Definición del mapa en una sola string

obstacle_definition = """\
#################################
#                          +++  #
#  ############# ########  +++  #
####           # #      #  +++  # 
#              # #      #########
# #######      # #      ####### #
# #     #      # #      #     # #
# #     ######## #      #     # #
# #              #      #     # #
# #     ######## #      #     # #
# #######      # #      ### ### #
#              # #        # #   #
#              # ########## #   #
#              #            #   #
#              # ############   #
#              # #              #
#              # #              #
#    ########### ###########    #
#    #                     #    #
#    #                     #    #
#    #                     #    #
#    #                     #    #
#    #                     #    #
#    #                     #    #
#    #                     #    #
#################################\
"""

# Declaración de variables

vida_inicial_charizard = 100
vida_inicial_squirtle = 80
vida_inicial_eevee = 70

vida_inicial_pikachu = 100
vida_pikachu = vida_inicial_pikachu

my_position = [1, 1]
enemigos = [[4, 8], [27, 7], [16, 22]]
last_position = [0, 0]

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

os.system("cls")

# Introducción del juego

print("Estás en una mazmorra repleta de enemigos, vencelos a todos y te convertirás en maestro pokemon")
input("Enter para continuar...")

print("Los enemigos están situados en los puntos marcados con un asterisco (*)")
print("A por ellos!!!")
input("Enter para continuar...")

os.system("cls")

# Dibujar mapa

while True:

    # Comprobación de si has eliminado a todos los enemigos
    if enemigos[0] == [None, None] and enemigos[1] == [None, None] and enemigos[2] == [None, None]:
        os.system("cls")
        print("Enhorabuena, te has convertido en maestro pokemon\n\n")
        input("Enter para continuar...")

    # Comprobación de si se ha iniciado una batalla
    if enemigos[1][POS_Y] == my_position[POS_Y] and enemigos[1][POS_X] == my_position[POS_X]:
        vida_squirtle = vida_inicial_squirtle
        while vida_squirtle > 0 and vida_pikachu > 0:
            print("Turno de Squirtle")
            ataque_squirtle = randint(1, 2)
            if ataque_squirtle == 1:
                print("Squirtle ataca con Pistola de Agua.")
                vida_pikachu -= 10
            elif ataque_squirtle == 2:
                print("Squirtle ataca con Mordisco.")
                vida_pikachu -= 11

            if vida_squirtle > 0 and vida_pikachu > 0:
                barra_p = ("#" * (vida_squirtle // 10) + " " * ((vida_inicial_squirtle - vida_squirtle) // 10))
                barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
                print("\n\n\n""Vida Squirtle:  [{}]{}".format(barra_p, vida_squirtle))
                print("Vida Pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
            else:
                if vida_pikachu > vida_squirtle:
                    print("Ha ganado Pikachu!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")
                else:
                    print("Ha ganado Squirtle!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")

            print("Turno de Pikachu")

            ataque_pikachu = None
            while ataque_pikachu not in ["B", "I", "R", "N"]:
                ataque_pikachu = input("Que ataque escoges? [B]ola Voltio, [I]mpactrueno, [R]ayo o [N]ada? ")
                if ataque_pikachu == "B":
                    # Pistola Agua
                    print("Pikachu ataca con Bola Voltio.")
                    vida_squirtle -= 10
                elif ataque_pikachu == "I":
                    # Burbuja
                    print("Pikachu ataca con Impactrueno.")
                    vida_squirtle -= 12
                elif ataque_pikachu == "R":
                    # Placaje
                    print("Pikachu ataca con Rayo.")
                    vida_squirtle -= 9
                elif ataque_pikachu == "N":
                    # Pacifismo
                    print("Pikachu no hace nada.")

            if vida_squirtle > 0 and vida_pikachu > 0:
                barra_p = ("#" * (vida_squirtle // 10) + " " * ((vida_inicial_squirtle - vida_squirtle) // 10))
                barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
                print("\n\n\n""Vida Squirtle:  [{}]{}".format(barra_p, vida_squirtle))
                print("Vida pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
            else:
                if vida_pikachu > vida_squirtle:
                    print("Ha ganado Pikachu!!")
                    input("Pulsa Enter para continuar...")
                    enemigos[1] = [None, None]
                    os.system("cls")
                else:
                    print("Ha ganado Squirtle!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")

            input("Pulsa Enter para continuar...")
            os.system("cls")
        my_position = [1, 1]

    if enemigos[0][POS_Y] == my_position[POS_Y] and enemigos[0][POS_X] == my_position[POS_X]:
        vida_eevee = vida_inicial_eevee
        while vida_eevee > 0 and vida_pikachu > 0:
            print("Turno de Eevee")
            ataque_eevee = randint(1, 2)
            if ataque_eevee == 1:
                print("Eevee ataca con Garra Metal.")
                vida_pikachu -= 10
            elif ataque_eevee == 2:
                print("Eevee ataca con Puño Fuego.")
                vida_pikachu -= 11

            if vida_eevee > 0 and vida_pikachu > 0:
                barra_p = ("#" * (vida_eevee // 10) + " " * ((vida_inicial_eevee - vida_eevee) // 10))
                barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
                print("\n\n\n""Vida Eevee:  [{}]{}".format(barra_p, vida_eevee))
                print("Vida Pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
            else:
                if vida_pikachu > vida_eevee:
                    print("Ha ganado Pikachu!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")
                else:
                    print("Ha ganado Eevee!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")

            print("Turno de Pikachu")

            ataque_pikachu = None
            while ataque_pikachu not in ["B", "I", "R", "N"]:
                ataque_pikachu = input("Que ataque escoges? [B]ola Voltio, [I]mpactrueno, [R]ayo o [N]ada? ")
                if ataque_pikachu == "B":
                    # Pistola Agua
                    print("Pikachu ataca con Bola Voltio.")
                    vida_eevee -= 10
                elif ataque_pikachu == "I":
                    # Burbuja
                    print("Pikachu ataca con Impactrueno.")
                    vida_eevee -= 12
                elif ataque_pikachu == "R":
                    # Placaje
                    print("Pikachu ataca con Rayo.")
                    vida_eevee -= 9
                elif ataque_pikachu == "N":
                    # Pacifismo
                    print("Pikachu no hace nada.")

            if vida_eevee > 0 and vida_pikachu > 0:
                barra_p = ("#" * (vida_eevee // 10) + " " * ((vida_inicial_eevee - vida_eevee) // 10))
                barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
                print("\n\n\n""Vida Eevee:  [{}]{}".format(barra_p, vida_eevee))
                print("Vida Pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
            else:
                if vida_pikachu > vida_eevee:
                    print("Ha ganado Pikachu!!")
                    input("Pulsa Enter para continuar...")
                    enemigos[0] = [None, None]
                    os.system("cls")
                else:
                    print("Ha ganado Eevee!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")

            input("Pulsa Enter para continuar...")
            os.system("cls")
        my_position = [1, 1]

    if enemigos[2][POS_Y] == my_position[POS_Y] and enemigos[2][POS_X] == my_position[POS_X]:
        vida_charizard = vida_inicial_charizard
        while vida_charizard > 0 and vida_pikachu > 0:
            print("Turno de Charizard")
            ataque_charizard = randint(1, 2)
            if ataque_charizard == 1:
                print("Charizard ataca con Garra Metal.")
                vida_pikachu -= 10
            elif ataque_charizard == 2:
                print("Charizard ataca con Puño Fuego.")
                vida_pikachu -= 11

            if vida_charizard > 0 and vida_pikachu > 0:
                barra_p = ("#" * (vida_charizard // 10) + " " * ((vida_inicial_charizard - vida_charizard) // 10))
                barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
                print("\n\n\n""Vida Charizard:  [{}]{}".format(barra_p, vida_charizard))
                print("Vida Pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
            else:
                if vida_pikachu > vida_charizard:
                    print("Ha ganado Pikachu!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")
                else:
                    print("Ha ganado Charizard!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")

            print("Turno de Pikachu")

            ataque_pikachu = None
            while ataque_pikachu not in ["B", "I", "R", "N"]:
                ataque_pikachu = input("Que ataque escoges? [B]ola Voltio, [I]mpactrueno, [R]ayo o [N]ada? ")
                if ataque_pikachu == "B":
                    # Pistola Agua
                    print("Pikachu ataca con Bola Voltio.")
                    vida_charizard -= 10
                elif ataque_pikachu == "I":
                    # Burbuja
                    print("Pikachu ataca con Impactrueno.")
                    vida_charizard -= 12
                elif ataque_pikachu == "R":
                    # Placaje
                    print("Pikachu ataca con Rayo.")
                    vida_charizard -= 9
                elif ataque_pikachu == "N":
                    # Pacifismo
                    print("Pikachu no hace nada.")

            if vida_charizard > 0 and vida_pikachu > 0:
                barra_p = ("#" * (vida_charizard // 10) + " " * ((vida_inicial_charizard - vida_charizard) // 10))
                barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
                print("\n\n\n""Vida Charizard:  [{}]{}".format(barra_p, vida_charizard))
                print("Vida Pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
            else:
                if vida_pikachu > vida_charizard:
                    print("Ha ganado Pikachu!!")
                    input("Pulsa Enter para continuar...")
                    enemigos[2] = [None, None]
                    os.system("cls")
                else:
                    print("Ha ganado Charizard!!")
                    input("Pulsa Enter para continuar...")
                    os.system("cls")
            input("Pulsa Enter para continuar...")
            os.system("cls")
        my_position = [1, 1]

    # Comprobación de si se está curando
    if obstacle_definition[my_position[POS_Y]][my_position[POS_X]] == "+":
        vida_pikachu = 100

    print("Para curarte ves al hospital (Símbolo '+')")
    print("Vida Pikachu: ", vida_pikachu)

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Dibujar mapa
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "

            for enemigo in enemigos:
                if enemigo[POS_Y] == coordinate_y and enemigo[POS_X] == coordinate_x:
                    char_to_draw = "* "
            if my_position[POS_Y] == coordinate_y and my_position[POS_X] == coordinate_x:
                char_to_draw = "@ "

            elif obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"
            elif obstacle_definition[coordinate_y][coordinate_x] == "+":
                char_to_draw = "+ "

            print(" {}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Movimiento
    direction = readchar.readchar()

    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    # Teleportarse de un limite del mapa al otro. No es necesario en este mapa.
    if my_position[POS_Y] < 0:
        my_position[POS_Y] += MAP_HEIGHT
    elif my_position[POS_Y] > MAP_HEIGHT - 1:
        my_position[POS_Y] = 0
    if my_position[POS_X] < 0:
        my_position[POS_X] += MAP_WIDTH
    elif my_position[POS_X] > MAP_WIDTH - 1:
        my_position[POS_X] = 0
    os.system("cls")
