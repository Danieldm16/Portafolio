from operator import itemgetter#libreria que se utiliza para seleccionar los nodos menos pesados de cada nivel

#El propósito de esta función es recibir un grafo y darle formato para poder usarlo.
def leergrafo(grafo):#Recibe un grafo sin formato, algo como: 1 2 13,1 3 15,1 4 12,2 5 4,2 7 4,3 6 8,3 2 6,4 2 9,4 7 8,5 8 4,5 10 8,6 5 2,6 9 7,6 8 6,7 5 10,7 10 15,8 10 8,9 10 10
    #El grafo debe estar escrito de esta manera, siendo que cada ramificaicon que tiene un nodo padre se escriba seguido, por ejemplo en este grafo sin formato se nota que los primeros tres nodos son de padre 1
    #los siguientes dos son de padres dos y asi, si esta una como padre uno y le sigue un nodo con padre dos y después de nuevo uno con padre uno la función "valor_de_k" no va a funcionar.
    grafosinseparar = grafo.split(",")#Separa los elementos del string por comas 
    
    grafoseparado = []#lista para guardar el grafo separado
    
    for nodoaristaypeso in grafosinseparar:#En este ciclo se vuelven a separar los elementos ahora por espacios en blanco
        grafoseparado.append(nodoaristaypeso.split(" "))
    
    grafoinamovibleseparado = tuple(grafoseparado)#se transforma el grafo formateado en una tupla para mayor seguridad
    
    return grafoinamovibleseparado#Se retorna el grafo formateado.
#El grafo que returna se veria algo asi: [['1', '2', '13'], ['1', '3', '15'], ['1', '4', '12'], ['2', '5', '4'], ['2', '7', '4'], ['3', '6', '8'], ['3', '2', '6'], ['4', '2', '9'], ['4', '7', '8'], ['5', '8', '4'], ['5', '10', '8'], ['6', '5', '2'], ['6', '9', '7'], ['6', '8', '6'], ['7', '5', '10'], ['7', '10', '15'], ['8', '10', '8'], ['9', '10', '10']]
#El primer valor es el nodo padre, el segundo el nodo hijo y el tercero el peso entre ellos.

#El propósito de esta función es retornar el valor de k, el cual es la mayor cantidad de ramificaciones que tiene un nodo en el grafo.
def valor_de_k(grafo):#Recibe un grafo formateado
    k = 0#Establece el valor de k en 0
    valores_de_k = []#Servira para guardar la cantidad de veces que se repite cada nodo
    auxiliar2 = grafo[0][0]#Guarda el padre del primer nodo
    
    for nodo in grafo:#Recorre cada nodo en el grafo
        auxiliar = nodo[0]#Es igual al padre del nodo actual
        
        if auxiliar == auxiliar2:#Si los padres son iguales k se incrementa
            k += 1
        else:#Si ya no son iguales se guarda la cantidad de veces que salio ese padre y se regresa k a 1 para contar las veces que sale el siguiente padre
            valores_de_k.append(k)
            k = 1
        
        auxiliar2 = auxiliar#Se guarda el valor del nodo padre del nodo que será el anterior
        
    for kauxiliar  in valores_de_k:#Recorre la cantidad de veces que salio cada nodo de todos los nodos
        if kauxiliar >= k:#El valor de k más grande será el que se quede asignado
            k = kauxiliar
        
    return k#Se retorna el valor de k

