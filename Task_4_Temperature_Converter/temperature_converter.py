print("==========================================")
print("        TEMPERATURE CONVERTER")
print("==========================================")

while True:
    print("\n========== MENU ==========")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))

            fahrenheit = (celsius * 9 / 5) + 32

            print("\nConversion Result")
            print("------------------------------------------")
            print("Celsius     :", celsius, "°C")
            print("Fahrenheit  :", round(fahrenheit, 2), "°F")
            print("------------------------------------------")

        except ValueError:
            print("\nInvalid input! Please enter a number.")

    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))

            celsius = (fahrenheit - 32) * 5 / 9

            print("\nConversion Result")
            print("------------------------------------------")
            print("Fahrenheit  :", fahrenheit, "°F")
            print("Celsius      :", round(celsius, 2), "°C")
            print("------------------------------------------")

        except ValueError:
            print("\nInvalid input! Please enter a number.")

    elif choice == "3":
        print("\nThank you for using Temperature Converter!")
        break

    else:
        print("\nInvalid choice! Please select 1, 2, or 3.")