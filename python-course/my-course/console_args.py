import sys
# args sent through console are available through sys.argv list
# starting from index 1
# sys.argv[0] - script_name/module_name/"-c"/""
print(sys.argv)

list=[1,2,3,4,5]
list2=list[1:3]
print(list)
print(list2)
list[1:3]=[222,333]
print(list)
print(list2)
list2[1]=33
print(list)
print(list2)
