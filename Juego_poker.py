import random

# Función para crear una baraja
def crear_baraja():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [{'valor': valor, 'palo': palo} for valor in valores for palo in palos]
    random.shuffle(baraja)
    return baraja

# Función para repartir 5 cartas a un jugador
def repartir_cartas(baraja):
    return [baraja.pop() for _ in range(5)]

# Función para mostrar las cartas de un jugador
def mostrar_cartas(jugador, cartas):
    print(f'{jugador} tiene las siguientes cartas:')
    for carta in cartas:
        print(f'{carta["valor"]} de {carta["palo"]}')

# Función para evaluar la mano de un jugador (en este caso, solo se verifica si hay un par)
def evaluar_mano(cartas):
    valores = [carta['valor'] for carta in cartas]
    for valor in valores:
        if valores.count(valor) == 2:
            return 'Par'
    return 'Nada'

# Función principal del juego
def jugar_poker():
    baraja = crear_baraja()
    jugador = repartir_cartas(baraja)
    
    print('¡Bienvenido al juego de Poker de 5 cartas!')
    mostrar_cartas('Jugador', jugador)
    
    resultado = evaluar_mano(jugador)
    
    print(f'Resultado: {resultado}')
    
    jugar_de_nuevo = input('¿Quieres jugar de nuevo? (S/N): ').strip().lower()
    if jugar_de_nuevo == 's':
        jugar_poker()
    else:
        print('Gracias por jugar. ¡Hasta la próxima!')

# Iniciar el juego
jugar_poker()
