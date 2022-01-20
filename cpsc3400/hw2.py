""" HW2.py by Haley Uyeunten
January 27, 2022
CPSC 3400

write doctests this time
"""

import sys

def create_time_list(file_name):
    """ need to throw exceptions
    :param file_name: the name of the file containing times
    :return: list of time tuples
    """
    print(file_name)

def time_compare_gen(time_list, target):
    """
    :param time_list: list of time tuples
    :param target: one time tuple
    :return: yield time between times in list and target time
    """
    print(time_list)
    print(target)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Usage: hw1.py text_file.txt")
        sys.exit(1)
    time_list = create_time_list(file_name)
    # exception handlers?
    # ???