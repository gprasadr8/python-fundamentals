Objects:
--------
-> when we assign a value to the variable for example: x=10 then an integer object will be created with value=10. if we reassign the value x=20 then it will cteate a new integer object with value=20 and value=10 object will be garbage collected by python because in python integers are immutable objects

id():
-----
-> id(object) built-in function returns a unique identifier which is unique and constant for the life time of the object

-> id() deal with the objects not with the references
-> 'is' property is used to check whether two objects has same id() values

Example1: immutable objects

x=10
y=10 
x == y True
x is y True
y = 20
x ==y False
x is y False

Example2: mutable objects

x = [10,20,30]
y = [10,20,30]
x == y True ==> content is equal
x is y False ==> two different objects(two different id())

-> in python there is no variables it's only named references to the object
Example:
x=10
x is the named reference to the integer object whose value=10

Value equality vs identity:
---------------------------
Value:  both objects have equal content
identity: both references pointing to the same object

Argument Passing:
------------------
-> when we are passing arguments to the function python will create a new reference for the same object with given argument name. If the argument object changes then the calling function object will be reflected.
-> pass by reference: the value of the reference is copied not the value of the object

Functions optional arguments:
----------------------------
-> If we pass default value to the functional argument then it will become optional argument
-> default value arguments should be defined at the end of the function arguments
Example:
    banner(message,border='-'):
	      line= border*len(message)
		  print(line)
		  print(message)
		  print(line)

    >>> banner("Hello!, This is border function")
	>>>banner("Hello!,",'*')
	
Positional Arguments vs keyword arguments:
------------------------------------------
-> Positional Arguments is passing arguments only with values of the argument and without the keyword(argument names)
-> For Keyword Arguments we need to pass both argument name and value
Example:
     banner(message,border='-'):
	      line= border*len(message)
		  print(line)
		  print(message)
		  print(line)
		  
	 banner("Hello!,","*") ==> This is called positional arguments
	 banner(message="Hello!",border='*') => keyword arguments
-> if we are passing all arguments are keyword arguments then no need to maintain order of the arguments	 
Example:
    banner(border='*',message="Hello")
-> if we are using the combination of positional arguments and keyword arguments then keyword arguments should be passed at the end
Example:
      banner("Hello!",border='-')

-> default value arguments will be evaluated only once for the fuction. So we should use only immutable objects as a default values

Example:
		import time
        getCurrentDate(def_time=time.ctime())
			print(def_time)
     getCurrentDate() -> it will display the current time t1
	 getCurrentDate() -> if we call same method after 10 secs it will display same time t1
	 
-> for default values we can user int, str or None objects

Type System:
------------
-> python has strong dynamic typing system means In dynamic type system object types only resolved at runtime.
Example:
     def add(a,b):
	     return a+b
	
	add(5,6)
	add(3.1,4.1)
	add("hello","world")
	add([1,2],[5,0,6])
	
-> this is called as dynamic typing. for add method we didn't mension the type of the object. it will evaluated at runtime.

-> Object references have no type
Example:
name = "Hello"
here name type is not defined. later on we can use same name reference to different type of object
name = ["john","Mark"]

Python named scopes:
--------------------
-> Four types of scopes in python
 1. Local = defined inside the current function
 2. Enclosing = any and all enclosing functions
 3. Global = will be defined at the top level of the module
 4. Built-in = Provided by the python built-in modules
 
-> check ../images/module_scope_names.PNG  and local_scope_names.png

-> to rebind a global name to the local scope then we have to use global keyword before rebind. check rebind_local_scope.png

Everything is an Object:
-------------------------
-> In python everything is an object like primitive type objects,functions are objects,modules are objects and so on
-> type(object_name) will be used to check the object type
-> dir(object_name) will be used to get the attributes of the module

 
