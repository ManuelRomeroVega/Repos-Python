# Detectar las combinaciones posibles

def detectar_pareja(cartas):
    valores = [carta[0] for carta in cartas]
    for valor in valores:
        if valores.count(valor) == 2:
            return "Pareja de " + valor
    return None


def detectar_trio(cartas):
    valores = [carta[0] for carta in cartas]
    for valor in valores:
        if valores.count(valor) == 3:
            return "Trío de " + valor
    return None

def detectar_escalera(cartas):
    valores = [carta[0] for carta in cartas]
    valores_unicos = list(set(valores))
    valores_unicos.sort()
    if len(valores_unicos) >= 5:
        for i in range(len(valores_unicos) - 4):
            if valores_unicos[i : i + 5] == list(
                range(int(valores_unicos[i]), int(valores_unicos[i]) + 5)
            ):
                return "Escalera"
    return None

def detectar_color(cartas):
    palos = [carta[1] for carta in cartas]
    for palo in palos:
        if palos.count(palo) >= 5:
            return "Color"
    return None

def detectar_full_house(cartas):
    valores = [carta[0] for carta in cartas]
    valores_unicos = list(set(valores))
    if len(valores_unicos) == 2 and (
        valores.count(valores_unicos[0]) == 3 or valores.count(valores_unicos[1]) == 3
    ):
        return "Full House"
    return None

def detectar_poker(cartas):
    valores = [carta[0] for carta in cartas]
    for valor in valores:
        if valores.count(valor) == 4:
            return "Póker de " + valor
    return None

def detectar_escalera_de_color(cartas):
    if detectar_color(cartas) and detectar_escalera(cartas):
        return "Escalera de Color"
    return None

# Función para verificar si una carta es válida

def es_carta_valida(carta):
    valores_validos = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos_validos = ['H', 'C', 'D', 'S']

    if len(carta) != 2:
        return False

    valor = carta[0]
    palo = carta[1]

    if valor not in valores_validos or palo not in palos_validos:
        return False

    return True

# Pedir las cartas

def obtener_carta():
    carta = input(
        "Ingresa una carta en formato numeroletra (por ejemplo, 2H para 2 de corazones): "
    )
    if len(carta) < 2:
        print(
            "Formato de carta incorrecto. Debe ser numeroletra (por ejemplo, 2H para 2 de corazones)."
        )
        return obtener_carta()
    valor = carta[:-1]  # Obtiene todos los caracteres excepto el último (el palo)
    palo = carta[-1]  # Obtiene el último carácter (el palo)
    return (valor, palo)

def cartas_en_mano():
    cartas = []
    for i in range(2):
        carta = obtener_carta()
        cartas.append(carta)
    return cartas

def cartas_en_mesa():
    cartas = []
    num_cartas_mesa = int(input("¿Cuántas cartas hay en la mesa? (3, 4 o 5): "))
    if num_cartas_mesa < 3 or num_cartas_mesa > 5:
        print("Número de cartas en la mesa no válido. Debe ser 3, 4 o 5.")
        return cartas_en_mesa()
    for i in range(num_cartas_mesa):
        carta = obtener_carta()
        cartas.append(carta)
    return cartas

# Ejemplo de uso

print("Cartas en la mano:")
mano = cartas_en_mano()
print("Cartas en la mesa:")
mesa = cartas_en_mesa()
print("Mano:", mano)
print("Mesa:", mesa)
todas_las_cartas = mano + mesa

# Aquí pasa los valores a las funciones

combinaciones_posibles = [
    detectar_pareja(todas_las_cartas),
    detectar_trio(todas_las_cartas),
    detectar_escalera(todas_las_cartas),
    detectar_color(todas_las_cartas),
    detectar_full_house(todas_las_cartas),
    detectar_poker(todas_las_cartas),
    detectar_escalera_de_color(todas_las_cartas),
]

combinaciones_posibles = [c for c in combinaciones_posibles if c is not None]

if combinaciones_posibles:
    print("Tienes:", ", ".join(combinaciones_posibles))
else:
    print("No tienes ninguna mano de póker conocida.")


# Sugerencias:

# Añadir comprobacion de cartas insertadas,
# Añadir la combinancion doble pareja,
# Modificar las funciones para pedir las cartas para poder añadirlas a la vez. (valorpalo-valorpalo-,etc--),  
# Correrir la funcion escalera para que funcione con los valores A,K,Q y J.