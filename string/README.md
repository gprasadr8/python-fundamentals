string:
-------
-> homogeneouse immutable sequence of unicode code points(characters)
-> strings can be written in '' or ""
-> to display multiline strings we can use triple quotes '''some string ''' or """ some String """ or escape sequence \n "first line \n second line"
-> to create raw string without escape sequences we need to prefix string with 'r'. path=r'C:\Users\userId\Documents\hello.pdf'
-> string in python is sequence type. so we can access the characters by using index
  Example: name='Prasad'
           print(name[3])
-> there is no character data type in python. characters are simply one element strings
-> 'this is a long string' and 'a' this is a small string
-> strings have lot of built-in methods. please check standard library for string or check help(str) in REPL
-> len(str) gives number of code points(characters)
-> the '+' operator used for string concatination
Example: 
   "Hello"+"! "+"world" => "Hello! World"
->String has join() method to concatenate the strings
->we can call join() method on separator string
Example:
greeting = ";".join(["Hello","! ","World"])=> 'Hello;! ;World'
greeting = "".join(["Hello","! ","World"])=> 'Hello! World'
->again we can use split method to get previous list
greeting.split(;) => ["Hello","! ","World"]

-> the partition() will devide the string into three around a separator: prefix,separator,suffix
Example: 
"unforgetable".partition("forget") => ('un', 'forget', 'able')
-> partition returns tuple object. so we can unpack the tuple
prefix,separator,suffix = "unforgetable".partition("forget")
print(prefix) => un
print(separator) => forget
print(suffix) => able

->Use underscope as a dummy name for the separator
departure,_,arrival = "Paris-London".partition('-')
print(departure) => Paris
print(arrival) => London

-> user format() to insert values into strings
-> Replacement fields delimited by { and }
-> integer field names matched with the positional arguments
-> field name can be used more than once
Example:
"The age of {0}, is {1}. {0}'s birthday on {2}".format('Fred','20','December 10')
=> "The age of Fred, is 20. Fred's birthday on December 10"
-> Field names can be ommited if used in sequence
Example: "Reticulating spline {} of {}. ".format(4,23) => 'Reticulating spline 4 of 23. '

-> Named fields can matched with keyword arguments
Example:
"Current position {latitude} {longitude}".format(latitude="60N",longitude="5E") 
=>'Current position 60N 5E'

-> access values through keys or indexes with square brackets in the replacement field
Example:
 pos = (65.2,23.1,82.2)
 "Galactic position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos)
 => 'Galactic position x=65.2 y=23.1 z=82.2'
 
->access attributes of the object by using dot in the replacement field
Example:
import math
"Math constants: pi={m.pi}, e={m.e}".format(m=math) => 'Math constants: pi=3.141592653589793, e=2.718281828459045'
-> user help(str) to list all the attributes in string


bytes:
------
-> bytes are similar to the strings
-> immutable sequences of bytes
-> bytes are used for raw binary data and fixed with single byte character encoding such as ASCII
-> byte literals are prefixed with 'b'. b'bytes data' or b"bytes data"
-> it supports most of the operations like string
-> str->encode = bytes and bytes->decode = str
->bytes_data ="hello world".encode("utf-8")
->str_data = bytes_data.decode("utf-8")
-> Files, Network streams and Http Response are transffered through the bytes stream

