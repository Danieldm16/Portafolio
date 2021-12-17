#Se importa todo lo que contiene el proyecto lexico
from ProyectoLexico import *

#Se lee el codigo o programa que se analizará
codigofuente = abriryguardar()

#Se consigue la tabla de tokens respectiva al programa analizado
tablatoken = analizarcodigofuente(codigofuente, matrizdeestados)

#Esta es la tabla sintactica perteneciente a la gramatica del proyecto.
tablasintactica = [[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 1, 404, 404, 404, 404, 404, 404, 404],
[404, 2, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 3, 3, 3, 3, 404, 3, 3, 3, 404, 404, 404, 404, 3, 3, 404, 404],
[404, 404, 5, 4, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 6, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 7, 8, 9, 404, 404, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 10, 404, 404],
[404, 404, 404, 404, 12, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 11, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 14, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 13, 13, 13, 13, 404, 14, 13, 13, 404, 404, 404, 404, 13, 13, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 15, 19, 22, 16, 404, 404, 24, 25, 404, 404, 404, 404, 23, 26, 404, 404],
[404, 404, 404, 404, 404, 404, 17, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 18, 404, 404],
[404, 404, 404, 20, 404, 404, 404, 404, 404, 404, 404, 404, 20, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 21, 404, 404, 404, 404, 404, 404, 404, 404, 21, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 27, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 28, 29, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 30, 404, 404],
[404, 404, 32, 404, 404, 404, 404, 404, 404, 404, 404, 31, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 33, 404, 404, 404, 404, 404, 404, 404, 404, 34, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 35, 36, 37, 38, 39, 40, 41, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 42, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 42, 42, 404],
[404, 404, 404, 404, 45, 45, 404, 404, 45, 404, 404, 404, 404, 45, 45, 45, 45, 45, 45, 45, 43, 44, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 46, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 46, 46, 404],
[404, 404, 404, 404, 49, 49, 404, 404, 49, 404, 404, 404, 404, 49, 49, 49, 49, 49, 49, 49, 49, 49, 47, 48, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404],
[404, 404, 404, 50, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 404, 51, 52, 404]]

#Esta función nos da el simbolo terminal que equivale a cada columna de la tabla sintactica,
#el simbolo terminal al que pertenece se establece dentro de cada if,
#para funcionar necesita el numero de la columna de un simbolo terminal.
#La funcion se usará al momento de identificar algún error.
def simboloterminalequivalenteacolumna(numcolumna):

    if numcolumna == 0:#:
        return ":"
    if numcolumna == 1:#@[
        return "@["
    if numcolumna == 2:#@]
        return "@]"
    if numcolumna == 3:#@(
        return "@("
    if numcolumna == 4:#@)
        return "@)"
    if numcolumna == 5:#.
        return "."
    if numcolumna == 6:#@{
        return "@{"
    if numcolumna == 7:#@}
        return "@}"
    if numcolumna == 8:#;
        return ";"
    if numcolumna == 9:#<+
        return "<+"
    if numcolumna == 10:#<-
        return "<-"
    if numcolumna == 11:#$case
        return "$case"
    if numcolumna == 12:#!
        return "!"
    if numcolumna == 13:#%=%
        return "%=%"
    if numcolumna == 14:#@>
        return "@>"
    if numcolumna == 15:#@<
        return "@<"
    if numcolumna == 16:#@<=
        return "@<="
    if numcolumna == 17:#@>=
        return "@>="
    if numcolumna == 18:#@|
        return "@|"
    if numcolumna == 19:#@&
        return "@&"
    if numcolumna == 20:#+
        return "+"
    if numcolumna == 21:#-
        return "-"
    if numcolumna == 22:#$*
        return "$*"
    if numcolumna == 23:#@/
        return "@/"
    if numcolumna == 24:#$suppose
        return "$suppose"
    if numcolumna == 25:#$while
        return "$while"
    if numcolumna == 26:#$Repeat
        return "$Repeat"
    if numcolumna == 27:#$for
        return "$for"
    if numcolumna == 28:#$enter
        return "$enter"
    if numcolumna == 29:#$Finishing
        return "$Finishing"
    if numcolumna == 30:#$Out
        return "$Out"
    if numcolumna == 31:#$Get
        return "$Get"
    if numcolumna == 32:#$main
        return "$main"
    if numcolumna == 33:#$integer
        return "$integer"
    if numcolumna == 34:#$real
        return "$real"
    if numcolumna == 35:#$string
        return "$string"
    if numcolumna == 36:#cases
        return "$cases"
    if numcolumna == 37:#identificador
        return "identificador/variable"
    if numcolumna == 38:#numero
        return "número"
    if numcolumna == 39:# $ END OF FILE
        return "EOF($)"


