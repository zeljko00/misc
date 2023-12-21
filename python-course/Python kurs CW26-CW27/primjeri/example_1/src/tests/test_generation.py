
import unittest
from code_generation.generator import CodeGen

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
        generated = self.code_gen.generate("main.c") 
        self.assertEqual(generated, True)      
             
        
    
        
