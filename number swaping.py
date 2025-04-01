try:
    # Accept two numbers from the user
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))

    # Display before swapping
    print(f"Before swapping: first_num = {first_num}, second_num = {second_num}")

    # Swap using tuple unpacking
    first_num, second_num = second_num, first_num

    # Display after swapping
    print(f"After swapping: first_num = {first_num}, second_num = {second_num}")

except ValueError:
    print("Error: Please enter valid numeric values.")
