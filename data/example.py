import os, json

# HOW TO load a json file as python object
# variable_name = json.load(open("/path/to/your/file", "r"))

# Location Data
# Object Fields
# {
#   "loc_id": 1.0,
#   "title": "Amherst Survival Center",
#   "type": "Agency",
#   "street1": "138 Sunderland Road",
#   "city": "Amherst",
#   "zip": "01002",
#   "state": "MA",
#   "long": -72.53289,
#   "lat": 42.41472
# }
locations = json.load(open(os.path.abspath("./locations.json"), "r"))

# Loop over Location data and access fields
for location in locations:
	print(location.get("loc_id"), location.get("title"))

# Distance Matrix
# 136x136 Matrix - Distances stored as Meters
distances_matrix = json.load(open(os.path.abspath("./distances_matrix.json"), "r"))

# get distance from location id i to location id j (note matrix are 0 (zero) indexed)
i = 1
j = 2
print(f'Distance from {locations[i-1].get("title")} to {locations[j-1].get("title")}: {distances_matrix[i-1][j-1]/1000} km')


#Travel Times Matrix
# 136x136 Matrix - Time travelled stored as Seconds
travel_times_matrix = json.load(open(os.path.abspath("./travel_times_matrix.json"), "r"))

# get travel time from location id i to location id j (note matrix are 0 (zero) indexed)
i = 20
j = 25
print(f'Travel time from {locations[i-1].get("title")} to {locations[j-1].get("title")}: {travel_times_matrix[i-1][j-1]} seconds')