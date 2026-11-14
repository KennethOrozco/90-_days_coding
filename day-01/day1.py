name = input("What is your name? ")

age = int(input("What is your age? "))

print(f"Hello {name}!")
print(f"You are {age} years old.")
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor")