dictionary:
----------
-> unordered mapping from unique, immutable keys to mutable values
->  dictionaries are delemited by { and }
-> key-value pair comma separated
->corresponding keys and values joined by colon
-> to create empty dictionary we can use empty curly braces
emp = {}

Example:

emp = {
  "name": "John",
  "emp_id":12342,
  "salary":"$1000"  
}

->values are accessible by keys
Example:
emp['name'] 
emp['salary']

Output:
John
$1000

->dictionaries can be created by using constructors
Example: emp = dict(name='John',id=12345,salary='$10000')

-> we can create dictionary from other collection
Example: emp = dict([('name','John'),('id',12345),('salary','$10000')])

-> to copy the dictionary d.copy() method or simply dict(d) constructor
-> extend the dictionary by using update()
Example:
dept = (name='Sales',id='SL120')
emp = emp.update(dept)

Iteration:
----------
-> Iteration is over keys
Example:
for key in emp:
    print("{k} => {v}".format(k=key,v=emp[key]))

-> we can use tuple unpacking to iterate through key-value pair

for key,value in emp.items():
    print("{k} => {v}".format(k=key,v=value))
	
->we can use 'in' and 'not in'  to check the availability of the keys
Example:
   print('salary' in emp) => True
   print('address' in emp) => False
   print('address' not in emp) => True
->use del keyword to remove by key
Syntax: del dict[key]
Example: del emp['salary']

-> keys must be immutable but values can be mutable
->the dictionary itself mutable. we can add or remove items from dictionary
Example:
del emp['salary']
emp['dept_name'] = 'Sales'

-> we can use pretty print to display dictionaries
from pprint import pprint as pp
pp(emp)   
