# Q8_factorial.py

num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial:", fact)
else:
    print("Invalid input! Please enter a positive integer.")