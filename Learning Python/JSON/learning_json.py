import json

# encoding Json is called "serialization" - writing -  Transformation of data into a series of bytes
# decoding JSON is called deserialization - decoding process, reading 


data = {
    "president": {
        "name": "Andrzej Duda",
        "nationality": "Polish"
    }
}


def writing_json_to_file(data, filename):
    with open(filename,"w") as write_file:
        json.dump(data,write_file) # dump method takes two arg: data object to be serialized and file name which the bytes will be written 


def read_json_file(filename):
    with open (filename, "r") as read_file:
        data = json.load(read_file)
    return data

#writing_json_to_file(data,"data_file.json")

# to convert JSON to string we use "dumps" method which takes only one data argument
json_string = json.dumps(data,indent=4) # argument indent = 4 gives nice formatting 
#print(json_string)

#---- READING JSON FILE -----# 

data = read_json_file("data_file.json")

#print(data)
#print(type(data))

# --- reading JSON from string --- #

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

# read from string we are using "loads" method 

data = json.loads(json_string)
print(data)