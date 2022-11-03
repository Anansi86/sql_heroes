from database.connection import execute_query
from pprint import pprint as bio

def create_hero():
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s);
    """
    heroName = input('Who are you new guy? ')
    heroAboutMe = input('catchphrase? ')
    heroBio = input('what is your story? ')

    execute_query(query, (heroName, heroAboutMe, heroBio))

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




