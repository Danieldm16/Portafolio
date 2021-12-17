import re#libreria para utilizar expresiones regulares

matrizdeestados = [[203, 2, 2, 4, 4, 6, 6, 8, 8, 105, 10, 107, 117, 119, 200, 200, 16, 17, 200, 200, 200, 21, 22, 200],
        [140, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 14, 200, 16, 17, 200, 200, 200, 21, 22, 200],
        [141, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
        [203, 200, 7, 201, 5, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
        [127, 200, 3, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [1, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 10, 10, 107, 117, 119, 200, 200, 16, 17, 200, 200, 200, 21, 22, 200],
	    [9, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 106, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 22, 136, 23, 200],
	    [14, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 12, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [138, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 123, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [139, 200, 100, 201, 101, 202, 103, 202, 102, 105, 10, 107, 117, 119, 121, 122, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 10, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [11, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [20, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 108, 117, 119, 200, 200, 125, 132, 200, 200, 21, 136, 200, 137],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 109, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 110, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 111, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 112, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 113, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 114, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 115, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 116, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [133, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 15, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 13, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 118, 120, 200, 200, 125, 132, 19, 200, 200, 136, 200, 200],
	    [16, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 124, 132, 200, 200, 200, 136, 200, 200],
	    [126, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [129, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [130, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [17, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 131, 200, 200, 200, 136, 200, 200],
	    [128, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 22, 200],
	    [134, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200],
	    [18, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 135, 200, 136, 200, 200],
        [203, 200, 100, 201, 101, 202, 103, 202, 102, 105, 104, 107, 117, 119, 200, 200, 125, 132, 200, 200, 200, 136, 200, 200]]
#Está es la matriz de estados, cada lista es una columna, por ejemplo la primera columna son los digitos

def abriryguardar():#Está función se utiliza para abrir el archivo fuente, leerlo, guardar su información y cerrarlo.
    f = open('codigofuente.txt', 'r')
    codigofuente = f.read()
    f.close()
    return codigofuente

def obtenercolumna(caracter, estadoanterior):#Recibe un caracter y el estado anterior
    #Está función nos ayuda a saber a que columna pertenece cierto caracter
    #dependiendo del caracter te llevara a una columna distinta según su if
    #si el caracter no coincide con ninguno de los indicados te regresa a la
    #columna de los caracteres no identificados
    if re.match("[0-9]", caracter):
        return 0
    if caracter == " ":
        return 1
    if caracter == "	":
        return 2
    if caracter == ".":
        return 4
    if caracter == "~":
        return 5
    if re.match("[a-zA-Z]", caracter):#la e es especial, ya que forma parte de las letras y puede indicar notacion cientifica
        #Entonces si el estado anterior es uno donde la e en especial tiene alguna consecuencia se lleva hacia su columna
        #si no se pasa como una letra más.
        if caracter == "e" and estadoanterior == 2:
            return 3
        elif caracter == "e" and estadoanterior == 4:
            return 3
        return 6
    if caracter == "$":
        return 7
    if caracter == "*":
        return 8
    if caracter == "<":
        return 9
    if caracter == "+":
        return 10
    if caracter == "-":
        return 11
    if caracter == "_":
        return 12
    if caracter == "@":
        return 13
    if caracter == "/":
        return 14
    if caracter == "{":
        return 15
    if caracter == "}":
        return 16
    if caracter == "(":
        return 17
    if caracter == ")":
        return 18
    if caracter == "|":
        return 19
    if caracter == "&":
        return 20
    if caracter == "[":
        return 21
    if caracter == "]":
        return 22
    if caracter == ":":
        return 23
    if caracter == ">":
        return 24
    if caracter == "=":
        return 25
    if caracter == '"':
        return 26
    if caracter == ";":
        return 27
    if caracter == "\\":
        return 28
    if caracter == ",":
        return 29
    if caracter == "'":
        return 30
    if caracter == "\n":
        return 31
    if caracter == "!":
        return 32
    if caracter == "%":
        return 33
    
    return 34

def analizarcodigofuente(inftxt, matrizdeestados):#Función que analiza el codigo fuente, recibe la información del codigo fuente y la matriz de estados
    
    estado = 0#esta variable nos indicara en que estado estamos
    contador = 0#nos deja saber en que caracter vamos
    estadoanterior = 0#nos deja saber cual fue el estado anterior
    inftxt += "\n"#añade un salto de linea final para acabar de analizar lo que este escrito
    numcaracteres = len(inftxt)#nos da el numero de caracteres en el archivo de texto

    loqueseencuentra = ""#nos ayuda a guardar los caracteres que se van leyendo hasta que se llegue a un estado final

    while contador != numcaracteres:#El for itera sobre todos los caracteres de el codigo fuente

        caracter = inftxt[contador]#Se obtiene el caracter

        columna = obtenercolumna(caracter, estadoanterior)#se obtiene la columna a la que pertenece el caracter

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
                cadenaencontrada = loqueseencuentra.strip()#esta linea quita los espacios y saltos de linea a la izquierda y derecha de lo encontrado.
                print(f"Se encontro el numero natural: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 101:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro el numero decimal: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 102:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro el numero natural con notación cientifica: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 103:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro el numero decimal con notación cientifica: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 104:#si se llega a este estado puede que sea una palabra reservada o una variable normal
                #por eso se checa si coincide con una de las palabras reservadas, en caso de que sea asi pues te indica que se encontro
                #si no se pasa como una variable normal
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra[:-1].strip()
                if cadenaencontrada == "$suppose":
                    print(f"Se encontro una indicación de condición: {cadenaencontrada}")
                elif cadenaencontrada == "$while":
                    print(f"Se encontro una indicación de ciclo while: {cadenaencontrada}")
                elif cadenaencontrada == "$Repeat":
                    print(f"Se encontro una indicación de ciclo Repeat: {cadenaencontrada}")
                elif cadenaencontrada == "$for":
                    print(f"Se encontro una indiciación de ciclo for: {cadenaencontrada}")
                elif cadenaencontrada == "$enter":
                    print(f"Se encontro un inicio de ciclo: {cadenaencontrada}")
                elif cadenaencontrada == "$Finishing":
                    print(f"Se encontro el final de un ciclo: {cadenaencontrada}")
                elif cadenaencontrada == "$Out":
                    print(f"Se encontro una impresión: {cadenaencontrada}")
                elif cadenaencontrada == "$Get":
                    print(f"Se encontro una lectura: {cadenaencontrada}")
                else:
                    print(f"Se encontro la variable: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 105:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro el simbolo $: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 106:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una multiplicacion: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 107:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un arroba: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 108:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una indicación de división: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 109:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una llave abierta: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 110:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una llave cerrada: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 111:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un parentesis abierto: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 112:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un parentesis cerrado: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 113:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un OR: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 114:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un AND: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 115:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un corchete abierto: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 116:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un corchete cerrado: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 117:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un menor que: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 118:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un menor o igual que: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 119:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un mayor que: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 120:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un mayor o igual que: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 121:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un decremento: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 122:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una asignación/igual: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 123:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un incremento: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 124:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro el texto (forma1): {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 125:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontraron dobles comillas: {cadenaencontrada[:-1]}")
                loqueseencuentra = ""
            if estado == 126:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un punto y coma: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 127:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un punto: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 128:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                #print(f"- Se encontro un salto de linea -") Comentado por que se menciono que no es necesario reportarlo.
                loqueseencuentra = ""
            if estado == 129:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una diagonal inversa: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 130:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una coma: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 131:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro el texto (forma2): {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 132:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una comilla simple: {cadenaencontrada[:-1]}")
                loqueseencuentra = ""
            if estado == 133:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un dos puntos: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 134:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una negación o simbolo de exclamación: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 135:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una comparación de iguales: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 136:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un comentario de una linea: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 137:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro un comentario de varias lineas: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 138:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una suma: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 139:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f"Se encontro una resta: {cadenaencontrada}")
                loqueseencuentra = ""
            if estado == 140:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                #print(f"- Se encontro un espacio -") Comentado por que se menciono que no es necesario reportarlo.
                loqueseencuentra = ""
            if estado == 141:
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                #print(f"- Se encontro un tabulador -") Comentado por que se menciono que no es necesario reportarlo.
                loqueseencuentra = ""
            if estado == 200:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f'ERROR: El siguiente caracter o conjunto de caracteres no se reconoce: {cadenaencontrada}')
                loqueseencuentra = ""
            if estado == 201:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f'ERROR: Un numero decimal no puede quedar asi: {cadenaencontrada}, debe continuar con otro digito')
                loqueseencuentra = ""
            if estado == 202:
                contador-=1
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f'ERROR: Un numero natural o decimal con notacion cientifica no puede quedar asi: {cadenaencontrada}, debe seguir con un otro digito')
                loqueseencuentra = ""
            if estado == 203:#Este error se repite ya que cuando viene del estado 0 no necesita regresar al caracter anterior, pero en los otros casos si es necesario.
                estado = 0
                cadenaencontrada = loqueseencuentra.strip()
                print(f'ERROR: El siguiente caracter o conjunto de caracteres no se reconoce: {cadenaencontrada}')
                loqueseencuentra = ""
            
        estadoanterior = estado
        contador+=1


codigofuente = abriryguardar()#Lee el codigo fuente
#print(codigofuente)imprime el codigo fuente para saber que vamos a analizar
analizarcodigofuente(codigofuente, matrizdeestados)#Se analiza el codigo fuente y se indica que se va encontrando