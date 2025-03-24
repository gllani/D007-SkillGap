
import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname="skill_gap_db", user="admin", password="password", host="localhost"
    )
    return conn