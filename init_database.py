
from app.scripts.prepare_data import combine_and_prepare_data, insert_data
from app.database.setup import setup_database

def initialize():
    print("Combining and preparing data...")
    df = combine_and_prepare_data()
    
    print("Setting up database...")
    conn, cursor = setup_database()
    
    print("Inserting data...")
    insert_data(cursor, df)
    
    print("Done!")

if __name__ == "__main__":
    initialize()