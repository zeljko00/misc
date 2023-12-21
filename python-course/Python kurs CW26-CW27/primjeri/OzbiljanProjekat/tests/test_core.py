
import unittest
from model.core import Module, Function, Parameter, NameSpace, Variable
from model.exceptions import ElementDoesNotExists, NameAlreadyExists, MismatchedNumberOfParameters



class TestCodeGen(unittest.TestCase):       

    def test_namespace (self):
            
        n = NameSpace("name_space")
        
        # checking if parameters are properly added:
        x1 = Parameter("x1", "float", True)
        x2 = Parameter("x2", "float", True)
        
        n.add_element(x1)
        n.add_element(x2)        
        
        x3 = Parameter("name_space", "float", True)
        self.assertRaises(NameAlreadyExists, n.add_element, x3)        
        
        self.assertEqual(x1, n.get_element("x1"))      
        self.assertEqual(x2, n.get_element("x2"))        
        
        self.assertEqual(2, len(n.elements()))
        
        n.remove_element("x1")        
        self.assertEqual(None, n.get_element("x1"))
        self.assertEqual(1, len(n.elements()))
        
        # trying to add duplicate element:
        self.assertRaises(NameAlreadyExists, n.add_element, x2)        
        
        # trying to remove non-existing element:
        self.assertRaises(ElementDoesNotExists, n.remove_element, "x3")
        
        
    def test_function (self):
            
        f = Function("sum", "float", "math.h")
        
        # checking if parameters are properly added:
        par1 = Parameter("par1", "float", True)
        par2 = Parameter("par2", "float", True)
        
        f.add_element(par1)
        f.add_element(par2)                               
        
        var1 = Variable("var1", "float")
        var2 = Variable("var2", "float")
        var3 = Variable("var3", "float")
        
        f.add_element(var1)
        f.add_element(var2)
        f.add_element(var3)
        
        self.assertEqual(set([var1, var2, var3]), set(f.variables()))
        self.assertEqual(set([par1, par2]), set(f.parameters()))               
        
        f.remove_element("par1")
        self.assertEqual([par2], f.parameters())
        
        f.remove_element("par2")
        self.assertEqual([], f.parameters())
        
        
    def test_callable (self):
        
        m = Module("glavni")
            
        f = Function("suma", "float", "math.h")
        f.add_element(Parameter("x1", "float", True))
        f.add_element(Parameter("x2", "float", True))
        
        m.add_element(f)                
                
        f = Function("razlika", "float", "math.h")
        f.add_element(Parameter("x1", "float", True))
        f.add_element(Parameter("x2", "float", True))
                
        m.add_element(f)                 
        
        f = Function("proizvod", "float", "math.h")
        f.add_element(Parameter("x1", "float", True))
        f.add_element(Parameter("x2", "float", True))
                
        m.add_element(f)
        
        m.add_element(Variable("res1", float))
        m.add_element(Variable("res2", float))
        m.add_element(Variable("res3", float))        
        
        m.add_call("suma", "res1", "5", "15")
        m.add_call("razlika", "res2", "24", "5")
        m.add_call("proizvod", "res3", "36", "17")
        
        self.assertEqual(len(m.calling_sequence), 3)        
        
        self.assertRaises(MismatchedNumberOfParameters, m.add_call, "suma", "res1", "5" )
        
        self.assertRaises(MismatchedNumberOfParameters, m.add_call, "suma", "res1", "5", "12", "24" )           
        
        self.assertRaises(ElementDoesNotExists, m.add_call, "nepostojeca_funkcija", "res1", "5", "12", "24" )
        
        self.assertRaises(ElementDoesNotExists, m.add_call, "suma", "nepostojeca_promenljiva", "5", "12", "24" )                    
        
        
        
        
              
