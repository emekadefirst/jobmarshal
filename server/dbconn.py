import os
import asyncio
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from pymongo import MongoClient

uri = "mongodb+srv://jobmarshal:RfBMZZaOV5Avl2f0@cluster0.iat96.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)

db = client["Apllicant"]
print("✅ Connected to MongoDB successfully!")


collection = db.applicants


# Save function
async def save(firstname, lastname, role, cv_url, interview_code):
    applicant_data = {
        "firstname": firstname,
        "lastname": lastname,
        "role": role,
        "resume_url": cv_url,
        "interview_code": interview_code,
    }
    try:
        # Insert data into the 'applicants' collection
        result = collection.insert_one(applicant_data)
        return f"Document inserted with ID: {result.inserted_id}"
    except Exception as e:
        return f"Error saving applicant data: {str(e)}"


if __name__ == "__main__":
    print(asyncio.run(save("victor", "chib", "dev", "https://hg.com", "AFSASFDED")))
