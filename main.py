import include.func as f

while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Logarithm")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Exit")
    choice = input("Enter your choice (1-12): ")

    if choice == '12':
        print("Exiting the calculator. Goodbye!")
        break
    
    elif choice in ['1', '2', '3', '4', '5']:
        n , m = [int(i) for i in input("Input two numbers:").split()]
        if choice == '1':
            r = f.add(n,m)
        elif choice == '2':
            r = f.subtract(n,m)
        elif choice == '3':
            r = f.multiply(n,m)
        elif choice == '4':
            r = f.divide(n,m)
        elif choice == '5':
            r = f.power(n,m)
        print(f"Result is {r}")
        input("Press enter to continue")
        continue

    elif choice in ['6','7','8','9','10','11']:
        n = int(input("Input one number:"))
        if choice == '6':
            r = f.sqrt(n)
        if choice == '7':
            r = f.factorial(n)
        if choice == '8':
            r = f.log(n)
        if choice == '9':
            r = f.sin(n)
        if choice == '10':
            r = f.cos(n)
        if choice == '11':
            r = f.tan(n)
        print(f"Result is {r}")
        input("Press enter to continue")
        continue