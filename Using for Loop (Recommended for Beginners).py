print("python programming")

n = int(input("enter a number: "))

total = 0
for i in range(1, n+1):
    total += i

print("Sum of first", n, "number is:", total)