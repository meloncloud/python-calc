class Persona:

    def cargar_datos (self,nom, edad, altura, DNI):
        self.nombre = nom
        self.edad = edad
        self.altura = altura
        self.DNI = DNI

    def imprimir(self):
        print('Su Nombre : ',self.nombre, 'y su edad es:', self.edad, 'anos', 'Su altura es:' , self.altura, 'DNI : ', self.DNI)

persona1=Persona()
persona1.cargar_datos("Pedro", "32", "1,70 mts", "27981816")
persona1.imprimir()
