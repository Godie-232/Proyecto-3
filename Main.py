#Creado por: Esteban Sibaja Alfaro y Diego Vega Mora
#Fecha de creacion: 11/1/2021 19:44
#Ultima modificacion: XX/XX/2021 XX:XX
#Version 3.8.6

#Importacion de librerias
import names 
import random
import requests
import pickle
#Creacion de funciones
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
    def correoOO (self, string1, string2, string3, num1, num2, num3):
        """
        Le da el atributo a los correos
        E: 3 string y 3 numeros
        S:
        """
        self.correo = [(num1, string1), (num2,string2), (num3,string3)]
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
    lista = ["", "", ""]
    correos = ["@gmail.com", "@hotmail.com", "@yahoo.com"]
    while i < num:
        lista[i] = str1[0] + str2[:4] + correos[i]
        i += 1
    if lista[2] == "":
        return lista[:1]
    elif lista[1] == "":
        return lista[0]
    else:
        return lista
def iniciarBD():
    global listaBD
    name = names.get_first_name()
    apellido = randomA()
    tipo = random.randint(1,4)
    numero = int(validarNumero(tipo))
    correos = validarCorreo(random.randint(1, 3), name, apellido)
    BD.nameOO(name)
    BD.apellidosOO(apellido)
    
