import random as rd

#variables
#estas son para cada ingreso del personaje diario, cada ingreso será menor al otro

pago_plan_celular = 31
ropa = 17
Comida_Chatarra = 29
Disney = 38
Comida_Sana = 70
Videojuegos = 52
Cine = 26
Netflix = 40
Gasolina = 43
salida_amigos = 33
medicinas = 52
pago_plan_celular2 = 42
internet = 20
Salida_novia = 80
hojas_impresora = 8
pago_plan_celular3 = 52
productos_para_la_cara = 51
calzado = 15
nuevo_iphone = 88
despensa_completa = 67
media_jornada = 0
manga = 11
productos_limpieza_casa = 43 
user = " "
godin = " "
ingresod6 = 0
restante1 = 0
opcion1 = []
opcion2 = []
opcion3 = []
opcion4 = []
opcion5 = []
opcion6 = []
opcion7 = []
restante2 = 0
restante3 = 0
restante4 = 0
restante5 = 0
restante6 = 0
restante7 = 0
total = 0
costos1 = [0,Comida_Chatarra,pago_plan_celular,Comida_Sana,Salida_novia]
costos2 = [0,ropa,Videojuegos,Gasolina,Comida_Sana]
costos3 = [0,Comida_Sana,Videojuegos,medicinas,Netflix]
costos4 = [0,pago_plan_celular2,Comida_Chatarra,calzado,productos_para_la_cara]
costos5 = [0,Comida_Sana,Cine,Salida_novia,Disney]
costos6 = [0,internet,pago_plan_celular3,hojas_impresora,salida_amigos]
costos7 = [0,productos_limpieza_casa,nuevo_iphone,despensa_completa,manga]
costos_total = [0,
                costos1,
                costos2,
                costos3,
                costos4,
                costos5,
                costos6,
                costos7]
opcion_opciones = []
ingreso_dias = []

#Funciones
#Aqui se presentan las instrucciones antes de empezar el juego
def instructions( ):
    input(print("Pefecto! \nBienvenid@", user, "a este simulador donde administrás las finanzas de",godin, "(presiona enter para seguir) "))
    input(print("Tu misión será que",godin,"logre sobrevivir una semana \nSIN que sus finanzas lleguen a 0. Tendrás que controlar sus gastos (presiona enter para seguir) "))
    input(print("¿Suena fácil no? Pues, cada día",godin,"ganará menos \nhaciendo que tendrás que pensar más cómo llevar los gastos de",godin, "(presiona enter para seguir) "))
    input(print("acabando el día se te asignará una ganancia cada vez menor \nLo que tendrás que hacer será escoger la mejor opcion para que",godin,"\npueda sobrevivir "
        "\nPara asignarla escribe el NÚMERO al que corresponda la opción que quieras" 
      "\nSi las finanzas de",godin, "llegan a 0, será GAME OVER (presiona enter para seguir)"))

#Estas son las funciones que utilicé para poder hacer los ingresos de manera aleatoria con la biblioteca de random, realizar reducciones de los ingresos para complicar el juego y poder realizar
#y promedios de lo que se ingresó con lo que se gastó utilizando ciclos for y listas anidadas
def pago_CFE(luz, d):   
        nuevo_ingreso = d - luz
        return nuevo_ingreso
def pago_CEA(agua,d2): 
        nuevo_ingreso2 = d2 - agua
        return nuevo_ingreso2 
def pago_media_jornada(media_jornada,d6):
        pago = d6 * media_jornada
        return pago
def sum_ingresos():
    global ingreso_dias
    suma = 0
    for i in ingreso_dias:
        suma = suma + i
    return suma
def suma_dias_opcion( ):
    total = 0
    global opcion_opciones, costos_total
    for i in range(1,8):
        var = opcion_opciones[i-1]
        total = total + costos_total[i][var]
    return total + 97
def ingresodia1( ):
    return rd.randint(80,90)
def ingresodia2( ): 
    return rd.randint(70,80)
def ingresodia3( ):
    return rd.randint(60,70)
def ingresodia4( ):
    return rd.randint(45,60)
def ingresodia5( ):
    return rd.randint(30,45)
def ingresodia6( ):
    return rd.randint(20,35)
def ingresodia7( ):
    return rd.randint(10,20)

