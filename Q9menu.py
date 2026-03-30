
positive_sum = 0
negative_sum = 0

while True:
    print("\n1. Enter Number")
    print("2. Exit")

    choice = input("Choose option: ")

    if choice == '1':
        num = float(input("Enter number: "))
        if num >= 0:
            positive_sum += num
        else:
            negative_sum += num
    elif choice == '2':
        break
    else:
        print("Invalid choice")

print("\nSum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)