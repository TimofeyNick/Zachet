from random import shuffle

def monkey_sort(A):
    while not A == sorted(A):
        shuffle(A)
    return A
