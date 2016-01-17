""" Solve Me First:

    Let's Start simple, return the sum of two integers passed as input
    parameters

"""




def integer_add(a, b):
    """
    This function adds two integers
    :param a: any integer
    :param b: any integer
    :return: the sum of integers a and b
    """
    return a + b


num1 = int(input())
num2 = int(input())
res = integer_add(num1, num2)
print(res)