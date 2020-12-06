'''
Created on 4 dic. 2020

@author: Ruby
'''

import os
import random

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
        return int(self.intentos)
    
    def setIntentos(self, intentos):
        self.intentos=intentos
    
    def descontarIntento(self):
        self.setIntentos(self.getIntentos()-1)

class Archivo :
    
    def verificar(self):
        if not os.path.isfile("palabras.txt"): 
            print("EL archivo no existe")
            archivo=open("palabras.txt","w+")
            archivo.close()
            if os.path.isfile("palabras.txt"):
                print("Se ha creado el archivo")
        if not os.path.getsize("palabras.txt") > 0:
            print("El archivo se encuentra vacio!")
            print("Por favor ingresa palabras...\n")
            Archivo.agregarPalabras(Archivo)
        else:
            with open("palabras.txt", "r+") as f:
                lineas = 0
                for l in f:
                    if l != "\n":
                        lineas+=1
                print(f"El archivo contiene {lineas} palabras\n")
    
    def eliminar(self):
        if os.path.isfile("palabras.txt"):
            os.remove("palabras.txt")
            
        with open("palabras.txt", "w+") as f:
            pass
        print("Se ha eliminado el archivo\n")
        
    def agregarPalabras(self):
        palabras=[]
        while True:
            try:
                numPalabras=int(input("Escribe el numero de palabras que deseas ingresar: "))
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
    
    def archivoVacio(self):
        return(not os.path.getsize("palabras.txt") > 0)
            
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
    def __init__(self):
        self.letra=None
        self.letrasIngresadas=AlmacenarLetras()
        self.palabraSecreta=None
        self.palabraAleatoria=None
        self.letrasAdivinadas=None
        self.contLetras=0
        self.op=Oportunidades()
        
    def inicioAhorcado(self, palabraAleatoria):
        self.palabraAleatoria=palabraAleatoria
        ja=JuegoAhorcado()
        print("Bienvenido al juego del Ahorcado\n")
        print(f"Estoy pensando en una palabra de {len(palabraAleatoria)} letras")
        print("-----------------------------------------\n")
        
    def ingresarLetra(self):

    
    def obtenerLetrasDisponibles(self, li):
        letrasIngresadas=li.getLetras()
        bb=BusquedaBinaria()
        letrasDisponibles=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(len(letrasDisponibles)):
            encontrado=bb.busqueda(letrasIngresadas, letrasDisponibles[i])
            if(encontrado==True):
                letrasDisponibles[i]='-'
        for i in letrasDisponibles:
            print(i, end=" ")
        print()
                
    def cargarPalabras(self):
        return Archivo.cargarPalabras(Archivo)
    
    def elegirPalabra(self,palabras):
        num=random.randint(0,(len(palabras))-1)
        self.palabraAleatoria=palabras[num]
        return self.palabraAleatoria
    
    def seAdivinoPalabra(self,palabraAleatoria,letrasIngresadas):
        self.letrasAdivinadas=0
        for i in range(len(palabraAleatoria)):
            letra=palabraAleatoria[i]
            for j in range(self.contLetras):
                if(letrasIngresadas[j]==letra):
                    self.letrasAdivinadas+=1
        return self.letrasAdivinadas==len(palabraAleatoria)
    
    def obtenerPalabraAdivinada(self,palabraAleatoria,pila,op):
        letrasIngresadas=pila.getLetras()
        palabraSecreta=[]
        palabraAleatoria=palabraAleatoria.upper()
        for i in range(len(palabraAleatoria)):
            palabraSecreta.append('_')
        for i in range(len(palabraAleatoria)):
            letra=palabraAleatoria[i]
            for j in range(self.contLetras):
                if(letrasIngresadas[j]==letra):
                    palabraSecreta[i]=letra
        x=0
        for i in range (len(palabraAleatoria)):
            if(palabraAleatoria[i]==letrasIngresadas[self.contLetras]):
                x+=1
        if (x>0):
            print("Bien hecho: ")
        else:
            print("Oops! Esa letra no esta en la palabra secreta: ")
            op.descontarIntento()
        palabraNueva=""
        for i in range(len(palabraSecreta)):
            palabraNueva+=palabraSecreta[i]+str(" ")
        return palabraNueva.upper()
    

                
class PruebaJuegoahorcado:
    
    def munuOpciones(self):
        def __init__(self):
            self.__op=0
        a=Archivo()    
        print("!Bienvenido al juego del ahorcado!\n")
        while True:
            print("1) Verificar archivo")
            print("2) Llenar archivo con palabras")
            print("3) Borrar archivo")    
            print("4) Jugar")   
            print("5) Salir")
            while True:
                try:
                    self.op=int(input("Elige una opcion:\n"))
                except:
                    print("Debes ingresar un numero")
                else:
                    if(self.op>0):
                        break
                    else:
                        print("El numero debe de ser mayor que 0")
            if(self.op==1):
                a.verificar()
            elif(self.op==2):
                a.agregarPalabras()
            elif(self.op==3):
                a.eliminar()
            elif(self.op==4):
                if(a.archivoVacio()):
                    print("El archivo se encuentra vacio!")
                    print("Por favor ingresa palabras...\n")
                    a.agregarPalabras()
                else:
                    ja=JuegoAhorcado()
                    palabras=ja.cargarPalabras()
                    ja.inicioAhorcado(ja.elegirPalabra(palabras))
            elif(self.op==5):
                print("Gracias por haber jugado al ahorcado!")
                break
            else:
                print("Opcion Invalida!\n")
                
pja=PruebaJuegoahorcado()
pja.munuOpciones()       
        
        