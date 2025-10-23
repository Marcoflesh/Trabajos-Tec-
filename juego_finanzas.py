"""
La biblioteca 'random' la uso para poder generar los salarios
del godin de manera aleatoria, 
mediante rangos para poder delimitar un ingreso
diferente y menor cada día.

La biblioteca 'sys' la uso para poder forzar terminar el juego
de manera forzosa.

La biblioteca 'time' la uso para poder generar los textos de manera
más elegante.
"""

import random as rd
import sys as s
import time as T


"""
==================Variables==================================
"""


"""Variables constantes, que se usrarán en funciones de descuentos."""

AGUA = 47
LUZ = 50
MEDIA_JORNADA = 0.5

"""Ingresos generados con ayuda de la biblioteca 'random'."""

ingreso_d1 = rd.randint(80,90)
ingreso_d2 = rd.randint(70,80)
ingreso_d3 = rd.randint(60,70)
ingreso_d4 = rd.randint(45,60)
ingreso_d5 = rd.randint(30,45)
ingreso_d6 = rd.randint(20,35)
ingreso_d7 = rd.randint(10,20)

"""
================Listas=========================
"""

"""
Estas listas son precios asignados para que el usuario escoja 
cada día tiene costos y opciones diferentes.
""" 

costos_1 = [0, 29, 31, 60, 80] # El 0 es para empezar en la posición 1
costos_2 = [0, 17, 52, 43, 60]
costos_3 = [0, 60, 52, 55, 40]
costos_4 = [0, 42, 29, 15, 51]
costos_5 = [0, 60, 26, 80, 38]
costos_6 = [0, 20, 57, 8, 33]
costos_7 = [0, 43, 88, 67, 11]

"""Lista que almacena todos los ingresos."""

lista_ingresos = [
                    0,
                    ingreso_d1,
                    ingreso_d2,
                    ingreso_d3,
                    ingreso_d4,
                    ingreso_d5,
                    ingreso_d6,
                    ingreso_d7,
                    ]

"""
================matrices============================
"""

"""
Almacena las demás listas para poder recorrer más fácil los precios
en base a las opciones.
"""

costos_total = [
                0,
                costos_1,
                costos_2,
                costos_3,
                costos_4,
                costos_5,
                costos_6,
                costos_7,
                ]

"""
Esta matriz almacena todos las opciones que hay
para que el usuario escoja en cada día.
"""

nombres_costos = [
    [0, "Comida Chatarra", "Plan Celular", 
     "Comida Sana", "Salida con la Pareja"],
    [0, "Gasolina", "Videojuegos", 
     "Ropa", "Comida Sana"],
    [0, "Comida Sana", "Videojuegos", 
     "Medicinas", "Netflix"],
    [0, "Pagar Celular", "Comida Chatarra", 
     "Calzado", "Productos para la Cara"],
    [0, "Comida Sana", "Cine", 
     "Salida con la Pareja", "Disney"],
    [0, "Pagar Internet", "Pagar Celular", 
     "Hojas para Impresora", "Salir con Amigos"],
    [0, "Productos para Limpiar la Casa", "Nuevo Iphone",
     "Despensa Completa", "Manga"],
]

"""
====================Funciones auxiliares=======================
"""

