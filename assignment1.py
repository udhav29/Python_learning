student_name = input("Please enter the student's name: ")
student_class = input("Please enter the student's class: ")
mark1 = float(input("Enter marks for Subject 1 (out of 100): "))
mark2 = float(input("Enter marks for Subject 2 (out of 100): "))
mark3 = float(input("Enter marks for Subject 3 (out of 100): "))
mark4 = float(input("Enter marks for Subject 4 (out of 100): "))
mark5 = float(input("Enter marks for Subject 5 (out of 100): "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
max_total_marks = 500
percentage = (total_marks / max_total_marks) * 100
print("\n--- Student Report Card ---")
print(f"Name: {student_name}")
print(f"Class: {student_class}")
print(f"Total Marks Obtained: {total_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print("---------------------------")


# --- Python String Manipulation Program (Beginner Level) ---

print("Welcome to the String Concatenation and Methods Demo!")

# Input two strings from the user
print("\nPlease enter two strings to see concatenation and string methods in action.")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Concatenate the two strings and store in a new variable
# We'll add a space in between for better readability
concatenated_string = string1 + " " + string2

print(f"\n--- Result of Concatenation ---")
print(f"The first string was: '{string1}'")
print(f"The second string was: '{string2}'")
print(f"The concatenated string is: '{concatenated_string}'")

# --- Performing General String Methods (Concise Display) ---
print("\n--- Demonstrating Common String Methods ---")

# 1. len() - Returns the length of the string
print(f"1. Length: {len(concatenated_string)}")

# 2. upper() - Converts all characters in the string to uppercase
print(f"2. Uppercase: '{concatenated_string.upper()}'")

# 3. lower() - Converts all characters in the string to lowercase
print(f"3. Lowercase: '{concatenated_string.lower()}'")

# 4. capitalize() - Converts the first character of the string to uppercase and the rest to lowercase
print(f"4. Capitalized: '{concatenated_string.capitalize()}'")

# 5. title() - Converts the first character of each word to uppercase
print(f"5. Title-cased: '{concatenated_string.title()}'")

# 6. strip() - Removes leading and trailing whitespace
# Demonstrating on a string with extra spaces
print(f"6. Stripped ('  Hi  '): '{'  Hi  '.strip()}'")

# 7. replace(old, new) - Replaces all occurrences of a substring with another substring
# Using example values directly
print(f"7. Replace (' ' with '-'): '{concatenated_string.replace(' ', '-')}'")

# 8. find(substring) - Returns the lowest index of the substring if found, otherwise -1
# Using example values directly
print(f"8. Find ('o'): Index {concatenated_string.find('o')}")

# 9. count(substring) - Returns the number of non-overlapping occurrences of substring
# Using example values directly
print(f"9. Count ('a'): {concatenated_string.count('a')} occurrence(s)")

# 10. startswith(prefix) - Checks if the string starts with the specified prefix
# Using example values directly
print(f"10. Starts with 'Hello'? {concatenated_string.startswith('Hello')}")

# 11. endswith(suffix) - Checks if the string ends with the specified suffix
# Using example values directly
print(f"11. Ends with 'World'? {concatenated_string.endswith('World')}")

print("\n--- End of String Operations Demo ---")
