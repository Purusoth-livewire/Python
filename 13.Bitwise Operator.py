"""
Bitwise Operator:
================

&  ---- And Operator
|  ---- Or Operator
^  ---- X-or Operator
~  ---- 1's Complement Operator
<<  ---- Left Shift Operator
>>  ---- Right Shift Operator



Explanation:
===========

a=5
b=3

1.And Operator
==============
c=a&b
a=5=  101
b=3=  011
========
c=a&b=001=1
==========

c=1

2.Or Operator
=============

c=a|b
a=5=  101
b=3=  011
========
c=a|b=111=7
==========

c=7

3.Xor Operator
=============

c=a^b
a=5=  101
b=3=  011
========
c=a^b=110=6
==========

c=6

4.1's complement Operator
========================

c=~(a|b)
a=5=  101
b=3=  011
========
c=a|b=111=7
==========

c=~(7)=~(7+1)=-8
c=-8

5.Left Shift Operator:
=====================

c=a<<1
c=a<<1=5<<1=  101<<1=1010=10
c=10

c=a<<2
c=a<<2=5<<2=101<<2=10100=20
c=20

6.Right Shift Operator:
=====================
c=a>>1
c=5>>1=5>>1=101>>1=10=2
c=2


c=a>>2
c=5>>2=5>>2=101>>2=1=1
c=1
"""

a=int(input("Enter value 1 : "))
b=int(input("Enter value 2 : "))

c=a&b
print("a&b : ",c)

c=a|b
print("a|b : ",c)

c=a^b
print("a^b : ",c)

c=~(a|b)
print("~(a\b) : ",c)

c=a<<1
print("a<<1 : ",c)

c=a<<2
print("a<<2 : ",c)

c=a>>1
print("a>>1 : ",c)

c=a>>2
print("a>>2 : ",c)
