from utilities import add, multiply, format_result

def main() -> None:
    a = 10
    b = 5
    print("Welcome to the Calculator!")
    print(format_result("Multiplication", multiply(a, b)))
    print(format_result("Addition", add(a, b)))



if __name__ == "__main__":
      main()



