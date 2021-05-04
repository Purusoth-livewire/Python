"""
Logical Operator:
================
it will checks the multiple conditions in one statements.

and   ---->  Logical And Operator
or     ---->  Logical Or Operator
not   ---->  Logical  Not Operator


#And Operator
it will checks the multiple condition
when it all condition should be  true,it will return true.
if any one will be false it will return false.

#program1
condition=False and False
print(condition)

condition=False and True
print(condition)

condition=True and False
print(condition)

condition=True and True
print(condition)


condition=True and True and False
print(condition)

#program2
s1=int(input("Enter Student 1 Mark : "))
s2=int(input("Enter Student 2 Mark : "))
s3=int(input("Enter Student 3 Mark : "))

s1Topper=s1>s2 and s1>s3
print("student 1 Topper ? ",s1Topper)

#program3
mark=int(input("Enter mark : "))
check=mark>=0 and mark<=100
print(check)



#or Operator
==============
it will checks the multiple condition
when it all condition should be  false,it will return false.
if any one will be True,it will return true.

#program1

condition=False or False
print(condition)

condition=False or True
print(condition)

condition=True or False
print(condition)

condition=True or True
print(condition)

condition=False or False or False or False or True
print(condition)

#program2
s1=int(input("Enter Student 1 Mark : "))
s2=int(input("Enter Student 2 Mark : "))
s3=int(input("Enter Student 3 Mark : "))

avg=s1>s2 or s1>s3
print("student 1 is Average ? ",avg)



#not operator:
==============
It will check the condition,
if the condition is true, it will return false.
if the condition is false,it will  return true.
"""
condition=not False 
print(condition)

condition=not True
print(condition)

condition=not True and True
print(condition)

condition=not False and True
print(condition)

condition=not (False or True)
print(condition)

condition=not False or True
print(condition)
