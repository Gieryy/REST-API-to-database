import os
import json
from dotenv import load_dotenv
from pokemon import get_pokemon_data_range
from insert_pokemon_to_db import insert_moves_data, insert_pokemon_data
from normalizing_json import normalized_data


def main():
    load_dotenv()

    print("Mengambil data Pokémon dan skill moves Pokémon...")
    try:
        get_pokemon_data_range(1, 250)
    except Exception as e:
        print(f"Error saat mengambil data Pokémon: {e}")
        return

    path = "/home/giery/assignment/pokemon.json"
    print(f"Normalisasi data dari {path}...")
    
    try:
        normalized_data
    except Exception as e:
        print(f"Error saat normalisasi data: {e}")
        return

    print("Memasukkan data ke dalam database...")
    try:
        insert_moves_data()
        insert_pokemon_data()
        print("Data berhasil dimasukkan ke dalam database!")
    except Exception as e:
        print(f"Error saat memasukkan data ke database: {e}")
        return

if __name__ == "__main__":
    main()
