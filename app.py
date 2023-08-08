from flask import Flask
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

# MongoDB config
client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
users_collection = db['users']

# Request parser
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help='Name is required.')
user_parser.add_argument('email', type=str, required=True, help='Email is required.')
user_parser.add_argument('password', type=str, required=True, help='Password is required.')


class User(Resource):
    def get(self, user_id=None):
        if user_id:
            user = users_collection.find_one({'_id': ObjectId(user_id)})
            if user:
                user['_id'] = str(user['_id'])
                return user, 200
            else:
                return {'message': 'User not found'}, 404
        else:
            users = list(users_collection.find())
            for user in users:
                user['_id'] = str(user['_id'])
            return users, 200

    def post(self):
        args = user_parser.parse_args()
        user_id = users_collection.insert_one(args).inserted_id
        return {'message': 'User created', '_id': str(user_id)}, 201

    def put(self, user_id):
        args = user_parser.parse_args()
        if not users_collection.find_one({'_id': ObjectId(user_id)}):
            return {'message': 'User not found'}, 404
        users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': args})
        return {'message': 'User updated'}, 200

    def delete(self, user_id):
        if not users_collection.find_one({'_id': ObjectId(user_id)}):
            return {'message': 'User not found'}, 404
        users_collection.delete_one({'_id': ObjectId(user_id)})
        return {'message': 'User deleted'}, 200


api.add_resource(User, '/users', '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
