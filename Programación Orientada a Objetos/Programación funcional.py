def suma(num1,num2):
    print("La suma es: ")
    print(num1+num2)
def multiplicacion(num1,num2):
    print("La multiplicación es: ")
    print(num1*num2)
def resta(num1,num2,):
    print("La resta es: ")
    print(num1-num2)
def division(num1,num2):
    print("La división es: ")
    print(num1/num2)
def menu():
    print("""Menu
        1-Suma
        2-Resta
        3-Multiplicación
        4-División""")
def resultado(op):
    if op == 1:
        suma(num1,num2)
    elif op == 2:
        resta(num1,num2)
    elif op == 3:
        multiplicacion(num1,num2)
    else:
        division(num1,num2)
if __name__ == '__main__':
    menu()
    op=int(input("Seleccione la operacion que desea usar: "))
    num1=int(input("Ingrese su primer numero: "))
    num2=int(input("Ingrese su segundo numero: "))
    resultado(op)