import json
from os import getenv
from dotenv import load_dotenv
import psycopg2


load_dotenv()
HOST = getenv("HOST")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
PORT = getenv("PORT")
DBNAME = getenv("DBNAME")

connection = psycopg2.connect(
    host = HOST,
    user = USER,
    password = PASSWORD,
    port = PORT,
    database = DBNAME
)

cursor = connection.cursor()

def insert_moves_data():
    with open("/home/giery/assignment/skill_moves.json") as file:
        data = json.load(file)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skill_moves (
        id SERIAL PRIMARY KEY,
        move_name VARCHAR(255)
    )
    """)

    for entry in data:
        # move_id = entry.get("move_id")
        move_name = entry.get("name", {}).get("name", "")   
        cursor.execute("""
        INSERT INTO skill_moves (move_name)
        VALUES ( %s)""", (move_name,))

        connection.commit()

def insert_pokemon_data():
    with open("/home/giery/assignment/pokemon_data_1nf.json") as file:
        data = json.load(file)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        height INTEGER,
        weight INTEGER,
        types_1 VARCHAR(255),
        types_2 VARCHAR(255),
        abilities_1 VARCHAR(255),
        abilities_2 VARCHAR(255),
        abilities_3 VARCHAR(255),
        hp INTEGER,
        attack INTEGER,
        defense INTEGER,
        special_attack INTEGER,
        special_defense INTEGER,
        speed INTEGER,
        move_1 INTEGER REFERENCES skill_moves(id),           
        move_2 INTEGER REFERENCES skill_moves(id),           
        move_3 INTEGER REFERENCES skill_moves(id),           
        move_4 INTEGER REFERENCES skill_moves(id),           
        move_5 INTEGER REFERENCES skill_moves(id)           
    )
    """)

    # entry data

    for entry in data:
        name = entry.get("name")
        height = entry.get("height")
        weight = entry.get("weight")
        types_1 = entry.get("types_0")
        types_2 = entry.get("types_1")
        abilities_1 = entry.get("abilities_0")
        abilities_2 = entry.get("abilities_1")
        abilities_3 = entry.get("abilities_2")
        hp = entry.get("stats_hp")
        attack = entry.get("stats_attack")
        defense = entry.get("stats_defense")
        special_attack = entry.get("stats_special-attack")
        special_defense = entry.get("stats_special-defense")
        speed = entry.get("stats_speed")
        move_1 = entry.get("move_0",None)
        move_2 = entry.get("move_1", None)
        move_3 = entry.get("move_2", None)
        move_4 = entry.get("move_3", None)
        move_5 = entry.get("move_4", None)


        cursor.execute("""
        INSERT INTO pokemon (name, height, weight, types_1, types_2, abilities_1,
        abilities_2, abilities_3, hp, attack, defense, special_attack, special_defense, speed,
                       move_1, move_2, move_3, move_4, move_5)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )               
        """, (name, height, weight, types_1, types_2, abilities_1, abilities_2, abilities_3,
        hp, attack, defense, special_attack, special_defense, speed, move_1, move_2, move_3, move_4, move_5 ))
        
        connection.commit()

    print("Data berhasil dimasukkan ke database")


insert_moves_data()
insert_pokemon_data()
cursor.close()
connection.close()