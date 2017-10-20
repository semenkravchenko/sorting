from bubble_sort import bubble_sort
from comb_sort import comb_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from stupid_sort import stupid_sort

def set_sorting_type():
    try:
        print("""Choose the type of sorting. Please, enter the number:"
        1. Bubble sorting
        2. Comb sorting
        3. Insertion sorting
        4. Selection sorting
        5. Stupid sorting""")

        sorting_type_choise = int(input())

        if sorting_type_choise == 1:
            return bubble_sort
        elif sorting_type_choise == 2:
            return comb_sort
        elif sorting_type_choise == 3:
            return insertion_sort
        elif sorting_type_choise == 4:
            return selection_sort
        elif sorting_type_choise == 5:
            return stupid_sort
        else:
            raise IndexError()
    except IndexError:
        print("Wrong choise...")

def set_numbers_quantity():

    try:

        print("""How many numbers will be sorted. Please, enter the number:""")

        numbers_quantity_choise = int(input())

        if numbers_quantity_choise <= 0:
            raise IOError

        return numbers_quantity_choise

    except IOError as error:
        print("Numbers quantity must be > 0")
        print(error)

        # повторный вызов не прокатывает. разобраться, почему
        # set_numbers_quantity()

def main():
    sorting_type = set_sorting_type()

    sorting_type(set_numbers_quantity())

if __name__ == '__main__':
    main()