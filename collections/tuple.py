#!/usr/bin/env python3



def create_tuple():
    t = (10,20,30)
    return t


def print_tuple_info(t):
    print("values in tuple: ",t)
    print("type of tuple: ",type(t))


def print_tuple_indexwise(t):
    print("t[0]=",t[0])
    print("t[1]=",t[1])


def print_tuple_for_loop(t):
    for item in t:
        print(item)


def create_tuple_from_string():
    return tuple("this is  a string tuple")


def create_tuple_from_list():
    return tuple(["New Yark","New Jersey","Paris"])

if __name__ == "__main__":
    t = create_tuple()
    print("\n\n print tuple and type of tuple")
    print("-------------------------------")
    print_tuple_info(t)
    print("\n\n acessing tuple using index")
    print("-------------------------------")
    print_tuple_indexwise(t)
    print("\n\n print tuple using for loop")
    print("--------------------------------")
    print_tuple_for_loop(t)
    print("create tuple from string")
    t = create_tuple_from_string()
    print("\n\n print string tuple info")
    print("-----------------------------")
    print_tuple_info(t)
    print("\n\n acessing String tuple using index")
    print("-------------------------------")
    print_tuple_indexwise(t)
    print("\n\ncrete tuple from other collection")
    print("----------------------------------------")
    t = create_tuple_from_list()
    print("\n\n print list tuple info")
    print("-----------------------------")
    print_tuple_info(t)