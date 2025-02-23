import requests
import json

def get_pokedex_data(pokedex_id=1):  # Default Pokedex ID 1 (Kanto)
    url = f"https://pokeapi.co/api/v2/pokedex/{pokedex_id}/"  # URL Pokedex dinamis

    response = requests.get(url)  # Mengirim permintaan GET ke API

    if response.status_code == 200:  # Memeriksa apakah status code 200 (OK)
        data = response.json()  # Mengambil data JSON dari response
        
        # Menulis data JSON ke file 'pokedex.json'
        with open('pokedex.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)  # Menulis data dengan indentasi untuk pembacaan yang lebih mudah
        
        print("Data has been written to pokedex.json")
        
    else:
        return json.dumps({"error": "Failed to retrieve data", "status_code": response.status_code})

# Panggil fungsi untuk mendapatkan data Pokedex (default ID 1: Kanto)
get_pokedex_data()

# Atau panggil dengan ID lain jika perlu (contoh ID 2: Johto)
# get_pokedex_data(2)
