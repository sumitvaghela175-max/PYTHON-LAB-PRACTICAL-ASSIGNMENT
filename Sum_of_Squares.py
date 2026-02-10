#WAP 1 2 +2 2 +3 2 +………………….n 2
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
    total += i**2
print(f"Sum of squares: {total}")
