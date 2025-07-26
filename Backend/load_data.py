import psycopg2
import csv
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

DB_NAME = os.getenv("DB_NAME", "e_commerce_db")
DB_USER = os.getenv("DB_USER", "your_username")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'products.csv')

def load_products():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER,
            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()
        with open(CSV_FILE_PATH, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute(
                    "INSERT INTO products (id, name, description, price, category) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;",
                    (row['id'], row['name'], row['description'], row['price'], row['category'])
                )
        conn.commit()
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    load_products()
