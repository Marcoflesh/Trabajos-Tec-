# TC1028 Proyecto Juego de Finanzas

## Marco Antonio Hernández Roque

Este proyecto es un juego que se hará en Python y tratará sobre como manejar los gastos darios de un godín, con el objetivo de educar al usuario sobre el manejo del dinero. La finalidad de que esto sea un juego es debido a que se intenta enseñar de una manera más interactiva el manejo de nuestras finanzas. 


## Contexto
Muchos de nosotros al ser gamers o personas con poca cultura sobre el manejo de las finanzas tendemos mucho a gastar en cosas que probablemente no necesitemos, dejando de un lado las cosas que SI importan tales como, la comida, artíulos de higiene, entre otras. Este es un simulador en forma de juego donde el usuario podrá administrar las finanzas del godín "X" (El nombre será definido por el Usuario) durante toda una semana para que pueda sobrevivir sin preocupaciones. Cada día se irá reduciendo el ingreso diario para generar un reto mayor al usuario y así plantearse en que debe de verdad gastar. Durante la semana habrán diversos eventos los cuales podrían reducir el dinero que se podrá gastar el "godin", al igual que habrán situaciones en las que deberá escoger una opción en específico para poder avanzar, también habrá una opción oculta la cual para poder avanzar el usuario la deberá escoger para así terminar el juego, mientras antes la escoja, más barata será esa opción. 
 En caso de no escoger cualquiera de esas opciones el juego terminará y volverá a iniciarse preguntandole al usuario si quiere jugar o no.
 
 

------------

