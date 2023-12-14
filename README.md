# Documentation
Microservice login is a microservice project with REST API for login and user access management built on Python and Flask. This project was created by Group 10 to complete the Midterm Exam project of Pemrograman PL SQL. 

This project leverages AES 256 to encrypt user data such as email and password. So, email and password will be encrypted first before being saved on the database. About the encryption and decryption function processes, please take a look at the microservice-login/encryption.py file. 
## Setting Up the Project in local
### Clone The Project
1. Clone the project with this command:
   ```
   git clone https://github.com/josikie/microservice-login.git
   ```
2. Open project on vscode. 
### Create environment variable:
1. Install virualenv with this command:
   ```
   pip install virtualenv
   ```
2. Open the terminal on vscode. If you use Windows, download [git bash](https://git-scm.com/downloads). Install it. Then open git bash on vscode. 
3. Create the virtual environment with this command:
   ```
   python -m virtualenv env
   ```
4. Run the project in your virtual environment with this command:
   ```
   source env/Scripts/activate
   ```
### Install all the requirements dependencies.
To install all the dependencies type this command:
```
pip install -r requirements.txt
```
### Setup Your Database:
1. Create .env file, and set variables for the database host, your database user, and your database password on .env file.
   For example:
   ```
   DB_HOST="localhost:5432"
   DB_USER="yourdb"
   DB_PASSWORD="yourpassword"
   KEY="secretkey"
   ```
2. Create a new terminal on vscode.
3. Run Postgres with the default database in Postgres. It would ask for your user password for user Postgres.
   Below is the command:
   ```
   psql postgres postgres
   ```
4. The command for creating a database is already defined in the setup.sql file, so we just need to type this command to create the needed database:
   ```
   \i setup.sql
   ```
5. To make sure that the database is already created. Let's switch to the microservice database by this command:
   ```
   \c microservice
   ```
### It's time to run our REST API. 
On the previous git bash terminal we opened, type this command one by one:
   ```
   export FLASK_APP=flaskr
   ```
   ```
   export FLASK_DEBUG=TRUE
   ```
   ```
   flask run
   ```
## REST API Endpoints
Endpoints users can access without login:
```
1. GET /microservices
2. POST /microservices/login
```
Endpoints users with Member role can access (with login):
```
1. GET /microservices
2. POST /microservices/login
3. GET /microservices/user
4. GET /microservices/user/<int:id>
5. GET /microservices/logout
```
Endpoints users with Admin role can access (with login):
```
1. GET /microservices
2. POST /microservices/login
3. GET /microservices/user
4. GET /microservices/user/<int:id>
5. GET /microservices/logout
6. POST /microservices/user/create_user
7. PATCH /microservices/user/<int:id>
8. DELETE /microservices/user/<int:id>
```
## REST API Resources
GET `http://127.0.0.1:5000/microservice`
- used to get the welcome message.
- return a JSON object containing a welcome message and success.
  
return example:

```
{
  "message": "Hello! Welcome to Microservice. To access another features, please log in.",
  "success": true
}
```

POST `http://127.0.0.1:5000/microservice/login`
- used for user login.
- return JSON object containing message, success, and status code.
- need email and password provided.

return example:

```
{
    "message": "Password and email correct. Succesfully Log in.",
    "status_code": 200,
    "success": true
}
```

GET `http://127.0.0.1:5000/microservice/user`
- used to fetch all user emails.
- return JSON object containing status code, success, and all user emails.
- need authorization to access (Admin or Member role).
  
return example:

```
{
    "status_code": 200,
    "success": true,
    "users": [
        {
            "email": "admin@gmail.com"
        },
        {
            "email": "member@gmail.com"
        },
        {
            "email": "admin5@gmail.com"
        }
    ]
}
```

GET `http://127.0.0.1:5000/microservice/user/<int:id>`
- used to fetch a specific user's email.
- return JSON object containing status code, success, and email from a specific user.
- need authorization to access (Admin or Member role)
- need to define the user id.
  
return example:

```
{
    "email": "admin@gmail.com",
    "isActive": false,
    "role_id": 1,
    "role_name": "Admin",
    "status_code": 200,
    "success": true
}
```

GET `http://127.0.0.1:5000/microservice/logout`
- used for user logout.
- return JSON object containing message, status code, and success.
- need authorization (Admin or role member).
  
return example:

```
{
    "message": "Successfully Log out",
    "status_code": 200,
    "success": true
}
```

POST `http://127.0.0.1:5000/microservice/user/create_user`
- used to create new user.
- return JSON object containing status code and success.
- need authorization (Admin role).
- need JSON object on the body to send user's data that wants to be created: email, password, and role.
  
return example:

```
{
    "status_code": 200,
    "success": true
}
```

PATCH `http://127.0.0.1:5000/microservice/user/7`
- used to update user's data.
- return JSON object containing status code, success, and the new role.
- need authorization (Admin role)
- need a user id on the link.
- need JSON object on the body to send user's data that wants to be updated.
  
return example:

```
{
    "new_role": "Admin",
    "status_code": 200,
    "success": true
}
```
DELETE `http://127.0.0.1:5000/microservice/user/7`
- used to delete a specific user.
- return JSON object containing status code and success.
- need authorization (Admin role).
- need a user id on the link.
  
return example:

```
{
    "status_code": 200,
    "success": true
}
```

### Error Handling
There are two error handlers for four errors. The errors returned JSON objects in the following format:
```
'success': False,
'status_code': 401,
'message': 'unauthorized access'
```
These are three error types when requests fail:
- 400: Bad Request
- 401: Unauthorized Access.

## Testing
You can test our REST API with [Postman](https://www.postman.com/). You can download Postman and install it on your local computer before testing the REST API

