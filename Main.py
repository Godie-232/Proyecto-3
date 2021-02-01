#Creado por: Esteban Sibaja Alfaro y Diego Vega Mora
#Fecha de creacion: 11/1/2021 19:44
#Ultima modificacion: XX/XX/2021 XX:XX
#Version 3.8.6

#Importacion de librerias
import names 
import random
from Frases import *
import pickle
import datetime 
import xml.etree.ElementTree as xml
#Creacion de funciones
# -*- coding: utf-8 -*-
listaFrases = []
listaBD = []
def guardar (archivo, lista):
    """
    guarda una lista en un archivo
    E: un str y una lista
    S: 
    """
    file = open(archivo, "wb")
    pickle.dump(lista, file)
    file.close
def leer(archivo):
    """
    lee un archivo
    E: un str
    S: una lista
    """
    file = open(archivo, "rb")
    lista = pickle.load(file)
    return lista
class BD:
    """
    Creacion de la clase7
    """
    def __init__(self):
        """
        Definicion de metodos
        """
        self.nombre = ""
        self.apellidos = ""
        self.tipo = 0
        self.numero = 0
        self.correo = []
    def nameOO (self, string):
        """
        Le da el atributo al nombre
        E: un string
        S:
        """
        self.nombre = string
        return ""
    def apellidosOO (self, strings):
        """
        Le da el atributo a los apellidos
        E: un string
        S:
        """
        self.apellidos = strings
        return ""
    def tipoOO (self, num):
        """
        Le da el atributo al tipo
        E: un numero
        S:
        """
        self.tipo = num
    def numeroOO (self, num):
        """
        Le da el atributo al numero
        E: un numero
        S:
        """
        self.numero = num
        return ""
    def correoOO (self, lista):
        """
        Le da el atributo a los correos
        E: 3 string y 3 numeros
        S:
        """
        self.correo = lista
def randomA ():
    """
    retorna el apellido completo de forma aleatoria
    E:
    S: un string
    """
    return names.get_last_name() + " " + names.get_last_name()
def validarNumero(num):
    """
    Dado un numero retorna un tipo de numero de telefono
    E: un numero
    S: un str
    """
    if num == 1:
        return str(random.choice([6,7,8,9])) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    else:
        return str(num) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
def validarCorreo(num, str1, str2):
    """
    recive la cantidad de correos y el nombre y crea los correos
    E: un numero y 2 strings
    S: una lista
    """
    i = 0
    lista = [("", ""), ("", ""), ("", "")]
    correos = ["@gmail.com", "@hotmail.com", "@yahoo.com"]
    while i < num:
        lista[i] = (random.randint(1, 2),str1[0] + str2[:4] + correos[i])
        i += 1
    return lista
def iniciarBD():
    """
    Guarda de forma aleatoria los datos del contacto
    E:
    S:
    """
    global listaBD
    clase = BD()
    name = names.get_first_name()
    apellido = randomA()
    tipo = random.randint(1,4)
    numero = int(validarNumero(tipo))
    correos = validarCorreo(random.randint(1, 3), name, apellido)
    clase.nameOO(name)
    clase.apellidosOO(apellido)
    clase.tipoOO(tipo)
    clase.numeroOO(numero)    
    clase.correoOO(correos)
    listaBD += [[name, apellido, tipo, numero, correos]]
    guardar("Contactos", listaBD)
    return ""
def llenarBD(num):
    """
    Dado un numero retorna la lista con la cantidad de contactos pedidos
    E: un numero
    S: una lista
    """
    global listaBD
    i = 0
    while i < num:
        iniciarBD()
        i += 1
    return listaBD
def validarLlenarBD(num):
    """
    Valida la funcion de llenarBD
    E: un numero
    S: una lista
    """
    if isinstance(num, int):
        if num > 0:
            if num < 500:
                return llenarBD(num)
            else:
                print("Ingrese un numero menor que 500")
                return ""
        else:
            print("Ingrese un numero mayor a 0")
            return ""
    else:
        print("Ingrese un numero entero positivo")
        return ""
def insertarContacto(nombre, apellidos, tipo, numero, correo1, correo2, correo3, num1, num2, num3):
    """
    Dado unos valores crea los objetos y los añade a la lista global luego la guarda
    E: 4 strings y 5 numeros
    S: una lista
    """
    global listaBD
    contactos = BD()
    contactos.nameOO(nombre)
    contactos.apellidosOO(apellidos)
    contactos.tipoOO(tipo)
    contactos.numeroOO(numero)
    lista = [(num1, correo1), (num2, correo2), (num3, correo3)]
    contactos.correoOO(lista)
    listaBD += [[nombre, apellidos, tipo, numero, lista]]
    guardar("Contactos", listaBD)
    return listaBD
