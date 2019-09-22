class Sumadora:

    def __init__(self,val1, val2):
        self.val1 = val1
        self.val2 = val2
        

    def add (self):
         print(self.val1 + self.val2)



persona1=Sumadora(10, 32)
persona1.add()
