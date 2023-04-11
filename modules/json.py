import json

# Data to be written
dictionary = {
 "name": "Goober",
 "credits": 56,
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("data.json", "w") as outfile:
	outfile.write(json_object)
