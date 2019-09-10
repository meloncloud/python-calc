class Persona:

    def __init__(self,name, age):
        self.name = name
        self.age = age
        

    def show (self):
         print('your name is : ',self.name, ', and your age is :', self.age, 'years old' )


class Persona2(Persona):

    def __init__(self,name, age,height):
        self.name = name
        self.age = age
        self.height = height
        

    def show (self):
         print('your name is : ',self.name, ', and your age is :', self.age, 'years old' )



persona1=Persona("Pedro", "32")
persona1.show()

persona2=Persona2("Pedro", "32",23)
persona2.show()



	 	


