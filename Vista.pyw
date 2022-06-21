
from ast import Tuple
from email.mime import image
import random
from re import I
import threading
import tkinter as tk
import time
from numpy import imag
from Ascensor import *
from tkinter import VERTICAL, Image, ttk

class Vista():
    __asc=Ascensor()
    __ventana=tk.Tk()
    
   
    def __init__(self):        
        self.__ventana.title("Prueba")
        self.__ventana.resizable(False,False)
        self.__ventana.geometry("650x408")
        self.__ventana.iconbitmap("iconos/elevator.ico")

        #IMAGENES
        self.__subir=tk.PhotoImage(file="iconos/arriba.png")
        self.__bajar=tk.PhotoImage(file="iconos/abajo.png")
        self.__imgAscensor=tk.PhotoImage(file="iconos/ascensor.png")
        self.__imgPared=tk.PhotoImage(file="iconos/pared.png")

        #FRAME
        self.__frame=tk.Frame(width="800",height="600",relief="raised")
        self.__frame.pack(fill="both",expand=True)
        #color=["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        self.__ascensor=tk.Scale(self.__frame, from_=600, to=100, length=400,orient=VERTICAL)
        self.__ascensor.grid(row=0,column=0,rowspan=6,)       
        
        #BOTONES       
        self.__botonBajar6=tk.Button(self.__frame,image=self.__bajar,command=self.bajar6)
        self.__botonBajar6.grid(row=0,column=2)

        self.__botonSubir5=tk.Button(self.__frame,image=self.__subir,command=self.subir5)
        self.__botonSubir5.grid(row=1,column=1)
        self.__botonBajar5=tk.Button(self.__frame,image=self.__bajar,command=self.bajar5)
        self.__botonBajar5.grid(row=1,column=2)
        
        self.__botonSubir4=tk.Button(self.__frame,image=self.__subir,command=self.subir4)
        self.__botonSubir4.grid(row=2,column=1)
        self.__botonBajar4=tk.Button(self.__frame,image=self.__bajar,command=self.bajar4)
        self.__botonBajar4.grid(row=2,column=2)

        self.__botonSubir3=tk.Button(self.__frame,image=self.__subir,command=self.subir3)
        self.__botonSubir3.grid(row=3,column=1)
        self.__botonBajar3=tk.Button(self.__frame,image=self.__bajar,command=self.bajar3)
        self.__botonBajar3.grid(row=3,column=2)

        self.__botonSubir2=tk.Button(self.__frame,image=self.__subir,command=self.subir2)
        self.__botonSubir2.grid(row=4,column=1)
        self.__botonBajar2=tk.Button(self.__frame,image=self.__bajar,command=self.bajar2)
        self.__botonBajar2.grid(row=4,column=2)

        self.__botonSubir1=tk.Button(self.__frame,image=self.__subir,command=self.subir1)
        self.__botonSubir1.grid(row=5,column=1)          

        self.__ventana.mainloop()    
        
    def subir1(self):
        self.llamar(1)
    def subir2(self):
        self.llamar(2)
    def subir3(self):
        self.llamar(3)
    def subir4(self):
        self.llamar(4)
    def subir5(self):
        self.llamar(5)    

    def bajar2(self):
        self.llamar(2)
    def bajar3(self):
        self.llamar(3)
    def bajar4(self):
        self.llamar(4)
    def bajar5(self):
        self.llamar(5)
    def bajar6(self):
        __hilo1=threading.Thread(target=self.llamar(6))
        __hilo1.start()
        
    def llamar(self,n):
        if self.__asc.pisoActual<n:
            self.__asc.estado=1
            for i in range(self.__asc.pisoActual*100,n*100):
                self.__asc.pisoActual=i               
                self.__ascensor.set(i)
                time.sleep(0.5)                               
                     
        if self.__asc.pisoActual>n:
            pass
Vista()