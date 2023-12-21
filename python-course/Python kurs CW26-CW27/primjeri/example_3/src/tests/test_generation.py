
import unittest
from code_generation.generator import CodeGen
from model.core import Module, Function, Parameter, Variable

class TestCodeGen(unittest.TestCase):    

    def setUp(self):
        """
        Setting up test
        """
        self.code_gen = CodeGen("Pera Petrovic")        
        
    def test_generate (self):
        """
        Testing code generation
        """    
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
        m.add_call("razlika", "res1", "24", "5")
        m.add_call("proizvod", "res1", "36", "17")


        generated = self.code_gen.generate("main.c", m) 
        self.assertEqual(generated, True)      
