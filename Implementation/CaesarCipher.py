#!/bin/python3
""" Caesar Cipher

    Julius Caesar protected his confidential information by encrypting it in
    a cipher. Caesar's cipher rotated every letter in a string by a fixed
    number, K, making it unreadable by his enemies. Given a string, S, and a
    number, K, encrypt S and print the resulting string.

    Note: The cipher only encrypts letters; symbols, such as -, remain
    unencrypted.

    Inputs:
    - line 1:: an integer N (the length of the unencrypted string)
    - line 2:: the unencrypted string
    - line 3:: the integer K (number of letters to rotate)

    Outputs:
    - print the encoded string
"""


# get the string length, unencrypted string, and encryption key
n = int(input().strip())
s = list(input().strip())
k = int(input().strip())

# take mod 26 of k to make k < 26
k %= 26
# create a dictionary of the alphabet, lower and upper
alphabet_dict = {}
for i in range(ord('a'), ord('a') + 26, 1):
    letter_lower = chr(i)
    letter_upper = letter_lower.upper()
    alphabet_index = i - ord('a')

    # create the new index
    if alphabet_index + k > 25:
        # need to loop the index back around
        new_index = alphabet_index + k - 26
    else:
        new_index = alphabet_index + k

    # get the offset letter
    offset_letter_lower = chr(ord('a') + new_index)
    offset_letter_upper = chr(ord('A') + new_index)

    # assign to a dictionary
    alphabet_dict[letter_lower] = offset_letter_lower
    alphabet_dict[letter_upper] = offset_letter_upper

# go through the string and create the encrypted string
encrypted_string = ''
for letter in s:
    if letter in alphabet_dict.keys():
        encrypted_string += alphabet_dict[letter]
    else:
        encrypted_string += letter

# print the encrypted string
print(encrypted_string)