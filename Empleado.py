class Persona:
    def __init__(self, Nombre, edad): 
     self.Nombre = Nombre
     self.edad = edad 

    def show (self):
         print('your name is : ',self.Nombre, ', and your age is :', self.edad, 'years old' )

class Empleado(Persona):

    def __init__(self, Nombre, edad, DNI, Domicilio , Cargo):
        self.DNI = DNI
        self.Domicilio = Domicilio 
        self.Cargo = Cargo 

        #falto iniciar
        self.Nombre = Nombre
        self.edad = edad 

    def show (self):
         print('Bienvenido : ' , self.Nombre, ', your age is :', self.edad, 'years old' ,'DNI is : ' , self.DNI, 'Domicilio : ,' , self.Domicilio, 'Cargo : ,' , self.Cargo)


Persona1 = Persona("Damien","25") 
Persona1.show()
Persona2 = Empleado("Juan", "34","27982828","santa fe 3222", "Profesor")
Persona2.show() 
