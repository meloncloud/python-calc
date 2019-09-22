class Sumadora:

   def __init__(self, num1 , num2):
   	    self.num1 = num1
   	    self.num2 = num2

   def sum (self):
   	      Suma = self.num1 + self.num2
   	      return Suma

a = Sumadora (2 , 4)
print (a)
