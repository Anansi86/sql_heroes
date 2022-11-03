from database.connection import execute_query

heroes = execute_query("""
    DELETE
    FROM heroes 
    WHERE id in (
    SELECT id 
    FROM heroes 
    ORDER BY id desc
    LIMIT 1
)
""")

ability_types = execute_query("""
    DELETE
    FROM ability_types 
    WHERE id in (
    SELECT id 
    FROM ability_types 
    ORDER BY id desc
    LIMIT 1
)
""")