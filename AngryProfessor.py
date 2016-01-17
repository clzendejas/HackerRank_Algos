""" Angry professor

    A Discrete Mathematics professor has a class of N students.
    Frustrated with their lack of discipline, he decides to cancel
    class if fewer than K students are present when class starts.
    Given the arrival time of each student, determine if the class is canceled.

    Inputs:
    - line 1:: an integer T, the number of test cases
    - for each Test Case:
        - line 1:: two space-separated integers N (students in the class)
                   and K (the cancellation threshold)
        - line 2:: N space-separated integers, describing the arrival time
                   of each student


    Output:
    for each test case, print the word 'YES' if class is cancelled, else 'NO'
"""

# function to determine if class is cancelled
def class_cancelled(arr, threshold):
    """
    this function tests to see if k students out of n are on time, and decides
    to cancel class if a minimum k are not on time in O(n) time

    :param arr: an array of arrival times relative to class starting
    :param threshold: the cancellation threshold
    :return: 'YES' if class is cancelled, else 'NO'
    """
    # create a logical vector of arrival times <= 0
    on_time = sum([1 if x <= 0 else 0 for x in arr])
    is_cancelled = 'YES' if on_time < threshold else 'NO'
    return is_cancelled


# get number of test cases
t = int(input().strip())

# loop through t number of test cases
cancelled = []
for i in range(t):
    # get the number of students (n) and cancellation threshold (k)
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (n, k) = (temp[0], temp[1])

    # get the arrival times of the students
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]

    # test to see if the class has been cancelled
    cancelled.append(class_cancelled(temp, k))

for test_output in cancelled:
    print(test_output)