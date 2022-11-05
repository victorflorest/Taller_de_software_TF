from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from messagebox import msg_error, msg_about
import pymysql as sql
import db

app = QtWidgets.QApplication([])


login = uic.loadUi("untitled.ui")
registro = uic.loadUi("registro.ui")
registro_profesor = uic.loadUi("registro_profesor.ui")
entrar= uic.loadUi("entrar.ui")


<<<<<<< HEAD
db=db.Database()
=======
try:
    con = sql.connect("base de datos2.db")
    con.commit()
    con.close()
except:
    print("Error en la base de datos...")
>>>>>>> a530ffbb68cc49318050678cb177838d1b6eb97c


def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(name) == 0 or len(password)==0:
        login.label_4.setText("Ingrese todos los datos")
    else:
<<<<<<< HEAD
        rs=db.login_alumno(name, password)
=======
        con = sql.connect("base de datos2.db")
        cursor = con.cursor()

        cursor.execute('SELECT usuario, contraseña FROM users2 WHERE usuario = ? AND contraseña = ?' ,(name, password))  

>>>>>>> a530ffbb68cc49318050678cb177838d1b6eb97c

        if rs:
            msg_about("","Se pudo iniciar sesión con éxito")
            gui_entrar()
        else:
            msg_error("Error", "El usuario o la contraseña no son correctos")


<<<<<<< HEAD
def gui_registro_alumno():
    nombre = registro.lineEdit.text()
    apellido = registro.lineEdit_2.text()
=======
def crear_tabla():
    con = sql.connect("base de datos2.db")
    cursor = con.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users (
            nombres text,
            apellidos text,
            correo text,
            usuario text,
            contraseña text
        )"""
    )

def crear_tabla_2():
    con = sql.connect("base de datos2.db")
    cursor = con.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users2 (
            nombres text,
            apellidos text,
            correo text,
            usuario text,
            contraseña text,
            DNI integer
        )"""
    )

    con.commit()
    con.close()

def registrar(nombres, apellidos, correo, usuario, contraseña):
    con = sql.connect("base de datos2.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO users VALUES ('{nombres}', '{apellidos}', '{correo}', '{usuario}', '{contraseña}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def registrar2(nombres, apellidos, correo, usuario, contraseña, DNI):
    con = sql.connect("base de datos2.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO users2 VALUES ('{nombres}', '{apellidos}', '{correo}', '{usuario}', '{contraseña}', '{DNI}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def datos():
    nombres = registro.lineEdit.text()
    apellidos = registro.lineEdit_2.text()
>>>>>>> a530ffbb68cc49318050678cb177838d1b6eb97c
    correo = registro.lineEdit_3.text()
    aula = registro.lineEdit_4.text()
    contraseña = registro.lineEdit_5.text()

    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
<<<<<<< HEAD
        db.registro_alumno(nombre, apellido, correo, contraseña, aula)
        msg_about("Éxito", "Se ha registrado al alumno correctamente")
=======
        registrar(nombres, apellidos, correo, usuario, contraseña)
        msg_about("Éxito", "Se ha registrado el profesor correctamente")
>>>>>>> a530ffbb68cc49318050678cb177838d1b6eb97c
        registro.lineEdit.setText("")
        registro.lineEdit_2.setText("")
        registro.lineEdit_3.setText("")
        registro.lineEdit_4.setText("")
        registro.lineEdit_5.setText("")


def datos2():
    nombres = registro_profesor.lineEdit.text()
    apellidos = registro_profesor.lineEdit_2.text()
    correo = registro_profesor.lineEdit_3.text()
    usuario = registro_profesor.lineEdit_4.text()
    contraseña = registro_profesor.lineEdit_5.text()
    DNI = registro_profesor.lineEdit_6.text()

    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
        registrar2(nombres, apellidos, correo, usuario, contraseña, DNI)
        msg_about("Éxito", "Se ha registrado el profesor correctamente")
        registro_profesor.lineEdit.setText("")
        registro_profesor.lineEdit_2.setText("")
        registro_profesor.lineEdit_3.setText("")
        registro_profesor.lineEdit_4.setText("")
        registro_profesor.lineEdit_5.setText("")
        registro_profesor.lineEdit_6.setText("")


def gui_entrar():
    login.hide()
    entrar.show()

def gui_volver_login():
    registro.hide()
    registro_profesor.hide()
    login.label_4.setText("")
    login.show()

def gui_registro_profesor():
<<<<<<< HEAD
    nombre = registro.lineEdit.text()
    apellido = registro.lineEdit_2.text()
    correo = registro.lineEdit_3.text()
    aula = registro.lineEdit_4.text()
    contraseña = registro.lineEdit_5.text()

    if len(contraseña) <= 6:
        msg_error("ERROR", "La contraseña debe tener como mínimo 7 dígitos")

    else:
        db.registro_tutor(nombre, apellido, aula, correo, contraseña)
        msg_about("Éxito", "Se ha registrado al tutor correctamente")
        registro.lineEdit.setText("")
        registro.lineEdit_2.setText("")
        registro.lineEdit_3.setText("")
        registro.lineEdit_4.setText("")
        registro.lineEdit_5.setText("")
    
=======
    login.hide()
    registro_profesor.show()
    crear_tabla_2()
>>>>>>> a530ffbb68cc49318050678cb177838d1b6eb97c

def gui_registro():
    login.hide()
    registro.show()
<<<<<<< HEAD
=======
    crear_tabla()
    
>>>>>>> a530ffbb68cc49318050678cb177838d1b6eb97c

def cerrar():
    app.exit()

 
login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(gui_registro)    
login.pushButton_4.clicked.connect(gui_registro_profesor)
<<<<<<< HEAD
registro.pushButton.clicked.connect(gui_registro_alumno)
registro.pushButton_2.clicked.connect(cerrar) 
registro.pushButton_3.clicked.connect(gui_volver_login)
registro_profesor.pushButton.clicked.connect(cerrar)   
=======
registro.pushButton.clicked.connect(datos)
registro.pushButton_3.clicked.connect(gui_volver_login) 
>>>>>>> a530ffbb68cc49318050678cb177838d1b6eb97c
registro_profesor.pushButton_2.clicked.connect(gui_volver_login)
registro_profesor.pushButton_3.clicked.connect(datos2)

login.show()
app.exec_()