##Algoritmo
    ## Algoritmo
    Inicio del Programa
    
    Preguntar al usuario: "¿Quieres iniciar el juego? (si/no)".
    
    SI la respuesta es "no":
    
    Mostrar "Gracias por jugar" y terminar el programa.
    
    SI la respuesta no es "si" o "no":
    
    Repetir la pregunta.
    
    SI la respuesta es "si":
    
    Mostrar "¡VAMOS A JUGAR!".
    
    Pedir el nombre del usuario (guardar como user).
    
    Pedir un nombre para el personaje (guardar como godin).
    
    Mostrar las instrucciones del juego.
    
    Comenzar el Juego Principal.
    
    Preparación (Antes de empezar el Día 1)
    
    Establecer costos fijos: LUZ = 50, AGUA = 47 y MEDIA_JORNADA = 0.5.
    
    Generar 7 ingresos aleatorios usando API random (uno para cada día), con rangos que van disminuyendo.
    
    Definir 4 opciones de gastos (con sus nombres y costos) para cada uno de los 7 días.
    
    Juego Principal (Día por Día)
    
    DÍA 1:
    
    dinero_actual = ingreso_dia_1.
    
    Mostrar dinero_actual y las 4 opciones del Día 1.
    
    Esperar a que el usuario elija una opción válida (1-4).
    
    dinero_restante = dinero_actual - costo_opcion_elegida.
    
    Mostrar gasto y dinero_restante.
    
    Comprobar Fin del Juego: Si dinero_restante <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    DÍA 2:
    
    dinero_actual = dinero_restante_dia_1 + ingreso_dia_2.
    
    EVENTO: Pagar recibo de LUZ.
    
    dinero_actual = dinero_actual - LUZ.
    
    Mostrar dinero_actual (después del pago) y las 4 opciones del Día 2.
    
    Comprobar Fin del Juego: Si dinero_actual <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    Esperar a que el usuario elija una opción válida (1-4).
    
    dinero_restante = dinero_actual - costo_opcion_elegida.
    
    Mostrar gasto y dinero_restante.
    
    Comprobar Fin del Juego: Si dinero_restante <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    DÍA 3:
    
    dinero_actual = dinero_restante_dia_2 + ingreso_dia_3.
    
    EVENTO: Alerta de enfermedad.
    
    Mostrar dinero_actual y las 4 opciones del Día 3.
    
    Esperar a que el usuario elija una opción válida (1-4).
    
    REGLA ESPECIAL:
    
    SI la opción elegida NO es la 3 ("Medicinas"):
    
    Mostrar "Game Over. Te moriste..." y volver al Inicio del Programa.
    
    dinero_restante = dinero_actual - costo_opcion_elegida (medicinas).
    
    Mostrar gasto y dinero_restante.
    
    Comprobar Fin del Juego: Si dinero_restante <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    DÍA 4:
    
    dinero_actual = dinero_restante_dia_3 + ingreso_dia_4.
    
    Mostrar dinero_actual y las 4 opciones del Día 4.
    
    Esperar a que el usuario elija una opción válida (1-4).
    
    dinero_restante = dinero_actual - costo_opcion_elegida.
    
    Mostrar gasto y dinero_restante.
    
    Comprobar Fin del Juego: Si dinero_restante <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    DÍA 5:
    
    dinero_actual = dinero_restante_dia_4 + ingreso_dia_5.
    
    EVENTO: Pagar recibo de AGUA.
    
    dinero_actual = dinero_actual - AGUA.
    
    Mostrar dinero_actual (después del pago) y las 4 opciones del Día 5.
    
    Comprobar Fin del Juego: Si dinero_actual <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    Esperar a que el usuario elija una opción válida (1-4).
    
    dinero_restante = dinero_actual - costo_opcion_elegida.
    
    Mostrar gasto y dinero_restante.
    
    Comprobar Fin del Juego: Si dinero_restante <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    DÍA 6:
    
    EVENTO: Media jornada. El ingreso del día se reduce a la mitad.
    
    ingreso_dia_6_real = ingreso_dia_6 * MEDIA_JORNADA.
    
    dinero_actual = dinero_restante_dia_5 + ingreso_dia_6_real.
    
    Mostrar dinero_actual y las 4 opciones del Día 6.
    
    Esperar a que el usuario elija una opción válida (1-4).
    
    REGLA ESPECIAL:
    
    SI (opción del Día 1 NO fue "Plan Celular") Y (opción del Día 4 NO fue "Pagar Celular") Y (opción del Día 6 NO es "Pagar Celular"):
    
    Mostrar "Game Over. Te quedaste sin celular..." y volver al Inicio del Programa.
    
    dinero_restante = dinero_actual - costo_opcion_elegida.
    
    Mostrar gasto y dinero_restante.
    
    Comprobar Fin del Juego: Si dinero_restante <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    DÍA 7:
    
    dinero_actual = dinero_restante_dia_6 + ingreso_dia_7.
    
    Mostrar dinero_actual y las 4 opciones del Día 7.
    
    Esperar a que el usuario elija una opción válida (1-4).
    
    dinero_restante = dinero_actual - costo_opcion_elegida.
    
    Mostrar gasto y dinero_restante.
    
    Comprobar Fin del Juego: Si dinero_restante <= 0, mostrar "Game Over" y volver al Inicio del Programa.
    
    Fin de la Partida (Victoria)
    
    (Se llega aquí solo si dinero_restante del Día 7 es > 0).
    
    Mostrar mensaje "¡FELICIDADES, COMPLETASTE EL JUEGO!".
    
    Calcular ingresos_totales (suma de los 7 ingresos generados).
    
    Calcular gastos_totales (suma de las 7 opciones elegidas + LUZ + AGUA).
    
    Calcular promedio_ingreso (ingresos_totales / 7).
    
    Calcular promedio_gasto (gastos_totales / 7).
    
    Mostrar todos los cálculos: ingresos, gastos y promedios.
    
    Preguntar "¿Quieres volver a jugar? (si/no)".
    
    SI la respuesta es "si":
    
    Volver al Inicio del Programa.
    
    SI la respuesta es "no":
    
    Mostrar "Gracias por jugar!" y terminar el programa.  (uso API system)
    
    SI la respuesta es otra:
    
    Repetir la pregunta.
    
    
    


## Instrucciones
### Descargar el archivo y abrir en la terminal: 
##### juego_finanzas.py
Seleccionar un nombre de usuario
 Seleccionar un nombre para el godín
 Administrar las finanzas del godín hasta el final de la semana sin llegar a $0.
Para administrar las finanzas del godín se deberá escoger la mejor opción de gasto por día
 Durante el juego habrán ciertos eventos los cuales reducirán el dinero restante del godín. 
Asímismo, habrán opciones obligatorias las cuales deberán ser escogidas para poder llegar al final del juego. 

## Uso API
Para este programa utilicé 3 bibliotecas de python, para poder realizar el juego. Estas les asigné una letra para identificarlas de manera más fácil, las cuales se mostrarán entre paréntesis.
##### Las bibliotecas son:
### random (r)
Esta se encarga de poder generar los ingresos de manera aleatoria con random.randint() el cual sirve para generar número en un rango determinado.
### time (t)
Esta se encarga para poder generar un cooldown mediante time.sleep() a los prints que estarán saliendo a la hora de jugar haciendo que sea más fácil de leer el programa.
### sys (s)
Esta se encarga para poder forzar la terminación del juego. Si el usuario decide no jugar y ya no volver a jugar al escoger la opción "no" la biblioteca forzará la terminación del juego mediante sys.exit().

### Gracias por leer

## Referencias API
#### https://docs.python.org/3/library/time.html
#### https://docs.python.org/3/library/random.html
#### https://docs.python.org/3/library/sys.html
