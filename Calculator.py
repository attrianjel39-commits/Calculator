while True:
    print("press one for addition")
    print("press two for subtraction")
    print("press three for multiplication")
    print("press four for division")
    print("press five to exit")

    choice = int(input("Enter your choice: "))
    if choice ==5:
        print("Exiting the program.")
        break
    if choice in [1, 2, 3, 4]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    if choice == 1:
        print("The sum is: ", num1 + num2)
    elif choice == 2:
        print("The difference is: ", num1 - num2)
    elif choice == 3:
         print("The product is: ", num1 * num2)
    elif choice == 4:
        if num2 ==0:
            print("Error: Division by zero is not allowed.")
        else:
            print("The quotient is: ", num1 / num2)
    else:
        print("Invalid choice. Please try again.")
        
    yes = input("Do you want to continue? (yes/no)").lower()
    if yes != "yes":
        print("Exiting the program.")
        break
