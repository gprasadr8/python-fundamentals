range:
------
->range is sequence of arithimatic progression of integers
->range will be created by using constructors
constructors:
range(stop) => by default it will take start=0
range(start,stop) => by default it will increase by 1 means (step=1)
range(start,stop,step)
Example:
range(5) => 0,1,2,3,4
range(10,15) =>10,11,12,13,14
range(0,10,2)=>0,2,4,6,8

-> range can be used to start loop counters
for i in range(5):
    print(i)
	
=> 0 1 2 3 4

-> go through range_constructors.png file
->range can be used with other collection
Example:
 list(range(0,5)) => [0,1,2,3,4]
 tuple(range(0,5)) => (0,1,2,3,4)
 
-> some times we need a counter then we have to use enumerate()
->prefer enumerate for counters
-> enumerate() yields (index,value) tuples
Example:
list = [10,20,30,40,50]
for pair in enumerate(list):
    print(pair)
	
=> (0,10) (1,20) (2,30) (3,40) (4,50)

-> combine with the tuple unpacking
Example:
list = [10,20,30,40,50]
for index,value in enumerate(list):
    print("index = {i}, value={v}".format(i=index,v=value))
output:
index=0 , value=10
index=1 , value=20
index=2 , value=30
index=3 , value=40
index=4 , value=50