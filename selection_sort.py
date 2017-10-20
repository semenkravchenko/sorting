from datetime import datetime
import random

def minimum(sequence):
    minimum_result = sequence[0]

    for value in sequence:
        if value < minimum_result: minimum_result = value

    return minimum_result

# unsorted_sequence = input('Enter the sequence of numbers and press \"Enter\": \n')
# unsorted_sequence = list(map(int, unsorted_sequence.split(" ")))

# unsorted_sequence = list(map(int, "15 11 15 25 12 22 64 3".split(" ")))

def selection_sort(quantity):

    unsorted_sequence = [random.randint(1, 100) for i in range(quantity)]

    time_start = datetime.now().timestamp()
    sorted_sequence = []

    for x in range(len(unsorted_sequence)):
        sorted_sequence.append(minimum(unsorted_sequence))
        # print(sorted_sequence)
        unsorted_sequence.remove(minimum(unsorted_sequence))

    time_stop = datetime.now().timestamp()
    time_delta = time_stop - time_start

    print("Result of {0} values sorting: \n {1}".format(len(sorted_sequence), " ".join(map(str, sorted_sequence))))
    print('Sequence was sorted for {0} seconds'.format(time_delta))