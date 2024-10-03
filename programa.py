print('programa que determina el tipo de triángulo por los lados')
x=float(input('introduzca valor de el primer lado: '))
y=float(input('introduzca valor de el segundo lado: '))
z=float(input('introduzca valor de el tercer lado: '))
if x+y>z and x+z>y and y+z>x:
    if x==y==z:
        print('es un triángulo equilátero')
    elif x==y or x==z or y==z:
        print('es un triángulo isósceles')
    elif x!=y!=z:
        print('es un triángulo escaleno')
else:
    print('no es un triángulo valido')