def instructions(godin, user):

    """Imprime instrucciones del juego."""
    
    T.sleep(0.09)
    print(
        "\nPerfecto! \nBienvenid@", user, 
        "a este simulador donde administrás las finanzas de", godin,
        "\n(presiona enter para seguir) "
        )
    
    input("") 

    T.sleep(0.09) 
    print(
        "Tu misión será que", godin, "logre sobrevivir una semana " 
        "\nSIN que sus finanzas lleguen a 0.",
        "Tendrás que controlar sus gastos \n(presiona enter para seguir)"
        )

    input("")
    
    T.sleep(0.09)
    print(
        "¿Suena fácil no? Pues, cada día", godin, "ganará menos " 
        "\nhaciendo que tendrás que pensar más cómo llevar los gastos de",
        godin, "\n(presiona enter para seguir) "
        )

    input("")
    
    T.sleep(0.09)
    print(
        "acabando el día se te asignará una ganancia cada vez menor"
        "\nLo que tendrás que hacer será escoger la mejor opcion para que",
        godin, "pueda sobrevivir \n(presiona enter para seguir)"
        )

    input("")

    T.sleep(0.09)
    print(
        "\nPara asignarla escribe el NÚMERO al que corresponda " 
        "a la opción que quieras" 
        "\nSi las finanzas de", godin, "llegan a 0, será GAME OVER "
        "\n(presiona enter para seguir)"
        )

    input("")


def pago_cfe(dia): 
    """ 
    Esta función sirve 
    para poder descontar al godin el recibo de la luz.

    Recibe = luz valor numerico, dia valor numerico.
    
    Resta LUZ a dia.
        
    Devuelve: el nuevo ingreso ya con el descuento aplicado.
    """   
    nuevo_ingreso = dia - LUZ
    
    return nuevo_ingreso
  
    
def pago_cea(dia): 
    """
    Calcula el dinero restante
    después de pagar el recibo del agua.

    Recibe: dia valor numerico.
    
    Resta AGUA a dia.

    Devuelve: el resultado entre el ingreso y el costo del agua.
    """
    nuevo_ingreso = dia - AGUA
    
    return nuevo_ingreso 
 
      
def pago_media_jornada(dia):
    """
    Calcula el pago correspondiente a la media jornada del trabajo.

    Recibe: dia valor numerico.
    
    Saca la multiplicacion entre dia y MEDIA_JORNADA.

    Devuelve: la multiplicacion entre dia y MEDIA_JORNADA.
    """
    pago = dia * MEDIA_JORNADA
    
    return pago
 
     
def sum_ingresos(ingreso_dias):
    """
    Suma todos los ingresos que el godin generó durante la semana
    mediante el parámetro 'ingreso_dias'.
    
    Deuvelve: suma total de los ingresos de todos los días.
    """
    suma = 0 
    
    for i in ingreso_dias:
        suma = suma + i
        
    return suma


def suma_dias_opcion(opcion_opciones, costos_total):
    """
    Suma todas las opciones de gasto que el usuario escogió.

    Devuelve: total de dinero que se gastó en la semana 
    más los gastos de agua y luz.
    """
    
    total = 0 
    
    for i in range(1,8):
        
        var = opcion_opciones[i-1]
        total = total + costos_total[i][var]
        
    return total + AGUA + LUZ


def prueba_respuesta():
    """ 
    Este ciclo me ayudó un amigo de mecánica a entenderlo.
    
    Si no se cumple la opcion del usuario dentro del rango 1=4,
    se repetirá el ciclo.
    """
    while True:  
        try:
            opcion = int(input(""))
            if opcion in [1, 2, 3, 4]:
                return opcion 
            else:  
                print("Escoge un numero válido")
        except ValueError: 
            print("Entrada inválida, escoge un número correcto")


"""
==================Funciónes principales del juego==============
"""

