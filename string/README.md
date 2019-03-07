string:
-------
-> immutable sequence of unicode code points(characters)
-> strings can be written in '' or ""
-> to display multiline strings we can use triple quotes '''some string ''' or """ some String """ or escape sequence \n "first line \n second line"
-> to create raw string without escape sequences we need to prefix string with 'r'. path=r'C:\Users\userId\Documents\hello.pdf'
-> string in python is sequence type. so we can access the characters by using index
  Example: name='Prasad'
           print(name[3])
-> there is no character data type in python. characters are simply one element strings
-> 'this is a long string' and 'a' this is a small string
-> strings have lot of built-in methods. please check standard library for string or check help(str) in REPL

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

