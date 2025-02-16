from app.scripts.prepare_data1 import prepare_learning_analytics, insert_learning_analytics
from app.database.setup1 import setup_database

def initialize():
    print("Combining and preparing data...")
    df = prepare_learning_analytics()
    
    print("Setting up database...")
    conn, cursor = setup_database()
    
    print("Inserting data...")
    insert_learning_analytics(cursor, df)
    
    print("Done!")

if __name__ == "__main__":
    initialize()