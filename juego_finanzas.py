"""
Esta biblioteca la uso para poder generar los salarios del godin de
manera aleatoria, mediante rangos para poder delimitar un ingreso
diferente y menor cada día.
"""

import random as rd


"""------------------Variables----------------------------------"""

"""Ingresos generados con ayuda de la biblioteca importada"""

ingreso_d1 = rd.randint(80,90)
ingreso_d2 = rd.randint(70,80)
ingreso_d3 = rd.randint(60,70)
ingreso_d4 = rd.randint(45,60)
ingreso_d5 = rd.randint(30,45)
ingreso_d6 = rd.randint(20,35)
ingreso_d7 = rd.randint(10,20)


"""----------------Listas-------------------------"""

"""
Estas listas son precios asignados para que el usuario escoja 
cada día tiene costos y opciones diferentes.
""" 

costos_1 = [0, 29, 31, 70, 80] # El 0 es para empezar en la posición 1
costos_2 = [0, 17, 52, 43, 70]
costos_3 = [0, 70, 52, 55, 40]
costos_4 = [0, 42, 29, 15, 51]
costos_5 = [0, 70, 26, 80, 38]
costos_6 = [0, 20, 57, 8, 33]
costos_7 = [0, 43, 88, 67, 11]

"""Esta lista almacena todos los ingresos"""

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


"""----------------matrices----------------------------"""

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
    [0, "Ropa", "Videojuegos", 
     "Gasolina", "Comida Sana"],
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


"""--------------------Funciones auxiliares-----------------------"""

def instructions(godin, user):

    """Imprime las instrucciones del juego."""
    
    print(
        "\nPerfecto! \nBienvenid@", user, 
        "a este simulador donde administrás las finanzas de", godin,
        "\n(presiona enter para seguir) "
        )
    
    input("") # Están para que el usuario pueda leer a gusto
    
    print(
        "Tu misión será que", godin, "logre sobrevivir una semana " 
        "\nSIN que sus finanzas lleguen a 0.",
        "Tendrás que controlar sus gastos \n(presiona enter para seguir)"
        )
    
    input("")
    
    print(
        "¿Suena fácil no? Pues, cada día", godin, "ganará menos " 
        "\nhaciendo que tendrás que pensar más cómo llevar los gastos de",
        godin, "\n(presiona enter para seguir) "
        )
    
    input("")
    
    print(
        "acabando el día se te asignará una ganancia cada vez menor"
        "\nLo que tendrás que hacer será escoger la mejor opcion para que",
        godin, "pueda sobrevivir \n(presiona enter para seguir)"
        )
    
    input("")

    print(
        "\nPara asignarla escribe el NÚMERO al que corresponda" 
        "a la opción que quieras" 
        "\nSi las finanzas de", godin, "llegan a 0, será GAME OVER "
        "\n(presiona enter para seguir)"
        )
          
    input("")


def pago_cfe(luz, dia): 
    """ 
    Esta función sirve 
    para poder descontar al godin el recibo de la luz.

    Recibe = luz valor numerico, dia valor numerico.
    
    Resta luz a dia.
        
    Devuelve: el nuevo ingreso ya con el descuento aplicado.
    """   
    nuevo_ingreso = dia - luz
    
    return nuevo_ingreso
  
    
def pago_cea(agua, dia): 
    """
    Calcula el dinero restante
    después de pagar el recibo del agua.

    Recibe: agua valor numerico, d_2 valor numerico.
    
    Resta agua a d_2.

    Devuelve: el resultado entre el ingreso y el costo del agua.
    """
    nuevo_ingreso_2 = dia - agua
    
    return nuevo_ingreso_2 
 
      
def pago_media_jornada(media_jornada, dia):
    """
    Calcula el pago correspondiente a la media jornada del trabajo.

    Recibe: media_jornada valor numerico, d_6 valor numerico.
    
    Saca la multiplicacion entre d_6 y media_jornada.

    Devuelve: la multiplicacion entre d_6 y media_jornada.
    """
    pago = dia * media_jornada
    
    return pago
 
     
def sum_ingresos(ingreso_dias):
    """
    Suma todos los ingresos que el godin generó durante la semana
    mediante el parámetro 'ingreso_dias'.
    
    Deuvelve: suma total de los ingresos de todos los días.
    """
    suma = 0 # Variable numérica acumuladora
    
    for i in ingreso_dias:
        # Recorre toda la lista y suma los valores de ella
        suma = suma + i
        
    return suma


