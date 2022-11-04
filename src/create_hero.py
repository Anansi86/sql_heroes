from database.connection import execute_query

def create_hero():
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    query_abilities = """
        INSERT INTO ability_types (name)
        VALUES (%s)
        RETURNING id;
    """
    query_pivot = """
        INSERT INTO abilities (hero_id, ability_type_id)
        VALUES (%s, %s)

    """    
    heroName = input('Who are you new guy? ')
    heroAboutMe = input('catchphrase? ')
    heroBio = input('what is your story? ')
    heroPower = input('What are your powers ')


    hero_id = execute_query(query, (heroName, heroAboutMe, heroBio)).fetchall()
    ability_types_id = execute_query(query_abilities, (heroPower,)).fetchall()
    execute_query(query_pivot, (hero_id[0][0], ability_types_id[0][0]))
    
#    print(hero_id[0][0])
#    print(ability_types_id[0][0])

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