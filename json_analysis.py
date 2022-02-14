'''Lab 2.2'''
import json
import sys

def exit_check(text):
    '''
    The function exits the program if user typed in 'exit'
    '''
    if text == "exit":
        sys.exit()

def read_file(file_url):
    '''
    Reads a file and returns a dictinary
    >>> read_file('twitter1.json') #doctest: +ELLIPSIS
    [{'created_at': 'Sun Jan 30 16:36:22 +0000 2022', 'id': 1487827036236394510, \
'id_str': '1487827036236394510', 'text': 'Great seminar about "Putin’s \
aggression and how to...
    >>> read_file('twitter2.json') #doctest: +ELLIPSIS
    {'users': [{'id': 2751434132, 'id_str': '2751434132', 'name': \
'Brilliant Maps', 'screen_name': 'BrilliantMaps', 'location': 'London \
and around the world', 'description':...
    '''
    with open(file_url, encoding = 'utf-8') as file:
        data = json.load(file)
    return data

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
                print("Enter the index of the list: ")
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
                print("Enter a specified index: ")
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
    data = read_file('twitter1.json')

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