#Esta función tiene como objetivo generar el árbol separado por niveles con sus pesos acumulados del grafo que fue ingresado.
def formararbolporniveles(grafoescrito, inicio):#Recibe como parametro el grafo sin formato y el nodo inicio
    nodospadres = [[inicio, 0]]#Aqui se van a ir guardando los nodos padres y su peso
    nivel = []#Aqui se guardaran todos los nodos perntenecientes al nivel
    arbolporniveles = {}#Este es el diccionario donde se irá formando el arbol por niveles
    contadorniveles = 1#Contador para saber en que nivel estamos

    while len(nodospadres) > 0:#Este ciclo se repetira hasta que se llegue al nodo final el cual ya no tiene conexiónes

        for nodopadre in nodospadres:#Recorre cada nodo padre en los nodos padres

            grafo = leergrafo(grafoescrito)#Formatea el grafo cada vez que se recorren los nodos padres
                                            #Esto por que si no se hace se va editando el grafo original

            for nodo in grafo:#Recorre cada nodo en el grafo

                nodotemporal = nodo#Se le asigna el valor del nodo a un nodo temporal para que no se edite el nodo original

                if nodotemporal[0] == nodopadre[0]:#Si el padre del nodo temporal es igual al padre de alguno de los nodos del nivel anterior se integra ese nodo.

                    pesonodo = int(nodotemporal[2])#Se consigue el peso del nodo

                    pesopadre = int(nodopadre[1])#Se consigue el peso de su nodo padre

                    pesoacumulado = pesonodo + pesopadre#Se acumulan los pesos

                    nodotemporal[2] = str(pesoacumulado)#Se hace string el peso para que conviva con los demás datos que son string

                    nivel.append(nodotemporal)#Se añade ese nodo con su nuevo peso acumulado a los nodos del nivel
        
        nodospadres = []#Se establece como vacia para añadir los nodos padres de los nodos que se encontraron en el nivel actual

        for nodopadreaañadir in nivel:#Se recorren los nodos del nivel para añadir sus nodos padres y sus pesos a la lista de los nodos padres que se usara en el siguiente recorrido del ciclo
            nodospadres.append([nodopadreaañadir[1],nodopadreaañadir[2]])

        arbolporniveles[f'nivel{contadorniveles}'] = nivel#Los nodos encontrados se suman como un nivel en total, dando el siguiente formato
                                                        #{'nivel1': [['1', '2', '13'], ['1', '3', '15'], ['1', '4', '12']]}
        contadorniveles+=1#Se aumenta para saber que se pasara a otro nivel
        nivel = []#Se vacía la lista para que se llene con los nodos del nivel en la siguiente corrida
    
    #Estas lineas son por que al terminar el llenado del arbol al final se llena un nivel con los hijos del nodo final, pero como no tiene hijos termina siendo un nivel vacio, entonces se 
    #reduce el contador de nivel, ya que si son 7 niveles el contador terminaria en 8 por la ultima iteración, y después se borra ese ultimo nivel añadido al arbol en el diccionario
    contadorniveles-=1
    del arbolporniveles[f'nivel{contadorniveles}']
    
    return arbolporniveles#Se retorna el diccionario que contiene el arbol por niveles

