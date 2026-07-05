print("=" * 50)
print("        SIMPLE MATHEMATICAL CALCULATOR")
print("=" * 50)

while True:

    print("\nSelect an Operation")
    print("1. +  (Addition)")
    print("2. -  (Subtraction)")
    print("3. *  (Multiplication)")
    print("4. /  (Division)")
    print("5. \\  (Floor Division)")
    print("6. ^  (Power)")
    print("7. %  (Modulus)")
    print("8. C  (Clear)")
    print("9. OFF (Exit)")

    choice = input("\nEnter Operation: ").upper()

    match choice:

        case "OFF":
            print("\nCalculator is shutting down...")
            break

        case "C":
            print("\nCalculator Screen Cleared.")

        case "+" | "-" | "*" | "/" | "\\" | "^" | "%":

            value1 = float(input("Enter First Value: "))
            value2 = float(input("Enter Second Value: "))

            match choice:

                case "+":
                    result = value1 + value2

                case "-":
                    result = value1 - value2

                case "*":
                    result = value1 * value2

                case "/":
                    if value2 == 0:
                        print("Division by zero is impossible.")
                        continue
                    result = value1 / value2

                case "\\":
                    if value2 == 0:
                        print("Division by zero is impossible.")
                        continue
                    result = value1 // value2

                case "^":
                    result = value1 ** value2

                case "%":
                    if value2 == 0:
                        print("Division by zero is impossible.")
                        continue
                    result = value1 % value2

            print("Result =", result)

        case _:
            print("Invalid operation selected.")