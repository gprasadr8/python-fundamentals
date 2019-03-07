import sys

def isGivenNumberEven(number):
    if(number%2==0):
        return True
    else:
        return False
		
if __name__=="__main__":
    number = int(sys.argv[1])
    print(sys.argv[0])
    print(isGivenNumberEven(number))