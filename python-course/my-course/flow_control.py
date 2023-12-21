from inspect import currentframe, getframeinfo
def if_flow(a,b):
    sign="?"
    if a>b:
        # modifying x variable from outer scope - in fact if/for/while/match don't have its own scope
        sign=">"
        # creating local variable, available only in this function
        flag=True
        print(getframeinfo(currentframe()).lineno,": ",a,">",b)
    elif a<b:
        sign = "<"
        print(getframeinfo(currentframe()).lineno,": ",a,"<",b)
        flag = True
    elif a==b:
        sign = "="
        flag = True
        print(getframeinfo(currentframe()).lineno,": ",a,"=",b)
    else:
        flag = True
        # do nothing
        pass
    print("sign=",sign)
    print("flag=",flag)

def for_flow(iterable):
    for item in iterable:
        print(getframeinfo(currentframe()).lineno,": ",iterable)
    else:
        # for and while loops can have else clause
        # else block is executed after last iteration/when condition becomes false
        # else block is not executed when loop is exited with break statement
        print("End of for loop!")

# range(start,end,step) returns arithmetic regression that starts at start, ends at end-1, with specified step
# range() returns iterable object, not particularly list
def for_flow_range(start,end, step):
    for i in range(start,end,step):
        print(getframeinfo(currentframe()).lineno,": ",i)

# iterating through range of data collection elements' indexes
def for_index_flow(iterable):
    for index in enumerate(iterable):
        print(getframeinfo(currentframe()).lineno,": ",index)

def for_zip_flow(iterable1,iterable2):
    for tuple in zip(iterable1,iterable2):
        print(getframeinfo(currentframe()).lineno,": ",tuple)

def while_flow(n):
    while n>0:
        print(getframeinfo(currentframe()).lineno,": ",n)
        n=n-1

def match_flow(tuple):
    match tuple:
        # matching tuples with 3+ elements
        # rest of tuple is bind to rest variable
        # *_ instead of *rest won't fetch rest of tuple/sequence
        case (x,y,z,*rest):
            print("CASE 0", "- rest:",rest)
        # similar to unpacking assignment
        case (0,0) | (0,1) | (1,0):
            print("CASE 1")
        # binding tuple second value to variable y
        case (0,y):
            print("CASE 2")
        case (x,0):
            print("CASE 3")
            # setting up guard condition
        case (x,y) if x==y:
            print("CASE 4")
        case(x, y):
            print("CASE 5")
        # underscore behaves as wildcard - default case
        # default case in this particular example will never be executed
        case _:
            print("DEFAULT CASE")

if_flow(4,7)
for_flow([1,2,3,4])
for_index_flow([4,3,2,1])
for_flow_range(1,10,1)
for_zip_flow([1,2,3],[4,5,6])
while_flow(10)
match_flow((3,5))
match_flow((3,5,6,7))