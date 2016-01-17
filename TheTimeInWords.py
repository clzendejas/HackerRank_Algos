#!/bin/python3

""" The Time in Words:

    Given the time in numerals we may convert it into words, as shown below:

    5:00 → five o' clock
    5:01 → one minute past five
    5:10 → ten minutes past five
    5:30 → half past five
    5:40 → twenty minutes to six
    5:45 → quarter to six
    5:47 → thirteen minutes to six
    5:28 → twenty eight minutes past five

    Write a program which prints the time in words for the input given in the
    format mentioned above.

    Inputs:
    - line 1:: H representing the hours
    - line 2:: M representing the minutes

    Output:
    - Display the time in words
"""


# Get the Hours and Minutes
H = int(input().strip())
M = int(input().strip())

# Create an Hour List
H_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
          'nine', 'ten', 'eleven', 'twelve']

# Create a minute List
M_List = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
          'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter',
          'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
          'twenty one', 'twenty two', 'twenty three', 'twenty four',
          'twenty five', 'twenty six', 'twenty seven', 'twenty eight',
          'twenty nine', 'half']

# create the rules
minute_str = 'minute' if M == 1 or M == 59 else 'minutes'

if M == 0:
    time_in_words = H_list[H] + ' o\' clock'
elif M == 30 or M == 15:
    time_in_words = M_List[M] + ' past ' + H_list[H]
elif M == 45:
    time_in_words = 'quarter to ' + H_list[H + 1]
elif M < 30:
    time_in_words = M_List[M] + ' ' + minute_str + ' past ' + H_list[H]
elif M > 30:
    time_in_words = M_List[60 - M] + ' ' + minute_str + ' to ' + H_list[H + 1]

print(time_in_words)