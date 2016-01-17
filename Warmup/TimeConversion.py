#!/bin/python3
""" Time Conversion

    Given a time in AM/PM format, convert it to military time.

    Input:
    - line 1:: a time in 12-hour clock format (i.e. hh:mm:ssAM)

    Output:
    - Print the given time in 24 hour format "hh:mm:ss"
"""

# input time
time = input().strip()

# determine am pm and amend time to military time
pm = time[8:] == 'PM'
time = [int(i[1]) if i[0] == '0' else int(i) for i in time[:8].split(':')]

# handle noon and midnight exceptions
if time[0] == 12:
    time[0] = 12 if pm else 0
else:
    # if not noon/midnight, add 12 to all PM times
    time[0] = time[0] + 12 if pm else time[0]

# print military time
print('%02d:%02d:%02d' % (time[0], time[1], time[2]))