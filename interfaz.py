#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: 11/1/2021 8:34pm
#ultima modificacion: 1/2/2021 10:42pm
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
    botonCrear = Button(panel1,text = 'Crear contactos',width=30, height = 2, command = lambda: validarLlenarBD(inputCaja1.get()))
    botonCrear.place(x=80,y=200)#crea los contactos
    botonLimpiar = Button(panel1,text = 'limpiar',width=30, height = 2, command = 'FUNCION LIMPIAR CONTACTOS').place(x=80,y=300)#limpia*?
    return ''
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
    botonRegistrar = Button(panel2,text = 'Registrar',width=30, height = 2, command = lambda:insertarContacto(inputCajaNombre.get(),inputCajaApellidos.get(),inputTipoNumero.get(),inputCajaNumero.get(),inputTipoCorreo1.get(),inputCorreo1.get(),inputTipoCorreo2.get(),inputCorreo2.get(),inputTipoCorreo3.get(),inputCorreo3.get(), leer("Contactos")))
    botonRegistrar.place(x=80,y=670)
    botonLimpiar = Button(panel2,text = 'Limpiar',width=30, height = 2, command = lambda: 'ad')
    botonLimpiar.place(x=300,y=670)
    return ''
def boton3():
    '''
    funcion: modificar contacto
    e:
    s:
    '''
    print(leer('Contactos'))
    ventana3 = Tk()# crea una ventana
    ventana3.title('ventana reto 3')
    ventana3.geometry("900x800")#tamaño de la ventana
    ventana3.resizable(True, True)#opcionde modifacar el tamaño
    panel3 = Frame(ventana3, bg='RoyalBlue3', width = 900, height = 800)
    panel3.place(x=0, y=0)
    labelTitulo3 = Label(panel3, text = "Modificar contacto", bg ='snow', fg = 'gray10',font = ('',15))
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
    cajaNombreNew = Label(panel3, text = 'Nombre nuevo:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaNombreNew.place(x=80,y=150)
    inputCajaNombreNew = Entry(panel3)#cuadro de texto donde se se escribe
    inputCajaNombreNew.place(x = 250, y =150)
    cajaApellidosNew = Label(panel3, text = 'Apellidos nuevos:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaApellidosNew.place(x=80,y=175)
    inputCajaApellidosNew = Entry(panel3)#cuadro de texto donde se se escribe
    inputCajaApellidosNew.place(x = 250, y =175)
    botonModificar = Button(panel3,text = 'modificar',width=30, height = 2, command = lambda: modificarContacto(inputCajaNombre.get(),inputCajaApellidos.get(),inputCajaNombreNew.get(),inputCajaApellidosNew.get(),leer('Contactos')))
    botonModificar.place(x=100,y=220)
    botonLimpiar = Button(panel3,text = 'Limpiar',width=30, height = 2, command = lambda: 'ad')
    botonLimpiar.place(x=320,y=220)
    return ''
def boton4():
    '''
    funcion: eliminar contacto
    e:
    s:
    '''
    print(leer('Contactos'))
    ventana4 = Tk()# crea una ventana
    ventana4.title('ventana reto 4')
    ventana4.geometry("900x800")#tamaño de la ventana
    ventana4.resizable(True, True)#opcionde modifacar el tamaño
    panel4 = Frame(ventana4, bg='RoyalBlue3', width = 900, height = 800)
    panel4.place(x=0, y=0)
    labelTitulo4 = Label(panel4, text = "eliminar contacto", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo4.place(x=150,y=50)
    cajaNombre = Label(panel4, text = 'Nombre:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaNombre.place(x=80,y=100)
    inputCajaNombre = Entry(panel4)#cuadro de texto donde se se escribe
    inputCajaNombre.place(x = 250, y =100)
    cajaApellidos = Label(panel4, text = 'Apellidos:', bg = 'snow', fg = 'gray10', font = ('',12))#caja de informacion
    cajaApellidos.place(x=80,y=125)
    inputCajaApellidos = Entry(panel4)#cuadro de texto donde se se escribe
    inputCajaApellidos.place(x = 250, y =125)
    botonEliminar = Button(panel4,text = 'Eliminar',width=30, height = 2, command = lambda: eliminarContacto(inputCajaNombre.get(),inputCajaApellidos.get(),leer('Contactos')))
    botonEliminar.place(x=300,y=200)
    return ''
def boton5():
    '''
    funcion: exportar a xml
    e:
    s:
    '''
    crearXML(leer('Contactos'))
    return ''
def boton6():
    '''
    funcion: extraer las frases celebres
    e:
    s:
    '''
    extraerFrases()
    return ''
def boton7():
    '''
    funcion: chatear
    e:
    s:
    '''
    ventana7 = Tk()# crea una ventana
    ventana7.title('ventana reto 7')
    ventana7.geometry("900x800")#tamaño de la ventana
    ventana7.resizable(True, True)#opcionde modifacar el tamaño
    panel7 = Frame(ventana7,bg='RoyalBlue3', width = 900, height = 800)
    panel7.place(x=0, y=0)
    labelTitulo7 = Label(panel7, text = "Chatear!", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo7.place(x=150,y=50)
    #cantidad de chats
    cajaCantidadChats = Label(panel7, text = 'cantidad de chats:', bg = 'snow', fg = 'gray10', font = ('',12))
    cajaCantidadChats.place(x=80,y=150)
    inputCantidadChats = Entry(panel7)
    inputCantidadChats.place(x = 250, y =150)
    #botones
    botonChatear = Button(panel7,text = 'Chatear',width=30, height = 2, command = lambda: generarChat(leer('Contactos'),leer('Frases'),[],inputCantidadChats.get()))
    botonChatear.place(x=100,y=200)
    botonLimpiar = Button(panel7,text = 'Limpiar',width=30, height = 2, command = lambda: 'FUNCION LIMPIAR')
    botonLimpiar.place(x=320,y=200)
    return ''
def boton8():
    '''
    funcion: generar los reportes
    e:
    s:
    '''
    ventana8 = Tk()# crea una ventana
    ventana8.title('ventana reto 8')
    ventana8.geometry("900x800")#tamaño de la ventana
    ventana8.resizable(True, True)#opcionde modifacar el tamaño
    panel8 = Frame(ventana8, bg='RoyalBlue3', width = 900, height = 800)
    panel8.place(x=0, y=0)
    labelTitulo8 = Label(panel8, text = "Reportes del sistema", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo8.place(x=150,y=50)
    botonReg1 = Button(panel8,text = 'Contactos del sistema',width=30, height = 2, command = lambda: reporte2(leer('Contactos')))
    botonReg1.place(x=100,y=100)
    botonReg2 = Button(panel8,text = 'Contactos que registran su número de celular',width=30, height = 2, command = lambda: reporte2(leer('Contactos')))
    botonReg2.place(x=100,y=200)
    botonReg3 = Button(panel8,text = 'La mayor cantidad de correos de un contacto',width=30, height = 2, command = lambda: reporte3(leer('Contactos')))
    botonReg3.place(x=100,y=300)
    botonReg4 = Button(panel8,text = 'Mostrar la frase célebre más larga y la más corta',width=30, height = 2, command = lambda: reporte4(leer('Frases')))
    botonReg4.place(x=100,y=400)
    botonReg5 = Button(panel8,text = 'Los contactos que han chateado',width=30, height = 2, command = lambda: reporte5(listaInfo(leer('Registro'))))
    botonReg5.place(x=100,y=500)
    botonReg6 = Button(panel8,text = 'El chat más largo generado',width=30, height = 2, command = lambda:reporte6(leer('Registro')))
    botonReg6.place(x=100,y=600)
    return ''
def boton9():
    '''
    funcion: ayuda, abre el manual de usuario
    e:
    s:
    '''
    ventana9 = Tk()# crea una ventana
    ventana9.title('ventana reto 9')
    ventana9.geometry("900x800")#tamaño de la ventana
    ventana9.resizable(True, True)#opcionde modifacar el tamaño
    panel9 = Frame(ventana9, bg='RoyalBlue3', width = 900, height = 800)
    panel9.place(x=0, y=0)
    labelTitulo9 = Label(panel9, text = "Manual de usuario", bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo9.place(x=150,y=50)
    cajaInfo = Label(panel9, text = '''MANUAL DE USUARIO!\n
    Bienvenido al sisema de chats con freses celebres!\n
    1)Presione el primer boton, luego inserte la cantidad de contactos deseadosa crear!\n
    2)Para el seugndo boton, puede generar contactos de manera manual, debe instertar nombre completo, numeros y correos\n
    3)Para modificar un contacto, presione el boton 3, debe insertar el nombre completo del contacto a modificar, luego llene la nueva informacion\n
    4)Para eliminar un contacto presione el boton 4, inserte el nombre completo y termine de eliminar el contacto deseado\n
    5)Con el boton 5 se exportara el archivo BD a un formato XML\n
    6)Con el boton 6 se extraeran las frases celebres para poder chatear!\n
    7)Para chatear presione el boton 7, se generara el chat de inmediato!\n
    8)Para generar los reportes, presione el boton 8\n
    9)Con este boton se pide ayuda y se genera el manual de usuario!\n
    10)Con este boton se genera toda la informacion acerca de el programa\n
    11)cerrar el programa''', bg = 'snow', fg = 'gray10', font = ('',10))
    cajaInfo.place(x=1,y=100)
    return ''
def boton10():
    '''
    funcion: mostrar acerda de
    e:
    s:
    '''
    ventana10 = Tk()# crea una ventana
    ventana10.title('ventana reto 10')
    ventana10.geometry("900x800")#tamaño de la ventana
    ventana10.resizable(True, True)#opcionde modifacar el tamaño
    panel10 = Frame(ventana10, bg='RoyalBlue3', width = 900, height = 800)
    panel10.place(x=0, y=0)
    labelTitulo10 = Label(panel10, text = 'Acerca de', bg ='snow', fg = 'gray10',font = ('',15))
    labelTitulo10.place(x=150,y=50)
    cajaInfo = Label(panel10, text = '''Sistema de chats con frases celebres\n
    Sistema: Python version 3.8.6\n
    Fecha de creacion: 18/1/2021\n
    Autores: Esteban Sibaja Alfaro y Diego Vega Mora''', bg = 'snow', fg = 'gray10', font = ('',11))
    cajaInfo.place(x=10,y=100)
    return ''
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
boton1 = Button(panel,text = '1)Llenar BD',width=30, height = 2, command = boton1).place(x=300,y=150)
boton2 = Button(panel,text = '2)Insertar contactos',width=30, height = 2, command = boton2).place(x=300,y=200)
boton3 = Button(panel,text = '3)Modificar contactos',width=30, height = 2,command = boton3).place(x=300,y=250)
boton4 = Button(panel,text = '4)Eliminar contactos',width=30, height = 2,command = boton4).place(x=300,y=300)
boton5 = Button(panel,text = '5)Exportar BD a XML',width=30, height = 2,command = boton5).place(x=300,y=350)
boton6 = Button(panel,text = '6)Extraer frases celebres',width=30, height = 2,command = boton6).place(x=300,y=400)
boton7 = Button(panel,text = '7)Chatear',width=30, height = 2,command = boton7).place(x=300,y=450)
boton8 = Button(panel,text = '8)reportes',width=30, height = 2, command = boton8).place(x=300,y=500)
boton9 = Button(panel,text = '9)Ayuda',width=30, height = 2,command = boton9).place(x=300,y=550)
boton10 = Button(panel,text = '10)Acerca de',width=30, height = 2,command = boton10).place(x=300,y=600)
boton11 = Button(panel,text = '11)Salir',width=30, height = 2,command = boton11).place(x=300,y=650)
#llamada a la ventana principal
ventana.mainloop()