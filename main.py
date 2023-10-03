numbers = []  # List to store user-entered numbers
largest = None
smallest = None

while True:
    try:
        user_input = float(input("Enter a number (or 'done' to finish): "))
        numbers.append(user_input)

        if largest is None or user_input > largest:
            largest = user_input

        if smallest is None or user_input < smallest:
            smallest = user_input

    except ValueError:
        if user_input.lower() == "done":
            break
        else:
            print("Invalid input. Please enter a number or 'done'.")

# Calculate and display the average, largest, and smallest
average = sum(numbers) / len(numbers)
print(f"Average: {average}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}"
