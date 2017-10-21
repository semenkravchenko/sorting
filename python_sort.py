from datetime import datetime
import random

def python_sort(quantity, range_start, range_end):
    # unsorted_sequence = input('Enter the sequence of numbers and press \"Enter\": \n')
    # unsorted_sequence = list(map(int, unsorted_sequence.split(" ")))

    # unsorted_sequence = list(map(int, "15 12 25 62 11 15 8 22 64 3".split(" ")))

    unsorted_sequence = [random.randint(range_start, range_end) for i in range(quantity)]

    time_start = datetime.now().timestamp()

    #########################################

    unsorted_sequence.sort()

    #########################################

    time_stop = datetime.now().timestamp()
    time_delta = time_stop - time_start

    print("Result of {0} values sorting: \n {1}".format(len(unsorted_sequence), " ".join(map(str, unsorted_sequence))))
    print('Sequence was sorted for {0} seconds'.format(time_delta))

if __name__ == '__main__':
    quantity = int(input())
    python_sort(quantity)