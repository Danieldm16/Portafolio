import random#libreria que nos ayuda a tener numeros aleatorios

#Está función nos ayuda a guardar en un arreglo la inversión y rendimiento de cada instrumento de inversión.
def pedirinstrumentos(numinstrumentos):#Necesita el numero de instrumentos para funcionar.
    contador = 0#contador de apoyo
    instrumentos = []#lista donde se guardan los instrumentos

    while contador < numinstrumentos:#Continua hasta que el numero de entradas se igual al numero de instrumentos.
        inversion = input(f'¿Cuanto se le tiene que invertir al instrumento {contador+1}?: ')#se pide la cantidad de inversión
        rendimiento = input(f'¿Cual es le rendimiento que saca de esa inversión?: ')#se pide la cantidad de rendimiento en numeros, no porcentaje.
        instrumentos+= [[float(inversion), float(rendimiento)]]#se añaden a la lista.
        contador+=1
    
    return instrumentos#retorna la lista que tiene la inversión y rendimiento de cada instrumento.

#Esta función se encarga de crear la primera generación la cual es aleatoria.
def primerageneracion(numinstrumentos, instrumentos):#necesita el numero de instrumentos y la lista instrumentos
    contadorprincipal = 0#contador de apoyo
    generacion = []#lista donde se guarda la primera generación
    generaciones = []#lista donde seguardaran todas las generaciónes
    individuo = []#lista donde se guardaran los datos de cada individuo
    inversion = 0#sirve para guardar la inversión de un individuo
    rendimiento = 0#sirve para guardar el rendimiento de un individuo

    while contadorprincipal < numinstrumentos:#el ciclo deja de repetirse cuando se llega al numero de instrumentos

        contador1 = 0#contador para los individuos dentro de cada generación

        while contador1 < numinstrumentos:#el ciclo deja de repetirse cuando se llega al numero de instrumentos
            individuo += [random.randint(0, 1)]#cada individuo puede ser 0 o 1, si es uno es que se toma el instrumento, si es cero no se toma
            contador1 +=1
        #de aqui puede salir algo asi: [0, 1, 0] que es un miembro de una generación.
    
        contador2 = 0#contador para la inversión y rendimiento de cada individuo.

        for gen in individuo:#el ciclo pasa por cada gen en un individuo
            if gen == 1:
                inversion += instrumentos[contador2][0]#se va sumando la inversión de los genes que son iguales a 1
                rendimiento += instrumentos[contador2][1]#se va sumando el rendimiento de los genes que son iguales a 1
            contador2+=1
        #se calcula la inversión y el rendimiento de cada gen en el individuo, de aqui sale algo así: inversión = 100 rendimiento = 68

        contadorprincipal+=1
        
        individuo += [inversion, rendimiento]#aqui se junta todo, dando algo asi: [0, 1, 0, 100, 68] teniendo todos los genes, la inversión y el rendimiento de cada individuo

        generacion += [individuo]#se ingresa el individuo a la generación

        individuo = []#se limpia el individuo para generar uno nuevo en el siguiente recorrido del ciclo
        inversion = 0#se regresa a cero para calcular la inversión de nuevo en el siguiente ciclo
        rendimiento = 0#se regresa a cero para calcular la inversión de nuevo en el siguiente ciclo

    generaciones += [generacion]#se ingresa la generación creada a la lista que contiene todas las generaciones

    return generaciones#se retorna la lista que contiene todas las generaciones, la cual ya lleva la primera generación hecha aleatoriamente.

