name = input("Enter your name: ")
age = int(input("Enter your age: "))
required_resident_age = int(input("Enter the required resident age: "))

if age >= 45 and required_resident_age >= 15:
    print(f"Hello {name}! You are {age} years old and you are eligible to be a USA president.")
else:
    print(f"Hello {name}! You are {age} years old and you are not eligible to be a USA president.")







