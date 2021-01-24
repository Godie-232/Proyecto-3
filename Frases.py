#Creado por: Esteban Sibaja Alfaro y Diego Vega Mora
#Fecha de creacion: 11/1/2021 19:44
#Ultima modificacion: XX/XX/2021 XX:XX
#Version 3.8.6

#Importacion de librerias
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
#Definicion de Funciones
# -*- coding: utf-8 -*-
def dFrases(lista):
    """
    toma de internet las frases y las separa en una lista
    E:
    S: 
    """
    url = "https://amazonia-teamfactory.com/blog/las-50-mejores-frases-de-motivacion-en-el-trabajo/"#Se extrae la informacion de la URL
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    frases = soup.find_all ("div", class_ = "wrap cf") #se divide la info segun el codigo html 
    info = ""
    for i in frases:
        info += i.text
    info = info.split("\n")
    for i in info:
        if i != "":
            lista.append(i)
    return ""
