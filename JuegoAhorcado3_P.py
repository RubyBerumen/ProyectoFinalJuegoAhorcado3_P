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
            
class BusquedaBinaria:
        
    def busqueda (self, letras, valorBuscado):
        inicio=0
        final=len(letras)-1
        x=0
        while inicio<=final:
            puntero=(inicio+final)//2
            if (valorBuscado==letras[puntero]):
                x=1
                break
            elif(valorBuscado>letras[puntero]):
                inicio=puntero+1
            else:
                final=puntero-1
        return x==1
            
class Oportunidades:
    
    def __init__(self):
        self.intentos=10
        
    def getIntentos(self):
        return self.__intentos
    
    def setIntentos(self, intentos):
        self.__intentos=intentos
    
    def descontarIntento(self):
        self.intentos-=1

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
    
    def cargarPalabras(self):
        print("Cargando lista de palabras desde el archivo...")
        self.ordenar(Archivo)
        palabras=[]
        with open("palabras.txt", "r") as f:
            for l in f:
                x = l.split()
                for i in x:
                    palabras.append(str(i).upper())
        print(f"{len(palabras)} palabra(s) cargada(s)")
        return palabras
        
class AlmacenarLetras:
    
    def __init__(self):
        self.letras=[]
                
    def getLetras(self):
        return self.letras
    
    def setLetras(self, letras):
        self.letras=letras   
    
    def Agregar(self,letra):
        letras2=[]
        letras2.append(letra)
        while not self.letras == []:
            letras2.append(self.letras.pop())
            
        ss=Shellsort()    
        ss=Shellsort.ordenar(ss,letras2)
        self.setLetras(letras2)
        
class JuegoAhorcado:
    
    def obtenerLetrasDisponibles(self, letrasIngresadas):
        bb=BusquedaBinaria()
        letrasDisponibles=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(0,len(letrasDisponibles)):
            encontrado=bb.busqueda(letrasIngresadas, i)
            if(encontrado==True):
                letrasDisponibles[i]="-"
                
    def cargarPalabras(self):
        return Archivo.cargarPalabras(Archivo)
    
        
        
        
        