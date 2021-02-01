#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: x/x/2020 8:34pm
#ultima modificacion: x/x/2020 11:05pm
#version: 3.8.6
#importacion  de librerias
import tkinter
from tkinter import *
import pip
from pip import *
from Main import *
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
    funcion: llenar BD
    e:
    s:
    '''
    ventana1 = Tk() # crea una ventana
    ventana1.title("ventana reto 1")#titulo de la ventana
    ventana1.geometry("900x800")#tamaño de la ventana
    ventana1.resizable(True, True)#opcionde modifacar el tamaño
    panel1 = Frame(ventana1, bg='RoyalBlue3', width = 900, height = 800)
    panel1.place(x=0, y=0)
    labelTitulo1 = Label(panel1, text = "crear contactos!", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo1.place(x=150,y=50)
    caja1 = Label(panel1, text = 'cantidad de contactos:', bg = 'snow', fg = 'gray10', font = ('',15))#caja de informacion
    caja1.place(x=80,y=150)
    inputCaja1 = Entry(panel1)#cuadro de texto donde se se escribe
    inputCaja1.place(x = 300, y =150)
    botonCrear = Button(panel1,text = 'Crear contactos',width=30, height = 2, command = lambda: validarLlenarBD(inputCaja1.get()))#crea los contactos
    botonCrear.place(x=80,y=200)
    botonLimpiar = Button(panel1,text = 'limpiar',width=30, height = 2, command = 'FUNCION LIMPIAR CONTACTOS').place(x=80,y=300)#limpia*?
def boton2():
    '''
    funcion: insertar un contacto
    e:
    s:
    '''
    ventana2 = Tk()# crea una ventana
    ventana2.title('ventana reto 2')
    ventana2.geometry("900x800")#tamaño de la ventana
    ventana2.resizable(True, True)#opcionde modifacar el tamaño
    panel2 = Frame(ventana2, bg='RoyalBlue3', width = 900, height = 800)
    panel2.place(x=0, y=0)
    labelTitulo2 = Label(panel2, text = "crear un contacto!", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo2.place(x=150,y=50)
    #nombre y apellidos
    cajaNombre = Label(panel2, text = 'Nombre:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaNombre.place(x=80,y=100)
    inputCajaNombre = Entry(panel2)#cuadro de texto donde se se escribe
    inputCajaNombre.place(x = 250, y =100)
    cajaApellidos = Label(panel2, text = 'Apellidos:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaApellidos.place(x=80,y=125)
    inputCajaApellidos = Entry(panel2)#cuadro de texto donde se se escribe
    inputCajaApellidos.place(x = 250, y =125)
    cajaTipoNumero = Label(panel2,text ='1.celular\n2.laboral\n3.particular\n4.fax\ntipo de numero:', bg = 'snow', fg = 'gray10', font = ('',11))
    cajaTipoNumero.place(x=80,y=150)
    inputTipoNumero = Entry(panel2)
    inputTipoNumero.place(x = 250, y =200)
    cajaNumero = Label(panel2, text = 'inserte el numero:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaNumero.place(x=80,y=250)
    inputCajaNumero = Entry(panel2)#cuadro de texto donde se se escribe
    inputCajaNumero.place(x = 250, y =250)
    #correo 1
    cajaTipoCorreo1 = Label(panel2,text ='1.particular\n2.laboral\ntipo de correo:', bg = 'snow', fg = 'gray10', font = ('',11))
    cajaTipoCorreo1.place(x=80,y=300)
    inputTipoCorreo1 = Entry(panel2)
    inputTipoCorreo1.place(x=250,y=325)
    cajaCorreo1 = Label(panel2, text = 'inserte el correo:', bg = 'snow', fg = 'gray10', font = ('',12))
    cajaCorreo1.place(x=80,y=375)
    inputCorreo1 = Entry(panel2)
    inputCorreo1.place(x=250,y=375)
    #correo 2
    cajaTipoCorreo2 = Label(panel2,text ='1.particular\n2.laboral\ntipo de correo:', bg = 'snow', fg = 'gray10', font = ('',11))
    cajaTipoCorreo2.place(x=80,y=425)
    inputTipoCorreo2 = Entry(panel2)
    inputTipoCorreo2.place(x=250,y=425)
    cajaCorreo2 = Label(panel2, text = 'inserte el correo:', bg = 'snow', fg = 'gray10', font = ('',12))
    cajaCorreo2.place(x=80,y=500)
    inputCorreo2 = Entry(panel2)
    inputCorreo2.place(x=250,y=500)
    #correo 3
    cajaTipoCorreo3 = Label(panel2,text ='1.particular\n2.laboral\ntipo de correo:', bg = 'snow', fg = 'gray10', font = ('',11))
    cajaTipoCorreo3.place(x=80,y=550)
    inputTipoCorreo3 = Entry(panel2)
    inputTipoCorreo3.place(x=250,y=550)
    cajaCorreo3 = Label(panel2, text = 'inserte el correo:', bg = 'snow', fg = 'gray10', font = ('',12))
    cajaCorreo3.place(x=80,y=625)
    inputCorreo3 = Entry(panel2)
    inputCorreo3.place(x=250,y=625)
    #botones registro y limpieza
    botonRegistrar = Button(panel2,text = 'Registrar',width=30, height = 2, command = lambda:insertarContacto(inputCajaNombre,inputCajaApellidos,inputTipoNumero.get(),inputCajaNumero.get(),inputTipoCorreo1.get(),inputCorreo1,inputTipoCorreo2.get(),inputCorreo2,inputTipoCorreo3.get(),inputCorreo3))
    botonRegistrar.place(x=80,y=670)
    botonLimpiar = Button(panel2,text = 'Limpiar',width=30, height = 2, command = lambda: 'ad')
    botonLimpiar.place(x=300,y=670)
def ModificarEliminar():
    '''
    funcion: da la opcion de eliminar o modificar un contacto
    e:
    s:
    '''
    '####AQUI SE DEBE CORRER LA FUNCION DE BUSQUEDA####'
    ventanaMod = Tk()# crea una ventana
    ventanaMod.title('ventana modificar/eliminar')
    ventanaMod.geometry("900x800")#tamaño de la ventana
    ventanaMod.resizable(True, True)#opcionde modifacar el tamaño
    panelMod = Frame(ventanaMod, bg='RoyalBlue3', width = 900, height = 800)
    panelMod.place(x=0, y=0)
    labelTituloMod = Label(panelMod, text = "Modificar/Eliminar un contacto", bg ='snow', fg = 'gray10',font = ('',15))
    labelTituloMod.place(x=150,y=50)
    botonModificar = Button(panelMod, text = 'Modificar',width=30, height = 2, command = lambda: 'FUNCION MODIFCAR')
    botonModificar.place(x=100,y=100)
    botonEliminar = Button(panelMod, text = 'Eliminar',width=30, height = 2, command = lambda: 'FUNCION ELIMINAR')
    botonEliminar.place(x=300,y=100)
def boton3():
    '''
    funcion: modificar y eliminar contacto
    e:
    s:
    '''
    ventana3 = Tk()# crea una ventana
    ventana3.title('ventana reto 2')
    ventana3.geometry("900x800")#tamaño de la ventana
    ventana3.resizable(True, True)#opcionde modifacar el tamaño
    panel3 = Frame(ventana3, bg='RoyalBlue3', width = 900, height = 800)
    panel3.place(x=0, y=0)
    labelTitulo3 = Label(panel3, text = "Buscar el contacto", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo3.place(x=150,y=50)
    #nombre y apellidos
    cajaNombre = Label(panel3, text = 'Nombre:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaNombre.place(x=80,y=100)
    inputCajaNombre = Entry(panel3)#cuadro de texto donde se se escribe
    inputCajaNombre.place(x = 250, y =100)
    cajaApellidos = Label(panel3, text = 'Apellidos:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaApellidos.place(x=80,y=125)
    inputCajaApellidos = Entry(panel3)#cuadro de texto donde se se escribe
    inputCajaApellidos.place(x = 250, y =125)
    #numero
    cajaNumero = Label(panel3, text = 'inserte el numero:', bg = 'snow', fg = 'gray10', font = ('',12))
    cajaNumero.place(x=80,y=150)
    inputCajaNumero = Entry(panel3)
    inputCajaNumero.place(x = 250, y =150)
    botonBuscar = Button(panel3,text = 'buscar',width=30, height = 2, command = lambda: ModificarEliminar())
    botonBuscar.place(x=100,y=200)
    botonLimpiar = Button(panel3,text = 'Limpiar',width=30, height = 2, command = lambda: 'ad')
    botonLimpiar.place(x=300,y=200)
def boton4():
    '''
    funcion: exportar a xml
    e:
    s:
    '''
    '###########FUNCION BD A XML##############'
def boton5():
    '''
    funcion: extraer las frases celebres
    e:
    s:
    '''
    '########FUNCION FRASES CELEBRES######'
def boton6():
    '''
    funcion: chatear
    e:
    s:
    '''
    ventana6 = Tk()# crea una ventana
    ventana6.title('ventana reto 7')
    ventana6.geometry("900x800")#tamaño de la ventana
    ventana6.resizable(True, True)#opcionde modifacar el tamaño
    panel6 = Frame(ventana6, bg='RoyalBlue3', width = 900, height = 800)
    panel6.place(x=0, y=0)
    labelTitulo6 = Label(panel6, text = "Chatear!", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo6.place(x=150,y=50)
    #cantidad de chats
    cajaCantidadChats = Label(panel6, text = 'cantidad de contactos:', bg = 'snow', fg = 'gray10', font = ('',12))
    cajaCantidadChats.place(x=80,y=150)
    inputCantidadChats = Entry(panel6)
    inputCantidadChats.place(x = 250, y =150)
    #botones
    botonChatear = Button(panel6,text = 'Chatear',width=30, height = 2, command = lambda: 'FUNCION CHATEAR')
    botonChatear.place(x=100,y=200)
    botonLimpiar = Button(panel6,text = 'Limpiar',width=30, height = 2, command = lambda: 'FUNCION LIMPIAR')
    botonLimpiar.place(x=320,y=200)
def boton7():
    '''
    funcion: generar los reportes
    e:
    s:
    '''
    'FUNCION REPORTES'
def boton8():
    '''
    funcion: ayuda, abre el manual de usuario
    e:
    s:
    '''
    ventana8 = Tk()# crea una ventana
    ventana8.title('ventana reto 8')
    ventana8.geometry("900x800")#tamaño de la ventana
    ventana8.resizable(True, True)#opcionde modifacar el tamaño
    panel8 = Frame(ventana8, bg='RoyalBlue3', width = 900, height = 800)
    panel8.place(x=0, y=0)
    labelTitulo8 = Label(panel8, text = "Manual de usuario", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo8.place(x=150,y=50)
def boton9():
    '''
    funcion: mostrar acerda de
    e:
    s:
    '''
    ventana9 = Tk()# crea una ventana
    ventana9.title('ventana reto 7')
    ventana9.geometry("900x800")#tamaño de la ventana
    ventana9.resizable(True, True)#opcionde modifacar el tamaño
    panel9 = Frame(ventana9, bg='RoyalBlue3', width = 900, height = 800)
    panel9.place(x=0, y=0)
    labelTitulo9 = Label(panel9, text = 'Acerca de', bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo9.place(x=150,y=50)
def boto10():
    '''
    funcion: cerrar la ventana principal
    e:
    s:
    '''
    ventana.destroy()
    print('Gracias por usar el sistema de Chat!')
    return ''
#BOTONES DEL MENU PRINCIPAL
boton1 = Button(panel,text = '1)Llenar BD',width=30, height = 2, command = boton1).place(x=350,y=150)
boton2 = Button(panel,text = '2)Insertar contactos',width=30, height = 2, command = boton2).place(x=350,y=200)
boton3 = Button(panel,text = '3)Modificar/eliminar contactos',width=30, height = 2,command = boton3).place(x=350,y=250)
boton4 = Button(panel,text = '4)Exportar BD a XML',width=30, height = 2,command = boton4).place(x=350,y=300)
boton5 = Button(panel,text = '5)Extraer frases celebres',width=30, height = 2,command = boton5).place(x=350,y=350)
boton6 = Button(panel,text = '6)Chatear',width=30, height = 2,command = boton6).place(x=350,y=400)
boton7 = Button(panel,text = '7)reportes',width=30, height = 2, command = boton7).place(x=350,y=450)
boton8 = Button(panel,text = '8)Ayuda',width=30, height = 2,command = 'boton8').place(x=350,y=500)
boton9 = Button(panel,text = '9)Acerca de',width=30, height = 2,command = 'boton9').place(x=350,y=550)
boton10 = Button(panel,text = '10)Salir',width=30, height = 2,command = 'boton10').place(x=350,y=600)
#llamada a la ventana principal
ventana.mainloop()