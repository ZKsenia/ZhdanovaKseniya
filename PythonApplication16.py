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
