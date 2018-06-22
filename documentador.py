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
    archivo = open(nombre, "r")
    datos = archivo.readlines()
    archivo.close()
    return datos, nombre

def resetearVariables():
    global parametros, entradas, salidas, funcionamiento, tabulaciones, borrar
    parametros = []
    entradas = ""
    salidas = ""
    funcionamiento = ""
    tabulaciones = "    "
    borrar = []
    return

def adaptarIdentaciones(linea, tabulaciones):
    if "    " in linea:
        tabulaciones += "    "
    return tabulaciones

def obtenerParametros(linea, parametros):
    if linea.count(")") == 1:
        parametros += linea[linea.index("(")+1:linea.index(")")].split(",")
    else:
        parametros += linea[linea.index("(")+1:linea.index(")", len(linea) - 3)].split(",")
    borrar, parametros = quitarValoresPorOmision(parametros)
    parametros = quitarTuplasPorOmision(linea, borrar, parametros)
    parametros = quitarSelf(parametros)
    return parametros

def quitarValoresPorOmision(parametros):
    borrar = []
    for i in range(len(parametros)):
        if "=" in parametros[i]:
            parametros[i] = parametros[i][:parametros[i].index("=")]
        if not parametros[i][0].isalpha():
            borrar += parametros[i:i + 1]
    return borrar, parametros

def quitarTuplasPorOmision(linea, borrar, parametros):
    if linea.count(")") != 1:
        for i in range(len(borrar)):
            parametros.remove(list(borrar)[i])
    return parametros

def quitarSelf(parametros):
    if "self" in parametros:
            parametros.remove("self")
    return parametros

def pedirEntradas(parametros, entradas):
    for j in range(len(parametros)):
        tipo = input("Ingrese el tipo de " + parametros[j] + ": ")
        entradas += parametros[j] + " de tipo " + tipo
        if j + 1 ==  len(parametros) - 1:
            entradas += " y "
        else:
            entradas += ", "

def escribirDocumentacion(tabulaciones, entradas, salidas, funcionamiento, datos, nombre):
    datos = datos[:i+1] + [tabulaciones + '"""\n' + tabulaciones + 'Entradas: ' + entradas + '\n' + tabulaciones + 'Salidas: ' + salidas + '\n' + tabulaciones + 'Funcionamiento: ' + funcionamiento + '\n' + tabulaciones + '"""\n'] +datos[i+1:]
    archivo = open(nombre, "w")
    archivo.writelines(datos)
    archivo.close()
    return

def estaDocumentado(datos, indice):
    if '"""' in datos[indice - 1] or '"""' in datos[indice + 1]:
        return True
    else:
        return False

def obtenerArchivos(ruta = ""):
    if ruta == "":
        archivos = glob.glob("*.py")
    else:
        archivos = glob.glob(ruta + "\*.py")
        for i in range(len(archivos)):
            while "\\" in archivos[i]:
                archivos[i] = archivos[i][archivos[i].index("\\") + 1:]
    return archivos

def listarArchivos(archivos):
    for i in range(len(archivos)):
        if archivos[i].count("\\") == 0:
            print(str(i + 1) + ")", archivos[i])
        else:
            print(str(i + 1) + ")", archivos[i][archivos[i].index("\\", archivos[i].count("\\") - 1) + 1:])
    return

def preguntarArchivos(ruta = ""):
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
    if "__init__(self" in linea:
        return True
    else:
        return False

def esSetterOGetter(linea):
    patronSet = re.compile("^    def set[A-Z][a-z]")
    patronGet = re.compile("^    def get[A-Z][a-z]")
    if patronSet.match(linea) or patronGet.match(linea):
        return True
    else:
        return False

def continuar():
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
            escribirDocumentacion(tabulaciones, entradas, salidas, funcionamiento, datos, nombre)
    if not continuar():
        break
