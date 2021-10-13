
#9.1
n = int(input())
klv = n % 60
print(klv)
#9.2
k = int(input())
if k in range(1,365+1):
    if (k%7) == 0:
        print('Воскресенье, номер 0')
    elif (k%7) == 1:
        print('Понедельник, номер 1')
    elif (k%7) == 2:
        print('Вторник, номер 2')
    elif (k%7) == 3:
        print('Среда, номер 3')
    elif (k%7) == 4:
        print('Четверг, номер 4')
    elif (k%7) == 5:
        print('Пятница, номер 5')
    elif (k%7) == 6:
        print('Суббота, номер 6')
else:
    print('Значение k не удовлетворяет диапозону')
#9.3
k = int(input())
n = int(input())
if (k in range(1,365+1) and n in range(1,7+1)):
    print('Номер дня недели =', ((k+n-2)%7)+1)
else:
    print('Значение k или n не удовлетворяет диапозону')
#9.4
A = int(input())
B = int(input())
C = int(input())
klv_kv = (A//C) * (B//C)
svob_mesto = (A*B) - (klv_kv**2)
print(klv_kv,svob_mesto)
#9.5 
n = int(input())
result = ((n-1)//100) + 1
print(result)
