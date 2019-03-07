#!/usr/bin/env python3



def create_tuple():
    t = (10,20,30)
    return t


def print_tuple_info(t):
    print("values in tuple: ",t)
    print("type of tuple: ",type(t))


if __name__ == "__main__":
    t = create_tuple()
    print_tuple_info()