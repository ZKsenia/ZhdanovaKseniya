#12.1 
n = int(input())
m = int(input())
if n in range (1,31+1):
    if (n==1):
        n1 = 'первое'
    elif (n==2):
        n1 = 'второе'
    elif (n==3):
        n1 = 'третье'
    elif (n==4):
        n1 = 'четвертое'
    elif (n==5):
        n1 = 'пятое'
    elif (n==6):
        n1 = 'шестое'
    elif (n==7):
        n1 = 'седьмое'
    elif (n==8):
        n1 = 'восьмое'
    elif (n==9):
        n1 = 'девятое'
    elif (n==10):
        n1 = 'десятое'
    elif (n==11):
        n1 = 'одиннадцатое'
    elif (n==12):
        n1 = 'двенадцатое'
    elif (n==13):
        n1 = 'тринадцатое'
    elif (n==14):
        n1 = 'четырнадцатое'
    elif (n==15):
        n1 = 'пятнадцатое'
    elif (n==16):
        n1 = 'шестнадцатое'
    elif (n==17):
        n1 = 'семнадцатое'
    elif (n==18):
        n1 = 'восемнадцатое'
    elif (n==19):
        n1 = 'девятнадцатое'
    elif (n==20):
        n1 = 'двадцатое'
    elif (n==21):
        n1 = 'двадцать первое'
    elif (n==22):
        n1 = 'двадцать второе'
    elif (n==23):
        n1 = 'двадцать третье'
    elif (n==24):
        n1 = 'двадцать четвертое'
    elif (n==25):
        n1 = 'двадцать пятое'
    elif (n==26):
        n1 = 'двадцать шестое'
    elif (n==27):
        n1 = 'двадцать седьмое'
    elif (n==28):
        n1 = 'двадцать восьмое'
    elif (n==29):
        n1 = 'двадцать девятое'
    elif (n==30):
        n1 = 'тридцатое'
    elif (n==31):
        n1 = 'тридцать первое'
else:
    print('Введите значение, удовлетворяющее дипозону')
if m in range (1,12+1):
    if (m==1):
        m1 = 'января'
    elif (m==2):
        m1 = 'февраля'
    elif (m==3):
        m1 = 'марта'
    elif (m==4):
        m1 = 'апреля'
    elif (m==5):
        m1 = 'мая'
    elif (m==6):
        m1 = 'июня'
    elif (m==7):
        m1 = 'июля'
    elif (m==8):
        m1 = 'августа'
    elif (m==9):
        m1 = 'сентября'
    elif (m==10):
        m1 = 'октября'
    elif (m==11):
        m1 = 'ноября'
    elif (m==12):
        m1 = 'декабря'
else:
    print('Введите значение, удовлетворяющее дипозону')
print (n1,m1,sep=' ')
#12.2 
C = input()
N = int(input())
if (C=='С'):
    if (N==0):
        print ('Север')
    elif (N==1):
        print('Запад')
    elif (N==-1):
        print ('Восток')
elif (C == 'З'):
    if (N==0):
        print ('Запад')
    elif (N==1):
        print('Юг')
    elif (N==-1):
        print ('Север')
elif (C == 'Ю'):
    if (N==0):
        print ('Юг')
    elif (N==1):
        print('Запад')
    elif (N==-1):
        print ('Восток')
elif (C == 'В'):
    if (N==0):
        print ('Восток')
    elif (N==1):
        print('Юг')
    elif (N==-1):
        print ('Север')
else:
    print('Введите допустимые значения')
