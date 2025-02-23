import json

path ="/home/giery/assignment/pokemon.json"

def normalize_json(data):
    normalize_json = []

    for iter in data:
        temp_data = {}

        for key, value in iter.items():
            if isinstance(value,dict):
                for sub_key, sub_value in value.items():
                    temp_data[f"{key}_{sub_key}"] = sub_value
            elif isinstance(value, list):
                if key == "moves":
                    selected_moves = value[:5]
                    for ind, move in enumerate(selected_moves):
                        temp_data[f"move_{ind}"] = move["id"]
                elif len(value) > 0 and isinstance(value[0], dict):
                    for ind, sub_value in enumerate(value):
                        for sub_key, sub_sub_value in sub_value.items():
                            temp_data[f"{key}_{ind}_{sub_key}"] = sub_sub_value
                elif len(value) > 0 and not isinstance(value[0], dict):
                    for ind, item in enumerate(value):
                        temp_data[f"{key}_{ind}"] = item
            else:
                temp_data[key] = value
            
        normalize_json.append(temp_data)

    return normalize_json


def read_json_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data

data = read_json_file(path) 

normalized_data = normalize_json(data)

with open('/home/giery/assignment/pokemon_data_1nf.json','w')as outfile:
    json.dump(normalized_data,outfile, indent=4)

print("Normalisasi telah selesai dilakukan")


normalize_json