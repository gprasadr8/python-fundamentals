print("if statements demo started...")
if True:
    print("if True") 
	
h=100
if h>50:
    print("number greater than 50")
elif h<20:
    print("Number is lesser than 20")
else:
    print("Number is 50 or lesser than 50")
	
print("values are converted to the bool constructor:")
if "hello":
    print("'Hello' is True")
	
if "":
    print("'' is True")
else: 
    print("'' is False")
	
if 142:
   print("142 is True")
   
if 0:
   print("0 is True")
else:
   print("0 is False")
   
if [10,2,30]:
   print("[10,2,30] is True")   
   
if []:
    print("[] is True")
else:
    print("[] is False")
print("if-else statements demo completed...")	

print("\n==============================\n")
print("while loop demo started...")
print("explicit c=5 to 1")
c=5
while c!=0:
   print(c,end=' ')
   c-=1
print()
print("implicit check c=5 to 1")
c=5
while c:
    print(c,end=' ')
    c-=1  
print()
print("break statements...")
while True:
    print("Enter Number")
    number=input()
    if int(number)%7==0:
        print("Number is divisible by 7 break the while")
        break;
    print("Number is not divisible by 7")
print("while loop demo completed...")