#11.1 
print('1)Введите значения двух переменных А и В')
A = int(input())
B = int(input())
if (A==B):
    A = 0
    B = 0
    print('ответ =',A,B, sep = ' ')
else:
    A = max(A,B)
    B = max(A,B)
    print('ответ =',A,B, sep = ' ')
#11.2
print('2)Введите три числа a,b,c')
a = int(input())
b = int(input())
c = int(input())
print('ответ =',max(a,b,c) + (a+b+c-min(a,b,c)-max(a,b,c)),sep = ' ')
#11.3
print('3)Введите координаты точек a,b,c')
xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
xc = int(input())
yc = int(input())
ab = ((xb-xa)**2 + (yb-ya)**2)**0.5
ac = ((xc-xa)**2 + (yc-ya)**2)**0.5
if ab<ac:
    print('B, расстояние равно', ab)
elif ac<ab:
    print('C, расстояние равно', ac)
#11.4
print('4)Введите координаты точки')
x = int(input())
y = int(input())
if ((x!=0) and (y!=0)):
    if ((x>0) and (y>0)):
        print('I')
    elif ((x<0) and (y>0)):
        print('II')
    elif ((x<0) and (y<0)):
        print('III')
    elif ((x>0) and (y<0)):
        print('IV')
else:
    print('Введённые координаты не удовлетворяют условию')
#11.5
print('5)Введите число')
n = int(input())
if (n==0):
    print('Нулевое число')
else:
    if ((n>0) and (n%2==0)):
        print('Положительное чётное число')
    elif ((n>0) and (n%2!=0)):
        print('Положительное нечётное число')
    elif ((n<0) and (n%2==0)):
        print('Отрицательное чётное число')
    elif ((n<0) and (n%2!=0)):
        print('Отрицательное нечётное число')
#11.6 
print('6)Введите число')
n = int(input())
if n in range(1,999+1):
    if ((n>=1) and (n<=9) and (n%2==0)):
        print('Однозначное чётное число')
    elif ((n>=1) and (n<=9) and (n%2!=0)):
        print('Однозначное нечётное число')
    elif ((n>=10) and (n<=99) and (n%2==0)):
        print('Двузначное чётное число')
    elif ((n>=10) and (n<=99) and (n%2!=0)):
        print('Двузначное нечётное число')
    elif ((n>=100) and (n<=999) and (n%2==0)):
        print('Трёхзначное чётное число')
    elif ((n>=100) and (n<=999) and (n%2!=0)):
        print('Трёхзначное нечётное число')
else:
    print('Введите число, удовлетворяющее условию')
