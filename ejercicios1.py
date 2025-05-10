import math as m 
import pandas as pd

"""
nombre = input("cuale es tu nombre?")
edad = int(input("cual es tu edad?"))  #el int transforma en entero el valor del input que es texto

print(f"la edad de la persona es {nombre} \n y la edad es {edad}") 
"""
#calculadora de IMC
# IMC = Peso (kg) / (estatura (m))**2
""" 
peso = float(input("cual es el peso ?:"))

estatura = float(input("cual es tu estatura en metros?:"))

IMC = peso / (estatura**2)
print(f"mi indice de masa corporal es ", IMC)
print(f"mi indice de masa corporal es: {IMC:.2f} ") #genera 2 decimales este sistema, el f es de float

 """

#calculadora de descuento

#descuento = precio original * (porcentaje de descuencto/100)
""" 
precio_original = int(input("cal es el precio? "))
descuento = float(input("cual es el porcentaje de descuento?"))

precio_con_descuencto = precio_original * (descuento/100)

precio_final = precio_original - precio_con_descuencto

print(f"el precio final con descuencto es : {precio_final}")
 """

#formula de promedio
#promedio de notas
#x= (n1+n2+n3)/ n
""" 
nota1 = float(input("ingresa nota1 "))
nota2 = float(input("ingresa nota2 "))
nota3 = float(input("ingresa nota3 "))

promedio = ( nota1 + nota2 + nota3) / 3
print(f"el promedio de notas es  {promedio:.1f}")
 """

# area de un triangulo

#area = (sqr(3)/4)*lado**2

""" lado = float(input("longitud de l lado del triangulo"))
area = (m.sqrt(3))/4 * (lado**2)
print(f"el area del triangulo es : {area:.2f}") """

#area de un anillo
# area = PI*(R**2-r**2)

""" R = float(input("radio mayor"))
r = float(input("radio menor"))
area = m.pi * (R**2 - r**2)
print(f"el area de anillo es : {area:.3f}") """

df = pd.read_csv('cronograma.csv')
print("las priemras lineas 5 filas en mi csv")
print(df.head()) 




lista = ["auto", "rt2345", "rojo"]

