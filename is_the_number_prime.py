def f(n):
    if n > 1:
        for i in range(n - 2):
            if n % (i + 2)  == 0:
                return False
    else:
        return False

    return True

n = int(input("Enter an integer (2 or greater): "))

print(f(n))