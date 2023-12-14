# Documentation
Microservice login is a microservice project with REST API for login and user access management built on Python and Flask. This project was created by Group 10 to complete the Midterm Exam project of Pemrograman PL SQL.
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
### REST API Endpoints
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

### Testing
You can test our REST API with [Postman](https://www.postman.com/). You can download Postman and install it on your local computer before testing the REST API

