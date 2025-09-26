import math
import sys


def show_menu():
    print("\nCalculator")
    print("1.Square Root")
    print("2.Factorial")
    print("3.Natural Logarithm")
    print("4.Power Function")
    print("5.Exit")
    print()



def square_root():
    try:
        x = float(input("Enter a non negative number \n"))
        if x < 0:
            print("Cannot calculate square root of a negative number.")
            return
        result = math.sqrt(x)
        print(f"√{x} = {result}")
    except ValueError:
        print("Invalid input")

def factorial():
    try:
        x = int(input("Enter a non-negative integer \n"))
        if x < 0:
            print("Factorial is not defined for negative numbers.")
            return
        result = math.factorial(x)
        print(f"{x}! = {result}")
    except ValueError:
        print("Invalid input.")

def natural_log():
    try:
        x = float(input("Enter a positive number \n"))
        if x <= 0:
            print("Natural logarithm is only defined for positive numbers.")
            return
        result = math.log(x)
        print(f"ln({x}) = {result}")
    except ValueError:
        print("Invalid input")

def power_function():
    try:
        x = float(input("Enter the base number (x): \n"))
        b = float(input("Enter the exponent (b): \n"))
        result = math.pow(x, b)
        print(f"{x}^{b} = {result}")
    except ValueError:
        print("Invalid input")



def main():
    while True:
        show_menu()
        choice = input("Select option\n")
        print()

        if choice == "1":
            square_root()
        elif choice == "2":
            factorial()
        elif choice == "3":
            natural_log()
        elif choice == "4":
            power_function()
        elif choice == "5":
            print("Exiting..")
            sys.exit()
        else:
            print("Invalid input")

        print("\n" + "-"*30)    

if __name__ == "__main__":
    main()
