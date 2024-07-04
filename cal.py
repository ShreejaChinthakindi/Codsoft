print("Calculator is opened!")
while True:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    print("Enter the operation that you wanna  perform: \n + for addition \n - for subtraction \n * for multiplication \n / for division ")
    operation = input("Enter the type of operation: ")
    if operation in ('+','-','*','/'):
        #perform operation
        if operation == "+":
            print(f" Addition of {n1} and {n2} is:",n1+n2)
        elif operation == '-':
            print(f"Difference of {n1} and {n2} is:",n1-n2)
        elif operation == '*':
            print(f" Multiplication of {n1} and {n2} is:",n1*n2)
        elif operation == '/':
            if n2 != 0:
                print(f" Division of {n1} and {n2} is:",n1/n2)
            else:
                print("Error!")
                print("Invalid operation")
    op = input("Do you really want to continue? (yes/no): ")
    if op.lower() == 'yes':
        continue
    else:
        print('Goodbye!')
        break