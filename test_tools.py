import os
from langchain_community.utilities.sql_database import SQLDatabase
from tools import setup_tools
from langchain_google_genai import ChatGoogleGenerativeAI

# Test database connection and tools
POSTGRES_USER = os.getenv("PG_USER")
POSTGRES_PASSWORD = os.getenv("PG_PASSWORD")
POSTGRES_PORT = os.getenv("PG_PORT")
POSTGRES_DB = os.getenv("PG_DB")

connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}"
db = SQLDatabase.from_uri(connection_string)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.1,
)

print("Testing database connection...")
print(f"Available tables: {db.get_usable_table_names()}")

print("\nTesting SQL query...")
result = db.run("SELECT COUNT(*) FROM core_condobuilding")
print(f"Number of buildings: {result}")

print("\nTesting tools setup...")
tools = setup_tools(db, llm)
print(f"Available tools: {[tool.name for tool in tools]}")

print("\nTesting SQL database tool...")
sql_tools = [tool for tool in tools if 'sql' in tool.name.lower()]
print(f"SQL tools: {[tool.name for tool in sql_tools]}")

if sql_tools:
    sql_tool = sql_tools[0]
    print(f"Testing {sql_tool.name}...")
    try:
        result = sql_tool.run("SELECT COUNT(*) FROM core_condobuilding")
        print(f"SQL tool result: {result}")
    except Exception as e:
        print(f"Error with SQL tool: {e}")
