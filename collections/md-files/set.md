set:5
----
-> unordered collection of unique and immutable objects
-> set is delimited by { and }
-> single comma separated elements

Example:
s = {10,20,30,45,65,70}

-> to create empty set we have to use set() constructor
-> {} -> empty dictionary

-> set can be created from other iterables. duplicates will be discarded
s= set([2,4,6,5,7,8,9,4,2,2,2,9])
-> oftenly used to remove the duplicates
-> sets are iterable but order is arbitrary
Example:
     for i in s:
         print(i)

->add(item) to insert a single element
s.add(50)
->To add multiple elements use update(items) passing any iterable series
s.update([5,63,784,78,95,5,63])

-> remove(item) item should be presented otherwise keyError will be thrown
s.remove(5)
s.remove(999) -> throws KeyError

->discard(item) if item doesnot exists then it won't throw any error
s.discard(999)



