import random#libreria que nos ayuda a tener numeros aleatorios

#Esta función se encarga de crear la primera generación la cual es aleatoria.
def primerageneracion():#
    contadorprincipal = 0#contador de apoyo
    generacion = []#lista donde se guarda la primera generación
    generaciones = []#lista donde se guardaran todas las generaciónes
    individuo = []#lista donde se guardaran los datos de cada individuo

    while contadorprincipal < 4:#el ciclo deja de repetirse cuando se llega al numero de instrumentos que ocupamos
        #en el examen se indico que habría 4 individuos en cada generación con 8 genes respectivamente.

        contador1 = 0#contador para los individuos dentro de cada generación

        while contador1 < 8:#el ciclo deja de repetirse cuando se llega al numero de reinas (genes en el individuo).
            individuo += [random.randint(1, 8)]#cada individuo puede ser 1 a 8
            contador1 +=1
        #de aqui puede salir algo asi: [8, 1, 3, 1, 4, 6, 3, 2] que es un miembro de una generación.

        contadorprincipal+=1

        generacion += [individuo]#se ingresa el individuo a la generación

        individuo = []#se limpia el individuo para generar uno nuevo en el siguiente recorrido del ciclo

    generaciones += [generacion]#se ingresa la generación creada a la lista que contiene todas las generaciones

    return generaciones#se retorna la lista que contiene todas las generaciones, la cual ya lleva la primera generación hecha aleatoriamente.

