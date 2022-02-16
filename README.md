# Twitter API navigator(task 2.2)

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




# Search the subscribers' location with Twitter API and get the map with markers of that locations(task 2.3)

## The main idea

The idea was to create a web aplication that easily would alow a user to type in a nickname and show all that person's friends' location on a map. It was great for me to work with folium module once again and to find some ways of connecting HTML with Python using Flask

## HTML pages

I created a main HTML page with a input field and a button on it. The field is used for a user to type in a username. I downloaded two images and created a CSS file to make the website look nicer

```html
<form name="test", action="{{ url_for('enter') }}", method="post">
    <input class="field_to_send" type="text" name="username", placeholder="@Username">
    <button>Search!</button>
</form>
```

I connected that main form to make POST requests to my python file which means to send a python file the information user entered

I also created an error page that is show whether a username doesn't exist. It has a link on it that throws you back to the main page

And the last page in the map page itself where you are directed right after the map is generated

## The main script

The script's function `get_information(username)`  gets information from Twitter using a Get request and a Bearer token

```python
headers = {'Authorization': f'Bearer {bearer_token}'}
params = {'screen_name': username, 'count': 200}

response = requests.get('https://api.twitter.com/1.1/friends/list.json', headers = headers, params = params)
```

Then `get_locations(json_obj)` gets the coordinates ofusers' locations

```python
location = Nominatim(user_agent="app_name").geocode(elem["location"])
```

`build_a_map(locations_and_text)` function builds a map with markers on it and then `connect_function(username)` works as a function that unites everything and makes it work together

The only thing required left is the username that user enteres using a form. I used Flask to make that

Loading the main page:

``` python
app = Flask(__name__)
@app.route("/")
def check():
    return render_template('index.html')
```

Loading either an error page or a map page:

```python
@app.route("/result", methods=['POST'])
def enter():
    username = request.form['username']
    h = connect_function(username)
    if h is False:
        return render_template('error.html')
    else:
        return render_template('map.html')
```

h is a variable that indicates whether the person was found by username or not

## Conclusion

The program was uploaded on pythonanywhere.com and works properly using the link: http://recir0.pythonanywhere.com