#Esta función nos da la columna que equivale a cada simbolo terminal
#el simbolo terminal esta escrito como comentario a la derecha de los if
#para funcionar requiere ingresar un token de un simbolo terminal.
#Si el simbolo terminal no se reconoce regresa un token 404 que representa error.
def columnaequivalente(simboloterminal):

	if simboloterminal == 133:#:
		return 0
	if simboloterminal == 115:#@[
		return 1
	if simboloterminal == 116:#@]
		return 2
	if simboloterminal == 111:#@(
		return 3
	if simboloterminal == 112:#@)
		return 4
	if simboloterminal == 127:#.
		return 5
	if simboloterminal == 109:#@{
		return 6
	if simboloterminal == 110:#@}
		return 7
	if simboloterminal == 126:#;
		return 8
	if simboloterminal == 123:#<+
		return 9
	if simboloterminal == 121:#<-
		return 10
	if simboloterminal == 104.16:#$case
		return 11
	if simboloterminal == 134:#!
		return 12
	if simboloterminal == 135:#%=%
		return 13
	if simboloterminal == 119:#@>
		return 14
	if simboloterminal == 117:#@<
		return 15
	if simboloterminal == 118:#@<=
		return 16
	if simboloterminal == 120:#@>=
		return 17
	if simboloterminal == 113:#@|
		return 18
	if simboloterminal == 114:#@&
		return 19
	if simboloterminal == 138:#+
		return 20
	if simboloterminal == 139:#-
		return 21
	if simboloterminal == 106:#$*
		return 22
	if simboloterminal == 108:#@/
		return 23
	if simboloterminal == 104.2:#suppose
		return 24
	if simboloterminal == 104.3:#while
		return 25
	if simboloterminal == 104.4:#Repeat
		return 26
	if simboloterminal == 104.5:#$for
		return 27
	if simboloterminal == 104.6:#enter
		return 28
	if simboloterminal == 104.7:#Finishing
		return 29
	if simboloterminal == 104.8:#$Out
		return 30
	if simboloterminal == 104.9:#$Get
		return 31
	if simboloterminal == 104.17:#$main
		return 32
	if simboloterminal == 104.12:#$integer
		return 33
	if simboloterminal == 104.13:#$real
		return 34
	if simboloterminal == 104.14:#$string
		return 35
	if simboloterminal == 104.15:#cases
		return 36
	if simboloterminal == 104.1:#identificador
		return 37
	if simboloterminal == 100:#numero
		return 38
	if simboloterminal == 105:# $ END OF FILE
		return 39

	return 404

#Esta función nos da la columna que equivale a cada simbolo NO terminal,
#el simbolo no terminal al que pertenece se establece dentro de cada if,
#para funcionar necesita un simbolo no terminal.
#Si el simbolo NO terminal no se reconoce regresa un token 404 que representa error.
def filaequivalente(simbolonoterminal):

	if simbolonoterminal == "P":
		return 0
	if simbolonoterminal == "VARIABLES":
		return 1
	if simbolonoterminal == "DECLARACION":
		return 2
	if simbolonoterminal == "VARS":
		return 3
	if simbolonoterminal == "TIPO":
		return 4
	if simbolonoterminal == "LISTA":
		return 5
	if simbolonoterminal == "LISTAPRIMA":
		return 6
	if simbolonoterminal == "INSTRUCCIONES":
		return 7
	if simbolonoterminal == "COMANDO":
		return 8
	if simbolonoterminal == "CUERPOINSTRUCCION":
		return 9
	if simbolonoterminal == "DETALLE-FOR":
		return 10
	if simbolonoterminal == "CUERPOWHILE":
		return 11
	if simbolonoterminal == "CUERPOIF":
		return 12
	if simbolonoterminal == "INCREDECRE":
		return 13
	if simbolonoterminal == "SIGNO":
		return 14
	if simbolonoterminal == "ASIGNACION":
		return 15
	if simbolonoterminal == "LISTACASES":
		return 16
	if simbolonoterminal == "CONDICION":
		return 17
	if simbolonoterminal == "OPERADOR":
		return 18
	if simbolonoterminal == "EXPRESION":
		return 19
	if simbolonoterminal == "EXPPRIMA":
		return 20
	if simbolonoterminal == "TERMINO":
		return 21
	if simbolonoterminal == "TERMPRIMO":
		return 22
	if simbolonoterminal == "FACTOR":
		return 23
	
	return 404

