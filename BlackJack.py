import random

# Función para crear una baraja
def crear_baraja():
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Función para calcular el valor de una mano
def calcular_valor_mano(mano):
    valor = 0
    ases = 0
    
    for carta in mano:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            ases += 1
            valor += 11
        else:
            valor += int(carta)
    
    while ases > 0 and valor > 21:
        valor -= 10
        ases -= 1
    
    return valor

# Función para mostrar la mano de un jugador
def mostrar_mano(jugador, mano):
    print(f'{jugador} tiene: {" ".join(mano)} (Valor: {calcular_valor_mano(mano)})')

# Función para jugar el turno de un jugador
def jugar_turno(mano, baraja):
    while True:
        mostrar_mano('Jugador', mano)
        accion = input('¿Deseas "Pedir" (P) o "Plantarte" (L)? ').strip().lower()
        
        if accion == 'p':
            carta = baraja.pop()
            mano.append(carta)
            if calcular_valor_mano(mano) > 21:
                mostrar_mano('Jugador', mano)
                print('¡Has perdido!')
                return 'perder'
        elif accion == 'l':
            return 'plantarse'
        else:
            print('Opción no válida. Por favor, elige "P" o "L".')

# Función para jugar el turno de la banca
def turno_banca(mano, baraja):
    while calcular_valor_mano(mano) < 17:
        carta = baraja.pop()
        mano.append(carta)
    
    mostrar_mano('Banca', mano)
    if calcular_valor_mano(mano) > 21:
        print('La banca ha perdido. ¡Ganaste!')
        return 'ganar'
    elif calcular_valor_mano(mano) >= 17 and calcular_valor_mano(mano) <= 21:
        return 'plantarse'

# Función principal del juego
def jugar_blackjack():
    baraja = crear_baraja()
    random.shuffle(baraja)
    
    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_banca = [baraja.pop(), baraja.pop()]
    
    print('¡Bienvenido a Blackjack!')
    
    while True:
        resultado_jugador = jugar_turno(mano_jugador, baraja)
        if resultado_jugador == 'perder':
            break
        
        resultado_banca = turno_banca(mano_banca, baraja)
        if resultado_banca == 'ganar':
            break
    
    if resultado_jugador == 'plantarse' and resultado_banca == 'plantarse':
        if calcular_valor_mano(mano_jugador) > calcular_valor_mano(mano_banca):
            print('¡Has ganado!')
        elif calcular_valor_mano(mano_jugador) < calcular_valor_mano(mano_banca):
            print('La banca ha ganado. ¡Perdiste!')
        else:
            print('Es un empate.')
    
    jugar_de_nuevo = input('¿Quieres jugar de nuevo? (S/N): ').strip().lower()
    if jugar_de_nuevo == 's':
        jugar_blackjack()
    else:
        print('Gracias por jugar. ¡Hasta la próxima!')

# Iniciar el juego
jugar_blackjack()
