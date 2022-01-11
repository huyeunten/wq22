# pain and suffering and pain

# 1
"""" makes all ints floats. returns true if all are floats. 
false if otherwise. """

def floatify(ints):
    for i in ints:
        if type(i) == int:
            i = float(i)
        if type(i) != float:
            return False
    return True

a = [1,2,3.5]
print("Floatify: ", floatify(a))

# 2
"""" turns all nums in sequence into ints. returns tuple. """
def purify(seq):
    out = ()
    for i in seq:
        if type(i) != str:
            temp = int(i)
            out += (temp,)
    return out

print("Purify: ", purify(a))