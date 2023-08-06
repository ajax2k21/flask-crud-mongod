from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)


app.config['MONGO_URI'] = 'mongodb://mongo:27017/user_database'  # 'mongo' is the Docker container name
mongo_client = MongoClient(app.config['MONGO_URI'])
db = mongo_client["user_database"]
users_collection = db["users"]


@app.route('/users', methods=['GET'])
def get_all_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])  
    return jsonify(users), 200

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({'_id': ObjectId(user_id)})
    if user:
        user['_id'] = str(user['_id'])  
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    result = users_collection.insert_one(data)
    user_id = str(result.inserted_id)
    return jsonify({"message": "User created", "_id": user_id}), 201

@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    result = users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
    if result.modified_count == 1:
        return jsonify({"message": "User updated"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)




'''from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
from models.user import User

app = Flask(__name__)
api = Api(app)

# MongoDB Configuration
mongo_client = MongoClient(r"mongodb://127.0.0.1:27017/")
db = mongo_client["user_database"]

# Use model
api.add_resource(User, "/users", endpoint="users", resource_class_kwargs={'db': db})
api.add_resource(User, "/users/<string:user_id>", endpoint="user", resource_class_kwargs={'db': db})

if __name__ == "__main__":
    app.run(debug=True)
'''