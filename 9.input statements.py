"""
Input statements:
=================
to get the value in output screen.
output screen/runtime screen/dynamic screen/late binding

var=input()
var=input("prompt")
var=eval(input("prompt"))
var=int(input("prompt"))
var=float(input("prompt"))
var1,var2=input("prompt").split("symbol")


#a=input()
#print("a : ",a)

a=input("Enter value : ")
b=input("Enter value : ")
print("a : ",a)
print("b : ",b)

print("type of a : ",type(a))
print("type of b : ",type(b))

a1=int(a)
b1=int(b)
c=a1+b1
print("c : ",c)



a=eval(input("Enter value 1 : "))
b=eval(input("Enter value 2 : "))
c=a+b
print("c : ",c)


a=int(input("Enter value 1 : "))
b=int(input("Enter value 2 : "))

c=a*b
print("c : ",c)


a=float(input("Enter value 1 : "))
b=float(input("Enter value 2 : "))

print(type(a))
print("a : ",a)
c=a*b
print("c : ",c)


"""

a,b=input("Enter Two Values : ").split(",")

print("type of a : ",type(a))
c=a+b
print("c : ",c)
a1=int(a)
b1=int(b)
c=a1+b1
print("c : ",c)
