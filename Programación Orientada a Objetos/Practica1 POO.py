class Persona (object):
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return self.nombre, str(self.edad)

class Empleado(Persona):
        def __init__(self, nombre, edad, sueldo_bruto):
            Persona.__init__(self, nombre, edad)
            self.sueldo_bruto = sueldo_bruto
        def mostrar(self):
            return self.nombre,self.edad,self.sueldo_bruto
        def calcular_salario_neto(self):
            sueldo = self.sueldo_bruto - self.sueldo_bruto * 0.04
            return sueldo

class Cliente(Persona):
        def __init__(self,nombre,edad,nombre_empresa,telefono_de_contacto):
            Persona.__init__(self,nombre,edad)
            self.nombre_empresa = nombre_empresa
            self.telefono_de_contacto = telefono_de_contacto
        def mostrar(self):
            return self.nombre, self.edad, self.nombre_empresa, self.telefono_de_contacto

class Directivo(Empleado):
    def __init__(self,nombre,edad,sueldo_bruto,categoria):
        Empleado.__init__(self,nombre,edad,sueldo_bruto)
        self.categoria=categoria
    def mostrar(self):
        return self.nombre, self.edad, self.sueldo_bruto, self.categoria

class Empresa(Empleado,Cliente):
    def __init__(self,nombre,edad,sueldo_bruto,nombre_empresa,telefono_de_contacto,Nombre):
        Empleado.__init__(self,nombre,edad, sueldo_bruto)
        Cliente.__init__(self,nombre,edad,nombre_empresa,telefono_de_contacto)
        self.Nombre = Nombre

persona1=Persona("Juan",12)
empleado1=Empleado("Juan",12,1200)
Cliente1=Cliente("Jose",40,"Impresiones Jose",2714035932)
Directivo1=Directivo("Jesus",25,35000,"Gerente")

print(persona1.mostrar())
print(empleado1.mostrar(), empleado1.calcular_salario_neto())
print(Cliente1.mostrar())
print(Directivo1.mostrar())