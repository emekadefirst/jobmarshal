import os
import asyncio
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection URI
uri = os.getenv("url")

# Establish the connection
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the database and collection
db = client.get_database('your_database_name')  # Specify your database name here
collection = db.applicants

# Save function
async def save(fullname, role, cv_url, interview_code):
    applicant_data = {
        "fullname": fullname,
        "role": role,
        "resume_url": cv_url,
        "interview_code": interview_code
    }
    try:
        # Insert data into the 'applicants' collection
        result = collection.insert_one(applicant_data)
        return f"Document inserted with ID: {result.inserted_id}"
    except Exception as e:
        return f"Error saving applicant data: {str(e)}"

