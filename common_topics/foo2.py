#source is copied from  https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# Suppose this is foo2.py.

def functionA():
    print("a1")
    from foo2 import functionB
    #print("__name__ after functionB import = ",__name__)
    print("a2")
    functionB()
    print("a3")

def functionB():
    print("b")

print("t1")
#if __name__ == "__main__":
print("m1")
functionA()
print("m2")
print("t2")