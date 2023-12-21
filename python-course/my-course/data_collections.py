from inspect import currentframe, getframeinfo
print("==========================COLLECTIONS==========================")
# checking if element is present in collection
print(str(getframeinfo(currentframe()).lineno),": ",5 in [1,2,3,4])
print(str(getframeinfo(currentframe()).lineno),": ","key1" in {"key1":1})

# list:
# mutable collection - variable length
# mutable elements
# elements of different types
# = array in Python
print("=============================LIST=============================")
list = [10, "eleven", True]
print(str(getframeinfo(currentframe()).lineno),": ",list)
list[2]=12
list.append(False)
# can't add elements this way
# list[4]=15
print(str(getframeinfo(currentframe()).lineno),": ",list)

# lists support concatenation
print(getframeinfo(currentframe()).lineno,": ", list + ["concatenated_1","concatenated_2","concatenated_3"])

# slicing list returns shallow copy of list
list_slice=list[1:3]
print(getframeinfo(currentframe()).lineno,": ",list_slice)
list_slice[1]="NEW VALUE"
print(getframeinfo(currentframe()).lineno,": ",list)
print(getframeinfo(currentframe()).lineno,": ",list_slice)
list[1:3]=["VALUE2","VALUE2"]
print(getframeinfo(currentframe()).lineno,": ",list)
print(getframeinfo(currentframe()).lineno,": ",list_slice)


# tuple:
# more efficient implementation of list
# immutable collection - fixed length
# immutable elements
# elements of different types
# accessing elements by their indexes
print("=============================TUPLE============================")
tuple=(1, "two", True, 1.23)
print(str(getframeinfo(currentframe()).lineno),": ",tuple)
print(str(getframeinfo(currentframe()).lineno),": ",tuple[3])
# can't modify elements
# tuple[0]=2

# dictionary:
# mutable collection
# mutable values, immutable keys
# collection of pars (key,value)
# values are accessible by their keys
# keys and values can have different types
print("==========================DICTIONARY==========================")
dictionary={ "key1":1, 2:"value2"}
print(str(getframeinfo(currentframe()).lineno),": ",dictionary)
print(str(getframeinfo(currentframe()).lineno),": ",dictionary[2])
dictionary["key1"]="value1"
dictionary["key3"]=3 # adding new key,value pair
dictionary["key4"]=4
print(str(getframeinfo(currentframe()).lineno),": ",dictionary)
del dictionary["key4"]
print(str(getframeinfo(currentframe()).lineno),": ",dictionary)

# sets:
# unique elements
# no order - no indexes
print("==============================SET=============================")
# duplicates are ignored
set1={1,2,"three",3,4,4}
set2={"three",2,7}
print(str(getframeinfo(currentframe()).lineno),": ",set1)
print(str(getframeinfo(currentframe()).lineno),": ",set2)
# union
print(str(getframeinfo(currentframe()).lineno),": ",set1 | set2)
# intersection
print(str(getframeinfo(currentframe()).lineno),": ",set1 & set2)
# difference
print(str(getframeinfo(currentframe()).lineno),": ",set1 - set2)
# symetric difference
print(str(getframeinfo(currentframe()).lineno),": ",set1 ^ set2)

# sequence collections
print("=====================SEQUENCE COLLECTIONS=====================")
list1=[1,2,3,4]
# sequence concatenation - creates shallow copy
list2=list1 + list1
list3=list1 * 3
print(str(getframeinfo(currentframe()).lineno),": ",list1)
print(str(getframeinfo(currentframe()).lineno),": ",list2)
print(str(getframeinfo(currentframe()).lineno),": ",list3)
list1[0]=0
print(str(getframeinfo(currentframe()).lineno),": ",list1)
print(str(getframeinfo(currentframe()).lineno),": ",list2)
print(str(getframeinfo(currentframe()).lineno),": ",list3)
list1[0]=1
# part of sequence - shallow copy
part1=list1[0:3]
part2=list1[0:3:2]
part3=list1[::-1]
# last element has index n-1 and also -1
part4=list1[-2:]
list1[0]=0
print(str(getframeinfo(currentframe()).lineno),": ",list1)
print(str(getframeinfo(currentframe()).lineno),": ",part1)
print(str(getframeinfo(currentframe()).lineno),": ",part2)
print(str(getframeinfo(currentframe()).lineno),": ",part3)
print(str(getframeinfo(currentframe()).lineno),": ",part4)
# sequence length
print(str(getframeinfo(currentframe()).lineno),": ",len(list1))
# destructuring sequence
v1,v2,v3,v4=list1
# not enough elements
# v1,v2,v3=list1
print(str(getframeinfo(currentframe()).lineno),": ",v1,v2,v3,v4)

