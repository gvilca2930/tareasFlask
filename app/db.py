import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

def get_connection():
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        raise Exception("DATABASE_URL no esta configurada")

    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    return psycopg2.connect(
        database_url,
        cursor_factory = RealDictCursor
    )

