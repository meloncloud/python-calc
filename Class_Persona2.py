class Persona:

    def __init__(self,name, age):
        self.name = name
        self.age = age
        

    def show (self):
         print('your name is : ',self.name, ', and your age is :', self.age, 'years old' )

persona1=Persona()
persona1.cargar_datos("Pedro", "32", "1,70 mts", "27981816")
persona1.show()

class Persona2(Persona):
	
	 def actualizar(self,apelli):
	 	self.apellido = apelli
	 	print('your name is : ',self.name, ', your age is :', self.age, 'years old' , 'your surname is:' self.apellido )


Persona2.actualizar()