- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
***************************** MODULE 6.1 PYTHON & API **************************************************************
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -`- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 01-Ins_RequestsIntro
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Dependencies
import requests
import json

 
# URL for GET requests to retrieve vehicle data
url = "https://api.spacexdata.com/v4/launchpads"

 
# Print the response object to the console
print(requests.get(url))

 
# Retrieving data and converting it into JSON
print(requests.get(url).json())

 
# Pretty Print the output of the JSON
response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 02-Stu_SpaceX-Request
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Dependencies
import requests
import json

 
# URL for GET requests to retrieve vehicle data
url = "https://api.spacexdata.com/v4/launchpads"

 
# Pretty print JSON for all launchpads
response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))

 
# Pretty print JSON for a specific launchpad
response = requests.get(url + "/5e9e4502f509094188566f88").json()
print(json.dumps(response, indent=4, sort_keys=True))

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 03-Ins_ManipulatingResponses
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# %%
# Dependencies
import requests
import json

# %%
# Performing a GET Request and saving the 
# API's response within a variable
url = "https://api.spacexdata.com/v2/rockets/falcon9"
response = requests.get(url)
response_json = response.json()
print(json.dumps(response_json, indent=4, sort_keys=True))

# %%
# It is possible to grab a specific value 
# from within the JSON object
print(response_json["cost_per_launch"])

# %%
# It is also possible to perform some
# analyses on values stored within the JSON object
number_payloads = len(response_json["payload_weights"])
print(f"There are {number_payloads} payloads.")

# %%
# Finally, it is possible to reference the
# values stored within sub-dictionaries and sub-lists
payload_weight = response_json["payload_weights"][0]["kg"]
print(f"The first payload weighed {payload_weight} Kilograms")

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 04-Stu_FarFarAway-APIData
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# %%
# Dependencies
import requests
import json

# %%
# URL for GET requests to retrieve Star Wars character data
base_url = "https://swapi.dev/api/people/"

# %%
# Create a url with a specific character id
character_id = '4'
url = base_url + character_id
print(url)

# %%
# Perform a get request for this character
response = requests.get(url)
print(response.url)

# %%
# Storing the JSON response within a variable
data = response.json()
# Use json.dumps to print the json
print(json.dumps(data, indent=4, sort_keys=True))

# %%
# Print the name of the character retrieved
character_name = data["name"]
print(character_name)

# %%
# Print the number of films that they were in (hint: use len())
film_number = len(data["films"])
print(film_number)

# %%
# Request the starships URI found in the starships property of the
# previously retreived json, then use the response to figure out what this 
# character's first starship was
first_ship_url = data["starships"][0]
ship_response = requests.get(first_ship_url).json()
ship_response

# %%
# Print the name of the character's first starship
first_ship = ship_response["name"]
print(f"Their first ship: {first_ship}")

# %%
# BONUS
films = []

for film in data['films']:
    cur_film = requests.get(film).json()
    film_title = cur_film["title"]
    films.append(film_title)
    
print(f"{character_name} was in:")
print(films)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API  05-Par_NumberFacts-APIApplication
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# %%
# Dependencies
import requests
import json

# %%
# Base URL for GET requests to retrieve number/date facts
url = "http://numbersapi.com/"

# %%
# Ask the user what kind of data they would like to search for
question = ("What type of data would you like to search for? "
            "[Trivia, Math, Date, or Year] ")
kind_of_search = input(question)

# %%
# If the kind of search is "date" take in two numbers
if(kind_of_search.lower() == "date"):

  # Collect the month to search for
  month = input("What month would you like to search for? ")
  # Collect the day to search for
  day = input("What day would you like to search for? ")

  # Make an API call to the "date" API and convert response object to JSON
  response = requests.get(f"{url}{month}/{day}/{kind_of_search.lower()}?json").json()
  # Print the fact stored within the response
  print(response["text"])

# If the kind of search is anything but "date" then take one number
else:

  # Collect the number to search for
  number = input("What number would you like to search for? ")

  # Make an API call to the API and convert response object to JSON
  response = requests.get(url + number + "/" +  kind_of_search.lower()+ "?json").json()
  # Print the fact stored within the response
  print(response["text"])

# %%

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 06-Ins_OMDbRequests
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# %%
import requests
import json
from config import api_key

# %%
# New Dependency! Use this to pretty print the JSON
# https://docs.python.org/3/library/pprint.html
from pprint import pprint

# %%
# Note that the ?t= is a query param for the t-itle of the
# movie we want to search for.
url = "http://www.omdbapi.com/?t="
api_key = "&apikey=" + api_key

# %%
# Performing a GET request similar to the one we executed
# earlier
response = requests.get(url + "Aliens" + api_key)

# %%
# Converting the response to JSON, and printing the result.
data = response.json()
pprint(data)

# %%
# Print a few keys from the response JSON.
print(f"Movie was directed by {data['Director']}.")
print(f"Movie was released in {data['Country']}.")

# %%

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MODULE 6.1 API 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -












- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
***************************** MODULE 6.2 PYTHON & API **************************************************************
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -





- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
***************************** MODULE 6.3 PYTHON & API **************************************************************
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -





