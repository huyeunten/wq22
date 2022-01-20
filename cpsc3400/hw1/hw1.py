""" HW1.py by Haley Uyeunten
January 18, 2022
CPSC 3400 

Accepts a file that contains a list of favorite colors. Creates a dictionary
of colors. Can find the number of first place votes, score colors, and rank
them based on their scores.
"""

import sys

def process_file(file_name):
    """ Takes a file and creates a dictionary using colors as keys and
    a tuple that counts the number of times the color was ranked 1st/2nd/3rd
    as values.
    :param file_name: The name of the file to read from.
    :return: A dictionary with color-tuple key-values.
    """
    try:
        file = open(file_name, 'r')
    except OSError:
        print("Could not read file")
        sys.exit(1)
    dict = {}
    for line in file:
        s = line.split()
        first = s[0]
        second = s[1]
        third = s[2]
        # Add colors to dictionary
        # Create lists so that they can be modified
        if first not in dict:
            dict[first] = [0, 0, 0]
        if second not in dict:
            dict[second] = [0, 0, 0]
        if third not in dict:
            dict[third] = [0, 0, 0]
        dict[first][0] += 1
        dict[second][1] += 1
        dict[third][2] += 1
    file.close()
    # Convert lists to tuples
    for key in dict:
        dict[key] = tuple(dict[key])
    return dict

def get_first_place_votes(dict, color):
    """ Provides the number of first place votes for a certain color.
    :param dict: Dictionary containing the names of colors and number of
    times it was ranked 1st/2nd/3rd
    :param color: String with the name of the color to find
    :return: The number of first place votes the color received.
    """
    # Convert string to lowercase since dict keys are all lowercase
    color = color.lower()
    if color not in dict:
        return 0
    return dict[color][0]

def create_favorite_color_list(dict):
    """ Creates a list of colors sorted by the number of first place votes, 
    second place votes, third place votes, and alphabetical order of keys.
    Only colors with at least one first place vote are included in the list.
    :param dict: Dictionary containing color names and tuples of votes
    :return: A sorted list of colors
    """
    sorted_color = sorted(sorted(dict.items(), key = lambda x:x[0]), 
        key=lambda x:(x[1][0], x[1][1], x[1][2]), reverse=True)
    favorite_color_list = [color[0] for color in sorted_color if color[1][0] > 0]
    return favorite_color_list

def create_color_score_dict(dict):
    """ Creates a dictionary of colors and scores based on the number of times
    each color was ranked 1st/2nd/3rd
    :param dict: Dictionary containing colors and number of rankings
    :return: Dictionary of key: value pairs with the color as the key and its
    score as the value
    """
    cs_dict = {}
    for key in dict:
        cs_dict[key] = dict[key][0] * 3 + dict[key][1] * 2 + dict[key][2]
    return cs_dict

def print_dictionary(dict):
    """ Prints the given dictionary as key: value pairs
    :param dict: Dictionary
    :return: None
    """
    for i in sorted(dict):
        print(i, ": ", dict[i], sep="")

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Usage: hw1.py text_file.txt")
        sys.exit(1)
    dict = process_file(file_name)
    print_dictionary(dict)
    blue_first_votes = get_first_place_votes(dict, "blue")
    print(blue_first_votes)
    green_first_votes = get_first_place_votes(dict, "green")
    print(green_first_votes)
    favorite_color_list = create_favorite_color_list(dict)
    print(favorite_color_list)
    cs_dict = create_color_score_dict(dict)
    print_dictionary(cs_dict)