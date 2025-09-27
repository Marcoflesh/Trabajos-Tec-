#simulador de finanzas de un Godin
#Inicio 
#Preguntar al usuario que si quiere jugar pidiéndole que presione la tecla start Entrada inicial
#Asignar nombre al protagonista con variable de cadena tipo (str) 
#Generar un número aleatorio como salario del día 1 utilizando variables de aleatorio
#Conforme pasan los días los números aleatorios serán un cierto porcentaje menor al inicial
#Mientras el protagonista esté vivo y con dinero mayor a 0 seguirá el juego
#si el godín llega a 0 o si no termina la semana debidamente, se termina el juego y GAME OVER Entrada final
#Al final de cada jornada se mostrarán opciones de pago que se seleccionarán escogiendo los números de las opciones correctas
#El jugador eligirá la opción que más le agrade para seguir con el juego y mantener al godín vivo
#se le restará el monto de su selección a su cuenta de ingresos
#si la opción que escogió pone el dinero en 0, (se terminará el juego y perderá el usuario) Entrada final
#Fin mientras
#Si el usuario llega a terminar la semana con un buen manejo del dinero del godín habrá ganado la run y \n
#saldrá un video de evangelion diciendo "FELICIDADES SHINJI" Entrada final

#En caso de que no termine la run, saldrá un Texto que diga "GAME OVER" y vuelve desde el inicio

import random as rd

#variables
#estas son para cada ingreso del personaje diario, cada ingreso será menor al otro
Gastos = 0
seleccion = 0
Nuevo_celular = 0
Comida_Chatarra = 29
Comida_Sana = 70
Videojuegos = 0
Cine = 0
Netflix = 40
Gasolina = 0
Medicina = 0
Salida_novia = 80
Entretenimiento = 0
luz = 0
agua = 0
media_jornada = 0
user = " "
godin = " "
ingresod6 = 0
restante1 = 0
restante2 = 0
restante3 = 0
restante4 = 0
restante5 = 0
restante6 = 0
restante7 = 0
total = 0
dia2 = 0

#Aqui se presentan las instrucciones antes de empezar el juego
def instructions( ):
    input(print("Pefecto! \nBienvenido a este simulador donde administrás las finanzas de",godin, "(presiona enter para seguir) "))
    input(print("Tu misión será que",godin,"logre sobrevivir una semana \nSIN que sus finanzas lleguen a 0. Tendrás que controlar sus gastos (presiona enter para seguir) "))
    input(print("¿Suena fácil no? Pues, cada día",godin,"ganará menos \nhaciendo que tendrás que pensar más cómo llevas los gastos de",godin, "(presiona enter para seguir) "))
    input(print("acabando el día se te asignará una ganancia cada vez menor \nLo que tendrás que hacer será escoger el/los mejores gastos para que",godin,"\npueda sobrevivir "
      "sin problemas. \nPara asignar la mejor opción escrible el NÚMERO al que corresponda la opción que quieras" 
      "\nSi llegas a 0",godin, "será GAME OVER (presiona enter para seguir)"))


## aqui inicia el juego con el "godin" y las primeras opciones y el avance 3 del proyecto jajajajaja
#de mientras las respuestas serán las mismas para cada condicional

def pago_CFE(luz, d):   
        nuevo_ingreso = d - luz
        return nuevo_ingreso
def pago_CEA(agua,d2): 
        nuevo_ingreso2 = d2 - agua
        return nuevo_ingreso2 
def pago_media_jornada(media_jornada,d6):
        pago = d6 * media_jornada
        return pago

costos = [0,29,40,70,80]
costos1 = [0,Comida_Chatarra,Netflix,Comida_Sana,Salida_novia]

