import glob
import re

#Variables globales
parametros = []
entradas = ""
salidas = ""
funcionamiento = ""
tabulaciones = "    "

#Definición de funciones
def abrirArchivo(nombre):
    """
    Entradas: nombre de tipo string
    Salidas: Devuelve la información que hay en le archivo pasado por parametro y el nombre de este
    Funcionamiento: Lee el archivo pasado y devuelve sus datos y su nombre
    """
    archivo = open(nombre, "r")
    datos = archivo.readlines()
    archivo.close()
    return datos, nombre

def resetearVariables():
    """
    Entradas: N/A
    Salidas: Variable globales con su valor inicial
    Funcionamiento: Devuelve todas las variables globales a el valor con el que se inicializaron originalmente
    """
    global parametros, entradas, salidas, funcionamiento, tabulaciones, borrar
    parametros = []
    entradas = ""
    salidas = ""
    funcionamiento = ""
    tabulaciones = "    "
    borrar = []
    return

def adaptarIdentaciones(linea, tabulaciones):
    """
    Entradas: linea de tipo string y  tabulaciones de tipo string
    Salidas: tabulaciones con cuatro espacios más si es necesario
    Funcionamiento: Agrega cuatro espacios a tabulaciones si la línea está identada
    """
    if "    " in linea:
        tabulaciones += "    "
    return tabulaciones

def obtenerParametros(linea, parametros):
    """
    Entradas: linea de tipo string y  parametros de tipo lista de strings
    Salidas: parametros de la función o método
    Funcionamiento: Guarda en parametros todo lo que este entre los parentesis de la función
    """
    if linea.count(")") == 1:
        parametros += linea[linea.index("(")+1:linea.index(")")].split(",")
        if "" in parametros:
            parametros.remove("")
    else:
        parametros += linea[linea.index("(")+1:linea.index(")", len(linea) - 3)].split(",")
    borrar, parametros = quitarValoresPorOmision(parametros)
    parametros = quitarTuplasPorOmision(linea, borrar, parametros)
    parametros = quitarSelf(parametros)
    return parametros

def quitarValoresPorOmision(parametros):
    """
    Entradas: parametros de tipo lista de strings
    Salidas: parametros sin valores por omisión
    Funcionamiento: Quita todo lo que esté después de un = en cada posición de parametros; además de eliminar todo lo que no cumpla con las condiciones de ser un parametro
    """
    borrar = []
    for i in range(len(parametros)):
        if "=" in parametros[i]:
            parametros[i] = parametros[i][:parametros[i].index("=")]
        if not parametros[i][0].isalpha():
            borrar += [parametros[i]]
    return borrar, parametros

def quitarTuplasPorOmision(linea, borrar, parametros):
    """
    Entradas: linea de tipo string,  borrar de tipo lista de strings y  parametros de tipo lista de strings
    Salidas: parametros sin lo que hay en borrar
    Funcionamiento: Quita de parametros todo lo que haya en borrar
    """
    if linea.count(")") != 1:
        for i in range(len(borrar)):
            parametros.remove(borrar[i])
    return parametros

def quitarSelf(parametros):
    """
    Entradas: parametros de tipo lista de strings
    Salidas: parametros sin selfs
    Funcionamiento: Quita todos los selfs que haya en parametros
    """
    if "self" in parametros:
            parametros.remove("self")
    return parametros

def pedirEntradas(parametros, entradas):
    """
    Entradas: parametros de tipo lista de strings y  entradas de tipo string 
    Salidas: Mensaje que va en las entradas
    Funcionamiento: Pide al usuario el tipo de dato de cada parametro y lo concatena para generar el mensaje que posteriormente se pondrá en entradas
    """
    for j in range(len(parametros)):
        tipo = input("Ingrese el tipo de " + parametros[j] + ": ")
        entradas += parametros[j] + " de tipo " + tipo
        if j + 1 ==  len(parametros) - 1:
            entradas += " y "
        elif j ==  len(parametros) - 1:
            pass
        else:
            entradas += ", "
    return entradas

def escribirDocumentacion(tabulaciones, entradas, salidas, funcionamiento, datos, nombre):
    """
    Entradas: tabulaciones de tipo string,  entradas de tipo string,  salidas de tipo string,  funcionamiento de tipo string,  datos de tipo lista de strings y  nombre de tipo string
    Salidas: datos del archivo actualizados
    Funcionamiento: Escribe en el archivo el comentario de la documentación
    """
    datos = datos[:i+1] + [tabulaciones + '"""\n' + tabulaciones + 'Entradas: ' + entradas + '\n' + tabulaciones + 'Salidas: ' + salidas + '\n' + tabulaciones + 'Funcionamiento: ' + funcionamiento + '\n' + tabulaciones + '"""\n'] +datos[i+1:]
    archivo = open(nombre, "w")
    archivo.writelines(datos)
    archivo.close()
    return datos

