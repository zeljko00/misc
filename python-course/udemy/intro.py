# this is comment
import math
from inspect import currentframe, getframeinfo

# newline represents end of statement  - row = statement
var1=23.12
var2=11.7

# newline is not end of statement if ()/[]/{} braces are previously opened
var3=math.sqrt(math.sin(0.23)
            +math.cos(0.45))

# one statement can be spread across multiple rows using backslash sign
"string value".capitalize() \
    .lower()

# number literals
var4=1.23
var5=0xcfd
var6=5+4j
var7=.67
# string literals
"string literal"
'also string literal'


print("========================VARIABLE DATA=========================")
var8="test"
# id() returns memory address of specified variable
print(str(getframeinfo(currentframe()).lineno),": ",id(var8))
# type() returns type of specified variable
print(str(getframeinfo(currentframe()).lineno),": ",(type(var8)))

# variable comparison
print("=====================VARIABLE COMPARISON======================")
# variable identity (memory address) comparison
var9="a"
var10=var9
var11="a"
var12=math.sqrt(9)
var13=math.sqrt(9)
# variables are pointing to same memory location
print(str(getframeinfo(currentframe()).lineno),": ",var9 is var10)
# variables have same literal as values
print(str(getframeinfo(currentframe()).lineno),": ",var9 is var11)
print(str(getframeinfo(currentframe()).lineno),": ",var9 is var12)
# values of var12 and var13 are same but are not literals,
# so there vars are located on different memory addresses
print(str(getframeinfo(currentframe()).lineno),": ",var12 is var13)

# variable value comparison
var14="var"
var15="vaR"
print(str(getframeinfo(currentframe()).lineno),": ",var14==var15)

#variable type comparison
var16="string1"
var17="string2"
var18=1
print(str(getframeinfo(currentframe()).lineno),": ",type(var16)==type(var17))
print(str(getframeinfo(currentframe()).lineno),": ",type(var16) is type(var17))
print(str(getframeinfo(currentframe()).lineno),": ",type(var16)==type(var18))
print(str(getframeinfo(currentframe()).lineno),": ",type(var16) is type(var18))

# type conversions
print("=======================TYPE CONVERSIONS========================")
var19=int("11",16) # 16 represents base
print(str(getframeinfo(currentframe()).lineno),": ",var19, type(var19))
var20=float("11.45")
print(str(getframeinfo(currentframe()).lineno),": ",var20, type(var20))
var21=complex(3,6)
print(str(getframeinfo(currentframe()).lineno),": ",var21, type(var21))
var22=str([1,2,3])
print(str(getframeinfo(currentframe()).lineno),": ",var22, type(var22))
var23=chr(123)
print(str(getframeinfo(currentframe()).lineno),": ",var23, type(var23))
var24=ord('c')
print(str(getframeinfo(currentframe()).lineno),": ",var24, type(var24))
var25=hex(16)
print(str(getframeinfo(currentframe()).lineno),": ",var25, type(var25))
var26=oct(16)
print(str(getframeinfo(currentframe()).lineno),": ",var26, type(var26))
var27=bin(16)
print(str(getframeinfo(currentframe()).lineno),": ",var27, type(var27))

# misc
print("=============================MISC=============================")
# evaluating collections as boolean
if []: # only empty collection is false
    print(str(getframeinfo(currentframe()).lineno),": ","True")
else:
    print(str(getframeinfo(currentframe()).lineno),": ","False")
# list as element in another list
list2=[1,2,3]
list3=[list2] # list3 contains reference to list2 as element
list4=list3 * 3
print(str(getframeinfo(currentframe()).lineno),": ",list3)
print(str(getframeinfo(currentframe()).lineno),": ",list4)
list3[0][1]=22
print(str(getframeinfo(currentframe()).lineno),": ",list3)
print(str(getframeinfo(currentframe()).lineno),": ",list4)

string_var="How are "
# auto string literal concatenation
print("How are "
      "you?")
# doesn't work with string vars
# print(string_var "you?")

print("===========================VARIABLES==========================")
a=1
def local_var():
    a=2
local_var()
print(getframeinfo(currentframe()).lineno," : ",a)
def global_var():
    global a
    a=3
global_var()
print(getframeinfo(currentframe()).lineno," : ",a)
