#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: x/x/2020 8:34pm
#ultima modificacion: x/x/2020 11:05pm
#version: 3.8.6
#importacion  de librerias
import tkinter
from tkinter import *
import pip
from pip import *
#VENTANA DEL PROGRAMA
ventana = Tk() # crea una ventana
ventana.title("ventana principal")#titulo de la ventana
ventana.geometry("900x800")#tamaño de la ventana
ventana.resizable(True, True)#opcionde modifacar el tamaño
#PANEL PRINCIPAL
panel = Frame(ventana, bg='RoyalBlue3', width = 900, height = 800)#crea un panel dentro de la ventana donde se va a trabajar
panel.place(x=0, y=0)#tamaño del panel
#TEXTOS(LABELS)
labelTitulo = Label(panel, text = "chat de texto", bg ='snow', fg = 'gray10',font = ('',25))#primer label con el titulo en el panel
labelTitulo.place(x=300,y=50)
#TEXTOS(LABELS)
labelNumero = Label(panel, text = "elige una opcion para llevar a cabo!", bg = 'snow', fg = 'gray10',font = ('',15))#otro label con texto de opciones
labelNumero.place(x=250, y=100)
#FUNCIONEZ BOTONES
def boton1():
    '''
    funcion: llenar bd 
    e:
    s:
    '''
def boton11():
    '''
    funcion: cerrar la ventana principal
    e:
    s:
    '''
    ventana.destroy()
    print('Gracias por usar el sistema de Chat!')
    return ''
#BOTONES DEL MENU PRINCIPAL
boton1 = Button(panel,text = '1)Llenar BD',width=30, height = 2, command = 'boton1').place(x=350,y=150)
boton2 = Button(panel,text = '2)Insertar contactos',width=30, height = 2, command = 'boton2').place(x=350,y=200)
boton3 = Button(panel,text = '3)Modificar contactos',width=30, height = 2,command = 'boton3').place(x=350,y=250)
boton4 = Button(panel,text = '4)Eliminiar contacto',width=30, height = 2,command = 'boton4').place(x=350,y=300)
boton5 = Button(panel,text = '5)Exportar BD a XML',width=30, height = 2,command = 'boton5').place(x=350,y=350)
boton6 = Button(panel,text = '6)Extraer frases celebres',width=30, height = 2,command = 'boton6').place(x=350,y=400)
boton7 = Button(panel,text = '7)Chatear',width=30, height = 2,command = 'boton7').place(x=350,y=450)
boton8 = Button(panel,text = '8)reportes',width=30, height = 2, command = 'boton8').place(x=350,y=500)
boton9 = Button(panel,text = '9)Ayuda',width=30, height = 2,command = 'boton9').place(x=350,y=550)
boton10 = Button(panel,text = '10)Acerca de',width=30, height = 2,command = 'boton10').place(x=350,y=600)
boton11 = Button(panel,text = '11)Salir',width=30, height = 2,command = 'boton11').place(x=350,y=650)
#llamada a la ventana principal
ventana.mainloop()