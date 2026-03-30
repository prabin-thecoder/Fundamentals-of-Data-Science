
marks = []

for i in range(6):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / 6
percentage = (total / 600) * 100

if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

print("\nTotal:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Grade:", grade)