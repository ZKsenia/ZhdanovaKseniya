#15.1 
print('Введите пять чисел для вычисления их третьей степени')
def PowerA3(a):
    return a*a*a 
a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())
a5=int(input())
b1=PowerA3(a1)
b2=PowerA3(a2)
b3=PowerA3(a3)
b4=PowerA3(a4)
b5=PowerA3(a5)
print('ответ =',b1,b2,b3,b4,b5,sep = ' ')

#15.2 
print('Введите два числа A и B')
def sign(x):
    if (x<0):
        return -1
    if (x==0):
        return 0
    if (x>0):
        return 1
a=int(input())
b=int(input())
print('ответ =', sign(a)+sign(b), sep=' ')

#15.3
print('Введите значения R1 и R2, R1>R2')
def RingS(r1,r2):
    return 3.14*(r1**2-r2**2)
r1=int(input())
r2=int(input())
if (r1>r2):
    print('ответ =',RingS(r1,r2),sep=' ')
else:
    print('Введите значения, удовлетворяюще условию')
print('Введите значения R1 и R2, R1>R2')
r3=int(input())
r4=int(input())
if (r3>r4):
    print('ответ =',RingS(r3,r4),sep=' ')
else:
    print('Введите значения, удовлетворяюще условию')
print('Введите значения R1 и R2, R1>R2')
r5=int(input())
r6=int(input())
if (r5>r6):
    print('ответ =',RingS(r5,r6),sep=' ')
else:
    print('Введите значения, удовлетворяюще условию')
    
#15.4
print('Введите ненулевые координаты точки')
def Quarter(x, y) :
    if ((x>0) and (y>0)):
        return ('I')
    elif ((x<0) and (y>0)):
        return('II')
    elif ((x<0) and (y<0)):
        return ('III')
    elif ((x>0) and (y<0)):
        return ('IV')
x1=int(input())
y1=int(input())
if ((x1!=0) and (y1!=0)):
    print('ответ =',Quarter(x1,y1),sep=' ')
else:
    print('Введённые координаты не удовлетворяют условию')
print('Введите ненулевые координаты точки')
x2=int(input())
y2=int(input())
if ((x2!=0) and (y2!=0)):
    print('ответ =',Quarter(x2,y2),sep=' ')
else:
    print('Введённые координаты не удовлетворяют условию')
print('Введите ненулевые координаты точки')
x3=int(input())
y3=int(input())
if ((x3!=0) and (y3!=0)):
    print('ответ =',Quarter(x3,y3),sep=' ')
else:
    print('Введённые координаты не удовлетворяют условию')
 
#15.5
print('Введите число')
def Fact2(n):
    x = 1
    if (n%2 == 0):
        y = 2
        while y <= n:
            x = x * y
            y = y + 2 
        return x
    else:
        y = 3
        while y <= n:
            x = x * y
            y = y + 2
        return x
n=int(input())
print('ответ =',Fact2(n),sep=' ')
