from supabase import create_client
import os
from dotenv import load_dotenv
import random

load_dotenv()

supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

def create_initial_data():
    # 1. First create topics
    print("Creating topics...")
    topics = [
        {
            'topic_name': 'Binary Trees',
            'description': 'Fundamentals of binary trees and their operations'
        },
        {
            'topic_name': 'Graph Algorithms',
            'description': 'Basic graph traversal and shortest path algorithms'
        },
        {
            'topic_name': 'Dynamic Programming',
            'description': 'Introduction to dynamic programming concepts'
        }
    ]
    
    for topic in topics:
        supabase.table('topics').insert(topic).execute()

    # 2. Create 16 students
    print("Creating students...")
    students = []
    for i in range(16):
        student_data = {
            'name': f'Student {i+1}',
            'email': f'student{i+1}@example.com'
        }
        result = supabase.table('students').insert(student_data).execute()
        students.append(result.data[0])

    # 3. Create assessment results with varied scores
    print("Creating assessment results...")
    topics = supabase.table('topics').select('*').execute()
    
    for student in students:
        for topic in topics.data:
            assessment_data = {
                'student_id': student['id'],
                'topic_id': topic['id'],
                'comprehension_score': random.randint(30, 90),
                'implementation_score': random.randint(20, 85),
                'integration_score': random.randint(15, 80),
                'weak_areas': [
                    f'Concept {random.randint(1,3)}',
                    f'Application {random.randint(1,3)}'
                ]
            }
            supabase.table('assessment_results').insert(assessment_data).execute()

    print("Initial data creation completed!")

if __name__ == "__main__":
    create_initial_data()