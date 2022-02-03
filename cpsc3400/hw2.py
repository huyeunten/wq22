""" HW2.py by Haley Uyeunten
January 30, 2022
CPSC 3400

Accepts a file containing two integers to represent hours and minutes, and
PM/AM. Can find the latest time (max) and sort the times from earliest to
latest.
"""

import os.path
import sys

class EmptyFileError(Exception): pass
class ImproperTimeError(Exception): pass
class FileNotFound(Exception): pass

def create_time_list(file_name):
    """ Creates a list of time tuples from a file containing hours, minutes,
    and AM/PM. Throws error if file is empty, or if times are incorrectly
    formatted.
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

def convert_to_military(time):
    """ Converts given time from twelve hour AM/PM to 24 hour military time.
    :param time: tuple consisting of hour, minute, and period
    :return: tuple with hour and minute
    """
    h = int(time[0])
    m = int(time[1])
    if time[2] == "PM" and h != 12:
        h += 12
    if time[2] == "AM" and h == 12:
        h = 0
    return (h, m)

def count_hours(early, late):
    """ Counts the hours between two given times.
    :param early: starting time
    :param late: ending time
    :return: the number of hours between the times
    """
    early_h = int(early[0])
    late_h = int(late[0]) - 1
    count = 0
    while (early_h != late_h):
        if early_h == 23:
            early_h = 0
        else:
            early_h += 1
        count += 1
    return count

def time_compare_gen(time_list, target):
    """ Generates a tuple of hours and minutes between a target time and every
    time on the given list
    :param time_list: list of time tuples
    :param target: one time tuple
    :return: yield time between times in list and target time
    """
    for time in time_list:
        m = (60 - int(target[1])) + int(time[1])
        converted_time = convert_to_military(time)
        converted_target = convert_to_military(target)
        h = count_hours(converted_target, converted_time)
        if m > 59:
            h += 1
            m %= 60
        if h == 24:
            h = 0
        yield (h, m)

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
        print(max(time_list, key=convert_to_military))
        print(sorted(time_list, key=convert_to_military))
        target = time_list[0]
        time_compare_gen(time_list, target)
        time_compare_list = [t for t in time_compare_gen(time_list, target)]
        print(time_compare_list)
    except EmptyFileError:
        print("File is empty")
        sys.exit(1)
    except ImproperTimeError:
        print("Time formatted incorrectly")
    