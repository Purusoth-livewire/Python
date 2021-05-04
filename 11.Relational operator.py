"""
Relational Operator:
==================

==  ----> equal to
!=   ----> Not equal to
<=  ----> Less than or equal to
>=  ----> Greater than or equal to
<    ----> Less Than
>    ----> Greater Than

"""

print(10==20)
print(10!=20)
print(10>=20)
print(10<=20)
print(10>20)
print(10<20)

a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))

print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

c=a==b
print("a==b : ",c)
c=a!=b
print("a!=b : ",c)
c=a>=b
print("a>=b : ",c)
c=a<=b
print("a<=b: ",c)
c=a>b
print("a>b : ",c)
c=a<b
print("a<b : ",c)

print()#space b/w line

c=a==b
d=a!=b
e=a>=b
f=a<=b
g=a>b
h=a<b
print("a==b : ",c)
print("a!=b : ",d)
print("a>=b : ",e)
print("a<=b: ",f)
print("a>b : ",g)
print("a<b : ",h)
