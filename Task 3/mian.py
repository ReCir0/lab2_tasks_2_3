'''Lab 2.3'''
import requests
from flask import Flask, render_template, url_for, request
from geopy.geocoders import Nominatim
from folium import FeatureGroup, Map, Marker, IFrame, Icon, Popup, LayerControl

def get_information(username):
    '''
    Gets information about a specific user's followers
    '''
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJ32ZAEAAAAA%2B5H%2BzF8MAfxahMPXdBrlbutKW30%3D6Vh4exUrn2x8RcsydpXnRQA7g5H3SmKqR1ouiOF1UQypZLNobl'

    headers = {'Authorization': f'Bearer {bearer_token}'}
    params = {'screen_name': username, 'count': 200}

    response = requests.get('https://api.twitter.com/1.1/friends/list.json',
                            headers=headers,
                            params=params)
    try:
        return response.json()["users"]
    except KeyError:
        return False

def get_locations(json_obj):
    '''
    Analyses given json object and gets all necessary information to build a map

    Returns a list with coordinates and a mane of a film
    '''
    full_list = []
    for elem in json_obj:
        if elem["location"] != '':
            try:
                location = Nominatim(user_agent="app_name").geocode(elem["location"])
            except:
                continue
            if location == None:
                continue
            full_list.append(((location.latitude, location.longitude), elem["screen_name"]))
    return full_list

def build_a_map(locations_and_text):
    '''
    Builds a map of locations of the followers of the user
    '''
    main_map = Map(location = [20, 0], zoom_start = 2, control_scale = True)

    markers_group = FeatureGroup(name="Markers of films", show=True)
    main_map.add_child(markers_group)

    for element in locations_and_text:
        iframe = (IFrame(element[1], width=300, height=100))
        markers_group.add_child(Marker(location = element[0], popup= \
            Popup(iframe), icon=Icon(color='green')))

    main_map.add_child(LayerControl())
    main_map.save("templates/map.html")


def connect_function(username):
    '''
    A main function that connects all of them together
    '''
    json_obj = get_information(username)
    if json_obj is False:
        return False
    else:
        locations_and_text = get_locations(json_obj)
        build_a_map(locations_and_text)

app = Flask(__name__)
@app.route("/")
def check():
    '''
    Loads main page
    '''
    return render_template('index.html')


@app.route("/result", methods=['POST'])
def enter():
    '''
    Loads a map by username
    '''
    username = request.form['username']
    h = connect_function(username)
    if h is False:
        return render_template('error.html')
    else:
        return render_template('map.html')


app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
