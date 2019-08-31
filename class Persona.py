class Persona:

    def cargar_datos (self,nom, edad):
        self.nombre = nom
        self.edad = edad

    def imprimir(self):
        print('Su Nombre : ',self.nombre, 'y su edad es:', self.edad, 'anos')

persona1=Persona()
persona1.cargar_datos("Pedro", "32")
persona1.imprimir()
