from database.connection import execute_query


def view_all():
    query = """
    SELECT heroes.id, heroes.name, heroes.about_me, heroes.biography, ability_types.name
    FROM heroes
    LEFT OUTER JOIN abilities
    ON heroes.id = abilities.hero_id
    LEFT OUTER JOIN ability_types
    ON abilities.ability_type_id = ability_types.id
    """
    list_of_heroes = execute_query(query).fetchall()
    for hero in list_of_heroes:
        print(hero[1] + ":")
        print("    " + hero[2])
        print("    " + hero[3])
        print("    Power: " + hero[4])
        print("---")
        print("")
    
view_all()

#heroes = execute_query("""
#SELECT *
#FROM ability_types
#""")
#print(list(heroes))

#def select_all():
#    query = """
#        SELECT * from ability_types
#    """

#    list_of_heroes = execute_query(query).fetchall()
#    print(list_of_heroes)
#    for record in list_of_heroes:
#         print(record[1])

#select_all()

#heroes = execute_query("""
#SELECT * FROM heroes
#LEFT JOIN ability_types on heroes.id = ability_types.id
#""")
#print(list(heroes))