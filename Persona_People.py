class Persona:

    def data (self,name,surname):
        self.name= name
        self.surname = surname
        

    def show(self):
        print('your name is : ',self.name, 'and your surname is:', self.surname)

persona1=Persona()
persona1.data("Pedro", "Lopez")
persona1.show()