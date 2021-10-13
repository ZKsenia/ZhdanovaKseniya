#10.1
A = int(input())
B = int(input())
print((A>2) and (B<=3))
#10.2
A = int(input())
B = int(input())
C = int(input())
print(A<B<C)
#10.3
n = int(input())
print((n%2==0) and (n>=10) and (n<=99))
#10.4
n = int(input())
a = n%10
b = (n//10)%10
c = n//100
print((a<b<c) or(a>b>c))
#10.5
n=int(input())
a=n%10
b=(n//10)%10
c=(n//100)%10
d=n//1000
print((a==d)and(b==c))
#10.6
a = int(input())
b = int(input())
c = int(input())
print((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2))
#10.7
a = int(input())
b = int(input())
c = int(input())
print(((a+b)>c) or ((b+c)>a) or ((a+c)>b))
