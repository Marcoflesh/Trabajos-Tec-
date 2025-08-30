import random
#esta función importó una biblioteca de Python que justo me generará los números aleatorios que usaré para el salario del godin
def start (inicio): 
    #esta función está principalmente puesta para que pueda detectar cuales son las respuestas del usuario y en base a eso asignar si quiere jugar o no
    if inicio == "si": #entrada inicial, si se cumple inicia el juego
        print("VAMOS A JUGAR!") #entrada final
        #estado inicial 
    while inicio == "no": #en caso de no poner "si", se hará este loop hasta que el usuario diga que si para iniciar
        inicio = input("quieres iniciar el juego? (di si o no en MINÚSCULAS) ") #entrada final
        #como se genera algo raro al poner "si" en vez de "no" a la primera, asigné esta para forzar al programa a iniciar debidamente  
        if inicio == "si": #entrada
            print("VAMOS A JUGAR!") #salida de datos 
    return inicio #esto asigna la variable de "inicio" a la funcion "start" 
#aquí se asignan los valores para que se pueda asignar la función de "inicio"
inicio = input("Quieres inicar el juego? (di si o no en minúsculas por favor) ")
#aqui voy a dar inicio al programa preguntando al jugadro si desea jugar
#tienen que ser minúsculas sino el programa hace lo que quiere (aun se trabaja en ello)
print("que bueno que escogiste","'",start(inicio),"'","me alegro de tu elección") #esto es para poder que se active la funcion "inicio" y puse un texto para que no se vea tan raro

def asignar_user (user):
    #aqui se está asignando los valores del nombre del usuario
    return user #aqui se almacena ese valor
user = input("¿Cómo te llamas? ") #se pide el nombre del usuario para registrarlo en la funcion "asingar_user"
user = asignar_user(user) #aqui el valor dado de la función se almacena en la variable para poder usarse después
print(user,"Bienvenido!")

def asignar_godin (godin): #pasa lo mismo que para el user solo que ahora será el nombre del personaje del juego el que se asignará en la función
    return godin
godin = input("¿cómo quieres que se llame el godín? ")
godin = asignar_godin(godin)
print(godin,"Me gusta ese nombre...")

#Aqui se presentan las instrucciones antes de empezar el juego
print("Pefecto! \nBienvenido a este simulador donde administrás las finanzas de",godin)
print("Tu misión será que",godin,"logre sobrevivir una semana \nSIN que sus finanzas lleguen a 0. Tendrás que controlar sus gastos")
print("¿Suena fácil no? Pues, cada día",godin,"ganará menos \nhaciendo que tendrás que pensar más cómo llevas los gastos de",godin)
print("acabando el día se te asignará una ganancia cada vez menor \nLo que tendrás que hacer será escoger el/los mejores gastos para que",godin,"\npueda sobrevivir"
      "sin problemas. \nPara asignar la mejor opción escrible el NÚMERO al que corresponda la opción que quieras" 
      "\nSi llegas a 0 o no cumples con ciertas demanas que necesite",godin, "será GAME OVER")

## aqui inicia el juego con el "godin" y las primeras opciones y el avance 2 del proyecto jajajajaja
#primero haré las operaciones para en la siguiente entrega hacer la estructura de cada día
#aqui estoy diciendole a Python que las variables que estoy asignando serán numéricas para que no haya problemas
#de mientras estas serán las variables iniciales, poco a poco se asignarán más
#las funciones de igual manera se pondrán después
Ingreso = 0
Gastos = 0
seleccion = 0
Nuevo_celular = 0
Comida = 0
Videojuegos = 0
Cine = 0
Netflix = 0
Gasolina = 0
Medicina = 0
Salida_novia = 0
gasto2 = 0
gasto3 = 0
gasto4 = 0
gasto5 = 0
gasto6 = 0
gasto7 = 0

Ingreso2 = random.randint(70,85)
Ingreso3 = random.randint(60,70)
Ingreso4 = random.randint(50,65)
Ingreso5 = random.randint(45,60)
Ingreso6 = random.randint(8,40)
Ingreso7 = random.randint(10,35)
gasto = 0

#aun no haré el return al juego si sale game over xd

Ingreso = random.randint(80,100)

print ("día 1.", godin, "ganó $", Ingreso, "¿En qué lo quieres gastar?")
print("1. cine $29 \n2. Netlfix $40 \n3. Comida $70 \n4. Salida con la novia $80")
seleccion = int(input("¿cúal escoges? "))
#escoge la 2
if seleccion == 2:
    gasto = Ingreso - 40
