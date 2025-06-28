import random

def obtener_nombre_usuario():
    nombre = input("🧑 Por favor, ingresa tu nombre: ").upper()
    return nombre

def jugar_piedra_papel_tijera(nombre):
    # Contadores
    contador_ganancia = 0
    contador_perdida = 0
    contador_empate = 0

    # Opciones válidas
    opciones = ("piedra", "papel", "tijera")

    try:
        rondas = int(input(f"{nombre}, ¿cuántas veces quieres jugar?: "))
    except ValueError:
        print("⚠️ ERROR: Debes ingresar un número entero.")
        return

    for i in range(rondas):
        print(f"\n-- RONDA {i+1} --")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")

        try:
            jugador = int(input("Elige tu opción (1-3): "))

            if 1 <= jugador <= 3:
                eleccion_jugador = opciones[jugador - 1]
                ordenador = random.choice(opciones)

                print(f"{nombre} elegiste: {eleccion_jugador}")
                print(f"El ordenador eligió: {ordenador}")

                if eleccion_jugador == ordenador:
                    print("🔁 EMPATE")
                    contador_empate += 1
                elif (
                    (eleccion_jugador == "tijera" and ordenador == "piedra") or
                    (eleccion_jugador == "piedra" and ordenador == "papel") or
                    (eleccion_jugador == "papel" and ordenador == "tijera")
                ):
                    print("❌ HAS PERDIDO")
                    contador_perdida += 1
                else:
                    print("✅ ¡HAS GANADO!")
                    contador_ganancia += 1
            else:
                print("⚠️ OPCIÓN INVÁLIDA. Elige 1, 2 o 3.")
        except ValueError:
            print("⚠️ ERROR: Debes ingresar un número válido.")
            return
    # Mostrar resultados finales
    print(f"\n--- RESULTADOS FINALES para {nombre} ---")
    print(f"Ganadas: {contador_ganancia}")
    print(f"Perdidas: {contador_perdida}")
    print(f"Empates: {contador_empate}")

while True:
    nombre_usuario = obtener_nombre_usuario()
    jugar_piedra_papel_tijera(nombre_usuario)

    otra = input("¿Quieres jugar otra vez? (s/n): ").upper()
    if otra != "S":
        print("👋 ¡Gracias por jugar!")
        break



