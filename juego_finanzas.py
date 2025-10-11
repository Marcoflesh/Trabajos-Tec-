#esta biblioteca la uso para poder generar los salarios del godin de manera aleatoria, mediante rangos para poder delimitar un ingreso diferente y menor cada día

import random as rd

#variables
#están diseñadas para poder tener variedad de opciones a la hora de escoger el gasto del usuario

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
Salida_pareja = 80
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

#estas son listas donde almacenaré las opciones que escogió el usuario y posteriormente hacer calculos al final del juego en caso de terminarlo bien
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

#estas listas contienen las variables con precios asignados para que el usuario escoja la que más le plazca 
#cada día tiene costos y opciones diferentes, para que sea un día diferente 
#se empieza con el valor "0" para que al escoger la opción 1, el programa entienda que será la posición 1 y no la 0. Así escogerá "Comida_Chatarra" por ejemplo
costos1 = [0,Comida_Chatarra,pago_plan_celular,Comida_Sana,Salida_pareja]
costos2 = [0,ropa,Videojuegos,Gasolina,Comida_Sana]
costos3 = [0,Comida_Sana,Videojuegos,medicinas,Netflix]
costos4 = [0,pago_plan_celular2,Comida_Chatarra,calzado,productos_para_la_cara]
costos5 = [0,Comida_Sana,Cine,Salida_pareja,Disney]
costos6 = [0,internet,pago_plan_celular3,hojas_impresora,salida_amigos]
costos7 = [0,productos_limpieza_casa,nuevo_iphone,despensa_completa,manga]

#esta es una lista de listas que contiene todos los costos y opciones dentro de una sola lista. 
#Se usará para poder generar los resultados de gastos totales al final
costos_total = [0,
                costos1,
                costos2,
                costos3,
                costos4,
                costos5,
                costos6,
                costos7]
nombres_costos = [
    [0,"Comida Chatarra","Plan Celular","Comida Sana","Salida con la Pareja"],
    [0,"Ropa","Videojuegos","Gasolina","Comida Sana"],
    [0,"Comida Sana","Videojuegos","Medicinas","Neftlix"],
    [0,"Pagar Celular","Comida Chatarra","Calzado","Productos para la Cara"],
    [0,"Comida Sana","Cine","Salida con la Pareja","Disney"],
    [0,"Pagar Internet","Pagar Celular","Hojas para Impresora","Salir con Amigos"],
    [0,"Productos para Limpar la Casa","Nuevo Iphone","Despensa Completa","Manga"]
]
#estas dos matrices o listas anidadas, están vacías ya que en la función juego se estarán llenando poco a poco conforme vaya pasando el usuario los días.
opcion_opciones = []
ingreso_dias = []

#Funciones
#Aqui se presentan las instrucciones antes de empezar el juego
def instructions( ):
    print("Pefecto! \nBienvenid@", user, "a este simulador donde administrás las finanzas de",godin, "(presiona enter para seguir) ")
    input("")
    print("Tu misión será que",godin,"logre sobrevivir una semana \nSIN que sus finanzas lleguen a 0. Tendrás que controlar sus gastos (presiona enter para seguir) ")
    input("")
    print("¿Suena fácil no? Pues, cada día",godin,"ganará menos \nhaciendo que tendrás que pensar más cómo llevar los gastos de",godin, "(presiona enter para seguir) ")
    input("")
    print("acabando el día se te asignará una ganancia cada vez menor \nLo que tendrás que hacer será escoger la mejor opcion para que",godin,"\npueda sobrevivir "
        "\nPara asignarla escribe el NÚMERO al que corresponda la opción que quieras" 
      "\nSi las finanzas de",godin, "llegan a 0, será GAME OVER (presiona enter para seguir)")
    input("")