def estaDocumentado(datos, indice):
    """
    Entradas: datos de tipo lista de strings y  indice de tipo entero
    Salidas: True/False si la función o método del indice se encuentra documentada
    Funcionamiento: Verifica si hay un comentario de bloque en la línea siguiente o anterior al indice y que tenga Entradas: o Funcionamiento: dependiendo de la posición y devuelve True/False
    """
    if '"""' in datos[indice - 1] or '"""' in datos[indice + 1]:
        if "Funcionamiento:" in datos[indice - 2] or "Entradas:" in datos[indice + 2]:
            return True
        else:
            return False
    else:
        return False

def obtenerArchivos(ruta = ""):
    """
    Entradas: ruta  de tipo string
    Salidas: archivos con extension .py en la ruta dada
    Funcionamiento: Busca en la ruta dada todos los archivos .py y devuelve su nombre
    """
    if ruta == "":
        archivos = glob.glob("*.py")
    else:
        archivos = glob.glob(ruta + "\*.py")
        for i in range(len(archivos)):
            while "\\" in archivos[i]:
                archivos[i] = archivos[i][archivos[i].index("\\") + 1:]
    return archivos

def listarArchivos(archivos):
    """
    Entradas: archivos de tipo lista de strings
    Salidas: Imprime y enumera los archivos pasados
    Funcionamiento: Enlista todos los archivos que se le pasaron por parametro y los imprime
    """
    for i in range(len(archivos)):
        if archivos[i].count("\\") == 0:
            print(str(i + 1) + ")", archivos[i])
        else:
            print(str(i + 1) + ")", archivos[i][archivos[i].index("\\", archivos[i].count("\\") - 1) + 1:])
    return

def preguntarArchivos(ruta = ""):
    """
    Entradas: ruta  de tipo string
    Salidas: Nombre y ruta del archivo seleccionado
    Funcionamiento: Pide al usuario una ruta o que seleccione uno de los archivos enlistados y devuelve su ruta completa
    """
    archivos = obtenerArchivos(ruta)
    if archivos == []:
        ruta = input("No se han encontrado archivos. Ingrese ruta en la que buscar: ")
        return preguntarArchivos(ruta)
    listarArchivos(archivos)
    archivo = input("Ingrese el número del archivo o una ruta en la que buscar: ")
    if archivo.isnumeric() and int(archivo) <= len(archivos):
        return ruta + "\\" + archivos[int(archivo) - 1] if ruta != "" else "" + archivos[int(archivo) - 1]
    elif archivo.isnumeric() and int(archivo) > len(archivos):
        print("Debe ingresar un números entre 1 y", len(archivos))
        preguntarArchivos()
    else:
        return preguntarArchivos(archivo)

def esInit(linea):
    """
    Entradas: linea de tipo string
    Salidas: True/False si la línea es un init
    Funcionamiento: Verifica si la línea es un init y devuelve True/False acorde a ello
    """
    if "__init__(self" in linea:
        return True
    else:
        return False

def esSetterOGetter(linea):
    """
    Entradas: linea de tipo string
    Salidas: True/False si la línea es un getter o setter
    Funcionamiento: Verifica con regex si la línea pasada cumple las condiciones de ser un getter o setter
    """
    patronSet = re.compile("^    def set[A-Z][a-z]")
    patronGet = re.compile("^    def get[A-Z][a-z]")
    if patronSet.match(linea) or patronGet.match(linea):
        return True
    else:
        return False

def continuar():
    """
    Entradas: N/A
    Salidas: True/False según lo escogido
    Funcionamiento: Pregunta al usuario si desea continuar y retorna True/False acorde a ello
    """
    opcion = input("¿Desea continuar? S/N: ")
    if opcion == "S" or opcion == "s":
        return True
    elif opcion == "N" or opcion == "n":
        return False
    else:
        print("Debe ingresar S o N")
        return continuar()

#Programa principal
while True:
    datos, nombre = abrirArchivo(preguntarArchivos())
    for i in range(len(datos)):
        resetearVariables()
        if "def " in datos[i]:
            if estaDocumentado(datos, i) or esInit(datos[i]) or esSetterOGetter(datos[i]):
                continue
            opcion = input("¿Documentar " + datos[i][4:datos[i].index("(")] + "? Ingrese -1 para no, en otro caso es si: ")
            if opcion == "-1":
                continue
            tabulaciones = adaptarIdentaciones(datos[i], tabulaciones)
            parametros = obtenerParametros(datos[i], parametros)
            if len(parametros) == 0:
                entradas = "N/A"
            else:
                entradas = pedirEntradas(parametros, entradas)
            salidas = input("Ingrese las salidas: ")
            funcionamiento = input("Ingrese el funcionamiento: ")
            datos = escribirDocumentacion(tabulaciones, entradas, salidas, funcionamiento, datos, nombre)
    if not continuar():
        break
