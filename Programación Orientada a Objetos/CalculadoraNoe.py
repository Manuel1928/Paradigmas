class calculadora():
    num1= 0
    num2= 0
    def _init_(self,num1,num2):
        self.num1= float(num1)
        self.num2= float(num2)
    def sum(self):
        suma = self.num1+self.num2
        print("el resultado de la suma es: ", suma)
    def res(self):
        resta = self.num1-self.num2
        print("el resultado de la resta es: ", resta)
    def multi(self):
        multiplicacion = self.num1*self.num2
        print("el resultado de la multiplicación es: ", multiplicacion)
    def dvr(self):
        divicion = self.num1/self.num2
        print("el resultado de la divición es: ", divicion)
num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")
calculadora = calculadora(num1,num2)
calculadora.sum()
calculadora.multi()
calculadora.res()
calculadora.dvr()
