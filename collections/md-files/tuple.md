tuple:
------
-> heterogeneous immutable sequence
syntax:
t = (value1,value2,...valuen)
Example:
t = (10,20,30,40)
-> tuple is an immutable object. New object will be created for every change
->we can combine multiple tuple by using '+' sign
Example:
t1 = (10,20)
t2 = (30,40)
print(t1+t2)

-> we can access the tuple by using zero based index
t = (10,20,30)
print(t[0]) => 10
print(t[1]) => 20
-> We can use built-in len() to find the length of the tuple
Example:
t = (10,20,30)
len(t) =3

-> we can iterate the tuple by using for loop
Example:
t = (10,20,30)
for item in t:
    print(item)
	
-> tuple can be repeated by using multiplication(*) operator
Example:
t = (10,20,30)
print(t*2) => (10,20,30,10,20,30)
-> To create single element touple we should give trailling comma
syntax: 
t1 = (10) -> this is consider as a int
t2 = (10,) -> type(t2) is tuple

-> To create empty tuple we can use empty parenthesis
syntax:
t = () -> type(t)=tuple

-> tuples can have nested tuples
Example:
t = ((10,20),(30,40))

-> delimiting parenthesis are optional for one or more elements
p = 1,2,3,4,5,6
type(t)=>tuple
print(t) => (1,2,3,4,5,6)

->this feature is often used when we are returning multiple values from the function
Example:
def minmax(items):
    return min(items),max(items)
minmax([2,6,7,9,1,7,3]) => (1,9)

-> tuple unpacking allows us to destructure directly into named references. For example we can assign min and max returns to object references 
Example:
lower,upper = minmax([2,6,7,9,1,7,3])
print(lower) => 1
print(upper) => 9

-> a,b = b,a is the idiomatic python swap	
-> we can create a tuple from other collections by using tuple(iterable)
Example: 

t = tuple([10,20,30,40])
t = tuple("hello world")

-> to check whether tuple contain particular element or not, we can use 'in' or 'not in' operators
Example:
5 in (10,3,5,8,9) => True
20 in (10,3,5,8,9) => False
20 not in (10,3,5,8,9) => True