def suma_dias_opcion(opcion_opciones, costos_total):
    """
    Suma todas las opciones de gasto que el usuario escogió.

    
    Devuelve: total de dinero que se gastó en la semana 
    más los gastos de agua y luz.
    """
    
    total = 0 # Variable numérica acumuladora
    
    for i in range(1,8): # Rango en el que se recorrerá la lista
        
        var = opcion_opciones[i-1]
        # Suma los costos de la opcion que el usuario escogió
        total = total + costos_total[i][var]
        
    return total + 97 # 50 de luz + 47 de agua

"""------------------Funciónes principales del juego--------------"""

def juego(
        godin, user, ingresos,
        costos_total, nombres_costos
        ):
    
    """Ejecuta el flujo completo del juego."""
    
    """-----------------dia_1-------------------------"""
    
    print(
        "En este primer día de trabajo", godin, "ganó: $", ingresos[1]
        )
    
    """ 
    Este ciclo me ayudó un amigo de mecánica a entenderlo.
    
    Si no se cumple la opcion del usuario dentro del rango 1-4,
    se repetirá el ciclo.
    """
    while True:  # Se repite hasta que se ingrese un valor entre 1-4
        try:
            opcion = int(input(
                            "¿En qué los quieres gastar? " 
                            "\nEscoge entre " 
                            "\n1. comida chatarra " 
                            "\n2. Plan del celular"
                            "\n3. comida sana"
                            "\n4. salidas con la pareja \n "
                            ))
            
            if opcion in [1, 2, 3, 4]:
                break  # Rompe el ciclo al ingresar número válido 
            else:  # Repite el bucle hasta dar un número valido
                print("Escoge un numero válido")
                
        except ValueError:  # Evita el crasheo al dar enter
            print("Entrada inválida, escoge un número")

    
    """Al pasar el ciclo Se restará el ingreso y la opción."""
    
    
    restante1 = ingresos[1] - costos_total[1][opcion]  
    # Resta ingreso con opción
    
    """
    Después de la resta se muestra lo que se gastó
    y la opción que escogió.
    
    Para eso uso una matriz donde tengo la opción que se escoge
    y la muestra en base
    a la opción que el usuario escogió.
    """
    
    print(
        "Gastaste:", "$", costos_total[1][opcion], "en", 
        nombres_costos[0][opcion]
        + ".", "Ahora te restan $", restante1
        )
    
    if restante1 <= 0:  # Comprueba que el saldo no sea 0 o negativo
        print("game over")
        main()  # Regresa a función main() en caso de estar en 0

    """Aqui se repite el proceso pero con otras variables."""
    
    """-----------------dia_2-------------------------"""
    
    dia2 = restante1 + ingresos[2]  # Nuevo día con variables distintas
    
    """ 
    Añadí el pago del agua para poder hacer más retador este juego.
    
    Se llama a pago_CFE y resta el precio del recibo del agua con
    el ingreso.
    """
    LUZ = 50
    if pago_cfe(LUZ, dia2) <= 0: # Verifica que la función no sea <= 0
        print("game over")
        main()

    """
    Asigné el valor del pago a la CFE.
    
    Para posteriormente alterar lo que se genera en este día.
    """

    print(
        "En el segundo día de trabajo", godin, "ganó: $", ingresos[2],
        " más el restante de ayer ahora", godin, "tiene $", dia2
        )
    
    print(
        "¡Oh no!, a ", godin, 
        "le llegó el recibo de luz y tuvo que pagar $50, " 
        "ahora le quedan $", pago_cfe(LUZ, dia2)
        )  # ya descontó la luz
    
    while True:  # Misma lógica que en el primer día y los demás
        try:
            opcion2 = int(input(
                            "¿En qué los quieres gastar?" 
                            "\nEscoge entre"
                            "\n1. Ropa" 
                            "\n2. Videojuegos" 
                            "\n3. Gasolina " 
                            "\n4. Comida Sana \n "
                          ))
            
            if opcion2 in [1, 2, 3, 4]:
                break
            else:
                print("Escoge un numero válido")
        except ValueError:
            print("Entrada inválida, escoge un número")

    restante2 = pago_cfe(LUZ, dia2) - costos_total[2][opcion2]
    print(
        "Gastaste:", "$", costos_total[2][opcion2], "en", 
        nombres_costos[1][opcion2]
        + ".", "Ahora te restan $", restante2
        )
     
    if restante2 <= 0:
        print("game over")
        main()

    """-----------------dia_3-------------------------"""
    
    dia3 = restante2 + ingresos[3]
    
    """ 
    Agregué una opción obligatoria para poder avanzar 
    que son las medicinas, si el usuario no las escoge, 
    resultará en "Game Over".
    """
    
    print(
        "En este tercer día", godin, "ganó $", ingresos[3], 
        "más el restante de ayer ahora", godin, "tiene $", dia3,
        "\n¡OH VAYA! te acabas de enfermar"  # advierte enfermedad 
        "y necesitas medicamentos para poder sobrevivir el día"
        ) 
   
    while True:
        try:
            opcion3 = int(input(
                            "¿En qué los quieres gastar?" 
                            "\nEscoge entre" 
                            "\n1. Comida Sana"
                            "\n2. Videojuegos"
                            "\n3. Medicinas" 
                            "\n4. Netflix  \n "
                            ))
            
            if opcion3 in [1,2,3,4]:
                break
            else:
                print("Escoge un numero válido")
        except ValueError:
            print("Entrada inválida, escoge un número")

    """"
    En caso de no escoger "medicinas", 
    el juego terminará debido a que el godín caerá enfermo.
    """
    
    if opcion3 != 3:  # Comprueba que se haya escogido "medicinas"
        print("Game Over. Te moriste por no comprar medicamentos")
        main()  # De no ser así, se reinicia

    restante3 = dia3 - costos_total[3][opcion3]
    print(
        "Gastaste:", "$", costos_total[3][opcion3], "en", 
        nombres_costos[2][opcion3]
        + ".", "Ahora te restan $", restante3
        )

    if restante3 <= 0:
        print("game over")
        return main()

    """-----------------dia_4-------------------------"""

    dia4 = restante3 + ingresos[4]
    print(
        "En este cuarto día", godin, "ganó $", ingresos[4], 
        "más el restante de ayer ahora", godin, "tiene $", dia4
        )
    
    while True:
        try:
            opcion4 = int(input(
                            "¿En qué los quieres gastar? " 
                            "\nEscoge entre " 
                            "\n1. Pagar el plan del Celular " 
                            "\n2. Comida Chatarra" 
                            "\n3. calzado " 
                            "\n4. Productos para la cara \n "
                            )
                          )
            
            if opcion4 in [1, 2, 3, 4]:
                break
            else:
                print("Escoge un numero válido")
        except ValueError:
            print("Entrada inválida, escoge un número")
    
    restante4 = dia4 - costos_total[4][opcion4]
    print(
        "Gastaste:", "$", costos_total[4][opcion4], "en",
        nombres_costos[3][opcion4] 
        + ".", "Ahora te restan $", restante4
        )
    
    if restante4 <= 0:
        print("game over")
        main()

    """-----------------dia_5-------------------------"""
    
    """Similar al día 2 pero ahora se descontará de la CEA."""
    
    dia5 = restante4 + ingresos[5]
    AGUA = 47
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

    while True:
        try:
            opcion5 = int(input(
                                "¿En qué los quieres gastar?" 
                                "\nEscoge entre " 
                                "\n1. Comida Sana" 
                                "\n2. Cine" 
                                "\n3. Salir con la pareja" 
                                "\n4. Disney+ \n "
                                ))
                            
            
            if opcion5 in [1, 2, 3, 4]:
                break
            else:
                print("Escoge un numero válido")
        except ValueError:
            print("Entrada inválida, escoge un número")

    restante5 = pago_cea(AGUA, dia5) - costos_total[5][opcion5] 
    print(
        "Gastaste:", "$", costos_total[5][opcion5], "en", 
        nombres_costos[4][opcion5]
         + ".", "Ahora te restan $", restante5
         )

    if restante5 <= 0:
        print("game over")
        main()

    """-----------------dia_6-------------------------"""
    
    """
    Aquí el godin trabajó media jornada.
    
    Por ende solo se le pagó la mitad de lo que le tocaba ese día.
    
    llamé a la función que hace el cálculo de lo que le tocará
    al godín por trabajar medio día.
    """
    
    dia6 = int(
            restante5 
               + pago_media_jornada(.5, ingresos[6])
               ) # Realiza descuento

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
   
    while True:
        try:
            opcion6 = int(input(
                        "¿En qué los quieres gastar? " 
                        "\nEscoge entre"
                        "\n1. Internet" 
                        "\n2. Pagar el celular"  
                        "\n3. Hojas para impresora " 
                        "\n4. Salida con amigos \n "
                        ))
            
            if opcion6 in [1, 2, 3, 4]:
                break
            else:
                print("Escoge un numero válido")
        except ValueError:
            print("Entrada inválida, escoge un número")

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

    # Comprueba que se haya escogido la opción antes
    while opcion != 2 and opcion4 != 1 and opcion6 != 2:
        print(
            "Game Over. \nte quedaste sin celular y"
            "ahora tu proveedor te lo bloqueo y explotó \ngg"
            )
        main()  # En caso de no ser escogida, retorna a main()

    restante6 = dia6 - costos_total[6][opcion6]
    print(
        "Gastaste:", "$", costos_total[6][opcion6], "en", 
        nombres_costos[5][opcion6]
        + ".", "Ahora te restan $", restante6
        )

    if restante6 <= 0:
        print("game over")
        main()

    """-----------------dia_7-------------------------"""
    
    dia7 = restante6 + ingresos[7]
    print(
        "En este séptimo y último día", godin, "ganó $", ingresos[7],
        "más el restante de ayer ahora él tiene $", dia7
        )

    while True:
        try:
            opcion7 = int(input(
                            "¿En qué los quieres gastar?" 
                            "\nEscoge entre" 
                            "\n1. Productos para limpieza de casa"
                            "\n2. El nuevo Iphone " 
                            "\n3. despensa completa " 
                            "\n4. manga \n "
                            ))
            
            if opcion7 in [1, 2, 3, 4]:
                break
            else:
                print("Escoge un numero válido")
        except ValueError:
            print("Entrada inválida, escoge un número")

    restante7 = dia7 - costos_total[7][opcion7]
    print(
        "Gastaste:", "$", costos_total[7][opcion7], "en", 
        nombres_costos[6][opcion7]
        + ".", "Ahora te restan $", restante7
        )

    if restante7 <= 0:
        print("game over")
        main()
    
    """Almacena las opciones dentro de una lista."""
    
    opcion_opciones = [
                        opcion,
                        opcion2,
                        opcion3,
                        opcion4,
                        opcion5,
                        opcion6,
                        opcion7
                        ]


    user = user.upper() # Cambia la variable a mayúsculas
    
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
        # Llama a sum_ingresos para mostrar los ingresos totales
        "En total ganaste: $", sum_ingresos(ingresos), 
        
        "con un ingreso promedio de: $",
        
        # Llama a sum_ingresos para promediar lo que se ingresó
        ('%.2f' % (sum_ingresos(ingresos) / 7)), 
        
        "por día, y gastaste: $",
        
        # Muestra la cantidad gastada durante la semana
        (suma_dias_opcion(opcion_opciones, costos_total)),
        
        "con un gasto promedio de: $",
        
        # Promedia la cantidad gastada durante la semana
        ('%.2f' % (suma_dias_opcion(opcion_opciones, costos_total) / 7)),
        
        "por día"
        )
    
    main() # Aquí retornará al usuario y reiniciará el juego


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
    inicio = inicio.lower() # Pone en minúsculas la respuesta
    
    while inicio != "si": # Inicio bucle
        if inicio == "no": 
            print("Gracias por jugar")
            return "" # Termina el juego
        inicio = input("quieres iniciar el juego? (di si o no) ")
        inicio = inicio.lower() # Pone en minúsculas la respuesta
        
    if  inicio == "si": # Fin bucle
        print("VAMOS A JUGAR!")
        user = input("¿Cómo te llamas? ")  # Asigna usuario
        print(user, "Bienvenid@!")
        godin = input( # Asigna personaje
                    "¿cómo quieres que se llame el godín? "  
                    ) 
        print(godin, "Me gusta ese nombre...")
        instructions(godin, user) # Llama función de instrucciones 
        juego(
            godin, user, lista_ingresos,
            costos_total, nombres_costos
            ) # Llama función de juego

main() # Inicia el juego
