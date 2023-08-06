# Flask CRUD with MongoDB - README

This project is a Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations on a User resource using a REST API with MongoDB as the database. The application provides REST API endpoints to manage user data, and it uses Docker to simplify the setup and deployment process.

## Prerequisites

Before running the project, make sure you have the following installed on your system:

- Docker
- Python (3.x)

## Getting Started

Follow the steps below to set up and run the Flask application with MongoDB using Docker.

1. **Clone the Repository:**

`git clone <repository-url>`
`cd flask-crud-mongodb`


2. **Build the Docker Image:**

`docker build -t flask-mongo-app`


3. **Run the MongoDB Container:**

`docker run -d --name mongo -p 27017:27017 mongo`


This will start the MongoDB server in a Docker container.

4. **Run the Flask Application:**

`docker run -p 5000:5000 --name flask-app flask-mongo-app`


The Flask application will now be running inside a Docker container.

## Accessing the API

You can access the API using tools like Postman or cURL.

- To get a list of all users: `GET http://localhost:5000/users`
- To get a specific user by ID: `GET http://localhost:5000/users/<user_id>`
- To create a new user: `POST http://localhost:5000/users`
JSON Payload:
```json
{
 "name": "Prashant Joshi",
 "email": "123213@gmail.com",
 "password": "1213adf"
}
```

To update a user by ID: PUT `http://localhost:5000/users/<user_id>`
```
{
  "name": "New name",
  "email": "new mail"
}
```

To delete a user by ID: DELETE `http://localhost:5000/users/<user_id>`

## Stopping the Containers
To stop the containers, use the following commands:

```
docker stop flask-app
docker stop mongo
```

# To Clean the Container

To remove the containers, use the following commands:
```
docker rm flask-app
docker rm mongo
```


