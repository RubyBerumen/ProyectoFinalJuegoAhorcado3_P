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
                print(f"El archivo contiene {lineas} palabra(s)\n")
    
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
        
    def quitar(self):
        if(self.getLetras()==[]):
            return ' '
        else:
            return self.letras.pop(0)
    
    def agregar(self,letra):
        letras2=[]
        letras2.append(letra)
        while not self.letras == []:
            letras2.append(self.letras.pop())
        x=0
        for i in range(1,len(letras2)):
            x=letras2[i]
            j=(i-1)
            while(j>=0 and letras2[j]>x):
                letras2[j+1]=letras2[j]
                letras2[j]=x    
                j-=1
        self.setLetras(letras2)
        
        def obtenerPalabraAdivinada(self,palabraSecreta):
            letras2=[]
            for i in palabraSecreta:
                x=0
                while not self.letras == []:
                    l=self.quitar()
                    letras2.append(l)
                    if (l==i):
                        x=1
                        print(i,end=" ")
                        break
                while not letras2 == []:
                    self.agregar(letras2.pop(0))
                if (x==0):
                    print("_",end=" ")    
        print("\n")
        
class JuegoAhorcado:
    def __init__(self):
        self.letra=None
        self.letrasIngresadas=AlmacenarLetras()
        self.palabraSecreta=None
        self.palabraAleatoria=None
        self.letrasAdivinadas=None
        self.contLetras=0
        self.op=Oportunidades()
        self.bb=BusquedaBinaria()
        
    def inicioAhorcado(self, palabraAleatoria):
        self.palabraAleatoria=palabraAleatoria
        ja=JuegoAhorcado()
        print("Bienvenido al juego del Ahorcado\n")
        print(f"Estoy pensando en una palabra de {len(palabraAleatoria)} letras")
        print(palabraAleatoria)
        print("-----------------------------------------\n")
        self.ingresarLetra(ja,palabraAleatoria)
        
    def ingresarLetra(self,ja,palabraAleatoria):
        pja=PruebaJuegoahorcado()
        
        print(f"Tienes {ja.op.getIntentos()} oportunidades")
        print(f"Letras disponibles: {ja.obtenerLetrasDisponibles(ja.letrasIngresadas)}")
        print("Por favor ingresa una letra: ")
        caracter=''
        while True:
            caracter = str(input()).lower()
            if (len(caracter)==1):
                x=ord(caracter[0])
                if(x>93 and x<123):
                    ja.letra=caracter.upper()
                    ja.letrasIngresadas.agregar(ja.letra)
                    for i in range(ja.contLetras):
                        if(ja.letrasIngresadas.getLetras()[i]==ja.letra):
                            print("Oops! Ya habias ingresado esa letra")
                            print("--------------------------------")
                            self.ingresarLetra(ja,palabraAleatoria)
                    print(ja.obtenerPalabraAdivinada(palabraAleatoria, ja.letrasIngresadas, ja.op))
                    print("--------------------------------")
                    ja.contLetras+=1
                else:
                    print("Caracter invalido!\n")
                    print("--------------------------------")
                    self.ingresarLetra(ja,palabraAleatoria)
            else:
                print("Debes ingresar una letra:")
        if(ja.seAdivinoPalabra(ja, ja.palabraAleatoria, ja.letrasIngresadas)):
            print("Felicidades, has ganado!\n")
            pja.munuOpciones(pja)
        else:
            if(ja.op.getIntentos()>0):
                self.ingresarLetra(ja,palabraAleatoria)
            else:
                print("Lo siento, te has quedado sin oportunidades para adivinar.")
                print("NO HAS ADIVINADO LA PALABRA.")
                print(f"La palabra secreta era: {self.palabraAleatoria.upper}")
                pja.munuOpciones()
            
    
    def obtenerLetrasDisponibles(self, li):
        letrasIngresadas=li.getLetras()
        letrasDisponibles='abcdefghijklmnopqrstuvwxyz'
        aux=[]
        for i in range(len(letrasDisponibles)):
            aux.append(ord(letrasDisponibles[i]))
        if(len(letrasIngresadas)>0):
            for i in range(len(aux)):
                x=aux[i]
                for j in range(len(letrasIngresadas)):
                    if(x==letrasIngresadas[j]):
                        aux[i]=32
        letrasDisponibles=''
        for i in range(len(aux)):
            if(aux[i]==32):
                letrasDisponibles=letrasDisponibles+"-"
            else:
                letrasDisponibles=letrasDisponibles+chr(aux[i])
        
        return letrasDisponibles
                
    def cargarPalabras(self):
        return Archivo.cargarPalabras(Archivo)
    
    def elegirPalabra(self,palabras):
        num=random.randint(0,(len(palabras))-1)
        self.palabraAleatoria=palabras[num]
        return self.palabraAleatoria
    
    def seAdivinoPalabra(self,palabraSecreta,letrasIngresadas):
        letras=letrasIngresadas.getLetras()
        palabraSecreta=palabraSecreta.replace(" ","")
        letras=self.ordenLetarsingresadas(letras)
        tamano=len(palabraSecreta)
        num=0
        if len(palabraSecreta)>0:
            for i in range(0,len(palabraSecreta)):
                x=palabraSecreta[i]
                for j in range(len(letras)):
                    if x==letras[x]:
                        num=num+1
        else:
            return False
        return num==tamano
                
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
        
        