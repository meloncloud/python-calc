class Persona:

    def cargar_datos (self,nom, edad, altura):
        self.nombre = nom
        self.edad = edad
        self.altura = altura

    def imprimir(self):
        print('Su Nombre : ',self.nombre, 'y su edad es:', self.edad, 'anos', 'Su altura es:' , self.altura)

persona1=Persona()
persona1.cargar_datos("Pedro", "32", "1,70 mts")
persona1.imprimir()
