from datetime import datetime
import random

# unsorted_sequence = input('Enter the sequence of numbers and press \"Enter\": \n')
# unsorted_sequence = list(map(int, unsorted_sequence.split(" ")))

# unsorted_sequence = list(map(int, "15 12 25 62 11 15 8 22 64 3".split(" ")))

def insertion_sort(quantity):
    unsorted_sequence = [random.randint(1, 100) for i in range(quantity)]

    time_start = datetime.now().timestamp()

    #########################################

    sorted_sequence = []

    for x in range(0, len(unsorted_sequence)):
        sorted_sequence.append(unsorted_sequence[x])
        minimum_index = len(sorted_sequence)

        # for y in range(len(sorted_sequence) - 1, -1, -1):
        for y in reversed(sorted_sequence[:-1]):
            if sorted_sequence[-1] < y:
                minimum_index = sorted_sequence.index(y)

            else:
                break

        if minimum_index != len(sorted_sequence):
            sorted_sequence.insert(minimum_index, sorted_sequence.pop())

    #########################################

    time_stop = datetime.now().timestamp()
    time_delta = time_stop - time_start

    print("Result of {0} values sorting: \n {1}".format(len(sorted_sequence), " ".join(map(str, sorted_sequence))))
    print('Sequence was sorted for {0} seconds'.format(time_delta))