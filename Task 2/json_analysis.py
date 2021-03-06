'''Lab 2.2'''
import json
import sys

def exit_check(text):
    '''
    The function exits the program if user typed in 'exit'
    '''
    if text == "exit":
        sys.exit()

def read_file():
    '''
    Reads a file and returns a dictinary
    '''
    while True:
        try:
            print("Type in the name of the file: ")
            name = input(">>> ")
            with open(name, encoding = 'utf-8') as file:
                data = json.load(file)
            return data
        except:
            print("File wasn't found")

def scan_main_list(json_obj):
    '''
    Scans the list for 'users' and returns info about the one user wanted to
    '''
    len_json = len(json_obj)

    print()
    for i in range(len(json_obj)):
        print("- Object " + str(i + 1))
    print()

    print("Enter the number of object: ")
    # the while loop that makes sure you entered the right number
    while True:
        number = input(">>> ")
        exit_check(number)
        if number.isdigit():
            number = int(number)
            if number > len_json or number <= 0:
                print("The number of object does not exist. Please try again")
                continue
            break
        else:
            print("You didn't enter a number. Please try again")
    return json_obj[number - 1]

def navigate_through_element(element):
    '''
    The function that navigates through json object
    '''
    if isinstance(element, dict):
        for key in element:
            print("-", str(key))
        print("Enter the key: ")
        key = input(">>> ")
        exit_check(key)
        while key not in element:
            print("You entered an incorrect key. Please try again: ")
            key = input(">>> ")
            exit_check(key)
        navigate_through_element(element[key])
    elif isinstance(element, list):
        if len(element) == 0:
            print("The list is empty")
            return
        elif len(element) == 1:
            print("The element was a list with one element. The navigation in this element:")
            navigate_through_element(element[0])
        else:
            print("The element is a list. Do you want to:")
            print("1) Print the whole list")
            print("2) Enter a specified index and print that element")
            while True:
                number = input(">>> ")
                exit_check(number)
                if number.isdigit():
                    number = int(number)
                    if number > 0 and number < 3:
                        break
                print("Entered action was incorrect")
            if number == 1:
                print()
                for i in range(len(element)):
                    print(str(i) + ') ' + str(element[i]))
                print()
                print("Select the index: ")
                print("Enter the index of the list. Enter a specified \
index from 0 to " + str(len(element) - 1))
                while True:
                    number = input(">>> ")
                    exit_check(number)
                    if number.isdigit():
                        number = int(number)
                        if number >= 0 and number < len(element):
                            break
                    print("The index was incorrect")
                navigate_through_element(element[number])
            else:
                print("Total number of elements in a list: " + str(len(element)) + \
                      ". Enter a specified index from 0 to " + str(len(element) - 1))
                while True:
                    number = input(">>> ")
                    exit_check(number)
                    if number.isdigit():
                        number = int(number)
                        if number >= 0 and number < len(element):
                            break
                    print("The index was incorrect: ")
                print(element[number])
                print()
                navigate_through_element(element[number])
    else:
        print("The value is:", element)

def main():
    '''
    Main function that organises everything and runs the program
    '''
    print("The navigation in json object")
    print()
    print("You can enter 'exit' to exit the program")
    print("Press Enter to continue")
    value = input(">>> ")
    exit_check(value)
    data = read_file()

    if isinstance(data, list):
        element = scan_main_list(data)
        navigate_through_element(element)
    else:
        for key in data:
            print("-", key)
        print("Enter the key: ")
        key = input(">>> ")
        exit_check(key)
        while key not in data:
            print("You entered an incorrect key. Please try again: ")
            key = input(">>> ")
            exit_check(key)
        if isinstance(data[key], int) or isinstance(data[key], str):
            print("The value is:", data[key])
            return
        elif isinstance(data[key], list):
            element = scan_main_list(data[key])
            navigate_through_element(element)

main()
