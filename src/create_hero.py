from database.connection import execute_query
from pprint import pprint as bio

def create_hero():
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s);
    """
    query_abilities = """
        INSERT INTO ability_types (name)
        VALUES (%s);
    """
    
    heroName = input('Who are you new guy? ')
    heroAboutMe = input('catchphrase? ')
    heroBio = input('what is your story? ')
    heroPower = input('What are your powers ')


    execute_query(query, (heroName, heroAboutMe, heroBio))
    execute_query(query_abilities, (heroPower,))

create_hero()


#bio(select_all)
#select_all()

#heroes = execute_query("""
#INSERT INTO heroes (name, about_me, biography)
#VALUES ('Filangies', 'Wheres the discoball?', 'exposed to too many lasers')
#""")

#ability_types = execute_query("""
#INSERT INTO ability_types (name)
#VALUES ('laser fingers')
#""")

#input('What is your superhero')