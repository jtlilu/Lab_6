# Lab 3
# Scienctific calculator
# June 7, 2022


import math
total = 0
sub = 0
mult = 0
div = 0
exp = 0
loga = 0
sum_cal = 0
num_cal = 0
calculator = True
choice = -1

print(f"Current Result: 0.0\n")

while calculator:
    print("Calculator Menu")
    print("-" * 15)
    print("0. Exit Program\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Exponentiation\n"
          "6. Logarithm\n"
          "7. Display Average")
    
    choice = int(input("\nEnter Menu Selection: "))
    if choice == 0:
        print("\nThanks for using this calculator. Goodbye!")
        calculator = False
        break
    elif choice == 1:
        ope11 = total if ope1 == "RESULT" else float(ope1)
        ope21 = total if ope2 == "RESULT" else float(ope2)
        ope1 = float(input("Enter first operand: "))
        ope2 = float(input("Enter second operand: "))
        total = ope1 + ope2
        num_cal += 1
        print(f"\nCurrent Result: {total}\n")
    elif choice == 2:
        ope11 = sub if ope1 == "RESULT" else float(ope1)
        ope21 = sub if ope2 == "RESULT" else float(ope2)
        ope1 = float(input("Enter first operand: "))
        ope2 = float(input("Enter second operand: "))
        sub = ope1 - ope2
        num_cal += 1
        print(f"\nCurrent Result: {sub}\n")
    elif choice == 3:
        ope11 = mult if ope1 == "RESULT" else float(ope1)
        ope21 = mult if ope2 == "RESULT" else float(ope2)
        ope1 = float(input("Enter first operand: "))
        ope2 = float(input("Enter second operand: "))
        mult = ope1 * ope2
        num_cal += 1
        print(f"\nCurrent Result: {mult}\n")
    elif choice == 4:
        ope11 = div if ope1 == "RESULT" else float(ope1)
        ope21 = div if ope2 == "RESULT" else float(ope2)
        ope1 = float(input("Enter first operand: "))
        ope2 = float(input("Enter second operand: "))
        div = ope1 / ope2
        num_cal += 1
        print(f"\nCurrent Result: {div}\n")
    elif choice == 5:
        ope11 = exp if ope1 == "RESULT" else float(ope1)
        ope21 = exp if ope2 == "RESULT" else float(ope2)
        ope1 = float(input("Enter first operand: "))
        ope2 = float(input("Enter second operand: "))
        exp = ope1 ** ope2
        #round(exp,2)
        num_cal += 1
        print(f"\nCurrent Result: {exp}\n")
    elif choice == 6:
        ope11 = loga if ope1 == "RESULT" else float(ope1)
        ope21 = loga if ope2 == "RESULT" else float(ope2)
        ope1 = float(input("Enter first operand: "))
        ope2 = float(input("Enter second operand: "))
        loga = math.log2(ope2)/math.log2(ope1)
        #round(loga,2)
        num_cal += 1
        print(f"\nCurrent Result: {loga}\n")
    elif choice == 7:
        sum_cal = total + sub + + mult + div + exp + loga
        if sum_cal == 0:
            print("\nError: No calculations yet to average!")
           
        else:
            print(f"\nSum of calculations: {sum_cal}")
            print(f"\nNumber of calculations: {num_cal}")
            average = sum_cal / num_cal
            #round = (average,2)
            print(f"\nAverage of calculations: {average:.2f}\n")
            
        choice = int(input("\nEnter Menu Selection: "))
        if choice == 0:
            print("\nThanks for using this calculator. Goodbye!")
            calculator = False
            break
    else:
        print("\nError: Invalid selection!")
        choice = int(input("\nEnter Menu Selection: "))
        if choice == 0:
            print("\nThanks for using this calculator. Goodbye!")
            calculator = False
            break
