student = {
    "name": "Alex",
    "scores": [92, 87, 95]
}

try:
    index = int(input("Score index: "))
    print(student["grades"][index])

except ValueError:
    print("invalid number")
except IndexError:
    print("That score does not exist!")
except KeyError:
    print("Student data is missing!")