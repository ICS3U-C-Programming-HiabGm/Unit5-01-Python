# Created by: Hiab G
# Date: Wed, May. 3rd
# This program gets celsius and converts it to fahrenheit


def convert_celsius():

    try:
    # Input
        celsius = float(input("Enter celsius that you would like to convert to fahrenheit :"))
    # Process to convert celsius to fahrenheit
        fahrenheit = celsius * 9/5 + 32
    # Output 
        print(f"{celsius} in fahrenheit is {fahrenheit} ". format(fahrenheit))

# Catch erroneous input
    except Exception:

        print("Please enter a valid input.")

if __name__ == "__main__":
    convert_celsius()

def main():
    # Call function
    convert_celsius()

if __name__ == "__main__":
    main()





