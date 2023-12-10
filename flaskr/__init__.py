from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import (
    setup_db,
    User,
    load_dotenv,
    os
)

from flask_login import login_manager, login_required, login_user, logout_user, current_user, LoginManager

from encryption import(
    decrypt,
    encrypt,
    BLOCK_SIZE,
    pad,
    unpad,
    SALT
)

def create_app(test_config=None):
    # create and configure app
    login_manager = LoginManager()
    app = Flask(__name__)
    app.secret_key = SALT
    with app.app_context():
        setup_db(app)
        login_manager.init_app(app)
    
    # set up cors
    cors = CORS(app, resources={f"/microservice/*": {'origins': '*'}})

    # set response header
    @app.after_request
    def afterRequest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response
    
    @app.login_manager.user_loader
    def user_loader(user_id):
        """Given *user_id*, return the associated User object.

        :param unicode user_id: user_id (email) user to retrieve

        """
        return User.query.get(user_id)

    # endpoint for base url
    @app.route('/microservice', methods=['GET'])
    def api_endpoint():
        return jsonify({
            'success': True,
            'message': 'Hello! Welcome to Microservice. To access another features, please log in.'
        })
    
    @app.route('/microservice/user/create_user', methods=['POST'])
    @login_required
    def create_user():
        body = request.get_json()
        email = body.get('email', None)
        password = body.get('password', None)

        if email == None or password == None:
            abort(400)
        
        encryptedEmail = encrypt(email, SALT)
        encryptedPassword = encrypt(password, SALT)

        try:
            user = User(encryptedEmail, encryptedPassword)
            user.insert()
            return jsonify({
                'success': True,
                'status_code': 200
            })
        except:
            abort(400)

    @app.route('/microservice/user/<int:id>', methods=['PATCH'])
    @login_required
    def patch_user(id):
        user = User.query.get(id)
        body = request.get_json()
        email = body.get('email', None)
        password = body.get('password', None)
        
        encryptedEmail = encrypt(email, SALT)
        encryptedPassword = encrypt(password, SALT)


        if email != None:
            user.email = encryptedEmail
        if password != None:
            user.password = encryptedPassword
        
        try:
            user.update()
            return jsonify({
                'success': True,
                'status_code': 200
            })
        except:
            abort(400)
        
    
    @app.route('/microservice/user/<int:id>', methods=['DELETE'])
    @login_required
    def delete_user(id):
        user = User.query.get(id)
        user.delete()
        return jsonify({
            'success': True,
            'status_code': 200
        })

    @app.route('/microservice/user', methods=['GET'])
    @login_required
    def get_all_user():
        
        users = User.query.all()
        all_users = []
        for user in users:
            all_users.append({
                "email" : decrypt(user.email, SALT)
            })
        return jsonify({
            'users': all_users,
            'success': True,
            'status_code': 200
        })

    @app.route('/microservice/user/<int:id>', methods=['GET'])
    @login_required
    def get_user(id):
        
        user = User.query.get(id)
        email = user.email
        decryptedEmail = decrypt(email, SALT)
        return jsonify({
            'email': decryptedEmail,
            "isActive": user.active,
            'succes': True,
            'status_code': 200
        })
       

    @app.route('/microservice/login', methods=['POST'])
    def login():
        body = request.get_json()
        email = body.get('email', None)
        password = body.get('password', None)

        if email == None:
            return jsonify({
                'message': 'Please Provide an Email',
                'status_code': 400,
                'success': False
            })
        
        if password == None:
            return jsonify({
                'message': 'Please Provide a Password',
                'status_code': 400,
                'success': False
            })
        
        checkedEmail = False
        checkedPassword = False
        isLogin = False

        users = User.query.all()
        demail = None
        eemail = None
        dpass = None
        for i in range(len(users)):
            if decrypt(users[i].email, SALT) == email:
                demail = decrypt(users[i].email, SALT)
                eemail = users[i].email
                dpass = decrypt(users[i].password, SALT)

        if email == demail:
            checkedEmail = True
                
        if password == dpass:
            checkedPassword = True

        if checkedEmail and checkedPassword:
            isLogin = True
            logedUser = User.query.filter_by(email=eemail).all()
            logedUser[0].active = True
            logedUser[0].update()
            login_user(logedUser[0], remember=True)

        if isLogin:
            return jsonify({
                'message': "Password and email correct. Succesfully Log in.",
                'status_code': 200,
                'success': True
            })
        else:
            return jsonify({
                'message': "Wrong Credentials, can't log in.",
                'status': 400,
                'success': False 
            })
    
    @app.route('/microservice/logout', methods=['GET'])
    @login_required
    def logout():
        user = current_user
        user.active = False
        user.update()
        logout_user()
        
        return jsonify({
            "success": True,
            "message": "Succesfully Log out",
            "status_code": 200
        })

    # Handle error
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'status_code': 400,
            'message': 'bad request'
        })
    
    @app.errorhandler(401)
    def bad_request(error):
        return jsonify({
            'success': False,
            'status_code': 401,
            'message': 'unauthorized access'
        })
    return app