#12.3 
n = int(input())
a = 'учебных заданий'
b = 'учебное задание'
if n in range (10,40+1):
    if (n==10):
        print ('десять',a,sep =' ')
    elif (n==11):
        print ('одиннадцать',a,sep =' ')
    elif (n==12):
        print ('двенадцать',a,sep =' ')
    elif (n==13):
        print ('тринадцать',a,sep =' ')
    elif (n==14):
        print ('четырнадцать',a,sep =' ')
    elif (n==15):
        print ('пятнадцать',a,sep =' ')
    elif (n==16):
        print ('шестнадцать',a,sep =' ')
    elif (n==17):
        print ('семнадцать',a,sep =' ')
    elif (n==18):
        print ('восемнадцать',a,sep =' ')
    elif (n==19):
        print ('девятнадцать',a,sep =' ')
    elif (n==20):
        print ('двадцать',a,sep =' ')
    elif (n==21):
        print ('двадцать одно',b,sep =' ')
    elif (n==22):
        print ('двадцать два',a,sep =' ')
    elif (n==23):
        print ('двадцать три',a,sep =' ')
    elif (n==24):
        print ('двадцать четыре',a,sep =' ')
    elif (n==25):
        print ('двадцать пять',a,sep =' ')
    elif (n==26):
        print ('двадцать шесть',a,sep =' ')
    elif (n==27):
        print ('двадцать семь',a,sep =' ')
    elif (n==28):
        print ('двадцать восемь',a,sep =' ')
    elif (n==29):
        print ('двадцать девять',a,sep =' ')
    elif (n==30):
        print ('тридцать',a,sep =' ')
    elif (n==31):
        print ('тридцать одно',b,sep =' ')
    elif (n==32):
        print ('тридцать два',a,sep =' ')
    elif (n==33):
        print ('тридцать три',a,sep =' ')
    elif (n==34):
        print ('тридцать четыре',a,sep =' ')
    elif (n==35):
        print ('тридцать пять',a,sep =' ')
    elif (n==36):
        print ('тридцать шесть',a,sep =' ')
    elif (n==37):
        print ('тридцать семь',a,sep =' ')
    elif (n==38):
        print ('тридцать восемь',a,sep =' ')
    elif (n==39):
        print ('тридцать девять',a,sep =' ')
    elif (n==40):
        print ('сорок',a,sep =' ')
else:
    print('Введите значение, удовлетворяющее диапозону')
