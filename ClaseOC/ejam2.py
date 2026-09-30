par=[]
impar=[]
try:
    while True:
        num= int(input("ingrese un numero"))
        if num%2==0:
            par.append(num) 
        elif num%2==1:
            impar.append(num)
except ValueError:
        print(par)
        print(impar)