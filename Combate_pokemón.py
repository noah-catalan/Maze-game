from random import randint
import os

vida_inicial_pikachu = 100
vida_inicial_squirtle = 100
vida_pikachu = vida_inicial_pikachu
vida_squirtle = vida_inicial_squirtle



while vida_squirtle > 0 and vida_pikachu > 0:
    print("Turno de squirtle")
    ataque_squirtle = randint(1, 2)
    if ataque_squirtle == 1:
        print("squirtle ataca con Garra Metal.")
        vida_pikachu -= 10
    elif ataque_squirtle == 2:
        print("squirtle ataca con Puño Fuego.")
        vida_pikachu -= 11

    if vida_squirtle > 0 and vida_pikachu > 0:
        barra_p = ("#" * (vida_squirtle // 10) + " " * ((vida_inicial_squirtle - vida_squirtle) // 10))
        barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
        print("\n\n\n""Vida squirtle:  [{}]{}".format(barra_p, vida_squirtle))
        print("Vida pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
    else:
        if vida_pikachu > vida_squirtle:
            print("Ha ganado pikachu!!")
            input("Pulsa Enter para continuar...")
            os.system("cls")
        else:
            print("Ha ganado squirtle!!")
            input("Pulsa Enter para continuar...")
            os.system("cls")

    print("Turno de pikachu")

    ataque_pikachu = None
    while ataque_pikachu not in ["B", "I", "R", "N"]:
        ataque_pikachu = input("Que ataque escoges? [B]ola Voltio, [I]mpactrueno, [R]ayo o [N]ada? ")
        if ataque_pikachu == "B":
            # Pistola Agua
            print("pikachu ataca con Bola Voltio.")
            vida_squirtle -= 10
        elif ataque_pikachu == "I":
            # Burbuja
            print("pikachu ataca con Impactrueno.")
            vida_squirtle -= 12
        elif ataque_pikachu == "R":
            # Placaje
            print("pikachu ataca con Rayo.")
            vida_squirtle -= 9
        elif ataque_pikachu == "N":
            # Pacifismo
            print("pikachu no hace nada.")

    if vida_squirtle > 0 and vida_pikachu > 0:
        barra_p = ("#" * (vida_squirtle // 10) + " " * ((vida_inicial_squirtle - vida_squirtle) // 10))
        barra_s = ("#" * (vida_pikachu // 10) + " " * ((vida_inicial_pikachu - vida_pikachu) // 10))
        print("\n\n\n""Vida squirtle:  [{}]{}".format(barra_p, vida_squirtle))
        print("Vida pikachu: [{}]{}\n".format(barra_s, vida_pikachu))
    else:
        if vida_pikachu > vida_squirtle:
            print("Ha ganado pikachu!!")
            input("Pulsa Enter para continuar...")
            os.system("cls")
        else:
            print("Ha ganado squirtle!!")
            input("Pulsa Enter para continuar...")
            os.system("cls")

    input("Pulsa Enter para continuar...")
    os.system("cls")
