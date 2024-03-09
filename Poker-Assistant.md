# Guía explicativa del código para detectar manos de póker

El código proporcionado es un programa en Python que permite detectar diferentes manos de póker en un conjunto de cartas. El póker es un juego de cartas en el que los jugadores intentan formar combinaciones específicas de cartas en sus manos. Las combinaciones detectadas por este programa son:

1. **Pareja**: Dos cartas con el mismo valor.
2. **Trío**: Tres cartas con el mismo valor.
3. **Escalera**: Cinco cartas consecutivas en valores, no necesariamente del mismo palo.
4. **Color**: Cinco cartas del mismo palo, no necesariamente en orden consecutivo.
5. **Full House**: Tres cartas con el mismo valor y dos cartas con otro valor igual.
6. **Póker**: Cuatro cartas con el mismo valor.
7. **Escalera de Color**: Cinco cartas del mismo palo en orden consecutivo.

## Cómo funciona el código

A continuación, se explican las funciones y el flujo del programa:

1. **Funciones de detección de manos**:
   - El código define varias funciones, como `detectar_pareja`, `detectar_trío`, `detectar_escalera`, `detectar_color`, `detectar_full_house`, `detectar_poker`, y `detectar_escalera_de_color`. Cada una de estas funciones toma un conjunto de cartas como entrada y verifica si se cumple una determinada combinación.

2. **Obtener una carta**:
   - La función `obtener_carta` permite al usuario ingresar una carta en el formato "numeroletra" (por ejemplo, "2H" para el 2 de corazones). Se asegura de que la entrada tenga la longitud correcta y devuelve la carta como una tupla (valor, palo).

3. **Cartas en la mano y en la mesa**:
   - Las funciones `cartas_en_mano` y `cartas_en_mesa` permiten al usuario ingresar las cartas en su mano y en la mesa respectivamente. El usuario debe proporcionar la cantidad correcta de cartas y el formato adecuado.

4. **Evaluación de combinaciones**:
   - El programa recopila todas las cartas en la mano y en la mesa y las almacena en la lista `todas_las_cartas`. Luego, llama a las funciones de detección de manos para verificar si alguna de las combinaciones mencionadas anteriormente se cumple.

5. **Resultado**:
   - Las combinaciones válidas se almacenan en la lista `combinaciones_posibles`. Si se detectan combinaciones, el programa imprime un mensaje indicando las combinaciones encontradas. Si no se detecta ninguna combinación, muestra un mensaje indicando que no se encontró ninguna mano de póker conocida.

## Ejemplo de uso

Al final del código, se muestra un ejemplo de uso. El usuario ingresa las cartas en su mano y en la mesa, y el programa evalúa las combinaciones posibles. El resultado se muestra en la salida estándar.

Este código es útil para los amantes del póker que desean verificar las combinaciones de cartas en su mano y en la mesa, lo que les permite identificar las jugadas ganadoras en un juego de póker. También puede ser una herramienta útil para enseñar y aprender sobre las reglas y las combinaciones de manos de póker.
