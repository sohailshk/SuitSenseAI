import os
from langchain_community.utilities.sql_database import SQLDatabase

# Database connection
POSTGRES_USER = os.getenv('PG_USER')
POSTGRES_PASSWORD = os.getenv('PG_PASSWORD')
POSTGRES_PORT = os.getenv('PG_PORT')
POSTGRES_DB = os.getenv('PG_DB')

print(f'PG_USER: {POSTGRES_USER}')
print(f'PG_PASSWORD: {POSTGRES_PASSWORD}')
print(f'PG_PORT: {POSTGRES_PORT}')
print(f'PG_DB: {POSTGRES_DB}')

connection_string = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}'
print('Connection string:', connection_string)

try:
    db = SQLDatabase.from_uri(connection_string)
    print('Database connected successfully!')
    print('Available tables:', db.get_usable_table_names())
    
    # Test a simple query
    result = db.run('SELECT COUNT(*) FROM core_condobuilding')
    print('Number of buildings:', result)
    
    # Test another query
    result = db.run('SELECT address FROM core_condobuilding LIMIT 3')
    print('Sample addresses:', result)
    
except Exception as e:
    print('Error:', e)
