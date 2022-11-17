import unittest
import sqlite3
import json
import os
# starter code

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):

    species = ["Rabbit",
    "Dog",
    "Cat",
    "Boa Constrictor",
    "Chinchilla",
    "Hamster",
    "Cobra",
    "Parrot",
    "Shark",
    "Goldfish",
    "Gerbil",
    "Llama",
    "Hare"
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)",(i,species[i]))
    conn.commit()

# TASK 1
# CREATE TABLE FOR PATIENTS IN DATABASE
def create_patients_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Patients")
    cur.execute("CREATE TABLE Patients (pet_id, name STRING, species_id NUMBER, age INTEGER, cuteness INTEGER, aggressiveness NUMBER)")
    conn.commit()
    


# ADD FLUFFLE TO THE TABLE
def add_fluffle(cur, conn):
    cur.execute('''INSERT INTO Patients (pet_id, name, species_id, age, cuteness, aggressiveness)
                VALUES (0, 'Fluffle', 'Rabbit', 3, 90, 100)''')
    conn.commit()
    

# TASK 2
# CODE TO ADD JSON TO THE TABLE
# ASSUME TABLE ALREADY EXISTS
def add_pets_from_json(filename, cur, conn):
    
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    # THE REST IS UP TO YOU
    
    for i in range(len(json_data)):
    
        cur.execute('''INSERT INTO Patients (name, species_id, age, cuteness, aggressiveness) VALUES (?,?,?,?,?)''', (json_data[i]['name'],json_data[i]['species'],json_data[i]['age'],json_data[i]['cuteness'],json_data[i]['aggressiveness']))

    cur.execute('UPDATE Patients SET pet_id=0 WHERE species_id="Rabbit"')
    cur.execute('UPDATE Patients SET pet_id=1 WHERE species_id="Dog"')
    cur.execute('UPDATE Patients SET pet_id=2 WHERE species_id="Cat"')
    cur.execute('UPDATE Patients SET pet_id=3 WHERE species_id="Boa Constrictor"')
    cur.execute('UPDATE Patients SET pet_id=4 WHERE species_id="Chinchilla"')
    cur.execute('UPDATE Patients SET pet_id=5 WHERE species_id="Hamster"')
    cur.execute('UPDATE Patients SET pet_id=6 WHERE species_id="Cobra"')
    cur.execute('UPDATE Patients SET pet_id=7 WHERE species_id="Parrot"')
    cur.execute('UPDATE Patients SET pet_id=8 WHERE species_id="Shark"')
    cur.execute('UPDATE Patients SET pet_id=9 WHERE species_id="Goldfish"')
    cur.execute('UPDATE Patients SET pet_id=10 WHERE species_id="Gerbil"')
    cur.execute('UPDATE Patients SET pet_id=11 WHERE species_id="Llama"')
    cur.execute('UPDATE Patients SET pet_id=12 WHERE species_id="Hare"')

    conn.commit()
    pass

# TASK 3
# CODE TO OUTPUT NON-AGGRESSIVE PETS
def non_aggressive_pets(aggressiveness, cur, conn):
    tup_list = []
    cur.execute('SELECT name, aggressiveness FROM Patients WHERE aggressiveness < 10')
    for row in cur:
        tup_list.append(row)
    return(tup_list)


def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('animal_hospital.db')
    create_species_table(cur, conn)

    create_patients_table(cur, conn)
    add_fluffle(cur, conn)
    add_pets_from_json('pets.json', cur, conn)
    ls = (non_aggressive_pets(10, cur, conn))
    print(ls)
    
    
if __name__ == "__main__":
    main()

