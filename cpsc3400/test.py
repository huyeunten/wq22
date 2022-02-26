def fun(n, f):
    def moreFun(aList):
        for i in aList:
            yield f(i, n)
    return moreFun
def moreFun(x, y):
    return x + y
def evenMoreFun(x, y):
    return x * y

z = fun(3, moreFun)
n = 6
f = evenMoreFun
w = z([1, 2, 3, 4])
for s in w:
 print(s)