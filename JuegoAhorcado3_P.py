'''
Created on 4 dic. 2020

@author: Ruby
'''

import os

class Shellsort:
    
    def ordenar(self,palabras):
        intervalo = len(palabras)/2
        intervalo = int(intervalo)
        while(intervalo>0):
            for i in range(int(intervalo),len(palabras)):
                j=i-int(intervalo)
                while(j>=0):
                    k=j+int(intervalo)
                    if(palabras[j] <= palabras[k]):
                        j-=1
                    else:
                        aux=palabras[j]
                        palabras[j]=palabras[k]
                        palabras[k]=aux
                        j-=int(intervalo)
            
            intervalo=int(intervalo)/2

class Archivo :
    
    def verificar(self):
        if not os.path.isfile("palabras.txt"): 
            print("EL archivo no existe")
            archivo=open("palabras.txt","w+")
            archivo.close()
            if os.path.isfile("palabras.txt"):
                print("Se ha creado el archivo")
        if not os.path.getsize("palabras.txt") > 0:
            print("El archivo esta vacio")
            return True
        else:
            with open("palabras.txt", "r+") as f:
                lineas = 0
                for l in f:
                    if l != "\n":
                        lineas+=1
                print(f"El archivo contiene {lineas} palabras")
            return False
    
    def eliminar(self):
        if os.path.isfile("palabras.txt"):
            os.remove("palabras.txt")
            
        with open("palabras.txt", "w+") as f:
            pass
        print("Se ha eliminado el archivo")
        
    def agregarPalabras(self):
        palabras=[]
        while True:
            try:
                numPalabras=int(input("¿Cuantas palabras deseas ingresar?"))
            except:
                print("Debes ingresar un numero")
            else:
                if numPalabras>0:
                    break
                else:
                    print("El numero debe ser mayor que 0!")
        for i in range(numPalabras):
            palabra=input(f"Ingresa la palabra {i+1} :")
            palabras.append(palabra)
            
        ss=Shellsort()    
        ss=Shellsort.ordenar(ss,palabras)
        with open("palabras.txt","a+") as f:
            for i in palabras:
                f.write(i+"\n")
        print("La(s) palabra(s) ha(n) sido cargada(s)\n")
        
    def ordenar(self):
        palabras=[]
        with open("palabras.txt", "r") as f:
            for l in f:
                x=l.split()
                for i in x:
                    palabras.append(i)
        ss=Shellsort()    
        ss=Shellsort.ordenar(ss,palabras)
        with open("palabras.txt", "w") as f:
            for i in palabras:
                f.write(i+"\n")
    
    
    
    
        
        
        
        