def juego():
    ingresod1 = ingresodia1( )
    print("ganaste: $", ingresod1)
    opcion = int(input("en que quieres gastar? \nEscoge entre \n1.comida chatarra \n2.Netflix \n3.comida sana \n4.salidas con la novia \n" ))
    
    while opcion not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion = int(input())

    restante1 = ingresod1 - costos1[opcion]
    print ("te restan $", restante1)
    
    if restante1 <= 0:
        print("game over")
        main( )
    

    ingresod2 = ingresodia2( )
    dia2 = restante1 + ingresod2

    if pago_CFE(50,dia2) <= 0:
        print("game over")
        main( )

    #asigné el valor yo mismo de lo que se tiene que pagar a la CFE para posteriormente alterar lo que se genera en este día
    #probablemente haga esta parte aleatoria

    print ("ganaste: $", ingresod2, "+ el restante de ayer son:", dia2)
    print ("oh no, te llegó el recibo de luz y tuviste que pagar $50, ahora te queda", pago_CFE(50,dia2))
    #aqui ya se está tomando el descuento por el recibo de luz
    opcion2 = int(input("en que quieres gastar? \nEscoge entre \n1.comida chatarra \n2.Netflix \n3.comida sana \n4.salidas con la novia \n " ))
    
    while opcion2 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion2 = int(input())
    
    restante2 = pago_CFE(50,dia2)-costos[opcion2]
    print ("te restan $", restante2)
    
    if restante2 <= 0:
        print("game over")
        main( )

    ingresod3 = ingresodia3( )
    dia3 = restante2 + ingresod3
    print ("ganaste: $", ingresod3, "+ el restante de ayer son:", dia3)
    opcion3 = int(input("en que quieres gastar? \nEscoge entre \n1.comida chatarra \n2.Netflix \n3.comida sana \n4.salidas con la novia  \n" ))
    
    while opcion3 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion3 = int(input())

    restante3 = dia3 - costos[opcion3]
    print ("te restan $", restante3)

    if restante3 <= 0:
        print("game over")
        main( )

    ingresod4 = ingresodia4( )
    dia4 = restante3 + ingresod4
    print ("ganaste: $", ingresod4, "+ el restante de ayer son:", dia4)
    opcion4 = int(input("en que quieres gastar? \nEscoge entre \n1.comida chatarra \n2.Netflix \n3.comida sana \n4.salidas con la novia \n " ))

    while opcion4 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion4 = int(input())

    restante4 = dia4 - costos[opcion4]
    print ("te restan $", restante4)

    if restante4 <= 0:
        print("game over")
        main( )

    #lo mismo que en el día 2 pero ahora con la CEA
    #igualmente probablemente haga aleatoria la parte del recibo del agua

    ingresod5 = ingresodia5( )
    dia5 = restante4 + ingresod5


    if pago_CEA(47,dia5) <= 0:
        print("game over")
        main( )
        
    print ("ganaste: $", ingresod5, "+ el restante de ayer son:", dia5)
    print ("oh no, te llegó el recibo del agua y tuviste que pagar $47, ahora te queda", pago_CEA(47,dia5))

    opcion5 = int(input("en que quieres gastar? \nEscoge entre \n1.comida chatarra \n2.Netflix \n3.comida sana \n4.salidas con la novia \n " ))

    while opcion5 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion5 = int(input())

    restante5 = pago_CEA(47,dia5) - costos[opcion5]
    print ("te restan $", restante5)

    if restante5 <= 0:
        print("game over")
        main( )


    ingresod6 = ingresodia6( )
    dia6 =int(restante5 + pago_media_jornada(.5,ingresod6))
    print("OH NO!, solo trabajaste media jornada, asi que lo que ganaste se dividirá a la mitad")
    print ("ganaste: $", ingresod6, "+ el restante de ayer, sumando el descuento de la mitad del salario queda en:", dia6)
    opcion6 = int(input("en que quieres gastar? \nEscoge entre \n1.comida chatarra \n2.Netflix \n3.comida sana \n4.salidas con la novia \n " ))
   
    while opcion6 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion6 = int(input())
   
    restante6 = dia6 - costos[opcion6]
    print ("te restan $", restante6)

    if restante6 <= 0:
        print("game over")
        main( )


    ingresod7 = ingresodia7( )
    dia7 = restante6 + ingresod7
    print ("ganaste: $", ingresod7, "+ el restante de ayer son:", dia7)
    opcion7 = int(input("en que quieres gastar? \nEscoge entre \n1.comida chatarra \n2.Netflix \n3.comida sana \n4.salidas con la novia \n " ))

    while opcion7 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion7 = int(input())

    restante7 = dia7 - costos[opcion7]
    print ("te restan $", restante7)

    if restante7 <= 0:
        print("game over")
        main( )
    else:
        print("FELICIDADES SHINJI!, COMPLETASTE EL JUEGO")

def ingresodia1( ):
    return rd.randint(80,100)
def ingresodia2( ):
    return rd.randint(60,80)
def ingresodia3( ):
    return rd.randint(50,60)
def ingresodia4( ):
    return rd.randint(30,50)
def ingresodia5( ):
    return rd.randint(25,30)
def ingresodia6( ):
    return rd.randint(15,25)
def ingresodia7( ):
    return rd.randint(8,15)

#me ayudó una becaria a poder realizar esto
#esta función es la madre de todo el programa, está hasta el final para que asi tenga todos las funciones y variables ya dentro de, esta funcion lo que hace es empezar el juego y
# cuando le das play te lleva primero a que ingreses si deseas jugar y este está dentro de un bucle el cual hasta que no digas que "si", no empiezas el juego
def main( ):
    global godin 
    inicio = input("quieres iniciar el juego? (di si o no) ")
    inicio.lower( )
    
    while inicio != "si":
        inicio = input("quieres iniciar el juego? (di si o no) ")
        inicio.lower( )    
    if  inicio == "si":
        print("VAMOS A JUGAR!")
        user = input("¿Cómo te llamas? ") #se pide el nombre del usuario para registrarlo
        print(user,"Bienvenido!")
        godin = input("¿cómo quieres que se llame el godín? ") #se pide el nombre del godin para registrarlo
        print(godin,"Me gusta ese nombre...")
        instructions( )
        juego ( )
main()
#aqui se inicia el juego en realidad