# Microservice-login
Midterm exam project for Pemrograman PL SQL. Group 10. 
## Setting Up the Project in local
### Clone The Project
1. Clone the project with this command:
   ```
   git clone https://github.com/josikie/microservice-login.git
   ```
3. Open project on vscode. 
### Create environment variable:
1. Install virualenv with this command:
   ```
   pip install virtualenv
   ```
3. Open the terminal on vscode. If you use Windows, download [git bash](https://git-scm.com/downloads). Install it. Then open git bash on vscode. 
4. Create the virtual environment with this command:
   ```
   python -m virtualenv env
   ```
6. Run the project in your virtual environment with this command:
   ```
   source env/Scripts/activate
   ```
### Install all the requirements dependencies.
To install all the dependencies type this command:
`pip install -r requirements.txt`
### Setup Your Database:
1. Create .env file, and set variables for the database host, your database user, and your database password on .env file.
   For example:
   ```
    DB_HOST="localhost:5432"
    DB_USER="yourdb"
    DB_PASSWORD="yourpassword"
   ```
2. Create a new terminal on vscode.
3. Run Postgres with the default database in Postgres. It would ask for your user password for user Postgres.
   Below is the command:
   ```
   psql postgres postgres
   ```
5. The command for creating a database is already defined in the setup.sql file, so we just need to type this command to create the needed database:
   ```
   \i setup.sql
   ```
7. To make sure that the database is already created. Let's switch to the microservice database by this command:
   ```
   \c microservice
   ```
9. It's time to run our rest api. On the previous git bash terminal we opened, type this command one by one:
   ```
   export FLASK_APP=flaskr
   ```
   ```
   export FLASK_DEBUG=TRUE
   ```
   ```
   flask run
   ```
11. You can test our REST API with [Postman](https://www.postman.com/).
