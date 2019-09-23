class Sumadora:

   def __init__(self, num1 , num2):
   	    self.num1 = num1 
   	    self.num2 = num2


   def sum (self):
   	    print(self.num1 + self.num2)

   def AbsSum (self):
   	      
   	      if self.num2 < 0:
   	      	self.num2 = -self.num2
   	      	print( self.num1 + self.num2)

   	      print( self.num1 + self.num2)

   


suma = Sumadora(2,2)
suma.sum()
suma.AbsSum()