def juego():
    global opcion_opciones
    opcion_opciones = []
    global costos_total
    global ingreso_dias
    ingreso_dias = []
    global ingresod1,ingresod2,ingresod3,ingresod4,ingresod5,ingresod6,ingresod7
    
    ingresod1 = ingresodia1( )
    ingreso_dias.append(ingresod1,)
    print("En este primer día de trabajo",godin,"ganó: $", ingresod1)
    opcion = int(input("¿En qué los quieres gastar? \nEscoge entre \n1.comida chatarra \n2. Plan del celular \n3.comida sana \n4.salidas con la novia \n" ))
    
    while opcion not in [1,2,3,4]:
        print("Ingresa un número válido")
        opcion = int(input())

    restante1 = ingresod1 - costos1[opcion]
    print ("Gastaste:",costos1[opcion],"ahora te restan $", restante1)
    opcion_opciones.append(opcion,)
    
    if restante1 <= 0:
        print("game over")
        main( )
    

    ingresod2 = ingresodia2( )
    dia2 = restante1 + ingresod2
    ingreso_dias.append(ingresod2,)

    if pago_CFE(50,dia2) <= 0:
        print("game over")
        main( )

    #asigné el valor yo mismo de lo que se tiene que pagar a la CFE para posteriormente alterar lo que se genera en este día
    #probablemente haga esta parte aleatoria

    print ("En el segundo día de trabajo",godin, "ganó: $", ingresod2, " más el restante de ayer ahora",godin,"tiene $", dia2)
    print ("¡Oh no!, a ", godin, "le llegó el recibo de luz y tuvo que pagar $50, ahora le quedan $", pago_CFE(50,dia2))
    #aqui ya se está tomando el descuento por el recibo de luz
    opcion2 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Ropa \n2. Videojuegos \n3. Gasolina \n4. Comida Sana \n " ))
    
    while opcion2 not in [1,2,3,4]:
        print("Ingresa un número válido")
        opcion2 = int(input())
    
    restante2 = pago_CFE(50,dia2)-costos2[opcion2]
    print ("Gastaste:",costos2[opcion2],"ahora te restan $", restante2)
    opcion_opciones.append(opcion2,)
    
    if restante2 <= 0:
        print("game over")
        main( )

    ingresod3 = ingresodia3( )
    dia3 = restante2 + ingresod3
    ingreso_dias.append(ingresod3,)
    print ("En este tercer día", godin, "ganó $", ingresod3, "más el restante de ayer ahora",godin,"tiene $", dia3,
           "\n¡OH VAYA! te acabas de enfermar y necesitas medicamentos para poder sobrevivir el día")
    opcion3 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Comida Sana \n2. Videojuegos \n3. Medicinas \n4. Netflix  \n" ))
    
    while opcion3 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion3 = int(input())
    
    if opcion3 != 3:
        print("Game Over, te moriste por no comprar medicamentos")
        main()

    restante3 = dia3 - costos3[opcion3]
    print ("Gastaste:",costos3[opcion3],"ahora te restan $", restante3)
    opcion_opciones.append(opcion3,)

    if restante3 <= 0:
        print("game over")
        main( )

    ingresod4 = ingresodia4( )
    dia4 = restante3 + ingresod4
    ingreso_dias.append(ingresod4,)
    print ("En este cuarto día",godin,"ganó $", ingresod4, "más el restante de ayer ahora",godin, "tiene $", dia4)
    opcion4 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Pagar el plan del Celular \n2. Comida Chatarra" \
    " \n3. calzado \n4. Productos para la cara \n " ))

    while opcion4 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion4 = int(input())

    restante4 = dia4 - costos4[opcion4]
    print ("Gastaste:",costos4[opcion4],"ahora te restan $", restante4)
    opcion_opciones.append(opcion4,)

    if restante4 <= 0:
        print("game over")
        main( )

    #lo mismo que en el día 2 pero ahora con la CEA
    #igualmente probablemente haga aleatoria la parte del recibo del agua

    ingresod5 = ingresodia5( )
    dia5 = restante4 + ingresod5
    ingreso_dias.append(ingresod5,)


    if pago_CEA(47,dia5) <= 0:
        print("game over")
        main( )
        
    print ("En este quinto día", godin, "ganó $", ingresod5, "más el restante de ayer ahora",godin, "tiene $", dia5)
    print ("Pero. ¡Oh Vaya!, te llegó el recibo del agua y tuviste que pagar $47, así que, ahora le quedan a",godin,"$", pago_CEA(47,dia5))

    opcion5 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Comida Sana \n2. Cine \n3. Salir con la novia \n4. Disney+ \n " ))

    while opcion5 not in [1,2,3,4]:
        print("ingresa un número válido")
        opcion5 = int(input())

    restante5 = pago_CEA(47,dia5) - costos5[opcion5]
    print ("Gastaste:",costos5[opcion5],"ahora te restan $", restante5)
    opcion_opciones.append(opcion5,)

    if restante5 <= 0:
        print("game over")
        main( )

    #forzar plan celular
    ingresod6 = ingresodia6( )
    dia6 =int(restante5 + pago_media_jornada(.5,ingresod6))
    ingreso_dias.append(ingresod6,)
    print("OH NO!, solo trabajaste media jornada, asi que lo que ganaste se dividirá a la mitad")
    print ("En este sexto día",godin, "ganó $", ingresod6, "más el restante de ayer, sumando el descuento de la media jornada",godin,"ahora tiene $", dia6)
    opcion6 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1.Internet \n2.Pagar el celular \n3. Hojas para impresora \n4. Salida con amigos \n " ))
   
    while opcion6 not in [1,2,3,4]:
        print("Ingresa un número válido")
        opcion6 = int(input())
   #darle detallitos a esta parte para forzarlo, en caso de pagarlo antes, mostrar que que bueno que liquida sus deudas desde antes 
    while opcion != 2 and opcion4 != 1 and opcion6 != 2:
        print("Game Over. \nte quedaste sin celular y ahora tu proveedor te lo bloqueo y explotó \ngg")
        main()

    restante6 = dia6 - costos6[opcion6]
    print ("Gastaste:",costos6[opcion6],"ahora te restan $", restante6)
    opcion_opciones.append(opcion6,)

    if restante6 <= 0:
        print("game over")
        main( )


    ingresod7 = ingresodia7( )
    dia7 = restante6 + ingresod7
    ingreso_dias.append(ingresod7,)
    print ("En este séptimo y último día",godin,"ganó $",ingresod7, "más el restante de ayer ahora él tiene $", dia7)
    opcion7 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Productos para limpieza de casa \n2. El nuevo Iphone \n3. despensa completa \n4. manga \n " ))

    while opcion7 not in [1,2,3,4]:
        print("Ingresa un número válido")
        opcion7 = int(input())

    restante7 = dia7 - costos7[opcion7]
    print ("Gastaste:",costos7[opcion7],"ahora te restan $", restante7)
    opcion_opciones.append(opcion7)

    if restante7 <= 0:
        print("game over")
        main( )

    print("FELICIDADES ",user+"!", "COMPLETASTE EL JUEGO \n lograste hacer que",godin,"Termine la semana con dinero de sobra")
    print("En total ganaste: $",sum_ingresos(),"con un promedio de: $",('%.2f'%(sum_ingresos()/7)),"por día, y gastaste: $",
            suma_dias_opcion(),"con un gasto promedio de: $",
              ('%.2f'%(suma_dias_opcion()/7)),"por día")
    main()
#me ayudó una becaria a poder realizar esto
#esta función es la madre de todo el programa, está hasta el final para que asi tenga todos las funciones y variables ya dentro de, esta funcion lo que hace es empezar el juego y
# cuando le das play te lleva primero a que ingreses si deseas jugar y este está dentro de un bucle el cual hasta que no digas que "si", no empiezas el juego
def main( ):
    global godin
    global user 
    inicio = input("quieres iniciar el juego? (di si o no) ")
    inicio.lower( )
    
    while inicio != "si":
        inicio = input("quieres iniciar el juego? (di si o no) ")
        inicio.lower( )    
    if  inicio == "si":
        print("VAMOS A JUGAR!")
        user = input("¿Cómo te llamas? ") #se pide el nombre del usuario para registrarlo
        print(user,"Bienvenid@!")
        godin = input("¿cómo quieres que se llame el godín? ") #se pide el nombre del godin para registrarlo
        print(godin,"Me gusta ese nombre...")
        instructions( )
        juego ( )
main()

#aqui se inicia el juego en realidad