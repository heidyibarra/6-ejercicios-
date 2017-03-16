print("Numeros Flotantes ")

a=4.56
b=198.1
c=3.1416
print(a+b+c)
# los numeros flotantes son numeros decimales 
print("----------------------------------------------------------------------------")

print("Area De Un Triangulo")

base=12
altura=34
area=(base*altura)/2
print(area)
# la ecuacion que nos proporciona el valos del AREA es base por altura sobre dos 
print("----------------------------------------------------------------------------")

print("Hipotenusa")

import math
lado1=13
lado2=26
c=lado1*lado1+lado2*lado2
print"El Valor De La Hipotenusa Es ",math.sqrt(c)
#para hallar la hipotenusa  es importante saber que esta misma es la parte as larga de un triangulo  de 90° (grados)
print("----------------------------------------------------------------------------")
print("Numeros Par")
cadena = "a,,c,s,2,4,f,8,1112"
contador = 0
for  p in cadena :
    try:
        h = int(p)
        j = h % 2 
        if(j == 0):  
            contador = contador + 1
    except:
        c = 1
print(contador) 
#Generalmente los numero pares son divisibles completamente en dos y su reciduo siempre va a ser cero
print("----------------------------------------------------------------------------")

print("Ejercicio Arbol")


cadena="arbolarbol"
print cadena.count("arbol")