#Esta función va a crear todas las demás generaciones dependiendo de cuantas generaciones se pidieron
def generargeneracionesymejorindividuo(numinstrumentos, instrumentos, generaciones, numgeneraciones, inversionmaxima):
    #Esta función necesita el numero de instrumentos, la lista de los instrumentos, la lista de las generaciones, el numero de generaciones y la inversión maxima que se puede hacer.
    contadorprincipal = 0#contador principal de los ciclos
    contadorsecundario = 0#contador secundario de los ciclos
    generacionanterior = generaciones[0]#guarda la generación que será usada para crear la siguiente generación
    contadoruno = 0#contador para referirse al primer individuo que se va a combinar
    contadordos = 1#contador para referirse al segundo individuo que se va a combinar
    contadorinversiones1 = 0#contador para las inversiónes del primer individuo nuevo generado
    contadorinversiones2 = 0#contador para las inversiones del segundo individuo nuevo generado
    generacion = []#guarda la generación actual
    individuo = []#guarda el primer individuo de una combinación generado
    individuo2 = []#guarda el segundo individuo de una combinación generado
    inversion = 0#guarda la inversión de un individuo
    rendimiento = 0#guarda el rendimiento de un individuo
    inversion2 = 0#guarda la inversión del segundo individuo de una combinación
    rendimiento2 = 0#guarda el rendimiento del segundo individuo de una combinación
    numindividuo = 0#nos dice cuantos individuos se han creado
    contadorinversiones3 = 0#contador para la inversión y rendimiento de un individuo que sale de una mutación
    mejoropcion = []#guarda el individuo que es mejor opcion, ganando más rendimiento sin revasar la inversión maxima
    contadoropcion = 0#contador para apoyar la mejor opcion inicial
    
    while contadoropcion < numinstrumentos+2:#es como un constructor de la lista mejor opción, la llena de 0 dependiendo el numero de instrumentos.
        mejoropcion = mejoropcion + [0]
        contadoropcion += 1

    print(f'Primera generacion generada aleatoriamente: {generacionanterior}')#se imprime la primera generación

    while contadorprincipal < numgeneraciones-1:#El ciclo funciona hasta que sean creadas todas las generaciones solicitadas

        for gen in generaciones:#se checha cual es la mejor opción en cada individuo de las generaciónes creadas hasta ahora.
            for ind in gen:
                if ind[-2] <= inversionmaxima and ind[-1] >= mejoropcion[-1]:
                    mejoropcion = ind

        print(f'La mejor opción por ahora es: {mejoropcion[:-2]}, con inversión de: {mejoropcion[-2]} y rendimiento de: {mejoropcion[-1]}') #imprime la mejor opción y sus datos.
        
        contadorsecundario = numinstrumentos#se inicializa el contador secundario cada corrida del ciclo.

        print(f'Generación de donde vienen los padres y o muta algún individuo: {generacionanterior}')#se imprime la generación de donde se harán combinaciones o mutara para la nueva generación.

        while contadorsecundario > 0:#El ciclo funciona hasta que se chequen todos los instrumentos en la generación pasada.

            if contadorsecundario > 1:#si quedan dos o más individuos para combinar se entra aqui.

                limite = len(generacionanterior[numindividuo]) - 3#se genera el limite del punto de cruce, este por que si los individuos son asi [0, 1, 0, 60, 30]
                #se podria seleccionar hasta el 2, ya que en 3 esta la inversion y en 4 el rendimiento.

                puntodecruce = random.randint(1, limite)#se genera el punto de cruce, de 1 a el limite generado anteriormente.

                print(f'Padres: {generacionanterior[contadoruno][:-2]} y {generacionanterior[contadordos][:-2]}')#imprime los padres de los individuos que se crearan por combinacion.

                print(f'El punto de cruce es: {puntodecruce}')#imprime el punto de cruce

                print(f'Parte 1: {generacionanterior[contadoruno][:puntodecruce]}')#imprime la parte uno del nuevo individuo
                print(f'Parte 2: {generacionanterior[contadordos][puntodecruce:-2]}')#imprime la segunda parte del nuevo individuo

                individuo = individuo + generacionanterior[contadoruno][:puntodecruce]#se concatena la primera parte del nuevo individuo
                individuo = individuo + generacionanterior[contadordos][puntodecruce:-2]#se concatena la segunda parte del nuevo individuo

                for gen in individuo:#se saca la inversión y el rendimiento del nuevo individuo
                    if gen == 1:
                        inversion += instrumentos[contadorinversiones1][0]
                        rendimiento += instrumentos[contadorinversiones1][1]
                    contadorinversiones1+=1
                
                individuo += [inversion, rendimiento]#se concatena la inversión y el rendimiento al individuo.

                print(f'Hijo uno : {individuo}')#se imprime el individuo creado.

                print(f'Parte 1: {generacionanterior[contadordos][:puntodecruce]}')#imprime la primera parte del segundo nuevo individuo
                print(f'Parte 2: {generacionanterior[contadoruno][puntodecruce:-2]}')#imprime la segunda parte del segundo nuevo individuo

                individuo2 = individuo2 + generacionanterior[contadordos][:puntodecruce]#se concatena la primera parte del segundo nuevo individuo
                individuo2 = individuo2 + generacionanterior[contadoruno][puntodecruce:-2]#se concatena la segunda parte del segundo nuevo individuo
                
                for gen in individuo2:#se saca la inversión y el rendimiento del segundo nuevo individuo
                    if gen == 1:
                        inversion2 += instrumentos[contadorinversiones2][0]
                        rendimiento2 += instrumentos[contadorinversiones2][1]
                    contadorinversiones2+=1
                
                individuo2 += [inversion2, rendimiento2]#se concatena la inversión el rendimiento del segundo nuevo individuo.

                print(f'Hijo dos : {individuo2}')#se imrpime el segundo nuevo individuo creado

                contadoruno += 2
                contadordos += 2
                #estos contadores apoyan a saber que individuos son padres de los que se estan combinando, entonces la primera vez que se combinan es el individuo 0 y el individuo 1
                #la segunda vez serán el individuo 2 y el individuo 3, y así continuamente.

                #se añaden los individuos creados de combinaciones a la generación actual.
                generacion += [individuo]
                generacion += [individuo2]

                #se limpian las listas de cada individuo para que se puedan crear sin residuos los otros individuos en la siguiente corrida del ciclo.
                individuo = []
                individuo2 = []

                #se suman los dos individuos creados a numero de individuos y se quitan dos de los que quedan por crear.
                numindividuo+=2
                contadorsecundario-=2

                #se regresan a su estado inicial todas las variables auxiliares usadas.
                inversion2 = 0
                inversion = 0
                rendimiento2 = 0
                rendimiento = 0
                contadorinversiones1 = 0
                contadorinversiones2 = 0
            
            else:#aqui solo se entra si no hay suficientes individuos para combinar, entonces se hace una mutación

                genquemuta = random.randint(0, len(generacionanterior[numindividuo])-3)#se elige de una forma aleatoria el gen que mutara en el individuo.

                individuo = []#se establece el individuo como una lista vacia

                individuo = individuo + generacionanterior[numindividuo][:-2]#se llena el individuo con los datos del individuo que va a mutar.

                print(f'Individuo que va a mutar: {generacionanterior[numindividuo][:-2]}')#se imprime el individuo que va a mutar

                if individuo[genquemuta] == 0:#muta el gen seleccionado, si era 0 pasa a 1 y si era 1 pasa a 0
                    individuo[genquemuta] = 1
                else:
                    individuo[genquemuta] = 0
                
                for gen in individuo:#se calcula la inversión y rendimiento del individuo con su mutación
                    if gen == 1:
                        inversion += instrumentos[contadorinversiones3][0]
                        rendimiento += instrumentos[contadorinversiones3][1]
                    contadorinversiones3+=1
                
                individuo += [inversion, rendimiento]#se concatenan la inversión y el rendimiento al individuo con gen mutado.

                print(f'Individuo con gen mutado : {individuo}')#imprime el individuo con gen mutado.

                generacion += [individuo]#se concatena el individuo a la generación actual.

                individuo = []#se vuelve a establecer el individuo como una lista vacia para el proximo recorrido del ciclo.

                #se suma un individuo al numero de individuos generados y se quita uno de los que faltan por generar.
                numindividuo+=1
                contadorsecundario-=1

                #se regresa a su estado inicial las variables auxiliares usadas.
                contadorinversiones3 = 0
        
        #la generación que se acaba de crear se establece como la siguiente generación a usar y se concatena las generaciones creadas.
        generacionanterior = generacion
        generaciones += [generacion]

        #se regresa a su estado inicial todas las variables auxiliares usadas para el siguiente recorrido del ciclo.
        generacion = []
        contadoruno = 0
        contadordos = 1
        numindividuo = 0
        inversion = 0
        rendimiento = 0
        inversion2 = 0
        rendimiento2 = 0
        contadorinversiones1 = 0
        contadorinversiones2 = 0
        contadorinversiones3 = 0

        #se aumenta el contador principal, indicando que se creo otra generación.
        contadorprincipal+=1
    
    #Con estas lineas de codigo se imprime de forma bonita todas las generaciones creadas.
    contgen = 1
    print(f'Todas las generaciones:')
    for gen in generaciones:
        print(f'Generacion {contgen}:')
        for ind in gen:
            print(f'{ind[:-2]} inversion: {ind[-2]} rendimiento: {ind[-1]}')
        contgen+=1

    #se busca la mejor opción en todas las generaciones que fueron creadas
    for gen in generaciones:
        for ind in gen:
            if ind[-2] <= inversionmaxima and ind[-1] >= mejoropcion[-1]:
                mejoropcion = ind

    print(f'La mejor opción al final es: {mejoropcion[:-2]}, con inversión de: {mejoropcion[-2]} y rendimiento de: {mejoropcion[-1]}') #se imprime la mejor opción
    
    return generaciones#retorna todas las generaciones creadas.

#------------------------------------------------------------------------------------------------

numinstrumentos = input("¿Cuantos instrumentos de inversión va a ingresar?: ")#guarda el numero de instrumentos de inversión en el ejercicio.
montomaximo = input("¿Cual es el monto maximo que se puede invertir?: ")#guarda el monto maximo de inversión en el ejercicio.
numgeneraciones = input('¿Cuantas generaciones va a generar?: ')#guarda el numero de generaciones que se deben crear en el ejercicio.
instrumentos = pedirinstrumentos(int(numinstrumentos))#se usa la funcion que nos da la inversión y rendimiento de cada instrumento.
generacionuno = primerageneracion(int(numinstrumentos), instrumentos)#se crea la primera generación aleatoriamente.
generaciones = generargeneracionesymejorindividuo(int(numinstrumentos), instrumentos, generacionuno, int(numgeneraciones), int(montomaximo))#se crean todas las siguientes generaciones.