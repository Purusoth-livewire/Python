print statements:
================
to display the output data.

print()#newline
print("prompt")
print(var)
print("prompt",var)
print("prompt1 ",var1," prompt2",var2,"prompt 3 ",var3, .............................,"prompt_n",var_n)
print(var1,var2,var3,sep="symbol",end="symbol")

sep---print(a,b,c,sep="+") ----> a+b+c
end---print(a,end="=")  ------> a=

print using %()
==============
print("prompt, format specifier",%(var))

format specifier
===============
integer : %d
float     : %f   digit : %.<num>f
charater :%c
string   : %s


print using .format()
===================
print("prompt,{}".format(var))
Escape sequance:
===============

\n ---> new line
\" ---> double quotes
\' ---> single quotes
\t --->  tab spce
\0 ---> null(after nothing)
\b ---> backspace

print()
print(" \'Livewire\" ")
print("\tlive\n\n\0wire")
print("Livewire")


Example:
========
a=10
print(a)
print("a : ",a)

name="Livewire"
print(name)
print("name : ",name)

a=10
b=20
c=30
print("a : ",a," b : ",b," c : ",c)
#a=10 b=20 c=30

#print(a,b,c,a+b+c)
print(a,"+",b,"+",c,"=",a+b+c)
print(a,b,c,sep="+",end="=")
print(a+b+c)


print("%d + %d + %d"%(a,b,c))
print("a : {}  b : {}  c: {}".format(a,b,c))

