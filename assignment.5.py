data = {"name": "Faiza", "age": 15, "city": "Dhaka"}

try:
    key = input("Enter the key to retrieve: ")
    value = data[key]
    print(f"The value for '{key}' is {value}.")
except KeyError:
    print("Error: The specified key does not exist.")
