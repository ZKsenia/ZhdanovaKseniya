#8.1
n = int(input())
klv_kb = n//1024
print(klv_kb)
#8.2
a = int(input())
b = int(input())
if (a>b):
    klv = a//b
    print(klv)
else:
    print('Введите величины так, чтобы А было больше В')
#8.3
a = int(input())
b = int(input())
if (a>b):
    klv = a%b
    print(klv)
else:
    print('Введите величины так, чтобы А было больше В')
#8.4
n = int(input())
a = n//10
b = n%10
print(b,a,sep='')
#8.5
n = int(input())
a = n//100
b = (n//10)%10
c = n%10
print(b,c,a,sep='')

