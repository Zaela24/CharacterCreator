import sqlite3

class CharacterDB:
    def __init__(self, first_connect):
        if first_connect:
            create_db()
        self.db = self.__enter__()

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

    def get_character_from_id(self, id):
        try:
            execute_string = '''SELECT * from characters WHERE id = %s
            ''' % (id)
            character = self.db.execute(execute_string)
        except Exception as e:
            print(e)
            character = None
        return character

    def get_max_character_id(self):
        try:
            id = self.db.execute("MAX(ID) expression")
        except Exception as e:
            id = None
            print(e)
        return id

    def get_all_characters(self):
        db = self.__enter__()
        try:
            characters = db.execute("SELECT * from characters")
            print(characters)
        except Exception as e:
            print(e)


    def create_character(self, name, game, char_class, race, level):
        id = string(int(get_max_character_id())+1)
        try:
            execute_string = '''INSTERT INTO characters \
            VALUES (%s, %s, %s, %s, %s, %s);
            ''' % (id, name, game, char_class, race, level)
        except Exception as e:
            print(e)




# We will need to figure out what tables we need and just create them when the
# database is initialized for the first time
#
# I'm inclluding the following methods just as practice and to show some examples:
def create_character_table():
    character_database = CharacterDB(False)

    with character_database.db as database:
        try:
            database.execute('''CREATE TABLE characters
                (id INT PRIMARY KEY NOT NULL,
                game TEXT NOT NULL,
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
    character_database = CharacterDB(False)

    with character_database.db as database:

        database.execute("INSERT INTO characters \
            VALUES (1, 'DnD', 'Phil','Barbarian','Half-Orc',5);")

        database.execute("INSERT INTO characters \
            VALUES (2, 'Pathfinder', 'Chuck','Bard','Human',4);")

        database.execute("INSERT INTO characters \
            VALUES (3, 'Other', 'Bartholomew','Rogue','Half-Elf',7);")

        database.commit()
        print("Characters added successfully")

def select_characters():
    character_database = CharacterDB(False)

    with character_database.db as database:
        cursor = database.execute("SELECT id, game, name, class, level FROM characters;")

        for row in cursor:
            print("ID =", row[0])
            print("GAME =", row[1])
            print("NAME =", row[2])
            print("CLASS =", row[3])
            print("LEVEL =", row[4], "\n")

def get_characters():
    character_db = CharacterDB(False)
    character_db.get_all_characters()

def update_characters():
    character_database = CharacterDB(False)

    with character_database.db as database:
        database.execute("UPDATE characters SET level = 6 WHERE name = 'Phil';")
        database.commit()
        print("Total number of rows updated:", database.total_changes)
        select_characters()

def delete_characters():
    character_database = CharacterDB(False)

    with character_database.db as database:
        database.execute("DELETE FROM characters WHERE name = 'Chuck';")
        database.commit()
        select_characters()

def cleanup():
    character_database = CharacterDB(False)

    with character_database.db as database:
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
    print("\n===GET ALL CHARACTERS===\n")
    get_characters()
    print("\n===DELETE CHARACTERS===\n")
    delete_characters()
    cleanup()
    print("\ndone.")



if __name__ == "__main__":
    example_run()
