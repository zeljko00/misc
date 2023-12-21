"""
Core contains classes that defines language metamodel.
"""

from collections import OrderedDict
from model.exceptions import NameAlreadyExists, ElementDoesNotExists, MismatchedNumberOfParameters

class NamedElement(object):
    """
    Base class for all elements that have name (variable, parameter, function, module...) 
    """
    def __init__(self, name, **kwargs):
        """
        NamedElement Constructor
        Args:
            name: name of the element
        """
        #TODO: proveriti da li ime odgovara konvenciji C jezika za davanje imena!
        super(NamedElement, self).__init__(**kwargs)
        self.name = name
        
class TypedElement(object):
    """
    Base class for all elements that have type (variable, parameter, function...) 
    """
    def __init__(self, data_type, **kwargs):
        """
        TypedElement Constructor
        Args:
            type: type of the element
        """
        super(TypedElement, self).__init__(**kwargs)
        self.data_type = data_type              
        
class Variable(NamedElement, TypedElement):
    """
    Variable
    """      
    def __init__(self, name, data_type, value=None, **kwargs):
        """        
        Variable constructor 
        """        
        super(Variable, self).__init__(name = name, data_type = data_type, **kwargs) 
        self.value = value       

        
class Parameter(Variable):
    """
    Function parameter
    """      
    def __init__(self, name, data_type, passing_by_value, **kwargs):
        """
        Parameter constructor
        """
        super(Parameter, self).__init__(name=name, data_type=data_type, **kwargs)
        self.passing_by_value = passing_by_value


class NameSpace(NamedElement):
    """
    Base class for elements that can contain instances of NamedElements (function, module...)
    """
    def __init__(self, name, **kwargs):
        """
        Constructor
        """
        super(NameSpace, self).__init__(name, **kwargs)
        # dictionary of NamedElementsf ordered by name:
        self._elements = OrderedDict()    
        
        
    def remove_element(self, name):
        """
        Removes element from namespace
        Args:
            name (string): name of the element to be removed
        """
        if not self._elements.has_key(name):
            raise ElementDoesNotExists(name, self.name)
        self._elements.pop(name)
    
    def add_element(self, element):
        """
        Adds element to the namespace.
        
        Args:
            element (NamedElement): element to add.
        """        
        
        name = element.name
        if name in self._elements:
            raise NameAlreadyExists(name, self.name)        
        self._elements[name] = element
        
    def get_element(self, name):            
        """
        Returns element with the given name or None, if the element doesn't exist
        
        Args:
            name (str): Name of the element to be fetched.
        """     
        if name in self._elements:           
            return self._elements[name]        
        
    def elements(self):
        """
        Returns list of elements contained in ordered dict.
        """
        return self._elements.values()
    
    def variables(self):
        """
        Returning list of function variables
        """
        return [el for el in self._elements.values() if isinstance(el, Variable)]        

    def functions(self):
        """
        Returning list of functions
        """        
        return [el for el in self._elements.values() if isinstance(el, Function)]                      
            
    # helper functions:
    def create_variable(self, name, data_type):
        """
        Creating a variable
        
        Returns: 
            created variable
        """
        var = Variable(name, data_type)
        self.add_element(var)
        return var
        
    def create_function(self, name, data_type, include):
        """
        Creating a function
        
        Returns:
            created function            
        """
        func = Function(name, data_type, include)
        self.add_element(func)
        return func    
       
class Function(NameSpace, TypedElement):
    """
    C Function 
    """
    def __init__(self, name, data_type, include, **kwargs):
        """
        Constructor
        """
        super(Function, self).__init__(name = name, data_type = data_type, **kwargs)
        self.include = include          
        self._parameters = []        
    
    def add_element(self, element):
        """
        Changing a base class method 
        """
        
        super(Function, self).add_element(element)
        if isinstance(element, Parameter):
            self._parameters.append(element)          
        
    def parameters(self):
        """
        Returning list of function parameters
        """        
        return self._parameters
    
    def remove_element(self, name):
        """
        Changing a base class method 
        """
        if not self._elements.has_key(name):
            raise ElementDoesNotExists(name, self.name)
        element = self._elements.pop(name)  
              
        if isinstance(element, Parameter):
            self._parameters.remove(element)
            
     
class FunctionCall(object):
    """
    Function call - containes reference to function and list of values for its parameters    
    """      
    def __init__(self, function, result):
        """        
        Value constructor
        Args:
            function (Function): a function to be called
            result (str): a name of a variable that will hold result of the function
        """  
        self.function = function
        self.result = result
        # list of parameter values converted to strings:
        self.param_values = []
        
#TODO:                 
# Razmisliti o radu sa vise modula gde samo jedan ima main
# Razmisliti o uvodjenju metaklase Project (ili Program) koja poseduje listu modula

class Module(NameSpace):
    """
    C Module 
    """
    def __init__(self, name, do_main=False, **kwargs):
        """
        Constructor
        
        Args:
            name: name of the module            
        """
        super(Module, self).__init__(name, **kwargs)
        # calling sequence specifies main:        
        self.calling_sequence = []
        self.do_main = do_main
        self.varijable_za_deklarisat = []
        
    def includes(self):
        """
        Returns list of includes for this module
        """
        include_set = set(f.include for f in self.functions())
        return list(include_set)

    def add_call(self, function_name, result, *args):
        """
        Specifying a call to a function

        Args:
            function_name: name of a function to call
            result name of a variable which will hold result
            *args: list with parameter values

         Example: add_call("razlika", "x3", "10", "8")
                  add_call("suma", "res", "x3", "x4")
        """
        # performing some checks:
        function = self.get_element(function_name)
        if function is None:
            raise ElementDoesNotExists(function_name, self.name)

        result_var = self.get_element(result)
        if result_var is None:
            raise ElementDoesNotExists(result, self.name)

        func_call = FunctionCall(function, result)
        self.calling_sequence.append(func_call)

        if len(args) != len(function.parameters()):
            raise MismatchedNumberOfParameters(function.name, str(args))
        i = 0
        # TODO:
        for index, arg in enumerate(args):
            var = self.get_element(arg)
            if var is not None:
                if not isinstance(var, Variable):
                    raise Exception("not Variable")
                self.varijable_za_deklarisat.append(var)
            else:  # broj je
                if not function._parameters[index].passing_by_value:
                    raise Exception("ne moze broj u passing by ref")

        # Ako se kao vrednost parametra navede promenljiva, proveriti da li je
        # promenljiva deklarisana!
        # Proveriti da li se parametar i prosledjena vrednost slazu po tipu i
        # nacinu prenosa vrednosti!
        for p in enumerate(function.parameters()):
            # every parameter must have value:
            arg_value = args[i]
            func_call.param_values.append(arg_value)
            i += 1
