functions:
----------
-> functions will be created by using 'def' keyword and method name parenthesis to take arguments and ':' to start new block

Syntax: 
  def function_name(param1,param2,..):
       function_body.....
-> calling a function function_name(arg1,arg2)	   
Example: 
  def sqaure(number):
     return number*number
	
>>> sqaure(5)
25

-> we can import multiple other module functions at a time
Example: from module_name import (function1,function2,..) 
         from module_name import *

-> if we don't return any value from the function then default return is 'None' type		 
CommandLine Arguments:
----------------------
-> to get command line arguments we have to import sys module
-> to get the arguments we have to use argv[] list from sys module
-> argv[0] is the module_name
Example:
    python module_name.py argv1,argv2,...
    import sys
	String firstArg = sys.argv[1]
-> for advanced concepts look into the Python Standard Library: argparse

DocStrings:
-----------
-> DocStrings used to create a documentation
Syntax:
    """ documentation info """
-> read Google python style guide
->module level DocStrings will be written at the first statement of the module file
-> function level DocStrings will be first line of the function



