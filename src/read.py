from database.connection import execute_query

#heroes = execute_query("""
#CREATE TABLE test_super (
#                id serial PRIMARY KEY,
#                heroes text,
#                ability_types text)
#""")
#print(heroes)

def select_all():
    query = """
        SELECT * from heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    print(list_of_heroes)
    for record in list_of_heroes:
        print(record[3])

select_all()
