
while True:
    try:
        a = int(input('ingrese un nro : ' ))
        b = int(input(' ingrese otro nro: '))
        sum = a+b
        print('la suma es :', sum,)
        break
    except:
        print ('El dato ingresado no es entero')
        pass