from database.connection import execute_query

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
#        print(record[1])

#select_all()

#heroes = execute_query("""
#SELECT * FROM heroes
#LEFT JOIN ability_types on heroes.id = ability_types.id
#""")
#print(list(heroes))