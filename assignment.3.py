def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive!")

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
    print("Number is positive.")
except ValueError as e:
    print(f"Error: {e}")
