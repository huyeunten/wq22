"""
??.py by Haley Uyeunten
"""

class NotFloat(Exception): pass
class BadScript(Exception): pass

def interpret(script, csv, pipeline):
    with open(script, 'r') as script_file:
        p = file.readline().split()
    for str in p:
        
    names = []
    data = {}
    count = 0
    with open(csv, 'r') as file:
        first = file.readline().split(",")
        for col_name in first:
            names.append(col_name)
            data[count] = []
            count += 1
        for line in file:
            s = line.split(",")
            temp = 0
            for num in s:
                if type(num) is not float:
                    raise NotFloat
                else:
                    data[temp].append(num)
                    temp += 1

if __name__ == "__main__":
    