n = int(input())
a = n%10
b = (n//10)%10
c = n//100
c.1 = 'сто'
c.2 = 'двести'
c.3 = 'триста'
c.4 = 'четыреста'
c.5 = 'пятьсот'
c.6 = 'шестьсот'
c.7 = 'семьсот'
c.8 = 'восемьсот'
c.9 = 'девятьсот'
b.10 = 'десять'
b.11 = 'одиннадцать'
b.12 = 'двенадцать'
b.13 = 'тринадцать'
b.14 = 'четырнадцать'
b.15 = 'пятнадцать'
b.16 = 'шестнадцать'
b.17 = 'семнадцать'
b.18 = 'восемнадцать'
b.19 = 'девятнадцать'
b.20 = 'двадцать'
b.30 = 'тридцать'
b.40 = 'сорок'
b.50 = 'пятьдесят'
b.60 = 'шестьдесят'
b.70 = 'семьдесят'
b.80 = 'восемьдесят'
b.90 = 'девяносто'
a.1 = 'один'
a.2 = 'два'
a.3 = 'три'
a.4 = 'четыре'
a.5 = 'пять'
a.6 = 'шесть'
a.7 = 'семь'
a.8 = 'восемь'
a.9 = 'девять'
if n in range (100,999+1):
    if (a == 1):
        if (n%100 == 11):
            print (c.1,b.11,sep=' ')
        elif (n%100 == 12):
            print (c.1,b.12,sep=' ')
        elif (n%100 == 13):
            print (c.1,b.13,sep=' ')
        elif (n%100 == 14):
            print (c.1,b.14,sep=' ')
        elif (n%100 == 15):
            print (c.1,b.15,sep=' ')
        elif (n%100 == 16):
            print (c.1,b.16,sep=' ')
        elif (n%100 == 17):
            print (c.1,b.17,sep=' ')
        elif (n%100 == 18):
            print (c.1,b.18,sep=' ')
        elif (n%100 == 19):
            print (c.1,b.19,sep=' ')
        elif (n%100 == 10):
            print (c.1,b.10,sep=' ')
        elif (n%100 == 20):
            print (c.1,b.20,sep=' ')
        elif (n%100 == 30):
            print (c.1,b.30,sep=' ')
        elif (n%100 == 40):
            print (c.1,b.40,sep=' ')
        elif (n%100 == 50):
            print (c.1,b.50,sep=' ')
        elif (n%100 == 60):
            print (c.1,b.60,sep=' ')
        elif (n%100 == 70):
            print (c.1,b.70,sep=' ')
        elif (n%100 == 80):
            print (c.1,b.80,sep=' ')
        elif (n%100 == 90):
            print (c.1,b.90,sep=' ')
        elif (b==2) and (c==1):
            print(c.1,b.20, a.1, sep=' ')
        elif (b==2) and (c==2):
            print(c.1,b.20, a.2, sep=' ')
        elif (b==2) and (c==3):
            print(c.1,b.20, a.3, sep=' ')
        elif (b==2) and (c==4):
            print(c.1,b.20, a.4, sep=' ')
        elif (b==2) and (c==5):
            print(c.1,b.20, a.5, sep=' ')
        elif (b==2) and (c==6):
            print(c.1,b.20, a.6, sep=' ')
        elif (b==2) and (c==7):
            print(c.1,b.20, a.7, sep=' ')
        elif (b==2) and (c==8):
            print(c.1,b.20, a.8, sep=' ')
        elif (b==2) and (c==9):
            print(c.1,b.20, a.9, sep=' ')
        elif (b==3) and (c==1):
            print(c.1,b.30, a.1, sep=' ')
        elif (b==3) and (c==2):
            print(c.1,b.30, a.2, sep=' ')
        elif (b==3) and (c==3):
            print(c.1,b.30, a.3, sep=' ')
        elif (b==3) and (c==4):
            print(c.1,b.30, a.4, sep=' ')
        elif (b==3) and (c==5):
            print(c.1,b.30, a.5, sep=' ')
        elif (b==3) and (c==6):
            print(c.1,b.30, a.6, sep=' ')
        elif (b==3) and (c==7):
            print(c.1,b.30, a.7, sep=' ')
        elif (b==3) and (c==8):
            print(c.1,b.30, a.8, sep=' ')
        elif (b==3) and (c==9):
            print(c.1,b.30, a.9, sep=' ')
        elif (b==4) and (c==1):
            print(c.1,b.40, a.1, sep=' ')
        elif (b==4) and (c==2):
            print(c.1,b.40, a.2, sep=' ')
        elif (b==4) and (c==3):
            print(c.1,b.40, a.3, sep=' ')
        elif (b==4) and (c==4):
            print(c.1,b.40, a.4, sep=' ')
        elif (b==4) and (c==5):
            print(c.1,b.40, a.5, sep=' ')
        elif (b==4) and (c==6):
            print(c.1,b.40, a.6, sep=' ')
        elif (b==4) and (c==7):
            print(c.1,b.40, a.7, sep=' ')
        elif (b==4) and (c==8):
            print(c.1,b.40, a.8, sep=' ')
        elif (b==4) and (c==9):
            print(c.1,b.40, a.9, sep=' ')
        elif (b==5) and (c==1):
            print(c.1,b.50, a.1, sep=' ')
        elif (b==5) and (c==2):
            print(c.1,b.50, a.2, sep=' ')
        elif (b==5) and (c==3):
            print(c.1,b.50, a.3, sep=' ')
        elif (b==5) and (c==4):
            print(c.1,b.50, a.4, sep=' ')
        elif (b==5) and (c==5):
            print(c.1,b.50, a.5, sep=' ')
        elif (b==5) and (c==6):
            print(c.1,b.50, a.6, sep=' ')
        elif (b==5) and (c==7):
            print(c.1,b.50, a.7, sep=' ')
        elif (b==5) and (c==8):
            print(c.1,b.50, a.8, sep=' ')
        elif (b==5) and (c==9):
            print(c.1,b.50, a.9, sep=' ')
        elif (b==6) and (c==1):
            print(c.1,b.60, a.1, sep=' ')
        elif (b==6) and (c==2):
            print(c.1,b.60, a.2, sep=' ')
        elif (b==6) and (c==3):
            print(c.1,b.60, a.3, sep=' ')
        elif (b==6) and (c==4):
            print(c.1,b.60, a.4, sep=' ')
        elif (b==6) and (c==5):
            print(c.1,b.60, a.5, sep=' ')
        elif (b==6) and (c==6):
            print(c.1,b.60, a.6, sep=' ')
        elif (b==6) and (c==7):
            print(c.1,b.60, a.7, sep=' ')
        elif (b==6) and (c==8):
            print(c.1,b.60, a.8, sep=' ')
        elif (b==6) and (c==9):
            print(c.1,b.60, a.9, sep=' ')
        elif (b==7) and (c==1):
            print(c.1,b.70, a.1, sep=' ')
        elif (b==7) and (c==2):
            print(c.1,b.70, a.2, sep=' ')
        elif (b==7) and (c==3):
            print(c.1,b.70, a.3, sep=' ')
        elif (b==7) and (c==4):
            print(c.1,b.70, a.4, sep=' ')
        elif (b==7) and (c==5):
            print(c.1,b.70, a.5, sep=' ')
        elif (b==7) and (c==6):
            print(c.1,b.70, a.6, sep=' ')
        elif (b==7) and (c==7):
            print(c.1,b.70, a.7, sep=' ')
        elif (b==7) and (c==8):
            print(c.1,b.70, a.8, sep=' ')
        elif (b==7) and (c==9):
            print(c.1,b.70, a.9, sep=' ')
        elif (b==8) and (c==1):
            print(c.1,b.80, a.1, sep=' ')
        elif (b==8) and (c==2):
            print(c.1,b.80, a.2, sep=' ')
        elif (b==8) and (c==3):
            print(c.1,b.80, a.3, sep=' ')
        elif (b==8) and (c==4):
            print(c.1,b.80, a.4, sep=' ')
        elif (b==8) and (c==5):
            print(c.1,b.80, a.5, sep=' ')
        elif (b==8) and (c==6):
            print(c.1,b.80, a.6, sep=' ')
        elif (b==8) and (c==7):
            print(c.1,b.80, a.7, sep=' ')
        elif (b==8) and (c==8):
            print(c.1,b.80, a.8, sep=' ')
        elif (b==8) and (c==9):
            print(c.1,b.80, a.9, sep=' ')
        elif (b==9) and (c==1):
            print(c.1,b.90, a.1, sep=' ')
        elif (b==9) and (c==2):
            print(c.1,b.90, a.2, sep=' ')
        elif (b==9) and (c==3):
            print(c.1,b.90, a.3, sep=' ')
        elif (b==9) and (c==4):
            print(c.1,b.90, a.4, sep=' ')
        elif (b==9) and (c==5):
            print(c.1,b.90, a.5, sep=' ')
        elif (b==9) and (c==6):
            print(c.1,b.90, a.6, sep=' ')
        elif (b==9) and (c==7):
            print(c.1,b.90, a.7, sep=' ')
        elif (b==9) and (c==8):
            print(c.1,b.90, a.8, sep=' ')
        elif (b==9) and (c==9):
            print(c.1,b.90, a.9, sep=' ')
    if (a == 2):
        if (n%100 == 11):
            print (c.2,b.11,sep=' ')
        elif (n%100 == 12):
            print (c.2,b.12,sep=' ')
        elif (n%100 == 13):
            print (c.2,b.13,sep=' ')
        elif (n%100 == 14):
            print (c.2,b.14,sep=' ')
        elif (n%100 == 15):
            print (c.2,b.15,sep=' ')
        elif (n%100 == 16):
            print (c.2,b.16,sep=' ')
        elif (n%100 == 17):
            print (c.2,b.17,sep=' ')
        elif (n%100 == 18):
            print (c.2,b.18,sep=' ')
        elif (n%100 == 19):
            print (c.2,b.19,sep=' ')
        elif (n%100 == 10):
            print (c.2,b.10,sep=' ')
        elif (n%100 == 20):
            print (c.2,b.20,sep=' ')
        elif (n%100 == 30):
            print (c.2,b.30,sep=' ')
        elif (n%100 == 40):
            print (c.2,b.40,sep=' ')
        elif (n%100 == 50):
            print (c.2,b.50,sep=' ')
        elif (n%100 == 60):
            print (c.2,b.60,sep=' ')
        elif (n%100 == 70):
            print (c.2,b.70,sep=' ')
        elif (n%100 == 80):
            print (c.2,b.80,sep=' ')
        elif (n%100 == 90):
            print (c.2,b.90,sep=' ')
        elif (b==2) and (c==1):
            print(c.2,b.20, a.1, sep=' ')
        elif (b==2) and (c==2):
            print(c.2,b.20, a.2, sep=' ')
        elif (b==2) and (c==3):
            print(c.2,b.20, a.3, sep=' ')
        elif (b==2) and (c==4):
            print(c.2,b.20, a.4, sep=' ')
        elif (b==2) and (c==5):
            print(c.2,b.20, a.5, sep=' ')
        elif (b==2) and (c==6):
            print(c.2,b.20, a.6, sep=' ')
        elif (b==2) and (c==7):
            print(c.2,b.20, a.7, sep=' ')
        elif (b==2) and (c==8):
            print(c.2,b.20, a.8, sep=' ')
        elif (b==2) and (c==9):
            print(c.2,b.20, a.9, sep=' ')
        elif (b==3) and (c==1):
            print(c.2,b.30, a.1, sep=' ')
        elif (b==3) and (c==2):
            print(c.2,b.30, a.2, sep=' ')
        elif (b==3) and (c==3):
            print(c.2,b.30, a.3, sep=' ')
        elif (b==3) and (c==4):
            print(c.2,b.30, a.4, sep=' ')
        elif (b==3) and (c==5):
            print(c.2,b.30, a.5, sep=' ')
        elif (b==3) and (c==6):
            print(c.2,b.30, a.6, sep=' ')
        elif (b==3) and (c==7):
            print(c.2,b.30, a.7, sep=' ')
        elif (b==3) and (c==8):
            print(c.2,b.30, a.8, sep=' ')
        elif (b==3) and (c==9):
            print(c.2,b.30, a.9, sep=' ')
        elif (b==4) and (c==1):
            print(c.2,b.40, a.1, sep=' ')
        elif (b==4) and (c==2):
            print(c.2,b.40, a.2, sep=' ')
        elif (b==4) and (c==3):
            print(c.2,b.40, a.3, sep=' ')
        elif (b==4) and (c==4):
            print(c.2,b.40, a.4, sep=' ')
        elif (b==4) and (c==5):
            print(c.2,b.40, a.5, sep=' ')
        elif (b==4) and (c==6):
            print(c.2,b.40, a.6, sep=' ')
        elif (b==4) and (c==7):
            print(c.2,b.40, a.7, sep=' ')
        elif (b==4) and (c==8):
            print(c.2,b.40, a.8, sep=' ')
        elif (b==4) and (c==9):
            print(c.2,b.40, a.9, sep=' ')
        elif (b==5) and (c==1):
            print(c.2,b.50, a.1, sep=' ')
        elif (b==5) and (c==2):
            print(c.2,b.50, a.2, sep=' ')
        elif (b==5) and (c==3):
            print(c.2,b.50, a.3, sep=' ')
        elif (b==5) and (c==4):
            print(c.2,b.50, a.4, sep=' ')
        elif (b==5) and (c==5):
            print(c.2,b.50, a.5, sep=' ')
        elif (b==5) and (c==6):
            print(c.2,b.50, a.6, sep=' ')
        elif (b==5) and (c==7):
            print(c.2,b.50, a.7, sep=' ')
        elif (b==5) and (c==8):
            print(c.2,b.50, a.8, sep=' ')
        elif (b==5) and (c==9):
            print(c.2,b.50, a.9, sep=' ')
        elif (b==6) and (c==1):
            print(c.2,b.60, a.1, sep=' ')
        elif (b==6) and (c==2):
            print(c.2,b.60, a.2, sep=' ')
        elif (b==6) and (c==3):
            print(c.2,b.60, a.3, sep=' ')
        elif (b==6) and (c==4):
            print(c.2,b.60, a.4, sep=' ')
        elif (b==6) and (c==5):
            print(c.2,b.60, a.5, sep=' ')
        elif (b==6) and (c==6):
            print(c.2,b.60, a.6, sep=' ')
        elif (b==6) and (c==7):
            print(c.2,b.60, a.7, sep=' ')
        elif (b==6) and (c==8):
            print(c.2,b.60, a.8, sep=' ')
        elif (b==6) and (c==9):
            print(c.2,b.60, a.9, sep=' ')
        elif (b==7) and (c==1):
            print(c.2,b.70, a.1, sep=' ')
        elif (b==7) and (c==2):
            print(c.2,b.70, a.2, sep=' ')
        elif (b==7) and (c==3):
            print(c.2,b.70, a.3, sep=' ')
        elif (b==7) and (c==4):
            print(c.2,b.70, a.4, sep=' ')
        elif (b==7) and (c==5):
            print(c.2,b.70, a.5, sep=' ')
        elif (b==7) and (c==6):
            print(c.2,b.70, a.6, sep=' ')
        elif (b==7) and (c==7):
            print(c.2,b.70, a.7, sep=' ')
        elif (b==7) and (c==8):
            print(c.2,b.70, a.8, sep=' ')
        elif (b==7) and (c==9):
            print(c.2,b.70, a.9, sep=' ')
        elif (b==8) and (c==1):
            print(c.2,b.80, a.1, sep=' ')
        elif (b==8) and (c==2):
            print(c.2,b.80, a.2, sep=' ')
        elif (b==8) and (c==3):
            print(c.2,b.80, a.3, sep=' ')
        elif (b==8) and (c==4):
            print(c.2,b.80, a.4, sep=' ')
        elif (b==8) and (c==5):
            print(c.2,b.80, a.5, sep=' ')
        elif (b==8) and (c==6):
            print(c.2,b.80, a.6, sep=' ')
        elif (b==8) and (c==7):
            print(c.2,b.80, a.7, sep=' ')
        elif (b==8) and (c==8):
            print(c.2,b.80, a.8, sep=' ')
        elif (b==8) and (c==9):
            print(c.2,b.80, a.9, sep=' ')
        elif (b==9) and (c==1):
            print(c.2,b.90, a.1, sep=' ')
        elif (b==9) and (c==2):
            print(c.2,b.90, a.2, sep=' ')
        elif (b==9) and (c==3):
            print(c.2,b.90, a.3, sep=' ')
        elif (b==9) and (c==4):
            print(c.2,b.90, a.4, sep=' ')
        elif (b==9) and (c==5):
            print(c.2,b.90, a.5, sep=' ')
        elif (b==9) and (c==6):
            print(c.2,b.90, a.6, sep=' ')
        elif (b==9) and (c==7):
            print(c.2,b.90, a.7, sep=' ')
        elif (b==9) and (c==8):
            print(c.2,b.90, a.8, sep=' ')
        elif (b==9) and (c==9):
            print(c.2,b.90, a.9, sep=' ')
