""" HW2.py by Haley Uyeunten
January 27, 2022
CPSC 3400

write doctests this time
"""

import os.path
import sys

class EmptyFileError(Exception): pass
class ImproperTimeError(Exception): pass
class FileNotFound(Exception): pass

def create_time_list(file_name):
    """ need to throw exceptions
    :param file_name: the name of the file containing times
    :return: list of time tuples
    """
    if os.path.getsize(file_name):
        time_list = []
        with open(file_name, 'r') as file:
            for line in file:
                s = line.split()
                if len(s) == 3:
                    if s[0].isdigit() and s[1].isdigit and (s[2] == "AM" or s[2] == "PM"):
                        hour = int(s[0])
                        minute = int(s[1])
                        if hour > 0 and hour < 13 and minute > 0 and minute < 60:
                            time_list.append((s[0], s[1], s[2]))
                        else:
                            raise ImproperTimeError
                    else:
                        raise ImproperTimeError
                else:
                    raise ImproperTimeError
    else:
        raise EmptyFileError
    return time_list

def time_to_midnight(time):
    t_h = int(time[0])
    t_m = int(time[1])
    p = time[2]
    h = 11 - t_h
    if t_h == 12:
        h = 11
    if p == "AM":
        h += 12
    m = 60 - int(t_m)
    return (h, m)
    
def time_compare_gen(time_list, target):
    """
    :param time_list: list of time tuples
    :param target: one time tuple
    :return: yield time between times in list and target time
    """
    for time in time_list:
        midnight_time = time_to_midnight(time)
        midnight_target = time_to_midnight(target)
        yield (midnight_time[0] - midnight_target[0], midnight_time[1] - midnight_target[1])
    #print(time_list)
    #print(target)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Usage: hw2.py text_file.txt")
        sys.exit(1)
    try:
        time_list = create_time_list(file_name)
        formatted_time = [h + ":" + m + " " + p for h, m, p in time_list]
        print(formatted_time)
        print(max(time_list, key=lambda x:(x[2], int(x[0]), int(x[1]))))
        print(sorted(time_list, key=lambda x:(x[2], int(x[0]), int(x[1]))))
        target = time_list[0]
        time_compare_list = [t for t in time_compare_gen(time_list, target)]
        print(time_compare_list)
    except EmptyFileError:
        print("File is empty")
        sys.exit(1)
    except ImproperTimeError:
        print("Time formatted incorrectly")
    