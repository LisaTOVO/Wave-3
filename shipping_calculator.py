def shipping(num):
    if num >= 0:
        return (num -1) *2.95 + 10.95
    else:
        print("Invalid")

print(shipping(int(input("Enter the number of item: "))))