def modificarContacto(nombre, apellidos, nombreN, apellidosN):
    """
    Dado el nombre de un contacto y su apellido los cambia por los nombre ingresados
    E: 4 strings
    S: una lista
    """
    global listaBD
    for i in listaBD:
        if nombre.upper() == i[0].upper() and apellidos.upper() == i[1].upper():
            i[0] = nombreN
            i[1] = apellidosN
            return listaBD
    print("El contacto no existe")
    return ""
def eliminarContacto(nombre, apellido):
    """
    Dado un nombre y un apellido elimina dicho contacto de la lista
    E: 2 strings
    S: una lista
    """
    global listaBD
    listaN = []
    for i in listaBD:
        if i[0].upper() != nombre.upper() and i[1].upper() != apellido.upper():
            listaN += [i]
    return listaN
def crearXML(lista):
    """
    Dado la lista con los contactos, crea un XML de ellos
    E: una lista
    S: 
    """
    root = xml.Element("Contactos")
    for i in lista:
        print(i)
        celda = xml.Element("Contactos")
        root.append(celda)
        name = xml.SubElement(celda, "Nombre")
        name.text = i[0]
        last = xml.SubElement(celda, "Apellidos")
        last.text = i[1]
        tipo = xml.SubElement(celda, "Tipo")
        tipo.text = str(i[2])
        number = xml.SubElement(celda, "Numero")
        number.text = str(i[3])
        tipoE1 = xml.SubElement(celda, "TipoCorreo")
        tipoE1.text = str(i[4][0][0])
        email1 = xml.SubElement(celda, "Correo")
        email1.text = i[4][0][1]
        tipoE1 = xml.SubElement(celda, "TipoCorreo")
        tipoE1.text = str(i[4][1][0])
        email2 = xml.SubElement(celda, "Correo")
        email2.text = i[4][1][1]
        tipoE1 = xml.SubElement(celda, "TipoCorreo")
        tipoE1.text = str(i[4][2][0])
        email3 = xml.SubElement(celda, "Correo")
        email3.text = i[4][2][1]
        tree = xml.ElementTree(root)
        with open("Contactos.xml", "wb") as files:
            tree.write(files)
def extraerFrases():
    """
    toma la lista de frases y las agrega a una variable, luego se guarda en memoria
    E:
    S: 
    """
    global listaFrases
    dFrases(listaFrases)
    listaFrases = listaFrases[8:48]
    print("Frases extraidas con exito")
    guardar("Frases", listaFrases)
    return ""
def ulam(num, lista):
    """
    Dado un numero y una lista vacia, retorna la lista con la susecion de Ulam del numero
    E: un numero y una lista
    S: una lista
    """
    if num > 40:
        num = 40
    if num == 1:
        return lista + [1] 
    elif num %2 == 0:
        return ulam (num//2, lista + [num])
    else:
        return ulam(num*3+1, lista + [num])
def getUlam(num):
    """
    retorna la susecion de Ulam de un numero
    E: un numero
    S: una lista
    """
    if num > 0:
        if num < 40:
            return ulam(num, [])
        else:
            print("Ingrese un numero menor a 40")
            return ""
    else:
        print("Ingrese un numero mayor a cero")
        return ""
def acercaDe():
    """
    Imprime la informacion acerca del programa, su version, cuando se creo y quienes lo crearon
    """
    print()
    print()
    print("Sistema: Python version 3.8.6          ")
    print("Fecha de creacion: 18/1/2021          ")
    print("Creado por: Esteban Sibaja y Diego Vega Mora          ")
    print()
    return ""
def sacarContactos(lista):
    """
    Dado una lista saca 2 personas diferentes
    E: una lista
    S: una lista
    """
    listaF = [0, 0]
    while listaF[0] == listaF[1]:
        listaF = [lista[random.randint(0, len(lista)-1)][:2] , lista[random.randint(0, len(lista)-1)][:2]]
    listaF = [listaF[0][0] + " " + listaF[0][1],listaF[1][0] + " " + listaF[1][1]]
    return listaF
def generarChat(listaObjetos, listaChat, ulam, num):
    """
    crea archivos con los chats 
    E: 3 listas y un numero
    S: 
    """
    i = 1
    while i < num + 1:
        file = open("Chat " + str(i) + '.txt', "w")
        k = 0
        contactos = sacarContactos(listaObjetos)
        ulam = getUlam(random.randint(0, 34))
        file.write(str(ulam) + "\n" + "Extraido de: https://amazonia-teamfactory.com/blog/las-50-mejores-frases-de-motivacion-en-el-trabajo/" + "\n")
        for j in ulam:
            file.write(str(datetime.datetime.today())[11:19] + "    " + "De: " + contactos[k] + ": " + listaChat[j-1][4:] + "\n")
            k += 1
            if k > 1:
                k = 0
        i += 1
    return ""
#def reporte1 (lista):




print(leer("Contactos"))