#Esta función obtiene la siguiente producción que se va a ingresar,
#las producciones están reescritas en orden de derecha a izquierda,
#para que al añadirlas al stack sintactico se añadan de forma correcta,
#como lo establece el proceso de analisis sintactico.
#Para funcionar necesita el numero de producción y el stack sintactico.
#si el numero de producción representa un token de error en vez de añadir
#una producción añade un token de error.
#Los simbolos terminales se reemplazan por su token equivalente.
def obtenerproduccion(numproduccion, stacksintactico):

	if numproduccion == 1:
		stacksintactico.extend([104.7, "INSTRUCCIONES", "VARIABLES", 104.6, 133, 104.17])
		return stacksintactico
	if numproduccion == 2:
		stacksintactico.extend(["VARIABLES", 116, "DECLARACION", 115])
		return stacksintactico
	if numproduccion == 3:
		stacksintactico.extend([])#no se añade nada pues la producción es nula.
		return stacksintactico
	if numproduccion == 4:
		stacksintactico.extend(["DECLARACION", "VARS"])
		return stacksintactico
	if numproduccion == 5:
		stacksintactico.extend([])#no se añade nada pues la producción es nula.
		return stacksintactico
	if numproduccion == 6:
		stacksintactico.extend([112, "LISTA", "TIPO", 111])
		return stacksintactico
	if numproduccion == 7:
		stacksintactico.extend([104.12])
		return stacksintactico
	if numproduccion == 8:
		stacksintactico.extend([104.13])
		return stacksintactico
	if numproduccion == 9:
		stacksintactico.extend([104.14])
		return stacksintactico
	if numproduccion == 10:
		stacksintactico.extend(["LISTAPRIMA", 104.1])
		return stacksintactico
	if numproduccion == 11:
		stacksintactico.extend(["LISTA"])
		return stacksintactico
	if numproduccion == 12:
		stacksintactico.extend([])#no se añade nada pues la producción es nula.
		return stacksintactico
	if numproduccion == 13:
		stacksintactico.extend(["INSTRUCCIONES", 127, "COMANDO"])
		return stacksintactico
	if numproduccion == 14:
		stacksintactico.extend([])#no se añade nada pues la producción es nula.
		return stacksintactico
	if numproduccion == 15:
		stacksintactico.extend(["CUERPOIF", 104.2])
		return stacksintactico
	if numproduccion == 16:
		stacksintactico.extend(["CUERPOINSTRUCCION", 112, "DETALLE-FOR", 111, 104.5])
		return stacksintactico
	if numproduccion == 17:
		stacksintactico.extend([110, "INSTRUCCIONES", 109])
		return stacksintactico
	if numproduccion == 18:
		stacksintactico.extend(["INCREDECRE", 126, "EXPRESION", "OPERADOR", 104.1, 126, "ASIGNACION"])
		return stacksintactico
	if numproduccion == 19:
		stacksintactico.extend(["CUERPOWHILE", 104.3])
		return stacksintactico
	if numproduccion == 20:
		stacksintactico.extend(["CUERPOINSTRUCCION", "CONDICION"])
		return stacksintactico
	if numproduccion == 21:
		stacksintactico.extend(["CUERPOINSTRUCCION", "CONDICION"])
		return stacksintactico
	if numproduccion == 22:
		stacksintactico.extend(["CONDICION", "CUERPOINSTRUCCION", 104.4])
		return stacksintactico
	if numproduccion == 23:
		stacksintactico.extend([116, "LISTACASES", 115, 104.1, 104.15])
		return stacksintactico
	if numproduccion == 24:
		stacksintactico.extend([116, 104.1, 115, 104.8])
		return stacksintactico
	if numproduccion == 25:
		stacksintactico.extend([116, 104.1, 115, 104.9])
		return stacksintactico
	if numproduccion == 26:
		stacksintactico.extend(["ASIGNACION"])
		return stacksintactico
	if numproduccion == 27:
		stacksintactico.extend(["SIGNO", 104.1])
		return stacksintactico
	if numproduccion == 28:
		stacksintactico.extend([123])
		return stacksintactico
	if numproduccion == 29:
		stacksintactico.extend([121])
		return stacksintactico
	if numproduccion == 30:
		stacksintactico.extend(["EXPRESION", 122, 104.1])
		return stacksintactico
	if numproduccion == 31:
		stacksintactico.extend(["LISTACASES", "CUERPOINSTRUCCION", 100, 104.16])
		return stacksintactico
	if numproduccion == 32:
		stacksintactico.extend([])#no se añade nada pues la produccion es nula.
		return stacksintactico
	if numproduccion == 33:
		stacksintactico.extend([112, "EXPRESION", "OPERADOR", "EXPRESION", 111])
		return stacksintactico
	if numproduccion == 34:
		stacksintactico.extend([112, "EXPRESION", "OPERADOR", "EXPRESION", 111, 134])
		return stacksintactico
	if numproduccion == 35:
		stacksintactico.extend([135])
		return stacksintactico
	if numproduccion == 36:
		stacksintactico.extend([119])
		return stacksintactico
	if numproduccion == 37:
		stacksintactico.extend([117])
		return stacksintactico
	if numproduccion == 38:
		stacksintactico.extend([118])
		return stacksintactico
	if numproduccion == 39:
		stacksintactico.extend([120])
		return stacksintactico
	if numproduccion == 40:
		stacksintactico.extend([113])
		return stacksintactico
	if numproduccion == 41:
		stacksintactico.extend([114])
		return stacksintactico
	if numproduccion == 42:
		stacksintactico.extend(["EXPPRIMA", "TERMINO"])
		return stacksintactico
	if numproduccion == 43:
		stacksintactico.extend(["EXPPRIMA", "TERMINO", 138])
		return stacksintactico
	if numproduccion == 44:
		stacksintactico.extend(["EXPPRIMA", "TERMINO", 139])
		return stacksintactico
	if numproduccion == 45:
		stacksintactico.extend([])#no se añade nada pues la producción es nula
		return stacksintactico
	if numproduccion == 46:
		stacksintactico.extend(["TERMPRIMO", "FACTOR"])
		return stacksintactico
	if numproduccion == 47:
		stacksintactico.extend(["TERMPRIMO", "FACTOR", 106])
		return stacksintactico
	if numproduccion == 48:
		stacksintactico.extend(["TERMPRIMO", "FACTOR", 108])
		return stacksintactico
	if numproduccion == 49:
		stacksintactico.extend([])#no se añade nada pues la producción es nula
		return stacksintactico
	if numproduccion == 50:
		stacksintactico.extend([112, "EXPRESION", 111])
		return stacksintactico
	if numproduccion == 51:
		stacksintactico.extend([104.1])
		return stacksintactico
	if numproduccion == 52:
		stacksintactico.extend([100])
		return stacksintactico
	
	stacksintactico.extend([404])
	return stacksintactico

