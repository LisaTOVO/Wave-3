def f(x,y):
    if x > 0 and y > 0:
        h = (x ** 2 + y ** 2) ** 0.5
    return h

x = int(input("Please enter one of the shorter side of the triangle: "))
y = int(input("Please enter one of the shorter side of the triangle: "))

print(f(x,y))