"""
Specification of functions we want to generate
""" 

from functions.function_attr import NAME, RETURN_TYPE, INCLUDE, PARAMETERS, PASSING_BY_VALUE, TYPE

#Using defined function attributes errors in specification is minimized:
 
functions = [
             {
              NAME: "zbir",
              RETURN_TYPE: "float",              
              INCLUDE: "math.h",
              PARAMETERS: [
                           {NAME: "x1",
                            TYPE: "float",
                            PASSING_BY_VALUE: True
                            },
                           {NAME: "x2",
                            TYPE: "float",
                            PASSING_BY_VALUE: True
                            },
                           ] 
              },
             {
              NAME: "razlika",
              RETURN_TYPE: "float",
              INCLUDE: "math.h",
              PARAMETERS: [
                           {NAME: "x1",
                            TYPE: "int",
                            PASSING_BY_VALUE: False
                            },
                           {NAME: "x2",
                            TYPE: "int",
                            PASSING_BY_VALUE: False
                            },
                           ]
              },
             {
              NAME: "proizvod",
              RETURN_TYPE: "float",
              INCLUDE: "math.h",
              PARAMETERS:[
                           {NAME: "x1",
                            TYPE: "int",
                            PASSING_BY_VALUE: False
                            },
                           {NAME: "x2",
                            TYPE: "int",
                            PASSING_BY_VALUE: False
                            }
                          ],              
              },
             {
              NAME: "stampa",
              RETURN_TYPE: "void",
              INCLUDE: "stdio.h",
              PARAMETERS:[
                           {NAME: "file_name",
                            TYPE: "char",
                            PASSING_BY_VALUE: False
                            }                           
                          ], 
              },
             ]