#Esta función nos regresa los simbolos terminales que son permitidos
#en la gramatica cuando hay un error sintactico,
#la función necesita la fila en la que fallo todo y la tabla sintactica.
#La función primero recorrera la fila añadiendo a una lista la columna
# de los elementos que no sean 404.
#Después recorrera esas columnas y nos dirá el simbolo terminal al que
#le pertenece la columna, estos se añaden a otra lista,
#y al final la lista que tiene los simbolos terminales se regresa.
def tokensqueseesperan(fila, tablasintactica):
	columnas = []
	tokensesperados = []
	contador = 0

	for token in tablasintactica[fila]:
		if token != 404:
			columnas.append(contador)
		contador+=1
	
	for col in columnas:
		simboloterminal = simboloterminalequivalenteacolumna(col)
		tokensesperados.append(simboloterminal)

	return tokensesperados

#Esta función cumple con el proceso de realizar el analisis sintactico
#para funcionar requiere la tabla de tokens referente al codigo que se
#analiza y la tabla de tokens.
#si obtiene algun token de error se detiene y lo informa.
def analisissintactico(tablasintactica, tablatoken):
	#Se declara el stack sintactico y se inicializa con el token EOF y
	#con el simbolo inicial no terminal de la gramatica.
	stacksintactico = [105, "P"]

	#El analisis continua hasta que la tabla de tokens referente al codigo
	#que se analiza se vacia.
	while len(tablatoken) > 0:

		#Se comparan el ultimo elemento del stack sintactico con
		#el primero de la tabla de tokens.
		if stacksintactico[-1] == tablatoken[0]:
			#Si son iguales quiere decir que se reconocio un simbolo terminal
			#y lo informa, después elimina los dos elementos analizados de
			#sus respectivos stacks y vuelve a imrpimir para ver como 
			#quedo la tabla de tokens y el stack sintactico.
			print("-----------------------------------------------------------")
			print("Los elementos coinciden, se reconoce un simbolo terminal.")
			print(f"Token de simbolo terminal reconocido: {tablatoken[0]}")
			print(f"Estado de stack sintactico: {stacksintactico}")
			print(f"Estado de tabla de tokens: {tablatoken}")
			#se elimina el ultimo elemento en el stack sintactico
			stacksintactico.pop()
			#se elimina el primer elemento en la tabla de tokens
			tablatoken.pop(0)
			print(f"Estado de stack sintactico después de pop: {stacksintactico}")
			print(f"Estado de tabla de tokens después de pop: {tablatoken}")
			print("-----------------------------------------------------------")
		else:
			#Si los elementos comparados no son iguales se realiza un proceso distinto.
			#primero se obtiene la columna y filas equivalentes al primer digito de
			#la tabla de tokens y al ultimo elemento de el stack sintactico.
			columna = columnaequivalente(tablatoken[0])
			fila = filaequivalente(stacksintactico[-1])

			#Se entra a este if cuando no se encuentra el simbolo terminal que debe seguir
			#el if primero checa la columna donde se fallo, después nos da el simbolo
			#terminal al que pertenece esa columna y se imprime que se espera ese simbolo terminal.
			if fila == 404 or columna == 404:
				columnadesimboloterminal = columnaequivalente(stacksintactico[-1])
				tokenesperado = simboloterminalequivalenteacolumna(columnadesimboloterminal)
				print(f"SE ENCONTRO UN ERROR, SE ESPERA: ' {tokenesperado} '")
				print(f"Nota: si alguno de los tokens de simbolos terminales es de 200 a 203 el error es de lexico.")
				break

			#Con el numero de fila y columna equivalentes obtenido se
			#consigue el numero referente a la siguiente producción que
			#se ingresará al stack sintactico.
			numproduccion = tablasintactica[fila][columna]

			#Se informa que no se reconocio ningún simbolo terminal,
			#se imprime el estado del stack sintactico y el numero de
			#la producción que va a incluirse
			print("-----------------------------------------------------------")
			print("No se reconocio ningún simbolo terminal")
			print(f"Estado de stack sintactico antes de añadir producción: {stacksintactico}")
			print(f"Producción que va a incluirse: {numproduccion}")
			#se saca el ultimo elemento del stack sintactico
			stacksintactico.pop()
			#se añade la producción.
			stacksintactico = obtenerproduccion(numproduccion, stacksintactico)
			#se imprime el estado del stack sintactico después de añadir la
			# producción y la tabla de token.
			print(f"Estado de stack sintactico después de añadir producción: {stacksintactico}")
			print(f"Tabla de tokens: {tablatoken}")
			print("-----------------------------------------------------------")

			#Si hay un error sintactico se entra a este if, y se imprimen los
			#simbolos terminales que se pueden usar a continuación.
			#el if hace uso de la función tokensqueseesperan.
			if stacksintactico[-1] == 404:
				tokensesperados = tokensqueseesperan(fila, tablasintactica)
				print(f"SE ENCONTRO UN ERROR SINTACTICO, SE ESPERABA ALGUNO DE ESTOS TOKENS TERMINALES: {tokensesperados}")
				print(f"Nota: si alguno de los tokens de simbolos terminales es de 200 a 203 el error es de lexico.")
				break
	
	#Si la tabla de token fue vaciada se informa que no hubo errores sintacticos.
	if len(tablatoken) == 0:
		print("EL PROGRAMA SE ANALIZO SIN PROBLEMAS, NO SE ENCONTRARON ERRORES.")

#Llama al metodo "analisissintactico" con la tablasintactica y la tablatoken como parametros.
analisissintactico(tablasintactica, tablatoken)