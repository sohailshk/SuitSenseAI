#!/usr/bin/env python3
"""
Database initialization script for SuitSenseAI
This script sets up the database schema and loads sample data
"""

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def get_db_connection():
    """Get database connection from environment variables"""
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL:
        return psycopg2.connect(DATABASE_URL)
    
    # Fallback to individual credentials
    return psycopg2.connect(
        host=os.getenv("PG_HOST", "localhost"),
        port=os.getenv("PG_PORT", "5432"),
        database=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD")
    )

def init_database():
    """Initialize the database with sample real estate data"""
    try:
        conn = get_db_connection()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        print("🏗️ Creating database schema...")
        
        # Create buildings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS core_condobuilding (
                id SERIAL PRIMARY KEY,
                address VARCHAR(255) NOT NULL,
                alt_name VARCHAR(255),
                city VARCHAR(100),
                state VARCHAR(50),
                zip_code VARCHAR(20),
                year_built INTEGER,
                total_units INTEGER,
                avg_price_psf DECIMAL(10,2),
                latitude DECIMAL(10,8),
                longitude DECIMAL(11,8),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Create sample data
        sample_buildings = [
            ("123 Main St", "Downtown Tower", "New York", "NY", "10001", 2010, 150, 1200.50, 40.7589, -73.9851),
            ("456 Oak Ave", "Oak Gardens", "Los Angeles", "CA", "90210", 2015, 80, 1500.75, 34.0522, -118.2437),
            ("789 Pine Rd", "Pine Heights", "Chicago", "IL", "60601", 2018, 120, 900.25, 41.8781, -87.6298),
            ("321 Elm St", "Elm Plaza", "Miami", "FL", "33101", 2020, 90, 1800.00, 25.7617, -80.1918),
            ("654 Maple Dr", "Maple Commons", "Seattle", "WA", "98101", 2019, 110, 1350.40, 47.6062, -122.3321)
        ]
        
        print("📊 Inserting sample real estate data...")
        
        for building in sample_buildings:
            cursor.execute("""
                INSERT INTO core_condobuilding 
                (address, alt_name, city, state, zip_code, year_built, total_units, avg_price_psf, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
            """, building)
        
        # Create schools table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schools (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address VARCHAR(255),
                city VARCHAR(100),
                state VARCHAR(50),
                school_type VARCHAR(50),
                rating DECIMAL(3,2),
                latitude DECIMAL(10,8),
                longitude DECIMAL(11,8)
            );
        """)
        
        sample_schools = [
            ("Washington Elementary", "100 School St", "New York", "NY", "Elementary", 4.5, 40.7505, -73.9934),
            ("Lincoln High School", "200 Education Ave", "Los Angeles", "CA", "High School", 4.2, 34.0522, -118.2500),
            ("Roosevelt Middle School", "300 Learning Blvd", "Chicago", "IL", "Middle School", 4.0, 41.8700, -87.6200),
            ("Jefferson Academy", "400 Knowledge Dr", "Miami", "FL", "Academy", 4.8, 25.7700, -80.1900),
            ("Madison Prep", "500 Wisdom Way", "Seattle", "WA", "Prep School", 4.6, 47.6100, -122.3300)
        ]
        
        for school in sample_schools:
            cursor.execute("""
                INSERT INTO schools 
                (name, address, city, state, school_type, rating, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
            """, school)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✅ Database initialized successfully!")
        print("🏢 Sample real estate data loaded")
        print("🏫 Sample school data loaded")
        return True
        
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting database initialization...")
    success = init_database()
    if success:
        print("🎉 Database setup complete! Your SuitSenseAI is ready to go!")
    else:
        print("💥 Database setup failed. Check your connection settings.")