#Esta función tiene como objetivo implementar el algoritmo de búsqueda haz sobre el árbol antes generado.
def busquedahaz(k, inicio, fin, arbol):#Recibe como parametro el valor de k, el nodo inicio, el nodo final y el arbol generado por niveles

    valoresdelarbol = arbol.values()#Guarda los valores del arbol en una lista, para no tener que 
    padresdenodosseleccionados = [inicio]#En esta lista se iran guardando los padres de los nodos seleccionados, inicia con el nodo inicio por que los nodos que se seleccionen en el primer nivel deben ser hijos de este
    nodosseleccionados = []#En esta lista se guardan los nodos seleccionados de todos los niveles
    nodosseleccionadosdelnivel = []#En esta lista se guardan los nodos seleccionados en cada nivel, por cada corrida del ciclo se reinician por los del nivel actual
    caminoalreves = []#Se guarda el camino hacia el nodo final pero al reves
    contadornivel = 1#Sirve para llevar la cuenta de en que nivel estamos
    nodofinalencontrado = False#Sirve para reconocer cuando el nodo final se haya encontrado, mientras no haya sido encontrado su valor seguirá en False
            
    for nivel in valoresdelarbol:#Recorre cada nivel en el arbol

        contador = 0#Este contador sirve para saber cuantos nodos han sido seleccionados en el nivel, por eso se restablece a 0 cada que comienza el ciclo

        if len(nivel) <= k:#Solo entra en este if si el numero de nodos que tiene el nivel es menor o igual a k, por ejemplo si k vale 3 y el nivel tiene 1, 2, o 3 nodos entrará

            for nodopadre in padresdenodosseleccionados:#Recorre cada nodo padre en la lista de los padres de nodos seleccionados

                if nodofinalencontrado == True:#Si el nodo final ha sido encontrado se sale del ciclo
                    break

                for nodo in nivel:#Recorre cada nodo en el nivel actual

                    #Este if en especifico es para revisar si el nodo meta se encuentra en el nivel.
                    if nodo[1] == fin and nodo[0] == nodopadre:#Si el nodo hijo es igual al nodo meta y el nodo padre pertenece a los padres de nodos seleccionados se establece como nodo meta y se sale del ciclo.
                        meta = nodo
                        nodofinalencontrado = True
                        break
                
                for nodo in nivel:#Recorre cada nodo en el nivel actual
                    if nodo[0] == nodopadre:#Si los padres de los nodos en el nivel son iguales a alguno de los padres de los nodos seleccionados se añadira el nodo a los nodos seleccionados en el nivel.
                        nodosseleccionadosdelnivel.append(nodo)
        else:#Si no se entra al if anterior se hace este proceso, esto quiere decir que el numero de nodos en el nivel es mayor a k, entonces se tienen que seleccionar los menos pesados.
            salio = False#establece el valor por default de la variable en False que servira para saber si el nodo que salio como el menos pesado se saco.
            while contador < k:#El ciclo se realizara hasta que el numero de nodos seleccionados sea igual a k
                nodoseleccionado = min(enumerate(map(itemgetter(-1), nivel)),key=itemgetter(1))#En esta linea se saca el indice y peso del nodo con menor peso de todos los nodos en el nivel
                indice = nodoseleccionado[0]#Se guarda el indice del nodo encontrado en la linea anterior

                contadorpadre = 0#Este contador ayuda para que en el siguiente ciclo los nodos se vayan checando con cada padre en los padres de nodos seleccionados

                while contadorpadre < len(padresdenodosseleccionados):#Se realizara hasta que se chequen todos los nodos padres

                    if contadorpadre == 0:#Este if hace que solamente se haga una vez el proceso de buscar si el nodo seleccionado como menor en el nivel es el nodo meta.

                        for nodopadre in padresdenodosseleccionados:#De aqui en adelante es el mismo proceso que se realiza de las lineas 105 a la 116 para encontrar el nodo meta

                            if nodofinalencontrado == True:
                                break

                            for nodo in nivel:
                                if nodo[1] == fin and nodo[0] == nodopadre:
                                    meta = nodo
                                    nodofinalencontrado = True
                                    break#----------------------------------------------------------------------------------------------------------------------------------------
                        
                    if nivel[indice][0] == padresdenodosseleccionados[contadorpadre]:#Este if checa que el nodo seleccionado como el menor en el nivel es hijo de alguno de los padres seleccionados
                        #si esto resulta cierto el nodo se sacará del nivel, se añadira a los nodos seleccionados del nivel y se marcara que el nodo si salio
                        nodosseleccionadosdelnivel.append(nivel.pop(indice))
                        contador +=1
                        salio = True
                        break
                        
                    contadorpadre+=1
                
                if salio == False:#si el nodo no fue seleccionado entonces se elimina del nivel, esto para que al buscar de nuevo el menor nodo en el nivel no nos de el mismo
                    nivel.pop(indice)
                salio = False

        padresdenodosseleccionados = []#Al terminar el proceso de seleccionar nodos se vacia la lista de los padres de nodos seleccionados

        for nodopadreaañadir in nodosseleccionadosdelnivel:#Aqui los padres de los nodos que fueron seleccionados en este nivel se añaden a los padres de nodos seleccionados,
            #para usarlos en el siguiente recorrido del ciclo.
            padresdenodosseleccionados.append(nodopadreaañadir[1])

        indiceyvalor = min(enumerate(map(itemgetter(-1), nodosseleccionadosdelnivel)),key=itemgetter(1))#Esta linea te da el indice y peso del nodo de menor peso en los nodos seleccionados.
        nodomenordelosseleccionados = nodosseleccionadosdelnivel[indiceyvalor[0]]

        #Se imprimen los nodos seleccionados en el nivel y el menor de esos nodos.
        print(f'Los nodos seleccionados del nivel {contadornivel} son: {nodosseleccionadosdelnivel} y el menor de esos nodos es: {nodomenordelosseleccionados}')
        contadornivel+=1#Se aumenta el contador del nivel.
        
        nodosseleccionados.append(nodosseleccionadosdelnivel)#Se añaden los nodos seleccionados del nivel a la lista que guarda todos los nodos seleccionados de cada nivel.
        
        nodosseleccionadosdelnivel = []#Se vacia la lista de los nodos seleccionados del nivel para llenarla de nuevo en el siguiente recorrido del ciclo.

        if nodofinalencontrado == True:#Si el nodo meta fue encontrado se imprime que el nodo meta fue encontrado y se sale del ciclo.
            print('¡SE ENCONTRO LA META!')
            break

    print(f'El nodo meta fue: {meta}')#Se imprime el nodo meta
    costo = meta[2]#Se guarda el costo que fue llegar hasta el nodo meta.
    meta = meta[1]#Se guarda el valor de la meta, por ejemplo en el grafo que se ha usado en ejemplos es el 10
    caminoalreves.append(meta)#Se añade al camino al reves

    for nivel in reversed(nodosseleccionados):#Se recorre el nivel al reves, de el ultimo al primero
            for nodo in nivel:
                if meta == nodo[1]:#Si el nodo meta es igual al nodo hijo de algun nodo se guardara como meta el padre de ese nodo
                    #por ejemplo si el nodo meta es 10 y uno de los nodos es igual a : [5, 10, 25] se guardara el cinco como el siguiente padre del nodo, y asi simultaneamente hasta llegar al nodo raiz
                    #para ir formando el camino al revés.
                    meta = nodo[0]
                    caminoalreves.append(meta)
                    break
    
    camino = []#Se declara una lista donde se guardara el camino en orden normal

    for nodo in reversed(caminoalreves):#Se recorre la lista al reves para asi ir guardando cada nodo de forma normal en la lista "camino"
        camino.append(nodo)
    
    print(f'El camino es: {camino}, con un costo de: {costo}')#Se imprime el camino y lo que costo llegar al nodo meta o nodo final.
        

