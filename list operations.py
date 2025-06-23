print("--- List Operations ---")
while True:
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        numbers_str = input_str.split()
        my_list = [float(num) for num in numbers_str]
        if not my_list:
            print("The list cannot be empty. Please enter some numbers.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")

print(f"Original list: {my_list}")

if my_list:
    smallest_num = min(my_list)
    print(f"Smallest number in the list: {smallest_num}")
else:
    print("Cannot find smallest number in an empty list.")

unique_sorted_list = sorted(list(set(my_list)))

if len(unique_sorted_list) >= 2:
    second_greatest = unique_sorted_list[-2]
    print(f"Second greatest number in the list: {second_greatest}")
else:
    print("Cannot find the second greatest number (need at least two unique numbers).")

if len(unique_sorted_list) >= 2:
    second_smallest = unique_sorted_list[1]
    print(f"Second smallest number in the list: {second_smallest}")
else:
    print("Cannot find the second smallest number (need at least two unique numbers).")
