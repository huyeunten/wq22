# continued pain and suffering

"""" takes dictionary and prints key and value in sorted order """
def print_dictionary(dict):
    for i in sorted(dict):
        print(i, dict[i])

catalog = {1220: 'Data-Driven Programming',
    5061: 'Programming I for Business',
    4600: 'Parallel Programming',
    2430: 'Data Structures and Algorithms'}
print_dictionary(catalog)

"""" takes letter grade and returns the number range """
def grade_range(grade):
    grade_table = {'A': (0.9, 1.0), 'B': (0.8, 0.9), 'C': (0.7, 0.8),
        'D': (0.6, 0.7), 'F': (0.0, 0.6)} 
    if grade in grade_table:
        return grade_table[grade]
    return "Not in table"

print(grade_range('Z'))

""" return a dictionary keyed by the alphabetic letters in given text, 
    counting the occurences of each letter. """
def letter_frequency(text):
    letter_counts = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha(): # only count letters
            if letter not in letter_counts:
                letter_counts[letter] = 0 # add key to dictionary
            letter_counts[letter] += 1 # increment count for letter
    return letter_counts

print(letter_frequency("Sally sold seashells"))