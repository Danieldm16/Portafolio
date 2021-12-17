import re#libreria para utilizar expresiones regulares

matrizdeestados = [[1, 1, 3, 3, 5, 5, 5, 7, 105, 108, 111, 113, 115],
            [7, 102, 200, 100, 202, 101, 201, 7, 105, 108, 111, 113, 115],
            [116, 2, 200, 100, 202, 101, 201, 103, 105, 108, 111, 113, 115],
            [9, 102, 200, 100, 6, 101, 201, 103, 105, 106, 111, 113, 115],
            [10, 102, 200, 100, 6, 101, 201, 103, 105, 107, 109, 113, 115],
            [8, 102, 200, 100, 202, 101, 201, 103, 104, 108, 110, 113, 114],
            [11, 102, 200, 100, 202, 101, 201, 103, 105, 108, 111, 112, 115],
            [12, 102, 200, 100, 202, 101, 201, 103, 105, 108, 111, 113, 115],
            [0, 102, 200, 100, 202, 101, 201, 103, 105, 108, 111, 113, 115],
            [7, 4, 200, 4, 202, 101, 201, 103, 105, 108, 111, 113, 115],
            [203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203]]
#Está es la matriz de estados, cada lista es una columna, por ejemplo la primera columna son los digitos

def abriryguardar():#Está función se utiliza para abrir el archivo fuente, leerlo, guardar su información y cerrarlo.
    f = open ('codigofuente.txt', 'r')
    codigofuente = f.readlines()
    f.close()
    return codigofuente

def obtenercolumna(caracter):#Recibe un caracter
    #Está función nos ayuda a saber a que columna pertenece cierto caracter
    #dependiendo del caracter te llevara a una columna distinta según su if
    #si el caracter no coincide con ninguno de los indicados te regresa a la
    #columna de errores
    if re.match("[0-9]", caracter):
        return 0
    if caracter == "e":
        return 9
    if re.match("[a-zA-Z]", caracter):
        return 1
    if caracter == ".":
        return 2
    if caracter == "+":
        return 3
    if caracter == "-":
        return 4
    if caracter == "=":
        return 5
    if caracter == ">":
        return 6
    if caracter == "<":
        return 7
    if caracter == " " or caracter == "\n":
        return 8
    
    return 10

def analizarcodigofuente(inftxt, matrizdeestados):#Función que analiza el codigo fuente, recibe la información del codigo fuente y la matriz de estados
    
    estado = 0#esta variable nos indicara en que estado estamos
    contador = 0#nos deja saber en que caracter de la linea vamos
    contadorlinea = 1#nos deja saber en que linea vamos
    numlineas = len(inftxt)#nos dice cuantas lineas tiene el codigo fuente

    loqueseencuentra = ""#nos ayuda a guardar los caracteres que se van leyendo hasta que se llegue a un estado final

    for linea in inftxt:#El for itera sobre todas las lineas de el codigo fuente

        #este if se utiliza solo si se esta checando la ultima linea del codigo fuente
        if contadorlinea == numlineas:#lo que hace es añadir un espacio para que nos lleve a un estado final
            linea += " "#y así analizar lo que se ha juntado de caracteres.

        while contador < len(linea):#Este while itera sobre cada caracter en cada linea
            caracter = linea[contador]#se guarda el caracter en el que va

            columna = obtenercolumna(caracter)#se ovtiene la columna a la que pertenece el caracter

            loqueseencuentra += caracter#se va sumando el caracter a una cadena string

            estado = matrizdeestados[columna][estado]#dependiendo la matriz de estados, la columna que se nos dio segun el caracter y el antiguo estado se nos otorga un nuevo estado
                
            if estado >= 100:
                #si el estado en el que estamos pertenece a un estado final entra a uno de los if
                #en cada if se indica que es lo que se encontro, se imprime y se regresa al estado cero y la cadena se vacia
                #si el estado es uno que tenia asterisco en el automata integral se regresa al caracter anterior
                #si el estado es 200 o mayor se indica a que tipo de error pertenece, y también se regresa al estado 0, al caracter anterior y la cadena se vacia.
                if estado == 100:
                    contador-=1
                    estado = 0
                    print(f"se encontro el numero con decimal: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 101:
                    contador-=1
                    estado = 0
                    print(f"se encontro el numero con decimal y notacion cientifica: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 102:
                    contador-=1
                    print(f"se encontro el numero natural: {loqueseencuentra[:-1]}")
                    estado = 0
                    loqueseencuentra = ""
                if estado == 103:
                    contador-=1
                    estado = 0
                    if loqueseencuentra[1] == " " or loqueseencuentra[1] == "\n" or loqueseencuentra[:1] == " " or loqueseencuentra[:1] == "\n":
                        print(f"se encontro la variable: {loqueseencuentra[1:-1]}")
                    else:
                        print(f"se encontro la variable: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 104:
                    estado = 0
                    print(f"se encontro el operador relacional: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 105:
                    contador-=1
                    estado = 0
                    print(f"se encontro un igual: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 106:
                    estado = 0
                    print(f"se encontro un incremento: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 107:
                    estado = 0
                    print(f"se encontro un incremento: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 108:
                    contador-=1
                    estado = 0
                    print(f"se indica una suma: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 109:
                    estado = 0
                    print(f"se encontro un decremento: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 110:
                    estado = 0
                    print(f"se encontro un decremento: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 111:
                    contador-=1
                    estado = 0
                    print(f"se indico una resta: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 112:
                    estado = 0
                    print(f"se indica un corrimiento de bits: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 113:
                    estado = 0
                    print(f"se encontro un mayor que: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 114:
                    estado = 0
                    print(f"se encontro un menor o igual que: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 115:
                    estado = 0
                    print(f"se encontro un menor que: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 116:
                    estado = 0
                    print(f"se encontro un punto: {loqueseencuentra[:-1]}")
                    loqueseencuentra = ""
                if estado == 200:
                    contador-=1
                    estado = 0
                    print(f'ERROR: Lo ingresado no puede quedar como: {loqueseencuentra}, pues después de un punto decimal debe seguir otro digito')
                    loqueseencuentra = ""
                if estado == 201:
                    contador-=1
                    estado = 0
                    print(f'ERROR: Lo ingresado no puede quedar como: {loqueseencuentra}, debe continuar con otro digito')
                    loqueseencuentra = ""
                if estado == 202:
                    contador-=1
                    estado = 0
                    print(f'ERROR: Lo ingresado no puede quedar como: {loqueseencuentra[1:-1]}, debe seguir con un "." o "digito" o "e", si se intenta introducir una variable, esta no puede empezar con un digito.')
                    loqueseencuentra = ""

            contador += 1#se aumenta el contador para seguir al siguiente caracter
        
        estado = 0#se regresa al estado 0 después de acabar cada linea
        contador = 0#se regresa a 0 para analizar todos los caracteres de la linea desde el principio
        contadorlinea+=1#se aumenta para saber que estamos en la siguiente linea


codigofuente = abriryguardar()#Lee el codigo fuente
print(codigofuente)#imprime el codigo fuente para saber que vamos a analizar
analizarcodigofuente(codigofuente, matrizdeestados)#Se analiza el codigo fuente y se indica que se va encontrando