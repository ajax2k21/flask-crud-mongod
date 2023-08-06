from pymongo import MongoClient

# MongoDB Configuration
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["user_database"]
users_collection = db["users"]

# Sample data
sample_users = [
    { "name": "Prashant", "email": "asdf@gmail.com", "password": "123123" },
    { "name": "Sonu", "email": "13123@gmail.com", "password": "sdfgsdfg" },
    { "name": "Akash", "email": "fghfgfh@gmail.com", "password": "dfghdfgh" }
]

# Insert sample data into the users collection
result = users_collection.insert_many(sample_users)
print("Sample data inserted successfully.")