print("Felicidades te quedan $",gasto)



dia2 = Ingreso + gasto
print("día 2.", godin, "Hoy trabajó 3 horas más, se te triplcará. la hora extra se paga a $10 y su ingreso es de", Ingreso2, "\n¿En qué deseas gastarlo?")
#aqui se calculan las horas extra
hora_extra = 3
pago_horaex = hora_extra * 10
pago_horaex = pago_horaex + Ingreso2
pago_horaex = pago_horaex + dia2

print("ahora tiene por las horas extra: ",pago_horaex)
print("1. cine $29 \n2. Nuevo_celular $65 \n3. Comida $40 \n4. Gasolina $50")
seleccion = int(input("¿cúal escoges? "))
#escoge la 1
if seleccion == 1:
    gasto2 = Ingreso2 - 29
print(gasto2)
#ya solo es un copy paste de lo anterior, posteriormente se pondrán ya completos los valores de las opciones


dia3 = Ingreso2 + gasto2   
print ("día 3.", godin, "ganó $", Ingreso3,"+ $",dia3, "¿En qué lo quieres gastar?")
print("1. cine $29 \n2. Netlfix $40 \n3. Comida $70 ")
seleccion = int(input("¿cúal escoges? "))
if seleccion == 1:
    gasto3 = Ingreso - 29
    print("Felicidades te quedan $",gasto3)
if seleccion == 2:
    gasto3 = Ingreso - 40
    print("Felicidades te quedan $",gasto3)
if seleccion == 3:
    gasto3 = Ingreso - 70
    print("Felicidades te quedan $",gasto3)


dia4 = Ingreso3 + gasto3 
print ("día 4.", godin, "ganó $", Ingreso4, "+ $",dia4, "¿En qué lo quieres gastar?")
print("1. cine $29 \n2. Netlfix $40 \n3. Comida $70 ")
seleccion = int(input("¿cúal escoges? "))
if seleccion == 1:
    gasto4 = Ingreso - 29
    print("Felicidades te quedan $",gasto4)
if seleccion == 2:
    gasto4 = Ingreso - 40
    print("Felicidades te quedan $",gasto4)
if seleccion == 3:
    gasto4 = Ingreso - 70
    print("Felicidades te quedan $",gasto4)


dia5 = Ingreso4 + gasto4 
print ("día 5.", godin, "ganó $", Ingreso5,"+ $",dia5, "¿En qué lo quieres gastar?")
print("1. cine $29 \n2. Netlfix $40 \n3. Comida $70 ")
seleccion = int(input("¿cúal escoges? "))
if seleccion == 1:
    gasto5 = Ingreso - 29
    print("Felicidades te quedan $",gasto5)
if seleccion == 2:
    gasto5 = Ingreso - 40
    print("Felicidades te quedan $",gasto5)
if seleccion == 3:
    gasto5 = Ingreso - 70
    print("Felicidades te quedan $",gasto5)


dia6 = Ingreso5 + gasto5 
print ("día 6.", godin, "ganó $", Ingreso6,"+ $",dia6, "¿En qué lo quieres gastar?")
print("1. cine $29 \n2. Netlfix $40 \n3. Comida $70 ")
seleccion = int(input("¿cúal escoges? "))
if seleccion == 1:
    gasto6 = Ingreso - 29
    print("Felicidades te quedan $",gasto6)
if seleccion == 2:
    gasto6 = Ingreso - 40
    print("Felicidades te quedan $",gasto6)
if seleccion == 3:
    gasto6 = Ingreso - 70
    print("Felicidades te quedan $",gasto6)


dia7 = Ingreso6 + gasto6 
print ("día 7.", godin, "ganó $", Ingreso7,"+ $",dia7, "¿En qué lo quieres gastar?")
print("1. cine $29 \n2. Netlfix $40 \n3. Comida $70 ")
seleccion = int(input("¿cúal escoges? "))
if seleccion == 1:
    gasto7 = Ingreso - 29
    print("Felicidades te quedan $",gasto7)
if seleccion == 2:
    gasto7 = Ingreso - 40
    print("Felicidades te quedan $",gasto7)
if seleccion == 3:
    gasto7 = Ingreso - 70
    print("Felicidades te quedan $",gasto7)
