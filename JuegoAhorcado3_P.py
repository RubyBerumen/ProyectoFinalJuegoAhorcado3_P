'''
Created on 4 dic. 2020

@author: Ruby
'''

class Archivo :
    
    def verificar(self):
        
        ruta='palabras.txt'
        palabras=""
        archivo=open(ruta,"r")
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
        
        
        
