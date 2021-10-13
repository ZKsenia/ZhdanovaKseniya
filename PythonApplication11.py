#11.1 
A = int(input())
B = int(input())
if (A==B):
    A = 0
    B = 0
    print(A,B)
else:
    A = max(A,B)
    B = max(A,B)
    print(A,B)
#11.2
a = int(input())
b = int(input())
c = int(input())
print(max(a,b,c) + (a+b+c-min(a,b,c)-max(a,b,c)))
#11.3
a = int(input())
b = int(input())
c = int(input())
ab = abs(a-b)
ac = abs(a-c)
if ab<ac:
    print('B, расстояние равно', ab)
elif ac<ab:
    print('C, расстояние равно', ac)
#11.4
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
n = int(input())
if ((n>0) and (n%2==0)):
    print('Положительное чётное число')
if ((n>0) and (n%2!=0)):
    print('Положительное нечётное число')
if ((n<0) and (n%2==0)):
    print('Отрицательное чётное число')
if ((n<0) and (n%2!=0)):
    print('Отрицательное нечётное число')
else:
    print('Нулевое число')
#11.6 
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
