#16.1 
print('Введите N, N>0')
n = int(input())
a=[]
if (n>0):
    for i in range(1,n+1):
        a.append(i*2-1)
    print('ответ =',a, sep = ' ')
else:
    print('Ввеите значение, удовлетворяющее условию')
    
#16.2
print('Введите N, N>1')
n = int(input())
print('Введите A')
a = int(input())
print('Введите D')
d = int(input())
m=[]
if (n>1):
    for i in range(1,n+1):
        m.append(a*d)
        a = a*d
    print('ответ =',m, sep = ' ')
else:
    print('Ввеите значение, удовлетворяющее условию')
