print("__name__ = ",__name__)

def square(number):
    return number*number

if __name__ == "__main__":
    print("inside __main__ statement")
    print(square(5))