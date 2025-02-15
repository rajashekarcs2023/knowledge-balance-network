from supabase import create_client
import os
import random
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

def create_initial_data():
    # 1. Create 4 hubs
    print("Creating hubs...")
    for i in range(4):
        hub_data = {
            'hub_name': f'Hub {i+1}'
        }
        supabase.table('hubs').insert(hub_data).execute()
    
    # 2. Create 4 nodes per hub
    print("Creating nodes...")
    hubs = supabase.table('hubs').select('*').execute()
    for hub in hubs.data:
        for i in range(4):
            node_data = {
                'student_name': f'Student {i+1} of Hub {hub["hub_name"]}',
                'hub_id': hub['id']
            }
            supabase.table('nodes').insert(node_data).execute()

    # 3. Create a sample topic
    print("Creating topic...")
    topic_data = {
        'topic_name': 'Binary Trees',
        'description': 'Introduction to binary trees and their operations'
    }
    topic = supabase.table('topics').insert(topic_data).execute()

    # 4. Generate random scores
    print("Generating scores...")
    nodes = supabase.table('nodes').select('*').execute()
    topic_id = topic.data[0]['id']
    
    for node in nodes.data:
        score_data = {
            'node_id': node['id'],
            'topic_id': topic_id,
            'comprehension_score': random.randint(30, 90),
            'implementation_score': random.randint(20, 85),
            'integration_score': random.randint(15, 80)
        }
        supabase.table('knowledge_scores').insert(score_data).execute()
    
    print("Initial data creation completed!")

if __name__ == "__main__":
    create_initial_data()