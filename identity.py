x = 8

if (type(x) is int):
    print("True")
else:
    print("False")

x = 6.7

if (type(x) is not float):
    print("True")
else:
    print("False")

x = 20
y = 20

if (x is y):
    print("x & y same identity")

y = 70

if (x is not y):
    print ("x & y have different identity")