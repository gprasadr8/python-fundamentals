list:
-----
-> heterogeneous mutable sequence
-> lists are delemited by square brackets and seperated by comma
syntax: 
    list_name = ['element1','element2','element3',...]
Example:
	names = ["John","Peter","Mark"]
	
-> list can be retrieved by zero based index
Example:
 print(names[0]) 
 print(names[2])
output:
 John 
 Mark
 
-> We can use negative indexes to retrieved the elements from the end
-> the last element is at index -1
Example:
  print(names[-1])
  print(names[-3])
  
output:
  Mark
  John
->slicing extracts the part of the list
Syntax:
   slice = seq[start:stop]
   
-> slice range is half-open stop not included
Example:
	names[0:2]
output:
    ["John","Peter"]

-> Omitting the stop index slices to the end
Syntax:
   slice_to_end =sequence[start:]
Example:
   names[1:]
Output:
    ["Peter","Mark"]
-> we can have full slice as well 
syntax:
    slice = sequence[:]
Example:
    names[:]
Output:
    ["John","Peter","Mark"]
   
-> full slice is useful to copy the list


copying lists:
--------------
-> Full slice:   new_list = sequence[:]
-> copy() method new_list = sequence.copy()
-> list() constructor  new_list = list(sequence)
-> please follow the shallow copy images for better understanding

-> repeat the list using the * operator
Example:
   list = [10,20]
   list1 = list*3
Output:
   list1 = [10,20,10,20,10,20]

Finding elements in list:
-------------------------
-> we can access by using zero based index
-> count(element) will return number of mathing elements in the list
list1.count(10) => 3

-> check the membership of the element in the list by using 'in' and 'not in' 
10 in list1 => True
30 not in list => True

-> to delete the element in list use del 
Syntax:  del sequence[index]
Example: del list1[2]

->to remove by element in the list 
Syntax:  sequence.remove(element) 
Example: list.remove(10)
->remove method throws an error if the element not found

-> inserts the elements by using insert method
Syntax: sequence.insert(index,element)

-> concatenate the lists by using + operator
Example:
   list1 = [10,20,30]
   list2 = [40,50,60]
   list3 = list1+list2
   
-> to extend the list we can use '+=' operator or extend() method
Example:
    list1 += list2
    list1.extend(list2)
->	
