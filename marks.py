marks = []
total_marks = 0
num_subjects = 5

for i in range(num_subjects):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                total_marks += mark
                break
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

percentage = (total_marks / (num_subjects * 100)) * 100

grade = ""
if percentage >= 60:
    grade = 'A'
elif 50 <= percentage < 60:
    grade = 'B'
elif 40 <= percentage < 50:
    grade = 'C'
elif 33 <= percentage < 40:
    grade = 'D'
else:
    grade = 'Fail'

print("\n--- Results ---")
print(f"Marks obtained: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
