"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def celsius_to_fahr(celsius):
    return celsius * 9.0 / 5 + 32


def fahr_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        print("Result: {:.2f} F".format(celsius_to_fahr(celsius)))
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        print("Result: {:.2f} C".format(fahr_to_celsius(fahrenheit)))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
