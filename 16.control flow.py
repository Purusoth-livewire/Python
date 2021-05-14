"""
Control Flow:
============

1.Decision Making
2.Looping Structure
3.Loop control Statements


1.Decision Making:
=================
    1.if statements
    2.if-else statements
    3.nested if else statements
    4.Ladder if-else or if-else-if statements

2.Looping Structure:
===================
    1.while loop
    2.for loop

3.Loop Control Statements:
=========================
    1.continue
    2.break


Decision Making:
===============
it have multiple path,
we can choose where to choose.

it have two condition,
if the condition is true it will excutes true  statements,
if the condiition is flase,it will excutes false statements

1.if  statements:
===============
it will checks the condition,
if the condition is true it will excutes true(if)  statements only.

syntax:
=======
if condition:
    statements
    statements


#check student 1 is topper?
s1=int(input("Enter student 1 mark : "))
s2=int(input("Enter student 2 mark : "))

if s1>s2:
    print("student 1 is Topper")
    print("Mark : ",s1)


2.if else statements:
===================
it will checks the condition,
if the condition is true it will excutes true(if)  statements.
if the condition is false it will excutes false(else)  statements.

syntax:
=======

if condition:
    statements
    statements
else:
    statements
    statements


Program:
========
s1=int(input("Enter number 1 : "))
s2=int(input("Enter number 2 : "))

if(s1>s2):
    print("Student 1 is Topper.")
    print("Student 1 Mark : ",s1)
else:
    print("Student 2 is Topper.")
    print("Student 2 Mark : ",s2)

3.Ladder if-else statements:
=========================
if the program having multiple condition, we can use ladder if-else statements.

program:
========
"""

s1=int(input("Enter number 1 : "))
s2=int(input("Enter number 2 : "))

if(s1>s2):
    print("Student 1 is Topper.")
    print("Student 1 Mark : ",s1)
else:
    print("Student 2 is Topper.")
    print("Student 2 Mark : ",s2)
s
