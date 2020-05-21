import sqlite3

class CharacterDB:
    """Returns database connection that should be used in a with statement"""
    def __enter__(self):
        # Creates database if it does not already exist, otherwise connects to
        #   an existing database named character.db :
        self.database = sqlite3.connect("character.db")
        print("connection successful") # debug
        return self.database

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("connection closed") # debug
        self.database.close()

# We will need to figure out what tables we need and just create them when the
# database is initialized for the first time
#
# I'm inclluding the following methods just as practice and to show some examples:
def create_character_table():
    with CharacterDB() as database:
        try:
            database.execute('''CREATE TABLE characters
                (id INT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                class TEXT NOT NULL,
                race TEXT NOT NULL,
                level INT NOT NULL);''')
            print("Table created successfully") # debug
        except Exception as e:
            if e == "sqlite3.OperationalError: table characters already exists":
                print("Table already exists")
            else:
                print(e)

def insert_characters():
    with CharacterDB() as database:

        database.execute("INSERT INTO characters \
            VALUES (1,'Phil','Barbarian','Half-Orc',5);")

        database.execute("INSERT INTO characters \
            VALUES (2,'Chuck','Bard','Human',4);")

        database.execute("INSERT INTO characters \
            VALUES (3,'Bartholomew','Rogue','Half-Elf',7);")

        database.commit()
        print("Characters added successfully")

def select_characters():
    with CharacterDB() as database:
        cursor = database.execute("SELECT id, name, class, level FROM characters;")

        for row in cursor:
            print("ID =", row[0])
            print("NAME =", row[1])
            print("CLASS =", row[2])
            print("LEVEL =", row[3], "\n")

def update_characters():
    with CharacterDB() as database:
        database.execute("UPDATE characters SET level = 6 WHERE name = 'Phil';")
        database.commit()
        print("Total number of rows updated:", database.total_changes)
        select_characters()

def delete_characters():
    with CharacterDB() as database:
        database.execute("DELETE FROM characters WHERE name = 'Chuck';")
        database.commit()
        select_characters()

def cleanup():
    with CharacterDB() as database:
        database.execute("DROP TABLE characters")

def example_run():
    print("\n===CREATE TABLE===\n")
    create_character_table()
    print("\n===INSERT CHARACTERS===\n")
    insert_characters()
    print("\n===SELECT CHARACTERS===\n")
    select_characters()
    print("\n===UPDATE CHARACTERS===\n")
    update_characters()
    print("\n===DELETE CHARACTERS===\n")
    delete_characters()
    cleanup()
    print("\ndone.")

if __name__ == "__main__":
    example_run()
