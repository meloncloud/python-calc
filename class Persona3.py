class Persona:

    def __init__ (self,name, age):
        self.name = name
        self.age = age
        

    def __str__ (self):
        return('your name is : ',self.name, ', and your age is :', self.age, 'years old' )

persona1=Persona("Pedro", "32")
persona1.__str__()