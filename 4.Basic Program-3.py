"""
id()-----address of the object

a=10
obj_ref=object
object_reference----->variale
object ----> values


python have automatic garbage collection mechanism.


type()---find data type


del value or variable----> delete the  variable but can't delete data


"""

print(id(10))
a=10
b=10
print(id(a))
print(id(b))



value=32767
print(100000)
print()


print(type(10))
print(type(3.5))
print(type(1+2j))



del a
del b

print(a)
