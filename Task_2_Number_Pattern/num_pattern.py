print("==========================================")
print("        NUMBER PATTERN GENERATOR")
print("==========================================")

while True:
    print("\nChoose a Pattern:")
    print("1. Number Triangle")
    print("2. Reverse Number Triangle")
    print("3. Same Number Triangle")
    print("4. Number Pyramid")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "5":
        print("\nThank you for using Number Pattern Generator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid choice! Please select 1 to 5.")
        continue

    rows = int(input("Enter number of rows: "))

    print("\nGenerated Pattern:")
    print("------------------------------------------")

    if choice == "1":
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif choice == "2":
        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif choice == "3":
        for i in range(1, rows + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    elif choice == "4":
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end=" ")

            for j in range(1, i + 1):
                print(j, end=" ")

            print()

    print("------------------------------------------")