#14.1 
print('Введите значения A и B, A<B')
a = int(input())
b = int(input())
if (a<b):
    for i in range(a,b+1):
        for n in range(1,i+1):
            print('ответ =', i, sep=' ')
else:
    print('Введите значениия, удовлетворяющие условию')
#14.2
print('Введите значения A и B, A>B')
a = int(input())
b = int(input())
if (a>b):
    while (a-b>=0):
        a = a-b
    print('ответ =', a, sep = ' ')
else:
    print('Введите значениия, удовлетворяющие условию')
#14.3
print('Введите значение N>1')
n=int(input())
if (n>1):
    x=0
    k=0
    while (x<n):
        k+=1
        x+=k
    print('значение k =',k,'сумма =',x, sep=' ')
else:
    print('Введите значение, удовлетворяющее условию')
#14.4 
print('Введите значение 0<P<25')
p=int(input())
if ((p>0) and (p<25)):
    s=1000
    k=0 
    while (s<1100):
        k+=1 
        s=s+(s*p//100)
    print('количество месяцев, значение k =',k,'итоговый размер вклада,значение s =',s, sep=' ')
else:
    print('Введите значение, удовлетворяющее условию')
#14.5 
print('Введите значения A и B')
a = int(input())
b = int(input())
while (a!=b):
    if a>b:
        a=a-b
    else:
        b=b-a 
print('ответ =', a, sep=' ')
#14.6 
print('Введите значение N>1')
n=int(input())
if (n>1):
    f1=1
    f2=1
    f=0 
    k=2 
    while(f<n):
        k+=1 
        f=f1+f2 
        f2=f1 
        f1=f 
    print('ответ =', k, sep=' ')
else:
    print('Введите значение, удовлетворяющее условию')
