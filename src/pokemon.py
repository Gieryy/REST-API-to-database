import requests
import json

def get_pokemon_by_id(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        
        pokemon_details = {
            'name': pokemon_data['name'],
            'id': pokemon_data['id'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'types': [type['type']['name'] for type in pokemon_data['types']],
            'abilities': [ability['ability']['name'] for ability in pokemon_data['abilities']],
            'stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']},
        }
        moves = [{'id': move_info['move']['url'].split('/')[-2], 'name': move_info['move']['name']} for move_info in pokemon_data['moves']]

        return pokemon_details, moves
    else:
        print(f"Failed to get data for Pokemon ID: {pokemon_id}")
        return None,None

def get_pokemon_data_range(start_id, end_id, save_to_json=True):
    all_pokemon_data = []
    all_moves_data = []
    move_id_counter =1

    for pokemon_id in range(start_id, end_id + 1):
        pokemon_details, moves = get_pokemon_by_id(pokemon_id)
        
        if pokemon_details:
            all_pokemon_data.append(pokemon_details)

            for move in moves:
                if move not in [m['name'] for m in all_moves_data]:
                    all_moves_data.append({'id':move_id_counter, 'name':move})
                    move_id_counter + 1
    
    if save_to_json:
        def save_pokemon_to_json(pokemon_data, filename="/home/giery/assignment/pokemon.json"):
            with open(filename, 'w') as f:
                json.dump(pokemon_data, f, indent=4)
            
            print(f"Data Pokémon ID {start_id} to {end_id} succesfully saved to 'pokemon.json'")

        def save_moves_to_json(moves_data, filename="/home/giery/assignment/skill_moves.json"):
            with open(filename, 'w') as f:
                json.dump(moves_data,f,indent=4)
            print(f"Pokemon Skill Moves Data Succesfully saved to '{filename}")

        save_pokemon_to_json(all_pokemon_data, "pokemon.json")
        save_moves_to_json(all_moves_data, "skill_moves.json")

    return all_pokemon_data, all_moves_data 

get_pokemon_data_range(1, 250)