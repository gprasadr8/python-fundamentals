""" this is the module level DocString """
import math

def sqrt(number):
    """ This method will calculate sqrt of the given number
	  Args:
	      integer number
	  Returns:
	      sqrt of the given number
	"""
    return math.sqrt(number)
	
if __name__=="__main__":
    print("execute 'help(doc_string_demo)' on REPL you will see doc strings")
    sqrt(9)