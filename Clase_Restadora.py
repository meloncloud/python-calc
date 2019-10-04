class Restadora:
   def __init__(self, num1 , num2):
   	    self.num1 = num1
   	    self.num2 = num2

   def rest (self):  
       if self.num2 != 0:     
   	    print( self.num1 - self.num2)
       else:
          print( ' ingrese un numero mayor que cero')
          
#resta = Restadora(4,5)
#resta .rest()