from database.connection import execute_query

def update_hero():
    
    query = """
        UPDATE heroes
        SET name = 'somethingElse'
        WHERE id = %s
    """

    updateName = input('What happened ')
   # updateAboutMe = input('I have changed ')
   # updateBio = input('I am new ')

    execute_query(query, (updateName,))

update_hero()