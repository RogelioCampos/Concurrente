#_*_ coding:utf-8 _*_
import shutil
from sys import exit

class Archivo:
    def __init__(self,nombre):
        try:
            self.f = open(nombre,'r')
            self.nombre = nombre
        except:
            print("No se puede abrir el archivo {}",nombre)
            exit()

    def muestra(self):
        i=1
        for linea in self.f.readlines():
            print("{:3}{:}".format(i ,linea),end=" ")
            i += 1
            self.f.seek(0)

    def cuentaVocales(self):
        def vocales(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set ("aeiouáéíóúAEIOUÁÉÍÓÚ"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f.readlines():
            contador += vocales(linea)
            self.f.seek(0)
        return contador

    def cuentaConsonantes(self):
        def consonantes(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set ("bcdfghjklmnñpqrstuvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f.readlines():
            contador += consonantes(linea)
            self.f.seek(0)
        return contador

    def cuentaSignos(self):
        def signos(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set (".,;:¿?¡!-()"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f.readlines():
            contador += signos(linea)
            self.f.seek(0)
        return contador

    def cuentaEspacios(self):
        def espacios(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set (" "):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f.readlines():
            contador += espacios(linea)
            self.f.seek(0)
        return contador
    
    def cuentaPalabras(self):
        def palabras(s):
            if len(s) > 0:
                contador = 1
            else:
                contador = 0
            for i in range((len(s)-1)):
                if s[i] in set (" "):
                    if s[i+1] in set ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú¡¿\"("):
                        contador += 1
            return contador
        contador = 0
        for linea in self.f.readlines():
            contador += palabras(linea)
            self.f.seek(0)
        return contador

    def cuentaLineas(self):
        contador = 0
        for linea in self.f.readlines():
            contador += 1
            self.f.seek(0)
        return contador

    def cuentaMayusculas(self):
        def mayusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f.readlines():
            contador += mayusculas(linea)
            self.f.seek(0)
        return contador

    def cuentaMinusculas(self):
        def minusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set ("abcdefghijklmnñopqrstuvwxyzáéíóú"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f.readlines():
            contador += minusculas(linea)
            self.f.seek(0)
        return contador

    def copiaArchivo(self,nombre):
        try:
            shutil.copy(nombre, 'copia.txt')
            print("\nArchivo copiado a copia.txt")
        except:
            print("\nNo se ha podido copiar")

    def convierteMayusculas(self):
        for linea in self.f.readlines():
            print(linea.upper(),end=" ")
            self.f.seek(0)
    
    def convierteMinusculas(self):
        for linea in self.f.readlines():
            print(linea.lower(),end=" ")
            self.f.seek(0)

    
    


nomb = input("Nombre del archivo: ")
archivo = Archivo(nomb)
archivo.muestra()
vocales = archivo.cuentaVocales()
print("\nHay", vocales, "vocales")
consonantes = archivo.cuentaConsonantes()
print("Hay", consonantes, "consonantes")
signos = archivo.cuentaSignos()
print("Hay", signos, "signos")
espacios = archivo.cuentaEspacios()
print("Hay", espacios, "espacios")
palabras = archivo.cuentaPalabras()
print("Hay", palabras, "palabras")
lineas = archivo.cuentaLineas()
print("Hay", lineas, "lineas")
mayusculas = archivo.cuentaMayusculas()
print("Hay", mayusculas, "mayusculas")
minusculas = archivo.cuentaMinusculas()
print("Hay", minusculas, "minusculas")
archivo.copiaArchivo(nomb)
print("\nTexto en mayúsculas:")
archivo.convierteMayusculas()
print("\nTexto en minúsculas:")
archivo.convierteMinusculas()
