# tuple thing
print(((1, 'xyzw', 4.2), (1, 3), (4, 5, 6, 7))[:2]) # ((1, 'xyzw', 4.2), (1, 3))
print(((1, 'xyzw', 4.2), (1, 3), (4, 5, 6, 7))[:2][0]) # (1, 'xyzw', 4.2)
print(((1, 'xyzw', 4.2), (1, 3), (4, 5, 6, 7))[:2][0][-2]) # xyzw
print(((1, 'xyzw', 4.2), (1, 3), (4, 5, 6, 7))[:2][0][-2][1]) # y

# last exercise
def get_print_user_nums():
    nums = ()
    next = input()
    while next != "DONE": # input numbers until DONE
        if type(next) == int: # check if input is ints
            nums += (int(next), ) # and then cast to int
        next = input()
    sum = 0
    for i in nums:
        print("Number:", i)
        sum += i
        print("Sum:", sum)

get_print_user_nums()