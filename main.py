# Importamos libreria random
import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = random.randint(0, 11)  #Numeos aleatorios
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0
# texto de bienvenida para quien juegue tu trivia
print("Bienvenido a mi trivia sobre programación")
time.sleep(2)
print("Pondremos a prueba tus conocimientos")
time.sleep(2)
print("Comenzarás con:", puntaje, "puntos\n")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
time.sleep(2)
nombre = input("Escriba su nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
print(
    BLUE + "\n¡Hola!", nombre,
    "para responder las siguientes preguntas debes escribir la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
    + RESET)
time.sleep(6)
while iniciar_trivia == True:  #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje = 0

    print(RED + "\nIntento número:", intentos)
    input("Presiona Enter para continuar\n" + RESET)
    # Pregunta 1
    print(
        GREEN +
        "1. ¿Cuál es el medio de transporte más conocido para el comercio mundial?"
    )
    print("a) Aéreo")
    print("b) Terrestre ")
    print("c) Marítimo")
    print("d) Fluvial" + RESET)

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_1 = input("\nTu respuesta: ")

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_1 == "c":
        puntaje += random.randint(5, 10)
        print(
            MAGENTA +
            "¡Muy bien! \nEl 80% del transporte de mercancías se lleva a cabo por mar en buques mercantes"
            + RESET)
    else:
        puntaje -= random.randint(1, 5)
        print(
            MAGENTA +
            "Incorrecto \nEl 80% del transporte de mercancías se lleva a cabo por mar en buques mercantes."
            + RESET)
    time.sleep(6)
    print("Tienes", puntaje, "puntos hasta el momento")
    #Pregunta 2
    time.sleep(2)
    print(GREEN +
          "\n2. ¿Qué diferencia a Caral de otras civilizaciones de la región?")
    print("a) Arquitectura")
    print("b) Defensa")
    print("c) Religión")
    print("d) Agricultura" + RESET)
    respuesta_2 = input("\nTu respuesta: ")

    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_2 == "b":
        puntaje += random.randint(10, 15)
        print(
            MAGENTA +
            "¡Muy bien! \nAl no encontrarse armas ni murallas se sabe que Caral no tuvo Ejército y desarrolló una vida comercial pacífica con otras culturas"
            + RESET)
    else:
        puntaje -= random.randint(5, 10)
        print(
            MAGENTA +
            "Incorrecto \nAl no encontrarse armas ni murallas se sabe que Caral no tuvo Ejército y desarrolló una vida comercial pacífica con otras culturas."
            + RESET)
    time.sleep(6)
    print("Tienes", puntaje, "puntos hasta el momento")
    #Pregunta 3
    time.sleep(2)
    print(GREEN + "\n3. ¿Dónde se dio la primera sensación de surcar una ola?")
    print("a) Polinesia")
    print("b) Hawai")
    print("c) Antiguo Perú")
    print("d) África" + RESET)
    respuesta_3 = input("\nTu respuesta: ")

    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_3 == "c":
        puntaje += random.randint(1, 5)
        print(
            MAGENTA +
            "¡Muy bien! \nSegún el portal: 'Historia de la tabla en Perú', 5 mil años surcando olas fue en esta zona del mundo donde se dio origen a este arte"
            + RESET)
    else:
        puntaje -= random.randint(5, 10)
        print(
            MAGENTA +
            "Incorrecto \nSegún el portal: 'Historia de la tabla en Perú', 5 mil años surcando olas fue en esta zona del mundo donde se dio origen a este arte."
            + RESET)
    time.sleep(6)
    print("Tienes", puntaje, "puntos hasta el momento")
    #Pregunta 4
    time.sleep(2)
    print(GREEN +
          "\n4. ¿Qué alimento 'apaciguó' a Europa y la salvó del hambre? ")
    print("a) El maíz")
    print("b) La Caña de azúcar")
    print("c) La papa")
    print("d) El arroz" + RESET)
    respuesta_4 = input("\nTu respuesta: ")

    while respuesta_4 not in ("a", "b", "c", "d", "x"):
        respuesta_4 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_4 == "a":
        print(MAGENTA + "Incorrecto" + RESET)
        puntaje = puntaje - 5
    elif respuesta_4 == "b":
        print(MAGENTA + "Totalmente incorrecto!" + RESET)
        puntaje = puntaje / 2
    elif respuesta_4 == "c":
        print(
            MAGENTA +
            "¡Corrrecto! \nSabemos que este tubérculo que trajeron los exploradores de las Américas a finales del siglo XVI fue para Europa un producto esencial para eliminar las hambrunas que asolaban al continente"
            + RESET)
        puntaje = puntaje * 2
    elif respuesta_4 == "d":
        print(MAGENTA + "..." + RESET)
        puntaje = puntaje + 5
    elif respuesta_4 == "x":
        puntaje += 10000
        print(MAGENTA + "Este es un mensaje secreto, ganas 1000 puntos" +
              RESET)
    time.sleep(8)
    print(YELLOW + "\n¡Bien hecho", nombre, "tu resultado es", puntaje,
          "puntos" + RESET)

    time.sleep(2)
    numero = int(input("\nAntes de acabar ingrese un número de la suerte: "))
    print(CYAN + "Su resultado final es", puntaje * numero,
          "\nGracias por jugar mi trivia!" + RESET)
    time.sleep(2)
    print(BLUE + "\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: " +
        RESET).lower()

    if repetir_trivia != "si":  # != significa "distinto"
        print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
        iniciar_trivia = False
