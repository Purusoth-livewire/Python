"""
Special Operator:
================
1.identity Operator
2.Membership OPerator

1.identity Operator:
==================
it will check a single value
is  ---> to check the values are equal
is not ---> to check the values are not equal


a=int(input("Enter a number : "))
print(a is 10)

b=int(input("Enter a number : "))
print(b is a )

print(b is not 20)

2.Membership Operator:
=======================
it will check the value in the list.

in   -----> to check a value available in a list
not in  ----> to  check a value not available in a list
"""


list1=[1,2,3,4,5,6,7,8]
print(10 in list1)#false
print(4 in list1)#True

print(10 not in list1)#True
print(4 not in list1)#False



