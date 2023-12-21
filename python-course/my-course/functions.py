import time,math
from inspect import currentframe, getframeinfo
print("===========================FUNCTIONS==========================")
# global variables and variables of enclosing functions cannot be directly assigned a value within a function
# (unless, for global variables, named in a global statement, or, for variables of enclosing functions,
# named in a nonlocal statement), although they may be referenced

# optional arguments - can appear only at the end of args list
def func1(first_arg, optional_arg=10):
    print(getframeinfo(currentframe()).lineno," : ",first_arg)
    print(getframeinfo(currentframe()).lineno," : ",optional_arg)

# warning: default value is evaluated only once - this makes a difference when the default
# is a mutable object (list, dictionary, instance of most classes, ...)
# for example, the following function, if called without specifying value for list argument,
# accumulates the element arguments passed to it on subsequent calls:
def append(element,list=[]):
    list.append(element)
    return list
print(getframeinfo(currentframe()).lineno," : ",append("element1"))
print(getframeinfo(currentframe()).lineno," : ",append("element2"))



# variable number of args - tuple
# args is a tuple
def func2(first_arg, *args):
    print(getframeinfo(currentframe()).lineno," : ",first_arg)
    print(getframeinfo(currentframe()).lineno," : ",args)

# default return value is None
def func3():
    print()

# returning more than one result
def func4():
    return ("result1",2,"result3")

func1("first")
func1("first","optional")
func2("first","second","third")
print(getframeinfo(currentframe()).lineno," : ",func3())
print(getframeinfo(currentframe()).lineno," : ",func4())

print("===========================CLOSURES===========================")
def outer_func(arg):
    # nested func that can access variables in enclosing scope is called closure
    # cant be invoked outside of enclosing scope (outside outer function)
    def inner_func():
        print(getframeinfo(currentframe()).lineno," : ",arg)
    # returning nested function as result from outer functions
    # enables calling inner function from other scopes
    return inner_func

# error: inner_func()
closure=outer_func("test")
# calling closure
# although outer function has already executed and argument arg from outer_func should have been destroyed
# closure function can access it afterward
closure()
# memory addresses (references) of enclosed variables are stored in __closure__
print(getframeinfo(currentframe()).lineno," : ",closure.__closure__)

# example - printing odd numbers with closure
# this approach mitigates using a global variable used for storing next odd number
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()
print(getframeinfo(currentframe()).lineno," : ",odd())
print(getframeinfo(currentframe()).lineno," : ",odd())
print(getframeinfo(currentframe()).lineno," : ",odd())
odd2 = calculate()
print(getframeinfo(currentframe()).lineno," : ",odd2())

print("==========================DECORATORS==========================")
# decorators extend function functionality without permanently modifying it

# example - creating decorator that measures func exec time
# func that represents decorator
def exec_time_decorator(func_to_decorate):
    # wrapping function and extending its func
    def wrapper_func():
        start=time.time()
        func_to_decorate()
        end=time.time()
        print(getframeinfo(currentframe()).lineno," : ",func_to_decorate.__name__," - exec time=",end-start,"s")
    # returning decorated and wrapped func
    return wrapper_func
# functions to be decorated
def simple_func():
    time.sleep(1)
    print("Hello from simple func!")
# applying decorator to the function without using python's decorator mechanism
decorated_simple_func =exec_time_decorator(simple_func)
decorated_simple_func()
# applying decorator to the function by using python's decorator mechanism
@exec_time_decorator
def simple_func_decorated():
    time.sleep(1)
    print("Hello from simple func!")
simple_func_decorated()

# example - creating decorator that measures func exec time
# now for functions with one argument
def exec_time_decorator_with_arg(func_to_decorate):
    def wrapper_func(n):
        start=time.time()
        result=func_to_decorate(n)
        end=time.time()
        print(getframeinfo(currentframe()).lineno," : ",func_to_decorate.__name__," - exec time=",end-start,"s")
        return result
    return wrapper_func
@exec_time_decorator_with_arg
def factorial(n):
    time.sleep(2)
    result=math.factorial(n)
    print(getframeinfo(currentframe()).lineno," : ","Factorial of",n, "calculated!")
    return result
print(getframeinfo(currentframe()).lineno," : ",factorial(10))

# example - creating decorator that measures func exec time
# now for functions with any number of argument
def exec_time_decorator_with_args(func_to_decorate):
    def wrapper_func(*args,**kwargs):
        start=time.time()
        result=func_to_decorate(*args,**kwargs)
        end=time.time()
        print(getframeinfo(currentframe()).lineno," : ",func_to_decorate.__name__," - exec time=",end-start,"s")
        return result
    return wrapper_func
@exec_time_decorator_with_args
def sum(a,b,c):
    time.sleep(2)
    result=a+b+c
    print(getframeinfo(currentframe()).lineno," : ","Sum calculated!")
    return result
print(getframeinfo(currentframe()).lineno," : ",sum(1,2,3))

print("==========================GENERATORS==========================")
# simple counter generator
def counter(n):
    count=n
    while count>0:
        yield count
        count-=1
    return
def fruit():
    yield "apple"
    yield "banana"
    yield "orange"
    yield "grapes"
    yield "peach"
    yield "watermelon"
def gen_example():
    print(getframeinfo(currentframe()).lineno," : ","Generator started!")
    yield "Value"
for i in counter(10):
    print(getframeinfo(currentframe()).lineno," : ",i)
for f in fruit():
    print(getframeinfo(currentframe()).lineno," : ",f)
# generator call doesn't call its body logic
generator=gen_example()
print(getframeinfo(currentframe()).lineno," : ","After generator call!")
# first __next()__ call starts execution of generator body
print(getframeinfo(currentframe()).lineno," : ",generator.__next__())

print("==========================COROUTINES==========================")
def containes(pattern):
    print(getframeinfo(currentframe()).lineno," : ","Pattern to look for: ",pattern)
    try:
        while True:
            phrase_to_search=(yield)
            if(pattern in phrase_to_search):
                print(getframeinfo(currentframe()).lineno," : ",phrase_to_search," containes key:",pattern,"!")
            else:
                print(getframeinfo(currentframe()).lineno," : ",phrase_to_search," doesn't containe key:",pattern,"!")
    except GeneratorExit:
        print(getframeinfo(currentframe()).lineno," : ","Stopping generator!")
coroutine=containes("haha")
coroutine.__next__()
coroutine.send("That's funny hahaha!")
coroutine.send("That's not funny!")
coroutine.close()

print("=============================MISC=============================")
def double(x):
    return x*2
numbers=[1,2,3,4,5]
odd_doubles=[double(x) for x in numbers if x%2!=0]
for i in odd_doubles:
    print(getframeinfo(currentframe()).lineno," : ",i)
letters=["a","b","c","d","e"]
# equivalent to
# list=[]
# for x in numbers:
#   for y in letters:
#       return list.append((x,y))
tuples=[(x,y) for x in numbers for y in letters]
for tuple in tuples:
    print(getframeinfo(currentframe()).lineno," : ",tuple)