#Estas son las funciones que utilicé para poder hacer los ingresos de manera aleatoria con la biblioteca de random, realizar reducciones de los ingresos para complicar el juego y poder realizar
#y promedios de lo que se ingresó con lo que se gastó utilizando ciclos for y listas anidadas
'''comentar las funciones'''

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
   
   #este ciclo me ayudó un amigo de mecánica a entenderlo 
   #mientras no se cumpla la opcion del usuario que sea un numero entre 1-4, se repetirá el ciclo
    while True:
        try:
            opcion = int(input("¿En qué los quieres gastar? \nEscoge entre \n1.comida chatarra \n2. Plan del celular \n3.comida sana \n4.salidas con la pareja \n" ))
            if opcion in [1,2,3,4]:
                break #en caso de cumplirse se rompe el ciclo y hará la resta del ingreso con la opción que escogió
            else: #en caso de dar un número fuera del rango, se repetirá el bucle
                print("Escoge un numero Válido")
        #En caso de dar por accidente la tecla enter, en vez de dar error, le pedirá al usuario que ingrese un número para poder seguir
        except ValueError:
            print("Entrada inválida, esoge un número")

    #En caso de pasar el ciclo, se hará un resta entre el ingreso y la opción
    restante1 = ingresod1 - costos1[opcion]
    #Después de la resta se muestra lo que se gastó y la opción que escogió, para eso uso una matriz donde tengo la opción que se escoge y la muestra en base
    # a la opción que el usuario escogió
    print ("Gastaste:","$",costos1[opcion],"en",nombres_costos[0][opcion]+".","Ahora te restan $", restante1)
    #para poder hacer los cálculos de gastos totales al final, la opción se guardará en una lista llamada opcion_opciones[]
    opcion_opciones.append(opcion,)
    #en caso de hacer un mal gasto y tener la cuenta del godin en 0. Perderás el juego y se te llevará a la función main(), a manera de reinicio del juego
    if restante1 <= 0:
        print("game over")
        main( )
    
    #aqui se repite el ciclo pero con otro día y otras variables.
    ingresod2 = ingresodia2( )
    dia2 = restante1 + ingresod2
    ingreso_dias.append(ingresod2,)

    #añadi el pago del agua para poder hacer más retador este juego
    #llama a la funcion pago_CFE y en base a lo que se ganó en el día lo restará al precio del recibo del agua
    #en caso de que ese gasto deje en 0 la cuenta del godin, será game over
    if pago_CFE(50,dia2) <= 0:
        print("game over")
        main( )

    #asigné el valor yo mismo de lo que se tiene que pagar a la CFE para posteriormente alterar lo que se genera en este día
    #probablemente haga esta parte aleatoria

    print ("En el segundo día de trabajo",godin, "ganó: $", ingresod2, " más el restante de ayer ahora",godin,"tiene $", dia2)
    print ("¡Oh no!, a ", godin, "le llegó el recibo de luz y tuvo que pagar $50, ahora le quedan $", pago_CFE(50,dia2))
    #aqui ya se está tomando el descuento por el recibo de luz
    
    while True:
        try:
            opcion2 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Ropa \n2. Videojuegos \n3. Gasolina \n4. Comida Sana \n " ))
            if opcion2 in [1,2,3,4]:
                break
            else:
                print("Escoge un numero Válido")
        except ValueError:
            print("Entrada inválida, esoge un número")

    restante2 = pago_CFE(50,dia2)-costos2[opcion2]
    print ("Gastaste:","$",costos2[opcion2],"en",nombres_costos[1][opcion2]+".","Ahora te restan $", restante2)
    opcion_opciones.append(opcion2,)
    
    if restante2 <= 0:
        print("game over")
        main( )

    ingresod3 = ingresodia3( )
    dia3 = restante2 + ingresod3
    ingreso_dias.append(ingresod3,)
    #Para darle más opciones de gasto al usuario y complicar el juego, puse una opción obligatoria para poder avanzar 
    #Que son las medicinas, si no las escoge el usuario resultará en Game Over
    print ("En este tercer día", godin, "ganó $", ingresod3, "más el restante de ayer ahora",godin,"tiene $", dia3,
           "\n¡OH VAYA! te acabas de enfermar y necesitas medicamentos para poder sobrevivir el día")
   
    
    while True:
        try:
            opcion3 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Comida Sana \n2. Videojuegos \n3. Medicinas \n4. Netflix  \n" ))
            if opcion3 in [1,2,3,4]:
                break
            else:
                print("Escoge un numero Válido")
        except ValueError:
            print("Entrada inválida, esoge un número")

    #En caso de no escoger la opción de las medicinas, El juego terminará debido a que el godín caerá enfermo
    if opcion3 != 3:
        print("Game Over. Te moriste por no comprar medicamentos")
        main()

    restante3 = dia3 - costos3[opcion3]
    print ("Gastaste:","$",costos3[opcion3],"en",nombres_costos[2][opcion3]+".","Ahora te restan $", restante3)
    opcion_opciones.append(opcion3,)

    if restante3 <= 0:
        print("game over")
        main( )

    ingresod4 = ingresodia4( )
    dia4 = restante3 + ingresod4
    ingreso_dias.append(ingresod4,)
    print ("En este cuarto día",godin,"ganó $", ingresod4, "más el restante de ayer ahora",godin, "tiene $", dia4)
    
    while True:
        try:
            opcion4 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Pagar el plan del Celular \n2. Comida Chatarra" \
    " \n3. calzado \n4. Productos para la cara \n " ))
            if opcion4 in [1,2,3,4]:
                break
            else:
                print("Escoge un numero Válido")
        except ValueError:
            print("Entrada inválida, esoge un número")
    
    restante4 = dia4 - costos4[opcion4]
    print ("Gastaste:","$",costos4[opcion4],"en",nombres_costos[3][opcion4]+".","Ahora te restan $", restante4)
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

    while True:
        try:
            opcion5 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Comida Sana \n2. Cine \n3. Salir con la pareja \n4. Disney+ \n " ))
            if opcion5 in [1,2,3,4]:
                break
            else:
                print("Escoge un numero Válido")
        except ValueError:
            print("Entrada inválida, esoge un número")

    restante5 = pago_CEA(47,dia5) - costos5[opcion5]
    print ("Gastaste:","$",costos5[opcion5],"en",nombres_costos[4][opcion5]+".","Ahora te restan $", restante5)
    opcion_opciones.append(opcion5,)

    if restante5 <= 0:
        print("game over")
        main( )

    ingresod6 = ingresodia6( )
    #aqui el godin trabajó media jornada, por ende solo se le pagó la mitad de lo que le tocaba ese día
    #llamé a la función que hace el cálculo de lo que le tocará al godín por trabajar medio día
    dia6 =int(restante5 + pago_media_jornada(.5,ingresod6))
    ingreso_dias.append(ingresod6,)
    print("OH NO!, solo trabajaste media jornada, asi que lo que ganaste se dividirá a la mitad")
    print ("En este sexto día",godin, "ganó $", ingresod6, "más el restante de ayer, sumando el descuento de la media jornada",godin,"ahora tiene $", dia6)
   
    while True:
        try:
            opcion6 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1.Internet \n2.Pagar el celular \n3. Hojas para impresora \n4. Salida con amigos \n " ))
            if opcion6 in [1,2,3,4]:
                break
            else:
                print("Escoge un numero Válido")
        except ValueError:
            print("Entrada inválida, esoge un número")
   #En caso de que en el día 1 o día 4 no se haya escogido la opción de pagar el celular, aquí se forzará ese hecho para poder seguir el juego
   #En caso de no pagarlo en ninguno de esos días, el usuarió habrá perdido el juego
   #Si el usuario llega a pagar el celular en cualquiera de los días donde aparezca, el juego continuará 
   #Si el usuario paga antes del día 6 el celular, en este día podrá escoger otra opción sin problemas
    while opcion != 2 and opcion4 != 1 and opcion6 != 2:
        print("Game Over. \nte quedaste sin celular y ahora tu proveedor te lo bloqueo y explotó \ngg")
        main()

    restante6 = dia6 - costos6[opcion6]
    print ("Gastaste:","$",costos6[opcion6],"en",nombres_costos[5][opcion6]+".","Ahora te restan $", restante6)
    opcion_opciones.append(opcion6,)

    if restante6 <= 0:
        print("game over")
        main( )


    ingresod7 = ingresodia7( )
    dia7 = restante6 + ingresod7
    ingreso_dias.append(ingresod7,)
    print ("En este séptimo y último día",godin,"ganó $",ingresod7, "más el restante de ayer ahora él tiene $", dia7)

    while True:
        try:
            opcion7 = int(input("¿En qué los quieres gastar? \nEscoge entre \n1. Productos para limpieza de casa \n2. El nuevo Iphone \n3. despensa completa \n4. manga \n " ))
            if opcion7 in [1,2,3,4]:
                break
            else:
                print("Escoge un numero Válido")
        except ValueError:
            print("Entrada inválida, esoge un número")

    restante7 = dia7 - costos7[opcion7]
    print ("Gastaste:","$",costos7[opcion7],"en",nombres_costos[6][opcion7]+".","Ahora te restan $", restante7)
    opcion_opciones.append(opcion7)

    if restante7 <= 0:
        print("game over")
        main( )

    #Si el jugador llega a pasar del día 7 con una cuenta superior a 0, se mostrará esta parte
    print("FELICIDADES ",user+"!", "COMPLETASTE EL JUEGO \n lograste hacer que",godin,"Termine la semana con dinero de sobra")
    #el .upper() es para poner en mayúsculas al usuario a manera de felicitarlo
    user.upper()
    #aqui se muestran las funciones a las cuales se estuvieron integrando los ingresos y las opciones de los días con sus variables
    #Se mostrarán los ingresos totales,el promedio de ingresos del godín, la suma de los gastos que hizo el usuario y el promedio de gasto por día del usuario
    print("En total ganaste: $",sum_ingresos(),"con un promedio de: $",('%.2f'%(sum_ingresos()/7)),"por día, y gastaste: $",
            suma_dias_opcion(),"con un gasto promedio de: $",
              ('%.2f'%(suma_dias_opcion()/7)),"por día")
    #Aquí retornará al usuario a poder volver a jugar el juego
    main()
#me ayudó una becaria a poder realizar esto
#esta función es la madre de todo el programa, está hasta el final para que asi tenga todos las funciones y variables ya dentro de, esta funcion lo que hace es empezar el juego y
# cuando le das play te lleva primero a que ingreses si deseas jugar y este está dentro de un bucle el cual hasta que no digas que "si", no empiezas el juego
#en caso de que el juego no empiece al dar "si", solo reinicie y estará solucionado
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
#aqui se inicia el juego 