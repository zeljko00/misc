'''
Handle complex numbers easily.

Classes:

    Complex

Functions:

    example(arg1,arg2) -> int

Misc variables:

    variable
'''
# the docstrings for Python modules should list all the available classes, functions, objects and exceptions
# that are imported when the module is imported; they should also have a one-line summary for each item
# they are written at the beginning of the Python file
class Complex:
    """
       A class to represent a complex number.

       ...

       Attributes
       ----------
       real : int
           real part of complex number
       comp : int
           imaginary part of complex number
       Methods
       -------
       conjugate():
           Conjugates complex number.
       """
    def __init__(self,a,b):
        """
               Constructs all the necessary attributes for the complex number object.

               Parameters
               ----------
                   a : int
                       real part
                   b : int
                       imaginary part
               """
        self.real=a
        self.comp=b
    def __add__(self, other):
        return Complex(self.real+other.real,self.comp+other.comp)
    def __str__(self):
        """Takes no arguments and returns string representation of complex number."""
        # single line docstring for function/method format: Takes ARGS returns RESULT.
        return str(self.real)+" + "+str(self.comp)+"j"
    def conjugate(self):
        self.comp=self.comp*(-1)
a=Complex(1,1)
b=Complex(2,2)
print(str(a+b))

def add(arg1,arg2):
    '''
        Returns the sum of two decimal numbers.

                Parameters:
                        arg1 (int): A decimal integer
                        arg2 (int): Another decimal integer

                Returns:
                        result (int): The sum of arg1 and arg2
        '''
    result=arg1+arg2
    return result