from clase.enemigo import Enemigo
from clase.jugador import Jugador
import random


def main():
    nombre_jugador = input(
        "Bienvenido a la aventura en el espacio, ingrese el nombre de tu jugador: "
    )
    jugador = Jugador(nombre_jugador)

    enemigo = [
        Enemigo("Alien", 20, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("monstruo", 70, 10),
    ]
    enemigo_derrotados = []

    print("comienza la aventura ")

    while enemigo:
        enemigo_actual = random.choice(enemigo)
        if enemigo_actual in enemigo_derrotados:
            continue

        print(f"tu enemigo actual es {enemigo_actual.nombre} ")
        while enemigo_actual.salud > 0:
            accion = input("que desea hacer?(atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"has atacado al enemigo {enemigo_actual.nombre} y le causaste {dano_jugador} de dolor"
                )
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"el {enemigo_actual.nombre} ataco y causo {dano_enemigo} de dano"
                    )
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print("has huido del enemigo")
                break

        if jugador.salud <= 0:
            print("has perdido la partida")
            break
        if enemigo_actual.salud <= 0:
            enemigo_derrotados.append(enemigo_actual)
            enemigo.remove(enemigo_actual)

        jugador.ganar_exp(40)
        continuar = input("quieres seguir jugando (si/no)").lower()
        if continuar != "si":
            print("fin del juego ")
            break
    if not enemigo:
        print("derrotaste a todos los enemigos ")
       


if __name__ == "__main__":
    main()
