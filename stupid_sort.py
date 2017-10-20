from datetime import datetime
import random

# unsorted_sequence = input('Enter the sequence of numbers and press \"Enter\": \n')
# unsorted_sequence = list(map(int, unsorted_sequence.split(" ")))

# unsorted_sequence = list(map(int, "15 11 15 25 12 22 64 3".split(" ")))

def stupid_sort(quantity):

    unsorted_sequence = [random.randint(1, 100) for i in range(quantity)]

    time_start = datetime.now().timestamp()

    #########################################

    iteration_count = 0
    work_mark = True

    if len(unsorted_sequence) <= 1:
        print('Nothing to sort...')
        work_mark = False

    while work_mark:
        free_turn_counter = 0

        for x in range(len(unsorted_sequence) - 1):
            iteration_count += 1
            # print(unsorted_sequence)

            if int(unsorted_sequence[x]) > int(unsorted_sequence[x+1]):
                unsorted_sequence[x], unsorted_sequence[x + 1] = unsorted_sequence[x + 1], unsorted_sequence[x]
                continue

            else:
                free_turn_counter += 1
                if free_turn_counter == len(unsorted_sequence) - 1: work_mark = False

    #########################################

    time_stop = datetime.now().timestamp()
    time_delta = time_stop - time_start

    print("Result of {0} values sorting: \n {1}".format(len(unsorted_sequence), " ".join(map(str, unsorted_sequence))))
    print('Sequence was sorted for {0} iterations. It took {1} seconds'.format(iteration_count, time_delta))

