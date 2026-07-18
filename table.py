for i in range(1, 11):
    print(f"23 x {i} = {23 * i}")

adj = ["red", "healthy", "tasty",]
fruits = ["apple", "banana", "mango"]

for x in adj:
    for y in fruits:
        print(x, y)

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

#loop counter

total_sum = 0
num = 1

while num <= 10:
    total_sum += num
    num += 1

print(f"The sum of the first 10 natural is: {total_sum}")

#All project

num = int(input("Enter a number:"))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number.")