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
#12.4 
n = int(input())
c = n%10
b = (n//10)%10
a = n//100
c_1 = 'сто'
c_2 = 'двести'
c_3 = 'триста'
c_4 = 'четыреста'
c_5 = 'пятьсот'
c_6 = 'шестьсот'
c_7 = 'семьсот'
c_8 = 'восемьсот'
c_9 = 'девятьсот'
b_10 = 'десять'
b_11 = 'одиннадцать'
b_12 = 'двенадцать'
b_13 = 'тринадцать'
b_14 = 'четырнадцать'
b_15 = 'пятнадцать'
b_16 = 'шестнадцать'
b_17 = 'семнадцать'
b_18 = 'восемнадцать'
b_19 = 'девятнадцать'
b_20 = 'двадцать'
b_30 = 'тридцать'
b_40 = 'сорок'
b_50 = 'пятьдесят'
b_60 = 'шестьдесят'
b_70 = 'семьдесят'
b_80 = 'восемьдесят'
b_90 = 'девяносто'
a_1 = 'один'
a_2 = 'два'
a_3 = 'три'
a_4 = 'четыре'
a_5 = 'пять'
a_6 = 'шесть'
a_7 = 'семь'
a_8 = 'восемь'
a_9 = 'девять'
if n in range (100,999+1):
    if (n==100):
        print(c_1)
    elif (n==200):
        print(c_2)
    elif (n==300):
        print(c_3)
    elif (n==400):
        print(c_4)
    elif (n==500):
        print(c_5)
    elif (n==600):
        print(c_6)
    elif (n==700):
        print(c_7)
    elif (n==800):
        print(c_8)
    elif (n==900):
        print(c_9)
    elif (a == 1):
        if (n%100 == 11):
            print (c_1,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_1,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_1,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_1,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_1,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_1,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_1,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_1,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_1,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_1,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_1,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_1,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_1,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_1,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_1,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_1,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_1,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_1,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_1,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_1,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_1,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_1,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_1,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_1,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_1,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_1,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_1,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_1,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_1,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_1,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_1,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_1,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_1,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_1,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_1,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_1,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_1,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_1,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_1,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_1,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_1,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_1,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_1,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_1,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_1,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_1,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_1,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_1,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_1,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_1,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_1,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_1,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_1,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_1,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_1,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_1,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_1,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_1,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_1,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_1,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_1,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_1,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_1,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_1,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_1,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_1,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_1,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_1,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_1,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_1,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_1,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_1,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_1,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_1,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_1,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_1,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_1,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_1,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_1,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_1,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_1,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_1,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_1,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_1,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_1,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_1,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_1,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_1,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_1,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_1,b_90, a_9, sep=' ')
    elif (a == 2):
        if (n%100 == 11):
            print (c_2,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_2,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_2,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_2,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_2,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_2,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_2,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_2,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_2,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_2,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_2,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_2,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_2,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_2,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_2,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_2,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_2,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_2,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_2,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_2,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_2,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_2,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_2,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_2,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_2,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_2,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_2,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_2,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_2,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_2,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_2,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_2,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_2,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_2,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_2,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_2,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_2,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_2,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_2,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_2,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_2,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_2,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_2,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_2,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_2,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_2,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_2,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_2,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_2,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_2,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_2,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_2,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_2,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_2,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_2,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_2,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_2,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_2,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_2,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_2,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_2,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_2,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_2,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_2,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_2,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_2,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_2,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_2,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_2,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_2,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_2,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_2,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_2,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_2,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_2,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_2,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_2,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_2,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_2,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_2,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_2,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_2,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_2,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_2,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_2,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_2,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_2,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_2,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_2,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_2,b_90, a_9, sep=' ')
    elif (a == 3):
        if (n%100 == 11):
            print (c_3,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_3,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_3,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_3,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_3,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_3,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_3,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_3,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_3,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_3,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_3,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_3,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_3,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_3,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_3,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_3,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_3,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_3,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_3,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_3,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_3,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_3,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_3,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_3,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_3,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_3,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_3,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_3,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_3,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_3,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_3,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_3,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_3,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_3,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_3,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_3,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_3,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_3,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_3,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_3,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_3,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_3,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_3,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_3,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_3,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_3,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_3,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_3,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_3,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_3,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_3,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_3,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_3,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_3,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_3,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_3,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_3,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_3,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_3,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_3,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_3,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_3,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_3,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_3,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_3,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_3,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_3,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_3,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_3,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_3,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_3,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_3,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_3,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_3,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_3,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_3,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_3,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_3,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_3,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_3,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_3,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_3,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_3,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_3,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_3,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_3,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_3,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_3,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_3,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_3,b_90, a_9, sep=' ')
    elif (a == 4):
        if (n%100 == 11):
            print (c_4,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_4,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_4,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_4,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_4,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_4,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_4,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_4,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_4,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_4,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_4,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_4,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_4,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_4,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_4,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_4,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_4,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_4,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_4,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_4,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_4,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_4,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_4,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_4,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_4,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_4,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_4,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_4,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_4,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_4,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_4,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_4,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_4,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_4,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_4,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_4,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_4,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_4,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_4,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_4,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_4,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_4,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_4,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_4,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_4,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_4,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_4,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_4,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_4,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_4,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_4,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_4,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_4,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_4,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_4,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_4,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_4,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_4,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_4,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_4,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_4,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_4,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_4,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_4,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_4,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_4,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_4,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_4,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_4,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_4,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_4,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_4,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_4,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_4,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_4,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_4,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_4,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_4,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_4,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_4,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_4,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_4,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_4,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_4,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_4,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_4,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_4,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_4,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_4,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_4,b_90, a_9, sep=' ')
    elif (a == 5):
        if (n%100 == 11):
            print (c_5,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_5,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_5,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_5,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_5,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_5,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_5,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_5,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_5,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_5,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_5,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_5,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_5,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_5,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_5,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_5,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_5,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_5,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_5,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_5,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_5,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_5,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_5,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_5,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_5,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_5,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_5,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_5,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_5,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_5,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_5,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_5,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_5,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_5,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_5,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_5,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_5,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_5,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_5,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_5,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_5,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_5,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_5,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_5,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_5,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_5,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_5,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_5,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_5,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_5,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_5,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_5,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_5,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_5,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_5,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_5,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_5,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_5,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_5,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_5,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_5,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_5,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_5,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_5,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_5,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_5,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_5,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_5,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_5,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_5,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_5,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_5,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_5,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_5,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_5,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_5,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_5,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_5,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_5,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_5,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_5,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_5,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_5,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_5,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_5,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_5,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_5,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_5,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_5,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_5,b_90, a_9, sep=' ')
    elif (a == 6):
        if (n%100 == 11):
            print (c_6,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_6,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_6,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_6,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_6,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_6,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_6,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_6,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_6,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_6,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_6,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_6,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_6,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_6,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_6,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_6,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_6,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_6,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_6,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_6,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_6,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_6,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_6,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_6,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_6,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_6,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_6,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_6,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_6,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_6,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_6,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_6,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_6,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_6,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_6,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_6,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_6,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_6,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_6,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_6,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_6,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_6,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_6,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_6,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_6,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_6,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_6,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_6,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_6,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_6,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_6,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_6,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_6,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_6,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_6,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_6,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_6,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_6,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_6,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_6,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_6,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_6,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_6,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_6,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_6,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_6,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_6,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_6,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_6,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_6,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_6,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_6,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_6,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_6,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_6,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_6,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_6,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_6,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_6,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_6,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_6,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_6,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_6,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_6,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_6,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_6,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_6,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_6,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_6,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_6,b_90, a_9, sep=' ')
    elif (a == 7):
        if (n%100 == 11):
            print (c_7,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_7,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_7,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_7,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_7,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_7,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_7,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_7,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_7,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_7,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_7,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_7,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_7,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_7,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_7,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_7,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_7,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_7,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_7,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_7,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_7,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_7,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_7,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_7,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_7,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_7,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_7,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_7,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_7,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_7,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_7,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_7,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_7,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_7,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_7,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_7,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_7,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_7,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_7,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_7,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_7,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_7,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_7,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_7,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_7,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_7,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_7,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_7,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_7,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_7,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_7,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_7,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_7,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_7,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_7,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_7,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_7,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_7,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_7,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_7,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_7,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_7,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_7,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_7,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_7,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_7,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_7,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_7,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_7,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_7,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_7,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_7,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_7,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_7,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_7,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_7,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_7,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_7,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_7,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_7,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_7,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_7,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_7,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_7,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_7,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_7,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_7,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_7,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_7,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_7,b_90, a_9, sep=' ')
    elif (a == 8):
        if (n%100 == 11):
            print (c_8,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_8,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_8,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_8,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_8,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_8,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_8,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_8,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_8,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_8,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_8,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_8,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_8,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_8,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_8,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_8,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_8,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_8,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_8,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_8,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_8,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_8,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_8,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_8,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_8,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_8,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_8,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_8,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_8,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_8,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_8,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_8,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_8,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_8,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_8,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_8,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_8,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_8,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_8,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_8,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_8,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_8,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_8,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_8,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_8,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_8,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_8,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_8,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_8,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_8,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_8,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_8,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_8,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_8,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_8,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_8,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_8,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_8,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_8,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_8,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_8,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_8,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_8,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_8,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_8,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_8,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_8,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_8,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_8,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_8,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_8,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_8,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_8,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_8,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_8,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_8,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_8,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_8,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_8,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_8,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_8,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_8,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_8,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_8,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_8,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_8,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_8,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_8,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_8,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_8,b_90, a_9, sep=' ')
    elif (a == 9):
        if (n%100 == 11):
            print (c_9,b_11,sep=' ')
        elif (n%100 == 12):
            print (c_9,b_12,sep=' ')
        elif (n%100 == 13):
            print (c_9,b_13,sep=' ')
        elif (n%100 == 14):
            print (c_9,b_14,sep=' ')
        elif (n%100 == 15):
            print (c_9,b_15,sep=' ')
        elif (n%100 == 16):
            print (c_9,b_16,sep=' ')
        elif (n%100 == 17):
            print (c_9,b_17,sep=' ')
        elif (n%100 == 18):
            print (c_9,b_18,sep=' ')
        elif (n%100 == 19):
            print (c_9,b_19,sep=' ')
        elif (n%100 == 10):
            print (c_9,b_10,sep=' ')
        elif (n%100 == 20):
            print (c_9,b_20,sep=' ')
        elif (n%100 == 30):
            print (c_9,b_30,sep=' ')
        elif (n%100 == 40):
            print (c_9,b_40,sep=' ')
        elif (n%100 == 50):
            print (c_9,b_50,sep=' ')
        elif (n%100 == 60):
            print (c_9,b_60,sep=' ')
        elif (n%100 == 70):
            print (c_9,b_70,sep=' ')
        elif (n%100 == 80):
            print (c_9,b_80,sep=' ')
        elif (n%100 == 90):
            print (c_9,b_90,sep=' ')
        elif (b==2) and (c==1):
            print(c_9,b_20, a_1, sep=' ')
        elif (b==2) and (c==2):
            print(c_9,b_20, a_2, sep=' ')
        elif (b==2) and (c==3):
            print(c_9,b_20, a_3, sep=' ')
        elif (b==2) and (c==4):
            print(c_9,b_20, a_4, sep=' ')
        elif (b==2) and (c==5):
            print(c_9,b_20, a_5, sep=' ')
        elif (b==2) and (c==6):
            print(c_9,b_20, a_6, sep=' ')
        elif (b==2) and (c==7):
            print(c_9,b_20, a_7, sep=' ')
        elif (b==2) and (c==8):
            print(c_9,b_20, a_8, sep=' ')
        elif (b==2) and (c==9):
            print(c_9,b_20, a_9, sep=' ')
        elif (b==3) and (c==1):
            print(c_9,b_30, a_1, sep=' ')
        elif (b==3) and (c==2):
            print(c_9,b_30, a_2, sep=' ')
        elif (b==3) and (c==3):
            print(c_9,b_30, a_3, sep=' ')
        elif (b==3) and (c==4):
            print(c_9,b_30, a_4, sep=' ')
        elif (b==3) and (c==5):
            print(c_9,b_30, a_5, sep=' ')
        elif (b==3) and (c==6):
            print(c_9,b_30, a_6, sep=' ')
        elif (b==3) and (c==7):
            print(c_9,b_30, a_7, sep=' ')
        elif (b==3) and (c==8):
            print(c_9,b_30, a_8, sep=' ')
        elif (b==3) and (c==9):
            print(c_9,b_30, a_9, sep=' ')
        elif (b==4) and (c==1):
            print(c_9,b_40, a_1, sep=' ')
        elif (b==4) and (c==2):
            print(c_9,b_40, a_2, sep=' ')
        elif (b==4) and (c==3):
            print(c_9,b_40, a_3, sep=' ')
        elif (b==4) and (c==4):
            print(c_9,b_40, a_4, sep=' ')
        elif (b==4) and (c==5):
            print(c_9,b_40, a_5, sep=' ')
        elif (b==4) and (c==6):
            print(c_9,b_40, a_6, sep=' ')
        elif (b==4) and (c==7):
            print(c_9,b_40, a_7, sep=' ')
        elif (b==4) and (c==8):
            print(c_9,b_40, a_8, sep=' ')
        elif (b==4) and (c==9):
            print(c_9,b_40, a_9, sep=' ')
        elif (b==5) and (c==1):
            print(c_9,b_50, a_1, sep=' ')
        elif (b==5) and (c==2):
            print(c_9,b_50, a_2, sep=' ')
        elif (b==5) and (c==3):
            print(c_9,b_50, a_3, sep=' ')
        elif (b==5) and (c==4):
            print(c_9,b_50, a_4, sep=' ')
        elif (b==5) and (c==5):
            print(c_9,b_50, a_5, sep=' ')
        elif (b==5) and (c==6):
            print(c_9,b_50, a_6, sep=' ')
        elif (b==5) and (c==7):
            print(c_9,b_50, a_7, sep=' ')
        elif (b==5) and (c==8):
            print(c_9,b_50, a_8, sep=' ')
        elif (b==5) and (c==9):
            print(c_9,b_50, a_9, sep=' ')
        elif (b==6) and (c==1):
            print(c_9,b_60, a_1, sep=' ')
        elif (b==6) and (c==2):
            print(c_9,b_60, a_2, sep=' ')
        elif (b==6) and (c==3):
            print(c_9,b_60, a_3, sep=' ')
        elif (b==6) and (c==4):
            print(c_9,b_60, a_4, sep=' ')
        elif (b==6) and (c==5):
            print(c_9,b_60, a_5, sep=' ')
        elif (b==6) and (c==6):
            print(c_9,b_60, a_6, sep=' ')
        elif (b==6) and (c==7):
            print(c_9,b_60, a_7, sep=' ')
        elif (b==6) and (c==8):
            print(c_9,b_60, a_8, sep=' ')
        elif (b==6) and (c==9):
            print(c_9,b_60, a_9, sep=' ')
        elif (b==7) and (c==1):
            print(c_9,b_70, a_1, sep=' ')
        elif (b==7) and (c==2):
            print(c_9,b_70, a_2, sep=' ')
        elif (b==7) and (c==3):
            print(c_9,b_70, a_3, sep=' ')
        elif (b==7) and (c==4):
            print(c_9,b_70, a_4, sep=' ')
        elif (b==7) and (c==5):
            print(c_9,b_70, a_5, sep=' ')
        elif (b==7) and (c==6):
            print(c_9,b_70, a_6, sep=' ')
        elif (b==7) and (c==7):
            print(c_9,b_70, a_7, sep=' ')
        elif (b==7) and (c==8):
            print(c_9,b_70, a_8, sep=' ')
        elif (b==7) and (c==9):
            print(c_9,b_70, a_9, sep=' ')
        elif (b==8) and (c==1):
            print(c_9,b_80, a_1, sep=' ')
        elif (b==8) and (c==2):
            print(c_9,b_80, a_2, sep=' ')
        elif (b==8) and (c==3):
            print(c_9,b_80, a_3, sep=' ')
        elif (b==8) and (c==4):
            print(c_9,b_80, a_4, sep=' ')
        elif (b==8) and (c==5):
            print(c_9,b_80, a_5, sep=' ')
        elif (b==8) and (c==6):
            print(c_9,b_80, a_6, sep=' ')
        elif (b==8) and (c==7):
            print(c_9,b_80, a_7, sep=' ')
        elif (b==8) and (c==8):
            print(c_9,b_80, a_8, sep=' ')
        elif (b==8) and (c==9):
            print(c_9,b_80, a_9, sep=' ')
        elif (b==9) and (c==1):
            print(c_9,b_90, a_1, sep=' ')
        elif (b==9) and (c==2):
            print(c_9,b_90, a_2, sep=' ')
        elif (b==9) and (c==3):
            print(c_9,b_90, a_3, sep=' ')
        elif (b==9) and (c==4):
            print(c_9,b_90, a_4, sep=' ')
        elif (b==9) and (c==5):
            print(c_9,b_90, a_5, sep=' ')
        elif (b==9) and (c==6):
            print(c_9,b_90, a_6, sep=' ')
        elif (b==9) and (c==7):
            print(c_9,b_90, a_7, sep=' ')
        elif (b==9) and (c==8):
            print(c_9,b_90, a_8, sep=' ')
        elif (b==9) and (c==9):
            print(c_9,b_90, a_9, sep=' ')
else:
    print('Введите значение из установленного диапозона')
