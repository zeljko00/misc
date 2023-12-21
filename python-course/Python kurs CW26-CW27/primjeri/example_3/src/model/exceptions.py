"""
Custom exceptions
"""

class CoreException(Exception):
    """
    Base class for all core exceptions.    
    """
    
    def __str__(self):
        return self.message
    
    def __repr__(self):
        return self.message       

    
class NameAlreadyExists(CoreException):
    """
    Raised if the name of the element already exists in the namespace.
    """
    def __init__(self, name, namespace):
        super(NameAlreadyExists, self).__init__(self)
        self.message = u'Name "%s" already exists in a namespace "%s"' % (name, namespace)
        
class ElementDoesNotExists(CoreException):
    """
    Raised if the element doesn't exists in the namespace.
    """
    def __init__(self, name, namespace):
        super(ElementDoesNotExists, self).__init__(self)
        self.message = u'Element "%s"  doesn''t exists in a namespace "%s"' % (name, namespace)        
        

class MismatchedNumberOfParameters(CoreException):
    """
    Raised if the element doesn't exists in the namespace.
    """
    def __init__(self, name, parameters):
        super(MismatchedNumberOfParameters, self).__init__(self)
        self.message = u'Mismatched number of parameters "%s" for a function "%s"' % (parameters, name)        
        

        
        