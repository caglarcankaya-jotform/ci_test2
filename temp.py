import os
import sys
def greet(name):
    print(f"Hello, {name}!")


def add_numbers(num1, num2):
    result = num1 + num2
    return result


def main():
    name = "Alice"
    greeting = greet(name)
    print(greeting)

    num1 = 10
    num2 = 5
    result = add_numbers(num1, num2)
    print(result)


if __name__ == "__main__":
    main()