def juego(
        godin, user, ingresos,
        costos_total, nombres_costos
        ):
    
    """Ejecuta el flujo completo del juego."""
    
    """
    =================dia_1=========================
    """
    
    print(
        "En este primer día de trabajo", godin, "ganó: $", ingresos[1]
        )

    """Esperar a que termine de imprimir línea por línea"""
    print("¿En qué los quieres gastar? ")    
    T.sleep(0.07) 
    print("Escoge entre ")  
    T.sleep(0.07)                           
    print("1. comida chatarra ")
    T.sleep(0.07) 
    print("2. Plan del celular")
    T.sleep(0.07)
    print("3. comida sana")
    T.sleep(0.07)
    print("4. salidas con la pareja")
    T.sleep(0.07)

    """Al pasar el ciclo Se restará el ingreso y la opción."""

    opcion_1 = prueba_respuesta()
    restante1 = ingresos[1] - costos_total[1][opcion_1]  
    
    """
    Después de la resta se muestra lo que se gastó
    y la opción que escogió.
    
    Para eso uso una matriz donde tengo la opción que se escoge
    y la muestra en base
    a la opción que el usuario escogió.
    """
    
    print(
        "Gastaste:", "$", costos_total[1][opcion_1], "en", 
        nombres_costos[0][opcion_1]
        + ".", "Ahora te restan $", restante1
        )
    
    if restante1 <= 0:  
        print("game over")
        main() 

    """Aqui se repite el proceso pero con otras variables."""
    
    """
    =================dia_2=========================
    """
    
    dia2 = restante1 + ingresos[2]  
    
    """ 
    Añadí el pago del agua para poder hacer más retador este juego.
    
    Le llama a pago_CFE y resta el precio del recibo del agua con
    el ingreso.
    """
    if pago_cfe(LUZ, dia2) <= 0: 
        print("game over")
        main()

    print(
        "En el segundo día de trabajo", godin, "ganó: $", ingresos[2],
        " más el restante de ayer ahora", godin, "tiene $", dia2
        )
    
    print(
        "¡Oh no!, a ", godin, 
        "le llegó el recibo de luz y tuvo que pagar $50, " 
        "ahora le quedan $", pago_cfe(LUZ, dia2)
        )
    
    print("¿En qué los quieres gastar?")
    T.sleep(0.07) 
    print("Escoge entre")
    T.sleep(0.07)
    print("1. Gasolina")
    T.sleep(0.07) 
    print("2. Videojuegos")
    T.sleep(0.07) 
    print("3. Ropa")
    T.sleep(0.07) 
    print("4. Comida Sana")
    T.sleep(0.07)
    
    opcion_2 = prueba_respuesta()
    restante2 = pago_cfe(LUZ, dia2) - costos_total[2][opcion_2]
    print(
        "Gastaste:", "$", costos_total[2][opcion_2], "en", 
        nombres_costos[1][opcion_2]
        + ".", "Ahora te restan $", restante2
        )
     
    if restante2 <= 0:
        print("game over")
        main()

    """
    =================dia_3=========================
    """
    
    dia3 = restante2 + ingresos[3]
    
    """ 
    Agregué una opción obligatoria para poder avanzar 
    que son las medicinas, si el usuario no las escoge, 
    resultará en "Game Over".
    """
    
    print(
        "En este tercer día", godin, "ganó $", ingresos[3], 
        "más el restante de ayer ahora", godin, "tiene $", dia3,
        "\n¡OH VAYA! te acabas de enfermar "  
        "y necesitas medicamentos para poder sobrevivir el día"
        ) 
   
    print("¿En qué los quieres gastar?")
    T.sleep(0.07) 
    print("Escoge entre") 
    T.sleep(0.07)
    print("1. Comida Sana")
    T.sleep(0.07)
    print("2. Videojuegos")
    T.sleep(0.07)
    print("3. Medicinas")
    T.sleep(0.07)
    print("4. Netflix")
    T.sleep(0.07)

    """"
    En caso de no escoger "medicinas", 
    el juego terminará debido a que el godín caerá enfermo.
    """
    opcion_3 = prueba_respuesta()
    if opcion_3 != 3:
        print("Game Over. Te moriste por no comprar medicamentos")
        main() 

    restante3 = dia3 - costos_total[3][opcion_3]
    print(
        "Gastaste:", "$", costos_total[3][opcion_3], "en", 
        nombres_costos[2][opcion_3]
        + ".", "Ahora te restan $", restante3
        )

    if restante3 <= 0:
        print("game over")
        main()

    """
    =================dia_4=========================
    """

    dia4 = restante3 + ingresos[4]
    print(
        "En este cuarto día", godin, "ganó $", ingresos[4], 
        "más el restante de ayer ahora", godin, "tiene $", dia4
        )
    
    print("¿En qué los quieres gastar?")
    T.sleep(0.07) 
    print("Escoge entre")
    T.sleep(0.07) 
    print("1. Pagar el plan del Celular")
    T.sleep(0.07) 
    print("2. Comida Chatarra")
    T.sleep(0.07)
    print("3. calzado")
    T.sleep(0.07) 
    print("4. Productos para la cara")
    T.sleep(0.07)
            
    opcion_4 = prueba_respuesta()
    restante4 = dia4 - costos_total[4][opcion_4]
    print(
        "Gastaste:", "$", costos_total[4][opcion_4], "en",
        nombres_costos[3][opcion_4] 
        + ".", "Ahora te restan $", restante4
        )
    
    if restante4 <= 0:
        print("game over")
        main()

    """
    =================dia_5=========================
    """
    
    """Similar al día 2 pero ahora se descontará de la CEA."""
    
    dia5 = restante4 + ingresos[5]
    if pago_cea(AGUA, dia5) <= 0: 
        print("game over")
        main() 
          
    print(
        "En este quinto día", godin, "ganó $", ingresos[5],
        "más el restante de ayer", godin, "ahora tiene $", dia5
        )
    print(
        "¡Oh Vaya!, te llegó el recibo del agua y tuviste que pagar $47",
        "así que, a", godin, "ahora le quedan $", pago_cea(AGUA, dia5)
        )

    print("¿En qué los quieres gastar?")
    T.sleep(0.07) 
    print("Escoge entre") 
    T.sleep(0.07)
    print("1. Comida Sana") 
    T.sleep(0.07)
    print("2. Cine")
    T.sleep(0.07) 
    print("3. Salir con la pareja") 
    T.sleep(0.07)
    print("4. Disney+")
    T.sleep(0.07)
                            
    opcion_5 = prueba_respuesta()
    restante5 = pago_cea(AGUA, dia5) - costos_total[5][opcion_5] 
    print(
        "Gastaste:", "$", costos_total[5][opcion_5], "en", 
        nombres_costos[4][opcion_5]
         + ".", "Ahora te restan $", restante5
         )

    if restante5 <= 0:
        print("game over")
        main()

    """
    =================dia_6=========================
    """
    
    """
    Aquí el godin trabajó media jornada.
    
    Por ende solo se le pagó la mitad de lo que le tocaba ese día.
    
    llamé a la función que hace el cálculo de lo que le tocará
    al godín por trabajar medio día.
    """

    dia6 = int(restante5 + pago_media_jornada(MEDIA_JORNADA, ingresos[6])) 

    print(
        "OH NO!, solo trabajaste media jornada," 
         " asi que lo que ganaste se dividirá a la mitad"
         )
    
    print(
        "En este sexto día", godin, "ganó $", ingresos[6],
        "más el restante de ayer,"
        "sumando el descuento de la media jornada", godin, 
        "ahora tiene $", dia6
        )
    
    print("¿En qué los quieres gastar?")
    T.sleep(0.07) 
    print("Escoge entre")
    T.sleep(0.07)
    print("1. Internet")
    T.sleep(0.07) 
    print("2. Pagar el celular")
    T.sleep(0.07)  
    print("3. Hojas para impresora")
    T.sleep(0.07) 
    print("4. Salida con amigos")
    T.sleep(0.07)
                
    """
    En caso de que en el día 1 o día 4 
    no se haya escogido la opción de 'pagar el celular',
    se forzará esa opción para poder seguir el juego.
    
    Si no se paga en ninguno de esos días,
    el usuarió habrá perdido el juego.
    
    Si el usuario llega a pagar el celular
    en cualquiera de los días donde aparezca, el juego continuará.
     
    Si se paga antes del día 6, 
    en este día se podrá escoger otra opción sin problema.
    """
    opcion_6 = prueba_respuesta()
    while opcion_1 != 2 and opcion_4 != 1 and opcion_6 != 2:
        print(
            "Game Over. \nte quedaste sin celular y"
            "ahora tu proveedor te lo bloqueo y explotó \ngg"
            )
        main()

    restante6 = dia6 - costos_total[6][opcion_6]
    print(
        "Gastaste:", "$", costos_total[6][opcion_6], "en", 
        nombres_costos[5][opcion_6]
        + ".", "Ahora te restan $", restante6
        )

    if restante6 <= 0:
        print("game over")
        main()

    """
    =================dia_7=========================
    """
    
    dia7 = restante6 + ingresos[7]
    print(
        "En este séptimo y último día", godin, "ganó $", ingresos[7],
        "más el restante de ayer ahora él tiene $", dia7
        )

    print("¿En qué los quieres gastar?")
    T.sleep(0.07) 
    print("Escoge entre")
    T.sleep(0.07) 
    print("1. Productos para limpieza de casa")
    T.sleep(0.07)
    print("2. El nuevo Iphone")
    T.sleep(0.07) 
    print("3. despensa completa")
    T.sleep(0.07) 
    print("4. manga")
    T.sleep(0.07)
    
    opcion_7 = prueba_respuesta()
    restante7 = dia7 - costos_total[7][opcion_7]
    print(
        "Gastaste:", "$", costos_total[7][opcion_7], "en", 
        nombres_costos[6][opcion_7]
        + ".", "Ahora te restan $", restante7
        )

    if restante7 <= 0:
        print("game over")
        main()
    
    """Almacena las opciones dentro de una lista."""
    
    opcion_opciones = [
                        opcion_1,
                        opcion_2,
                        opcion_3,
                        opcion_4,
                        opcion_5,
                        opcion_6,
                        opcion_7
                        ]

    user = user.upper()
    
    """
    Si el jugador llega a pasar del día 7 con una cuenta superior a 0,
    se mostrará esta parte.
    """
    print(
        "FELICIDADES ", user + "!", 
        "COMPLETASTE EL JUEGO \n lograste hacer que",
        godin, "termine la semana con dinero de sobra"
        )

    """
    Se mostrarán los ingresos totales, 
    el promedio de ingresos del godín,
    la suma de los gastos que hizo el usuario
    y el promedio del usuario de gasto por día.
    """
    print(
        "En total ganaste: $", sum_ingresos(ingresos), 
        "con un ingreso promedio de: $",
        ('%.2f' % (sum_ingresos(ingresos) / 7)), 
        "por día, y gastaste: $",
        (suma_dias_opcion(opcion_opciones, costos_total)),
        "con un gasto promedio de: $",
        ('%.2f' % (suma_dias_opcion(opcion_opciones, costos_total) / 7)),
        "por día"
        )
    
    main()


""" 
Me ayudó una becaria a poder realizar main().

Sí el juego no inicia al dar "si", solo reinicie y estará solucionado.
"""
def main():
    """
    Controla inicio y reinicio del juego.
    
    Aqui se asignan parámetros necesarios a las funciones
    Para correr el juego.
    """ 
    inicio = input("quieres iniciar el juego? (di si o no) ")
    inicio = inicio.lower() 
    
    while inicio != "si":
        if inicio == "no": 
            print("Gracias por jugar")
            s.exit()
        inicio = input("quieres iniciar el juego? (di si o no) ")
        inicio = inicio.lower() 
        
    if  inicio == "si":
        print("VAMOS A JUGAR!")
        user = input("¿Cómo te llamas? ") 
        print(user, "Bienvenid@!")
        godin = input(
                    "¿cómo quieres que se llame el godín? "  
                    ) 
        print(godin, "Me gusta ese nombre...")
        instructions(godin, user) 
        juego(
            godin, user, lista_ingresos,
            costos_total, nombres_costos
            )

main()
