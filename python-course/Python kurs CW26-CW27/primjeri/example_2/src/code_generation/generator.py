
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from code_generation.settings import DESTINATION, TEMPLATES_ROOT

import os
import time

class CodeGen(object):
    """
    CodeGen example no. 2: using includes and lists
    """
    
    def __init__(self, author):
        """
        Constructor        
         
        Args:
            author: author name          
        """
        self._author = author   
        

    def generate(self, file_name, functions):
        """
        Activates code generation
        
        Args:
            file_name: name of a generated file 
            functions: list of functions to generate code for    
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
        data = {}
        data["author"] = self._author
        data["date"] = time.strftime("%d.%m.%Y %H:%M:%S")
        data["functions"] = functions
        
        template.stream(data).dump(destination_path)        
        return True