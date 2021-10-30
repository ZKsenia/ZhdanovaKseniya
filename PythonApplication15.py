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

