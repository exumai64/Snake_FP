import random

def ha_comido_serpiente(serpiente: list[tuple[int, int]], posicion_comida: tuple[int, int]) -> bool:
    '''
    Comprueba si la cabeza de la serpiente está en la misma posición que la comida.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    posicion_comida: Tupla representando la posición de la comida (columna, fila).

    Devuelve:
    True si la cabeza de la serpiente está en la misma posición que la comida, False en caso contrario.
    '''
    cabeza_serpiente = serpiente[0]

    if cabeza_serpiente == posicion_comida:
        return True
    else:
        return False 

def comprueba_choque(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]]) -> bool:
    '''
    Comprueba si la serpiente se ha chocado consigo misma o con las paredes. Tenga en cuenta
    que la serpiente avanza siempre por su cabeza, que está situada en la 
    primera posición de la lista.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de cada segmento de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.

    Devuelve:
    True si la serpiente se ha chocado consigo misma o con las paredes, False en caso contrario.
    '''
    
    cabeza_serpiente = serpiente[0]
    if cabeza_serpiente in serpiente[1:]:
        return True
    elif cabeza_serpiente in paredes[0]:
        return True
    else:
        return False

def crece_serpiente(serpiente: list[tuple[int, int]]) -> None:
    '''
    Hace crecer la serpiente añadiendo duplicando la posición de la cola

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    '''
    serpiente_crecida = serpiente.append(serpiente[-1])
    return serpiente_crecida

def genera_comida_aleatoria(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]], filas: int, columnas: int) -> tuple[int, int]:
    '''
    Genera una posición aleatoria para la comida que no esté en la misma posición que la serpiente o las paredes.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.

    Devuelve:
    Posición aleatoria para la comida (columna, fila).
    '''
    posicion_aleatoria_fila = random.randint(0,filas-1)
    posicion_aleatoria_columna = random.randint(0,columnas-1)
    posicion_comida = (posicion_aleatoria_columna, posicion_aleatoria_fila)

    while posicion_comida in serpiente or posicion_comida in paredes[0]:
        posicion_aleatoria_fila = random.randint(0,filas-1)
        posicion_aleatoria_columna = random.randint(0,columnas-1)

    return posicion_comida

def mueve_serpiente(serpiente: list[tuple[int, int]], direccion: str, filas: int, columnas: int) -> None:
    '''
    Mueve la serpiente en el tablero según la dirección dada. El tablero es circular, lo que significa
    que si la serpiente se sale por la derecha, debe aparecer por la izquierda, y viceversa (y lo 
    mismo si se sale por arriba o por abajo).

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    direccion: Dirección en la que se debe mover la serpiente ('Left', 'Right', 'Down', 'Up').
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.
    '''
    if direccion not in 'LeftRightDownUp':
        return None

    if direccion == 'Up':
        serpiente.insert(0,(serpiente[0][0],serpiente[0][1]-1))
        serpiente.pop()
        if serpiente[0][1] <= 0:
            serpiente[0] = (serpiente[0][0], filas-1)         
    elif direccion == 'Down':
        serpiente.insert(0,(serpiente[0][0],serpiente[0][1]+1))
        serpiente.pop()
        if serpiente[0][1] >= filas:
            serpiente[0] = (serpiente[0][0], 0)     
    elif direccion == 'Right':
        serpiente.insert(0,(serpiente[0][0]+1,serpiente[0][1]))
        serpiente.pop() 
        if serpiente[0][0] >= columnas:
            serpiente[0] = (0, serpiente[0][1])    
    elif direccion == 'Left':
        serpiente.insert(0,(serpiente[0][0]-1,serpiente[0][1]))
        serpiente.pop() 
        if serpiente[0][0] <= 0:
            serpiente[0] = (columnas-1, serpiente[0][1]) 
         
    return serpiente