#Esta función va a crear todas las demás generaciones dependiendo de cuantas generaciones se pidieron
def generargeneracionesymejorindividuo(numinstrumentos, generaciones, numgeneraciones):
    #Esta función necesita el numero de instrumentos el cual es 8 para el problema de las reinas
    # , la lista de las generaciones, y el numero de generaciones que se van a crear.
    contadorprincipal = 0#contador principal de los ciclos
    contadorsecundario = 0#contador secundario de los ciclos
    generacionanterior = generaciones[0]#guarda la generación que será usada para crear la siguiente generación
    contadoruno = 0#contador para referirse al primer individuo que se va a combinar
    contadordos = 1#contador para referirse al segundo individuo que se va a combinar
    generacion = []#guarda la generación actual
    individuo = []#guarda el primer individuo de una combinación generado
    individuo2 = []#guarda el segundo individuo de una combinación generado
    numindividuo = 0#nos dice cuantos individuos se han creado
    mejoropcion = []#guarda el individuo que es mejor opcion
    contadoropcion = 0#contador para apoyar la mejor opcion inicial
    numinstrumentos = 4 #en el problema 1 del examen se pidio 4 indivudos en cada generación y son 8 genes.
    
    while contadoropcion < numinstrumentos+2:#es como un constructor de la lista mejor opción, la llena de 0 dependiendo el numero de instrumentos.
        mejoropcion = mejoropcion + [0]
        contadoropcion += 1

    print(f'Primera generacion generada aleatoriamente: {generacionanterior}')#se imprime la primera generación

    while contadorprincipal < numgeneraciones-1:#El ciclo funciona hasta que sean creadas todas las generaciones solicitadas
        contadorsecundario = numinstrumentos#se inicializa el contador secundario cada corrida del ciclo.

        print(f'Generación de donde vienen los padres : {generacionanterior}')#se imprime la generación de donde se harán combinaciones o mutara para la nueva generación.

        while contadorsecundario > 0:#El ciclo funciona hasta que se chequen todos los instrumentos en la generación pasada.

                limite = len(generacionanterior[numindividuo]) - 1#genera el punto de cruce
                #hasta el penultimo gen en un individuo, para que al mezclarse no se cambien por completo.

                puntodecruce = random.randint(1, limite)#se genera el punto de cruce, de 1 a el limite generado anteriormente.

                print(f'Padres: {generacionanterior[contadoruno]} y {generacionanterior[contadordos]}')#imprime los padres de los individuos que se crearan por combinacion.

                print(f'El punto de cruce es: {puntodecruce}')#imprime el punto de cruce

                print(f'Parte 1: {generacionanterior[contadoruno][:puntodecruce]}')#imprime la parte uno del nuevo individuo
                print(f'Parte 2: {generacionanterior[contadordos][puntodecruce:]}')#imprime la segunda parte del nuevo individuo

                individuo = individuo + generacionanterior[contadoruno][:puntodecruce]#se concatena la primera parte del nuevo individuo
                individuo = individuo + generacionanterior[contadordos][puntodecruce:]#se concatena la segunda parte del nuevo individuo

                print(f'Hijo uno : {individuo}')#se imprime el individuo creado.

                print(f'Parte 1: {generacionanterior[contadordos][:puntodecruce]}')#imprime la primera parte del segundo nuevo individuo
                print(f'Parte 2: {generacionanterior[contadoruno][puntodecruce:]}')#imprime la segunda parte del segundo nuevo individuo

                individuo2 = individuo2 + generacionanterior[contadordos][:puntodecruce]#se concatena la primera parte del segundo nuevo individuo
                individuo2 = individuo2 + generacionanterior[contadoruno][puntodecruce:]#se concatena la segunda parte del segundo nuevo individuo
                
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
        
        #Esto decide si va a mutar algún gen, en algún individuo de la generación, para que mute
        #debe salir un numero del uno al 10, eso hace la probabilidad de mutar del 10%
        mutar = random.randint(1, 100)
        if mutar <= 10:
            #dice en que generación hay mutación y se consigue cual individuo en la generación mutara.
            print("    SE REALIZARÁ MUTACION EN ESTA GENERACIÓN")
            print(f"    Es la generación {len(generaciones) + 1}")
            individuoamutar = random.randint(0, len(generacion) -1)
            print(f"    En el individuo {individuoamutar}")
            print(f"    Individuo a mutar: {generacion[individuoamutar]}")
            #se descubre que gen en el individuo va a mutar aleatoriamente
            genamutar = random.randint(0, 7)
            #se crea la mutacion de forma aleatoria
            mutacion = random.randint(1, 8)

            #Se realiza un ciclo pequeño para comprobar que el gen cambie y no se quede igual.
            dif = False
            while dif == False:
                if generacion[individuoamutar][genamutar] == mutacion:
                    mutacion = random.randint(1, 8)
                    if generacion[individuoamutar][genamutar] != mutacion:
                        dif = True
                else:
                    dif = True
            
            #se cambia el valor del gen en el individuo por su mutación.
            generacion[individuoamutar][genamutar] = mutacion

            #se indica en que gen muto y se imprime el individuo después de mutar
            print(f"    Se realizo mutación en el gen {genamutar + 1}")
            print(f"    Después de mutar: {generacion[individuoamutar]}")
    
        #la generación que se acaba de crear se establece como la siguiente generación a usar y se concatena a las generaciones creadas.
        generacionanterior = generacion
        generaciones += [generacion]

        #se regresa a su estado inicial todas las variables auxiliares usadas para el siguiente recorrido del ciclo.
        generacion = []
        contadoruno = 0
        contadordos = 1
        numindividuo = 0

        #se aumenta el contador principal, indicando que se creo otra generación.
        contadorprincipal+=1

    #Se consigue el mejor individuo de la generación
    #se checa cuantas veces se golpean las reinas en cada individuo, y en el que menos se golpeen es el mejor
    #se sabe que se golpearon cuando aparece más de una vez un mismo numero en el individuo
    #por ejemplo si 1 sale dos veces, quiere decir que las reinas se pueden golpear 2 veces.
    numderepeticionesenindividuo = 0
    golpes = 0
    for generacionindividual in generaciones:#recorre cada generacion en las generaciones
        for individuo in generacionindividual:#recorre cada individuo en una generación

            individuosinrepeticiones = set(individuo)#nos da una lista sin que se repitan los genes

            for gen in individuosinrepeticiones:#recorre cada gen en un individuo
                numderepeticionesenindividuo = individuo.count(gen)#nos dice cuantas veces sale un gen en el individuo
                if numderepeticionesenindividuo > 1:#si sale más de una vez quiere decir que hay reinas golpeandose
                    numderepeticionesenindividuo -= 1#se quita uno para solo sumar las veces que se golpean
                    while numderepeticionesenindividuo > 0:#se van acumulando las veces que se golpean en el individuo
                        golpes += 1
                        numderepeticionesenindividuo -= 1
            
            individuo += [golpes]#se meten los golpes que hay en cada individuo
            golpes = 0#se regresa a su estado inicial los golpes en un individuo
    
    mejorindividuo = generaciones[0][0]#se inicializa el mejor individuo.
    
    for generacionindividual in generaciones:#se recorren cada generacion en las generaciones
        for individuo in generacionindividual:#se recorre cada individuo en las generaciones

            if individuo[-1] < mejorindividuo[-1]:#si el numero de golpes en el individuo es menor que el individuo
                #ya establecido como el mejor se deja al individuo con menos golpes como el mejor
                mejorindividuo = individuo
    
    #Con estas lineas de codigo se imprime de forma bonita todas las generaciones creadas.
    contgen = 1
    print(f'Todas las generaciones:')
    for gen in generaciones:
        print(f'Generacion {contgen}:')
        for ind in gen:
            print(f'{ind[:-1]}, veces que se golpean las reinas: {ind[-1:]}')
        contgen+=1
    
    #se imprime el mejor individuo y el numero de golpes que tiene.
    print(f"El mejor individuo fue: {mejorindividuo[:-1]} con un numero de golpes de reinas de: {mejorindividuo[-1:]}")
    
    return generaciones#retorna todas las generaciones creadas.

#------------------------------------------------------------------------------------------------

print('Algoritmo para el problema de las 8 reinas.')
print('El mejor individuo será en el que se repita el menor numero de veces un numero en la lista')
print('Esto es así por que cuando se repite un numero en un individuo quiere decir que se ')
print('están golpeando las reinas en la fila que dice el numero')
print('Por ejemplo en una lista [1, 3, 2, 5, 7, 2, 6, 8]')
print('en las columnas 3, y 6 se pueden golpear dos reinas al estar en la misma fila (fila 2).')
print('el programa utiliza 4 individuos con 8 genes en cada generación, como indica el problema 1 del ordinario')
print('por eso solo pide saber cuantas generaciones se harán.')
numgeneraciones = input('¿Cuantas generaciones va a generar?: ')#guarda el numero de generaciones que se deben crear en el ejercicio.
generaciones = primerageneracion()#guarda la primera generacion
generargeneracionesymejorindividuo(8, generaciones, int(numgeneraciones))#hace el proceso del algoritmo genetico