from bubble_sort import bubble_sort
from comb_sort import comb_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from stupid_sort import stupid_sort
from python_sort import python_sort

def set_sorting_type():
    try:
        print("""Choose the type of sorting. Please, enter the number:"
        1. Bubble sorting
        2. Comb sorting
        3. Insertion sorting
        4. Selection sorting
        5. Stupid sorting
        6. Python own sorting""")

        sorting_type_choice = int(input())

        if sorting_type_choice == 1:
            return bubble_sort
        elif sorting_type_choice == 2:
            return comb_sort
        elif sorting_type_choice == 3:
            return insertion_sort
        elif sorting_type_choice == 4:
            return selection_sort
        elif sorting_type_choice == 5:
            return stupid_sort
        elif sorting_type_choice == 6:
            return python_sort
        else:
            raise IndexError()
    except IndexError:
        print("Wrong choice...")

def set_numbers_quantity():

    try:

        print("""How many numbers will be sorted. Please, enter the number:""")

        numbers_quantity_choice = int(input())

        if numbers_quantity_choice <= 0:
            raise IOError

        return numbers_quantity_choice

    except IOError as error:
        print("Numbers quantity must be > 0")
        print(error)

        # повторный вызов не прокатывает. разобраться, почему
        # set_numbers_quantity()

def set_ranges():
    try:

        print("""Please, enter the ranges of numbers to sort. We need two numbers, divided by space (0 100):""")

        ranges = input().split(" ")
        ranges = list(map(int, ranges))

        if ranges[0] > ranges[1] or len(ranges) != 2:
            raise IOError

        return ranges

    except:
        print("Using default ranges: 0 100...")
        ranges = [0, 100]
        return ranges


def main():
    sorting_type = set_sorting_type()
    range_start, range_end = set_ranges()

    sorting_type(set_numbers_quantity(), range_start, range_end)

if __name__ == '__main__':
    main()