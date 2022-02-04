""" hw3.py by Haley Uyeunten
February 6, 2022
CPSC 3400

Simulates the mark/sweep algorithm from a file containing variables and
the heap blocks they point to.
"""

import sys

def mark_sweep(file_name):
    """Performs the mark/sweep algorithm based on a file with variables and
    heap blocks. 
    :param file_name: the name of a file containing heap blocks
    :return: a dictionary with two keys (marked and swept) and lists of
    marked/swept blocks
    """
    graph_dict = {}
    start = []
    with open(file_name, 'r') as file:
        n = int(file.readline())
        for line in file:
            input = line.split(',')
            if input[0] not in graph_dict:
                graph_dict[input[0]] = [input[1].strip()]
                if not input[0].isdigit():
                    start.append(input[0])
            else:
                graph_dict[input[0]].append(input[1].strip())
    # BFS starting from all variables
    marked = []
    queue = []
    for var in start:
        marked.append(int(graph_dict[var][0]))
        queue.append(graph_dict[var][0])
    while queue:
        block = queue.pop()
        if block in graph_dict:
            for i in graph_dict[block]:
                if int(i) not in marked:
                    queue.append(i)
                    marked.append(int(i))
    swept = []
    for i in range(n):
        if i not in marked:
            swept.append(i)
    return {"marked": sorted(marked), "swept": sorted(swept)}

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        marked_swept = mark_sweep(file_name)
        print("Marked nodes:", sep="", end=" ")
        for i in marked_swept["marked"]:
            print(i, end=" ")
        print("\nSwept nodes:", end = " ")
        for i in marked_swept["swept"]:
            print(i, end=" ")
    except IndexError:
       print("Usage: hw3.py text_file.txt")
       sys.exit(1)