list1 = []
for i in range(9, -3, -1):
    list1.append(i*i)

new_list1 = [i * i for i in range(9, -3, -1)]

print(list1)
print(new_list1)

list2 = []
for c in '1234987723':
    list2.append(int(c))

new_list2 = [int(c) for c in '1234987723']

print(list2)
print(new_list2)

list3 = []
for i in range(100_000):
    if i%3 == 0:
        list3.append(i)

new_list3 = [i for i in range(100_000) if 1 % 3 == 0]

print(list3)
print(new_list3)

x = [i**3.2 for i in range(300)]

xx = []
for i in range(300):
    xx.append(i ** 3.2)

print(x)
print(xx)

y = [int(c) for c in s if c.isdigit()]
z = [d[k] for k in d if type(k) == int and k%2 == 0]
w = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]