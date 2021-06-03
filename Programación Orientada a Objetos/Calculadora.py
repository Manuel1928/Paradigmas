class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        suma =self.num1+ self.num2
        return  suma
    def resta (self):
        resta = self.num1 - self.num2
        return  resta
    def multiplicacion (self):
        mul= self.num1*self.num2
        return  mul
    def division(self):
        div=self.num1 / self.num2
        return  div
if __name__ == '__main__':
    menu="""
Menu
1-Suma
2-Resta
3-Multiplicación
4-División
5- Modulo
"""
    print(menu)
    op=int(input("Seleccione la operación que desea hacer: "))
    n1=int(input("ingrese su numero: "))
    n2=int(input("ingrese su numero: "))
    cal =Calculadora(n1,n2)
    pop =True
    if op == 1:
        s = cal.suma()
        while pop == True:
            print(f"La suma es: {s}")
            a = str(input("Desea sumar un numero mas? (Y,N)"))
            if a == "Y":
                d=int(input("Ingresa el numero: "))
                s=s+d
                pop = True
            else:
                pop = False
    elif op == 2:
        f = cal.resta()
        while pop==True:
            print(f"La resta es: {f}")
            a = str(input("Desea restar un numero mas? (Y,N)"))
            if a == "Y":
                d=int(input("Ingresa el numero: "))
                f=f-d
                pop = True
            else:
                pop = False
    elif op == 3:
        g = cal.multiplicacion()
        while pop == True:
            print(f"La multiplicación es: {g}")
            a = str(input("Desea multiplicar un numero mas? (Y,N)"))
            if a == "Y":
                d=int(input("Ingresa el numero: "))
                g=g*d
                pop = True
            else:
                pop = False
    elif op == 4:
        h=cal.division()
        print(f"La divición es: {h}")
    elif op == 5:
        j=cal.Modulo()
        print(f"El resultado es: {j}")