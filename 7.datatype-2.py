list:
====
order sequance of data.
duplicate data's are accepted.
data can be modify.---> mutable

mutable---> once obj created then it was modified.  create,del,add

l1=[]#empty list
list2=[]#empty list
print(list2)
list3=list([3,2,5])
print(list3)
list1=[1,3,2,6,7]
print(list1)
print(list1[2])
print(type(list1))
list1.append(10)
print(list1)

list1.pop()
***********************************************************
tuple:
=====
order sequance of data
duplicate data's are accepted.
data's can't modify----> immutable


tup1=()#empty tuple
t1=(1,3,7,8)
print(type(t1))
print(t1)
t2=tuple([2,5,6,5,6,2])
print(t2)
**************************************************************
set:
====
unorder sequance of data.
duplicate data are not allowed.
it is mutable---modify data


set2=set()#empty set
set1={}#---dictionary
print(type(set1))
s1={2,10,100,3,4,4,6,4}
print(type(s1))
print(s1)

s2=set([2,3,4])
print(s2)
print(type(s2))

***************************************************************
dictionary:
==========
unorder sequance of elements but it have key:value pair
#var={key1:value1,key2:value2,,,,,,key_n=value_n}

dict1={1:"lokesh",2:"Rahul"}
print(type(dict1))
print(dict1)

d2=dict({3:"muthukrishnan"})
print(d2)
