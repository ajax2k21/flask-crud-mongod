from flask_restful import Resource, reqparse
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId

from pymongo import MongoClient

mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
db = mongo_client["user_database"]
users_collection = db["users"]  # MongoDB collection for users

# User model
class User(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name", type=str, required=True, help="Name field is required.")
        self.parser.add_argument("email", type=str, required=True, help="Email field is required.")
        self.parser.add_argument("password", type=str, required=True, help="Password field is required.")

    def get(self, user_id=None):
        if user_id:
            user = users_collection.find_one({"_id": ObjectId(user_id)})
            if user:
                user["_id"] = str(user["_id"])  # Convert ObjectId to string
                return user, 200
            else:
                return {"message": "User not found"}, 404
        else:
            users = list(users_collection.find())
            for user in users:
                user["_id"] = str(user["_id"])  # Convert ObjectId to string
            return users, 200

    def post(self):
        data = self.parser.parse_args()
        result = users_collection.insert_one(data)
        user_id = str(result.inserted_id)
        return {"message": "User created", "_id": user_id}, 201

    def put(self, user_id):
        data = self.parser.parse_args()
        user = users_collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": data},
            return_document=True
        )
        if user:
            user["_id"] = str(user["_id"])  # Convert ObjectId to string
            return user, 200
        else:
            return {"message": "User not found"}, 404

    def delete(self, user_id):
        result = users_collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 1:
            return {"message": "User deleted"}, 200
        else:
            return {"message": "User not found"}, 404
