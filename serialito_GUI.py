import tkinter as GUI
import serial
import time

ventana = GUI.Tk()
ventana.title("Conectar a ESP32")
arduino= None

PUERTO = "COM4"
arduino = serial.Serial(port=PUERTO, baudrate= 115200, timeout= .1)


def CONECTAR():
    global PUERTO
    print("funcion conectar")
    PUERTO = EntryCOM.get()
   
   
def SEND():
    global PUERTO
    print("funcion enviar")
    x= SpinDATA.get()
    arduino.write(bytes(x,"utf-8"))
    time.sleep(0.05)
    data=arduino.readline()
    LAbelRECIBE.config(text=f"dato recibido = {data}")

def CERRAR():
    print("cerrar")
    arduino.close()
    ventana.destroy()


#instancia de los objetos

labelCOm_NAME = GUI.Label(ventana,text="escribe el nombre del puerto; emjemplo: COM2")
EntryCOM = GUI.Entry(ventana)
BtonCONECT = GUI.Button(ventana,text="conecta",
                        command=CONECTAR())

SpinDATA = GUI.Spinbox(ventana, from_=0, to=500)
BotonSEND = GUI.Button(ventana, text= "envia",
                       command= SEND)
LAbelRECIBE = GUI.Label(ventana, text= "dato recibido")
BotonCerrar = GUI.Button(ventana, text= "salir", command = CERRAR)

#incrustacion en ventana

labelCOm_NAME.pack(padx=1, pady=2)
EntryCOM.pack(padx=1,pady=2)
BtonCONECT.pack(padx=1, pady=2)
SpinDATA.pack(padx=1,pady=2)
LAbelRECIBE.pack(padx=1,pady=2)
BotonSEND.pack(padx=1,pady=2)
BotonCerrar.pack(padx=1, pady=2)

ventana.mainloop()