#--------------------------------------------------------------------

grafoescrito = input("Introduce tu grafo: ")#Se pide el grafo por consola
inicio = input("¿Cual es tu nodo inicial?: ")#Se pide el nodo inicial por consola
fin = input("¿cual es el nodo final?: ")#Se pide el nodo final o meta por consola

grafoformateado = leergrafo(grafoescrito)#Se hace uso de la función "leergrafo" para formatear el grafo y poder usarlo.

k = valor_de_k(grafoformateado)#Se hace uso de la función "valor_de_k" para obtener el valor de k.

arbolporniveles = formararbolporniveles(grafoescrito,inicio)#Se hace uso de la función "formararbolporniveles" para obtener el arbol por niveles.

print(f'Valor de k: {k}')#De aqui a la linea 218 se imprime el valor de k y el arbol por niveles
print('Arbol por niveles con sus pesos acumulados: ')

for key in arbolporniveles:
  print(key, ":", arbolporniveles[key])

print('-------------------------------------------------------------------')
print('Comienzo de la busqueda del nodo meta por el algoritmo busqueda haz')#Separador para indicar que lo impreso después de estas lineas serán el proceso del algoritmo busqueda haz.
print('-------------------------------------------------------------------')

busquedahaz(k, inicio, fin, arbolporniveles)#Se hace el proceso de busqueda haz.