from database.connection import execute_query

def hidden_rows():
    
    query_update = """
        UPDATE INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        RETURNING id;
    """

    update_hero = input('Who are you new guy? ')

    change = execute_query(query_update, (heroName, heroAboutMe, heroBio)).fetchall()

hidden_rows()