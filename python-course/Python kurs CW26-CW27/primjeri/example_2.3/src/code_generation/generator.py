
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from code_generation.settings import DESTINATION, TEMPLATES_ROOT

import os
import time

class CodeGen(object):
    """
    CodeGen example no. 2.3: added support for little internal DSL for functions specification  
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
        
        # creating list of libraries to include (duplicates removed): 
        include_set = set(f["include"] for f in functions)
        data["includes"] = list(include_set) 
        
        
        template.stream(data).dump(destination_path)        
        return True