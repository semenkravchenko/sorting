from datetime import datetime
import random

def bubble_sort(quantity):
    # unsorted_sequence = input('Enter the sequence of numbers and press \"Enter\": \n')
    # unsorted_sequence = list(map(int, unsorted_sequence.split(" ")))

    # unsorted_sequence = list(map(int, "15 12 25 62 11 15 8 22 64 3".split(" ")))

    unsorted_sequence = [random.randint(1, 100) for i in range(quantity)]

    time_start = datetime.now().timestamp()

    #########################################

    sequence_is_sorted = False
    fixed_element_count = 0

    while not sequence_is_sorted:
        # sorted_sequence_counter = 0

        for x in range(len(unsorted_sequence) - 1 - fixed_element_count):

            if unsorted_sequence[x] > unsorted_sequence[x + 1]:
                unsorted_sequence[x], unsorted_sequence[x + 1] = unsorted_sequence[x + 1], unsorted_sequence[x]

        fixed_element_count += 1

        if fixed_element_count == len(unsorted_sequence) - 1:
            sequence_is_sorted = True

        # print(unsorted_sequence)

    #########################################

    time_stop = datetime.now().timestamp()
    time_delta = time_stop - time_start

    print("Result of {0} values sorting: \n {1}".format(len(unsorted_sequence), " ".join(map(str, unsorted_sequence))))
    print('Sequence was sorted for {0} seconds'.format(time_delta))


if __name__ == '__main__':
    quantity = int(input())
    bubble_sort(quantity)
