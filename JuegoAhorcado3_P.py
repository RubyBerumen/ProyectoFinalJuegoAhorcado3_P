'''
Created on 4 dic. 2020

@author: Ruby
'''

import os

class Archivo :
    
    def verificar(self):
        
        palabras=""
        archivo=open("palabras.txt","r")
        palabras=archivo.read()
        archivo.close()
        comas=0
        i=0
        
        for i in range(i,len(palabras)):
            if(palabras[i]==","):
                comas+=1
        if(comas>0):
            print(f"El archivo contiene {comas} palabras")
        elif(len(palabras)==0):
            print("El archivo esta vacio")
    
    def eliminar(self):
        if os.path.isfile("palabras.txt"):
            os.remove("palabras.txt")
            
        with open("palabras.txt", "w+") as f:
            pass
        print("Se ha eliminado el archivo")
        
