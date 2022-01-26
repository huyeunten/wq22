g = 5
def bar(a, b, c):
  print("in bar")
  d = a + b
  def fun1(g):
    print("in fun1")
    x = g + c
    print("x is", x)
    return x
  def fun2(y):
    print("in fun2")
    z = y * g + d
    return z
  print(fun1(3))
  return fun2

f1 = bar(1, 2, 3)
g = 10
f2 = bar(6, 7, 8)
print("f1 is", f1(4))
print("f2 is", f2(4))

# def foo(a, b):
#   a[0] = 1
#   b[1] = 2
#   b = a
#   b[2] = 3
#   a = [4, 5, 6, 7, 8]
#   b[3] = 9
#   a[4] = 10
#   return (a, b)

# c = [11, 12, 13, 14, 15]
# d = [16, 17, 18, 19, 20]
# e, f = foo(c, d)

# print(c)
# print(d)
# print(e)
# print(f)