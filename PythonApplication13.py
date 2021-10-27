#13.1
print('Введите цену 1 кг конфет')
n = int(input())
for i in range (1,10+1):
    ans = i*0.1*n
    print(i*0.1,'кг',': ',ans, sep = ' ')
    
#13.2
print('Введите число N')
n = int(input())
if (n>0):
    x = 1
    for i in range(1,n+1):
        x = x*(1+0.1*i)
    print('ответ =',x ,sep = ' ')
else:
  print('Введите число N, удовлетворяющее услвовию')
  
#13.3 
print('Введите число N')
n = int(input())
if (n>0):
    x = 0
    for i in range(1,n+1):
        x=x+(2*i-1)
        print('результат =',x,sep = ' ')
else:
  print('Введите число N, удовлетворяющее услвовию')
 
#13.4 
print('Введите числа A и N')
a = int(input())
n = int(input())
if (n>0):
    x = 1
    st=1
    for i in range(1,n+1):
        st=st*a
        x = x+st
    print('ответ =',x ,sep = ' ')
else:
  print('Введите число N, удовлетворяющее услвовию')
  
#13.5
print('Введите числа A и N')
a = int(input())
n = int(input())
if (n>0):
    x = 1
    y=1
    for i in range(1,n+1):
        y=(-1)*y*a
        x = x+y
    print('ответ =',x ,sep = ' ')
else:
  print('Введите число N, удовлетворяющее услвовию')
