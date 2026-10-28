# Juego la guayabita

from Dado import dibujar_dado, lanzar_dado


def jugar():
    dinero_jugador1 = 2000
    dinero_jugador2 = 2000
    dinero_case = 500

    print("Bienvenido al juego de la guayabita")
    print(f" jugador 1 empieza con $: {dinero_jugador1}")
    print(f" jugador 2 empieza con $: {dinero_jugador2}")
    print(f" case $: {dinero_case}")

    case = 200

    while dinero_jugador1 > 0 and dinero_jugador2 > 0:
        for jugador in [1, 2]:
            if jugador == 1:
                dinero = dinero_jugador1
                nombre = "jugador 1"
            else:
                dinero = dinero_jugador2
                nombre = "jugador 2"

            if dinero < case:
                print(f"{nombre} no tiene suficiente dinero para apostar.")
                return

            dinero -= case
            dinero_case += case
            print(f"\nTurno del {nombre}:")
            print(f"{nombre} coloca ${case} en la mesa. ")

            primer_lanzamiemto = lanzar_dado()
            print(f"Lanzamiento 1: ")
            dibujar_dado(primer_lanzamiemto)

            if primer_lanzamiemto in [1, 6]:
                print(f"{nombre} saco {primer_lanzamiemto}. Pierde el turno y debe colocar ${case} mas ene la mesa ")
                dinero -= case
                dinero_case += case
                print(f"El saldo de {nombre}: es ${dinero}")
                print(f"El saldo de la case: es ${dinero_case}")
                if jugador == 1:
                    dinero_jugador1 = dinero
                else:
                    dinero_jugador2 = dinero
                continue

            segundo_lanzamiento = lanzar_dado()
            print(f"Lanzamiento 2: ")
            dibujar_dado(segundo_lanzamiento)

            if segundo_lanzamiento > primer_lanzamiemto:
                print(f"{nombre} saco {segundo_lanzamiento}. Pierde ${case} ")
                dinero -= case
                dinero += case

            print(f"El saldo de {nombre}: es ${dinero}")
            print(f"El saldo de el case es : ${dinero_case}")

            if jugador == 1:
                dinero_jugador1 = dinero
            else:
                dinero_jugador2 = dinero

            if dinero_jugador1 < case and dinero_jugador2 < case:
                print("\nAmbos jugadores se han quedado sin dinero. El juego ha terminado.")
                return
            

            if dinero_case < case:
                print("\nLa mesa no tiene suficiente dinero para pagar las apuestaas. El juego ha terminado.")
                return

    if dinero_jugador1 <= 0:
        print("\nJugador 1 se ha quedado sin dinero. El jugador 2 gana el juego.")
    elif dinero_jugador2 <= 0:
        print("\nJugador 2 se ha quedado sin dinero. El jugador 1 gana el juego.")
    elif dinero_case <= 0:
        print("\nLa mesa se ha quedado sin dinero. Los jugadores han empatado el juego")
    
if __name__ == "__main__":
    jugar()