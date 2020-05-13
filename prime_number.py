n = int(input("Enter an integer (2 or greater): "))
f = 2

print("The prime factors of", n, "are: ")
while f <= n:
    if n % f == 0:
        print(f)
        n = n / f
    else:
        f = f + 1
