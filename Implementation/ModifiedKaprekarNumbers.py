#!/bin/python3

""" Modified Kaprekar Numbers:

    A modified Kaprekar number is a positive whole number n with d digits,
    such that when we split its square into two pieces - a right hand piece
    r with d digits and a left hand piece l that contains the remaining
    d or d−1 digits, the sum of the pieces is equal to the original number
    (i.e. l + r = n).

    Note: r may have leading zeros.

    You are given the two positive integers p and q, where p is lower than q.
    Write a program to determine how many Kaprekar numbers are there in the
    range between p and q (both inclusive) and display them all.
"""


# function that tests if a kaprekar number
def is_kaprekar(k):
    """
    Takes a number and tests to see if it is a kaprekar number
    :param k: any positive, whole number
    :return: TRUE if a kaprekar, else False
    """
    # convert x into a string
    x = str(k**2)
    if x == '1':
        return True
    elif len(x) < 2:
        return False
    else:
        pivot = int(len(x)/2) if len(x) % 2 == 0 else int(len(x)//2)
        left = int(x[:pivot])
        right = int(x[pivot:])

        if left + right == k:
            return True
        else:
            return False

p = int(input().strip())
q = int(input().strip())

kaprekar_list = []
for i in range(p, q+1, 1):
    # test all numbers in range between p & q for being kaprekar numbers
    if is_kaprekar(i):
        kaprekar_list.append(i)

# change kaprekar list to string and print
if len(kaprekar_list) == 0:
    print('INVALID RANGE')
else:
    kaprekar_list = [str(i) for i in kaprekar_list]
    print(' '.join(kaprekar_list))