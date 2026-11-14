def get_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            print(f"You entered {number}")
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def analyze_number(number):
    even = number % 2 == 0
    positive = number >= 0
    data = {
        "number": number,
        "even": even,
        "positive": positive
    }
    return data

message = analyze_number(get_number())

for key, value in message.items():
    print(f"{key}: {value}")
      
    



  

    
