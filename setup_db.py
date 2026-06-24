import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

dsn = os.getenv("NEON_CONNECTION_STRING")

if not dsn:
    raise ValueError("Missing NEON_CONNECTION_STRING. Check your .env file.")

try:
    print("Connecting to Neon endpoint...")
    conn = psycopg2.connect(dsn)
 
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    db_name = "iocr_pipeline_db"
    
    print(f"Executing: CREATE DATABASE {db_name};")
    cursor.execute(f"CREATE DATABASE {db_name};")
    
    print(f"Database '{db_name}' created successfully.")

except psycopg2.errors.DuplicateDatabase:
    print(f"Error: Database '{db_name}' already exists.")
except Exception as e:
    print(f"Execution failed: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
