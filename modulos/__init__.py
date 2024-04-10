
def generar_estructura(lista,list2,list3,list4):
    """"
    Genera una estructura con tres datos:lista recibida como parametro.
    En este caso lo retorna en formato lista de tuplas donde cada tupla 
    posee los datos (nombre, goles, goles evitados, asistencias)
    al ser formato listas puede agregarse un nuevo jugador de ser necesario

    """
    return list(zip(lista,list2,list3,list4))


def goleador(list):
    """
    Esta funcion calcula el goleador o goleadora entre todos.
    Retorna el goleador/a en una tupla asi puede usarse de ser neceario
    en otros modulos dode se necesite algo de informacion del mismo

    retorna del goleador/a : 
    (nombre, goles, goles evitados, asistencias)

    """
    return  max(list, key = lambda l: l[1])


def mas_influyente(list):
    """
    Retorna en una tupla la informacion del jugador/a mas influyente,
    para el uso que se necesite  se retorna la sig informacion en una tupla : 
    
    (nombre, goles, goles evitados, asistencias)

    El calculo del mas influyente se calcula multiplicando los valores dados , por sus
    equivalentes (1.5,1.25,1)
    """
    return max(list, key= lambda x: x[1]*1.5+ x[2]*1.25+ x[3])

 
def goles_prom_partido(list,x):
    """
    Esta funcion calcula y retorna los goles promedio por partido del equipo ,
    el cual recibe la lista --> hace la suma de los goles de todos los jugadores 
    --> y lo divide por x que son los partidos jugados por el equipo

    """
    return sum(aux[1] for aux in list) / x


def prom_goles_persona(num, x):
    """
    Esta funcion calcula y retorna los goles promedio por partido de una persona,
    lo que recibe es un entero el cual representa la cantidad de goles tot en el campionato
    y lo divide por los partidos jugados, en este caso es x

    """
    return num / x

