def menu():
    print("Basic Calculator")
    print("-"*20)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

menu()

while True:
    print("Enter your choice: ")
    user_choice = int(input())

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if user_choice == 4 and num2 == 0:
        print("Error! Cannot divide by zero")
        exit(0)
    elif user_choice == 1:
        print("%d + %d = %d" %(num1, num2, num1 + num2))
    elif user_choice == 2:
        print("%d - %d = %d" %(num1, num2, num1 - num2))
    elif user_choice == 3:
        print("%d * %d = %d" %(num1, num2, num1 * num2))
    elif user_choice == 4:
        print("%d / %d = %f" %(num1, num2, (num1 / num2)))
    else: 
        print("Invalid Option")
    
    print("Do you wish to continue calculating?(y/n): ")
    user_wish = input()
    if user_wish == "n":
        print("Thanks for using our calculator")
        break