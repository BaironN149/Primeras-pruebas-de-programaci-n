"""
(1) suma
(2) resta
(3) multiplicacion
(4) division
"""
def calculadora(num1 , num2 , opcion):
    print("bienvenido a mi primera calculadora" .center(50, '-'))
    if opcion == 1:
        print(F"El resultado de la suma de {num1} y {num2} es: {num1 + num2}")
    elif opcion == 2:
        print(F"El resultado de la resta de {num1} y {num2} es: {num1 - num2}")
    elif opcion == 3:
        print(F"El resultado de la multiplicación de {num1} y {num2} es: {num1 * num2}")
    elif opcion == 4:
        print(F"El resultado de la divición de {num1} y {num2} es: {num1 / num2}")
    else:
        print("Te equivocaste de número bro")
variable1= float(input("introduzca el primer valor"))
variable2= float(input("introduzca el segundo valor"))
Operacion= float(input("ingrese la operación que desea"))
calculadora(variable1,variable2,Operacion)
