# Documentation
Microservice login is a microservice project with REST API for login, CRUD on users table, and user access management (Role: Admin, Member) built on Python and Flask. This project was created by Group 10 to complete the Final Semester Exam project of Pemrograman PL SQL. 

This project leverages AES 256 to encrypt user data such as email and password. So, email and password will be encrypted first before being saved on the database. About the encryption and decryption function processes, please take a look at the [microservice-login/encryption.py](https://github.com/josikie/UTS-Microservice-CRUD-API-PL-SQL-UNSIA/blob/main/encryption.py) file.

Group 10:
- Josi Kie Nababan ( 220401010122 )
- Ismal Zikri ( 220401010009 )
- Jefrianto (220401010114)

# Methodology Software Development Life Cycle (SDLC): Agile Approach 

We do the Agile Approach because we thought is the best for us because everyone can do some flexible things, and do various things, like who the first initiation, the last updated feature, and so on. 

we try to separate and implement practices using SCRUM, let us explain this stuff: 

Agile Principles
Discuss the key principles of Agile as outlined in the Agile Manifesto. These principles include:

- Individuals and interactions over processes and tools.
- Working solutions over comprehensive documentation.
- Customer collaboration over contract negotiation.
- Responding to change by following a plan.

Agile Practices
Explain the Agile practices that your team follows. Common Agile practices include:

- Scrum: An iterative and incremental framework for managing complex knowledge work.
- Kanban: A visual management method to balance demand with available capacity.
- User Stories: Short, simple descriptions of a feature told from the perspective of the person who desires the new capability.
- Daily Standups: Brief daily meetings to discuss progress, plans, and impediments.

Postman Export: [Microservice.postman_collection.json](https://github.com/josikie/UTS-Microservice-CRUD-API-PL-SQL-UNSIA/blob/main/Microservice.postman_collection.json)

## Setting Up the Project in local
### Clone The Project
1. Clone the project with this command:
   ```
   git clone https://github.com/josikie/UTS-Microservice-CRUD-API-PL-SQL-UNSIA.git
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
- need JSON object on the body containing the user's email and password.

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
- need to define the user id on the link.
  
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
- used to create a new user.
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
There are two error handlers for errors. The errors returned JSON objects in the following format:
```
'success': False,
'status_code': 401,
'message': 'unauthorized access'
```
These are two error types when requests fail:
- 400: Bad Request
- 401: Unauthorized Access.

### Trigger Log
Trigger Log is configured in the database, not in the application, with this query
1. Create audit_log table
```
CREATE TABLE audit_log(
   log_id serial PRIMARY KEY,
   users_id VARCHAR(255),
   changed_field VARCHAR(255),
   old_value VARCHAR(255),
   new_value VARCHAR(255),
   log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
```
2. Create log_user_changes function
```
CREATE OR REPLACE FUNCTION log_users_changes()
RETURNS TRIGGER AS $$
BEGIN
   IF NEW.email IS DISTINCT FROM OLD.email THEN
   INSERT INTO audit_log(users_id, changed_field, old_value, new_value)
   VALUES (current_user::text, 'email', OLD.email, NEW.email);
END IF;

   IF NEW.password IS DISTINCT FROM OLD.password THEN
   INSERT INTO audit_log(users_id, changed_field, old_value, new_value)
   VALUES(current_user::text, 'password', OLD.password, NEW.password);
END IF;

RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```
3. Create trigger users_changes_trigger and execute log_users_changes function
```
CREATE TRIGGER users_changes_trigger
AFTER UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION log_users_changes();
```
## Testing
1. REST API
You can test our REST API with [Postman](https://www.postman.com/). You can download Postman and install it on your local computer before testing the REST API

2. TRIGGER LOG
there is email and password that saved on database
![image](https://github.com/josikie/UAS-Microservice-CRUD-API-PL-SQL-UNSIA/assets/63739078/565b4c31-8ab8-4009-b91d-8cc8cbf4e5fc)

when the user changes data, the changes will be saved in the audit_log table with encypted aes256 format
![image](https://github.com/josikie/UAS-Microservice-CRUD-API-PL-SQL-UNSIA/assets/63739078/2912bc33-57bc-4f21-9623-e56ccdd0f432)
