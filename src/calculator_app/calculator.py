import math
import sys
from .logging_config import setup_logging  


logger = setup_logging()


def calculate_sqrt(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number.")
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)

def calculate_factorial(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(number)

def calculate_ln(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number.")
    if number <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(number)

def calculate_power(base, exponent):
    if not all(isinstance(n, (int, float)) for n in [base, exponent]):
        raise TypeError("Both base and exponent must be numbers.")
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Negative base with a non-integer exponent results in a complex number.")
    return math.pow(base, exponent)



# Interface user menu
def show_menu():
    print("\nCalculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Logarithm")
    print("4. Power Function")
    print("5. Exit")
  

def square_root():
    logger.info("START OP: Square Root")
    try:
        x = float(input("Enter a non-negative number: "))
        result = calculate_sqrt(x)
        print(f"√{x} = {result}")
        logger.info(f"[SUCCESS] √{x} = {result}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        logger.error(f"[FAILURE] {e}")
    finally:
        logger.info("END OP: Square Root")

def factorial():
    logger.info("START OP: Factorial")
    try:
        x = int(input("Enter a non-negative integer: "))
        result = calculate_factorial(x)
        print(f"{x}! = {result}")
        logger.info(f"[SUCCESS] {x}! = {result}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        logger.error(f"[FAILURE] {e}")
    finally:
        logger.info("END OP: Factorial")

def natural_log():
    logger.info("START OP: Natural Log")
    try:
        x = float(input("Enter a positive number: "))
        result = calculate_ln(x)
        print(f"ln({x}) = {result}")
        logger.info(f"[SUCCESS] ln({x}) = {result}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        logger.error(f"[FAILURE] {e}")
    finally:
        logger.info("END OP: Natural Log")

def power_function():
    logger.info("START OP: Power")
    try:
        x = float(input("Enter the base number (x): "))
        b = float(input("Enter the exponent (b): "))
        result = calculate_power(x, b)
        print(f"{x}^{b} = {result}")
        logger.info(f"[SUCCESS] {x}^{b} = {result}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        logger.error(f"[FAILURE] {e}")
    finally:
        logger.info("END OP: Power")

def main():
    logger.info("Calculator application started.")
    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            square_root()
        elif choice == "2":
            factorial()
        elif choice == "3":
            natural_log()
        elif choice == "4":
            power_function()
        elif choice == "5":
            logger.info("Calculator application exiting.")
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid input. Please enter a number in 1 to 5.")
            logger.warning(f"Invalid menu choice: {choice}")
        print("\n" + "-" * 30)

if __name__ == "__main__":
    main()