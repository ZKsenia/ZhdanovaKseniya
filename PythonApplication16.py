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
m=[a]*n
if (n>1):
    for i in range(1,len(m)):
        m[i]=a*d
        a = a*d
    print('ответ =',m, sep = ' ')
else:
    print('Ввеите значение, удовлетворяющее условию')
    
#16.3
print('Введите N, N>2')
n = int(input())
print('Введите A')
a = int(input())
print('Введите B')
b = int(input())
m=[a,b]
if (n>2):
    for i in range(2,n):
        k = sum(m)
        m.append(k)
    print('ответ =',m, sep = ' ')
else:
    print('Ввеите значение, удовлетворяющее условию')
    
#16.4
print('Введите N')
n = int(input())
k=n//2
a=[i+1 for i in range(n)]
m=[]
for i in range(0,k):
    m.append(a[i])
    m.append(a[n-i-1])
if (2*k < n):
    m.append(a[k])
print('ответ =', m, sep=' ')
