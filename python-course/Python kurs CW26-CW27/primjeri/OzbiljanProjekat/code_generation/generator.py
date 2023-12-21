
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from code_generation.settings import DESTINATION, TEMPLATES_ROOT

import os
import time
from model.podaci import getPodaci

class CodeGen(object):
    """
    CodeGen example no. 3: "metamodel" introduced  
    """
    
    def __init__(self, author):
        """
        Constructor        
         
        Args:
            author: author name          
        """ 
        self._author = author

    def generate(self, file_name, modules):
        """
        Activates code generation
        
        Args:
            file_name: name of a generated file
            model: list of model to generate code for  
        Returns: 
            True, if code is successfully generated, None otherwise
        """
        
        #loader for templates from disk:        
        file_system_loader = FileSystemLoader([TEMPLATES_ROOT])
        
        destination_path = os.path.join(DESTINATION, file_name)                                   
                         
        env=Environment(loader=file_system_loader, trim_blocks = True)  
                
        # getting main template                 
        template = env.get_template("main.template")
                        
        # dictionary with data for code generator:                        
        for key in modules:
            destination_path = "%s.c" % os.path.join(DESTINATION,
                                                     modules[key].name)
            data = {}
            data["author"] = self._author
            data["date"] = time.strftime("%d.%m.%Y %H:%M:%S")  
            data["main"] = modules[key]
            
            
            template.stream(data).dump(destination_path)        
        return True

CodeGen("autor").generate("c1.c", getPodaci())