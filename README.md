# Json navigator(task 2.2)

## Reading a file

I use the file that I got after using Twitter API and read it with json module

```python
def read_file(file_url):
    with open(file_url, encoding = 'utf-8') as file:
        data = json.load(file)
    return data
```

## Main list scanner

I go through a main list, ask user to print a specified number of a list

## Navigating through all file

I used recursion to go through all file. My function consists of one if-elif-else block, that analyses information depending on a type of the object that the program dived into

## Exit checker

I made a simple function that is called after every `input()` and checks if the user entered `exit` and closes the app if they did so

```python
if text == "exit":
    sys.exit()
```

## Conclusion

Every function is connected wia `main()`. All different scenarios of what can be inside a file are taken into consideration and the navigation is completed




# Some task(task 2.3)
