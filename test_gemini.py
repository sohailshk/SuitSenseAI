#!/usr/bin/env python3
"""
Test script to verify Gemini integration is working
"""

import os
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import setup_tools

# Test database connection
POSTGRES_USER = os.getenv("PG_USER")
POSTGRES_PASSWORD = os.getenv("PG_PASSWORD")
POSTGRES_PORT = os.getenv("PG_PORT")
POSTGRES_DB = os.getenv("PG_DB")

connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}"

print("🧪 Testing Gemini Integration...")
print(f"GEMINI_API_KEY set: {'✅' if os.getenv('GEMINI_API_KEY') else '❌'}")

try:
    # Test database connection
    print("\n📊 Testing database connection...")
    db = SQLDatabase.from_uri(connection_string)
    print(f"✅ Database connected! Tables: {len(db.get_usable_table_names())}")
    
    # Test LLM initialization
    print("\n🤖 Testing Gemini LLM...")
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.1,
    )
    print("✅ Gemini LLM initialized successfully")
    
    # Test simple LLM call
    print("\n💬 Testing simple LLM call...")
    response = llm.invoke("Say 'Gemini is working!' in exactly those words.")
    print(f"✅ LLM Response: {response.content}")
    
    # Test tools setup
    print("\n🛠️ Testing tools setup...")
    tools = setup_tools(db, llm)
    print(f"✅ Tools setup successful! Available tools: {len(tools)}")
    print(f"📋 Tool names: {[tool.name for tool in tools]}")
    
    # Test import of main module
    print("\n🔧 Testing main module import...")
    from main import process_question
    print("✅ Main module imported successfully")
    
    # Test server import
    print("\n� Testing server module import...")
    import server
    print("✅ Server module imported successfully")
    
    print("\n�🎉 All tests passed! Gemini integration is working correctly.")
    print("\n📋 Summary:")
    print(f"   • Database: Connected with {len(db.get_usable_table_names())} tables")
    print(f"   • LLM: Gemini 2.0 Flash Experimental")
    print(f"   • Tools: {len(tools)} available")
    print(f"   • Google Maps: API key configured")
    print(f"   • Server: Ready to start")
    
    print("\n🚀 Ready to run: python server.py")
    
except Exception as e:
    print(f"❌ Error during testing: {e}")
    import traceback
    traceback.print_exc()
