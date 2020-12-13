import sqlite3

class CharacterDB:
    def __init__(self, first_connect):
        if first_connect:
            self.create_character_table()
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

    def create_character_table():
        try:
            self.database.execute('''CREATE TABLE characters
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

    def get_character_from_id(self, id):
        try:
            execute_string = '''SELECT * from characters WHERE id = %d;''' % (id)
            character = self.db.execute(execute_string)
        except Exception as e:
            print(e)
            character = None
        return character

    def get_max_character_id(self):
        try:
            id = self.db.execute("SELECT MAX(id) FROM characters;")
        except Exception as e:
            id = None
            print(e)
        return id

    def get_all_characters(self):
        try:
            characters = self.db.execute("SELECT * from characters;")
        except Exception as e:
            characters = None
            print(e)
        return characters


    def create_character(self, name, game, char_class, race, level):
        id = string(int(get_max_character_id())+1)
        try:
            execute_string = '''INSERT INTO characters \
            VALUES (%d, %s, %s, %s, %s, %s);
            ''' % (id, name, game, char_class, race, level)
            character = self.db.execute(execute_string)
            self.database.commit()
        except Exception as e:
            character = None
            print(e)
        return character

    def update_character(self, id, key, value):
        try:
            execute_string = "UPDATE characters SET %s = %s WHERE id = %d;" % (key, value, id)
            character = self.db.execute(execute_string)
            self.database.commit()
        except Exception as e:
            character = None
            print(e)
        return character

    def delete_character(self, id):
        try:
            execute_string = "DELETE FROM characters WHERE id = %d;" % (id)
            self.db.execute(execute_string)
            self.datbase.commit()
            return True
        except Exception as e:
            print(e)
            return False


class WeaponDB:
    def __init__(self, first_connect):
        if first_connect:
            create_weapon_tables()
        self.db = self.__enter__()

    """Returns database connection that should be used in a with statement"""
    def __enter__(self):
        # Creates database if it does not already exist, otherwise connects to
        #   an existing database named weapon.db :
        self.database = sqlite3.connect("weapon.db")
        print("connection successful") # debug
        return self.database


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("connection closed") # debug
        self.database.close()

    def create_weapon_tables():
        try:
            self.database.execute('''CREATE TABLE melee
            (id INT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            range TEXT NOT NULL,
            price TEXT,
            expertise TEXT NOT NULL,
            handling TEXT NOT NULL,
            size TEXT NOT NULL,
            damage_type TEXT NOT NULL,
            damage_dice TEXT NOT NULL,
            condition TEXT NOT NULL););''')

            self.database.execute('''CREATE TABLE ranged
            (id INT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            range TEXT NOT NULL,
            price TEXT,
            ammunition TEXT NOT NULL,
            expertise TEXT NOT NULL,
            handling TEXT NOT NULL,
            damage_type TEXT NOT NULL,
            damage_dice TEXT NOT NULL,
            size TEXT NOT NULL,
            condition TEXT NOT NULL););''')
        print("Table created successfully") # debug
    except Exception as e:
        if e == "sqlite3.OperationalError: table characters already exists":
            print("Table already exists")
        else:
            print(e)

    def get_melee_weapon_from_id(self, id):
        try:
            execute_string = "SELECT * FROM melee WHERE id = %d;" % (id)
            weapon = self.database.execute(execute_string)
        except Exception as e:
            print(e)
            weapon = None
        return weapon

    def get_ranged_weapon_from_id(self, id):
        try:
            execute_string = "SELECT * FROM ranged WHERE id = %d;" % (id)
            weapon = self.database.execute(execute_string)
        except Exception as e:
            print(e)
            weapon = None
        return weapon

    def get_max_melee_id(self):
        try:
            id = self.db.execute("SELECT MAX(id) from melee;")
        except Exception as e:
            print(e)
            id = None
        return id

    def get_max_ranged_id(self):
        try:
            id = self.db.execute("SELECT MAX(id) from ranged;")
        except Exception as e:
            print(e)
            id = None
        return id

    def get_all_melee_weapons(self):
        try:
            weapons = self.db.execute("SELECT * from melee;")
        except Exception as e:
            print(e)
            weapons = None
        return weapons

    def get_all_ranged_weapons(self):
        try:
            weapons = self.db.execute("SELECT * from ranged;")
        except Exception as e:
            print(e)
            weapons = None
        return weapons

    def create_melee_weapon(self, name, range, price, expertise, handling, size,
        damage_type, damage_dice, condition):
        id = string(int(get_max_melee_id())+1)
        try:
            execute_string = '''INSERT INTO melee \
            VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            ''' % (id, name, range, price, expertise, handling, size, damage_type,
                    damage_dice, condition)
            weapon = self.db.execute(execute_string)
            self.database.commit()
        except Exception as e:
            weapon = None
            print(e)
        return weapon

    def create_ranged_weapon(self, name, range, price, ammunition, expertise,
        handling, damage_type, damage_dice, size, condition):
        id = string(int(get_max_ranged_id())+1)
        try:
            execute_string = '''INSERT INTO melee \
            VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            ''' % (id, name, range, price, ammunition, expertise, handling, size,
            damage_type, damage_type, damage_dice, size, condition)
            weapon = self.db.execute(execute_string)
            sefl.database.commit()
        except Exception as e:
            weapon = None
            print(e)
        return weapon

    def update_melee_weapon(self, id, key, value):
        try:
            execute_string = "UPDATE melee SET %s = %s WHERE id = %d;" % (key, value, id)
            weapon = self.db.execute(execute_string)
            self.database.commit()
        except Excpetion as e:
            weapon = None
            print(e)
        return weapon

    def update_ranged_weapon(self, id, key, value):
        try:
            execute_string = "UPDATE ranged SET %s = %s WHERE id = %d;" % (key, value, id)
            weapon = self.db.execute(execute_string)
            self.database.commit()
        except Excpetion as e:
            weapon = None
            print(e)
        return weapon

    def delete_melee_weapon(self, id):
        try:
            execute_string = "DELETE FROM melee WHERE id = %d;" % (id)
            self.db.execute(execute_string)
            self.database.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_ranged_weapon(self, id):
        try:
            execute_string = "DELETE FROM ranged WHERE id = %d;" % (id)
            self.db.execute(execute_string)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False



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
