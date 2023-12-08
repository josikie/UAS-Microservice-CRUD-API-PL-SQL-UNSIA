from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import (
    setup_db,
    User,
    load_dotenv,
    os
)

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
    app = Flask(__name__)
    with app.app_context():
        setup_db(app)
    
    # set up cors
    cors = CORS(app, resources={f"/microservice/*": {'origins': '*'}})

    # set response header
    @app.after_request
    def afterRequest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response
    
    # endpoint for base url
    @app.route('/microservice', methods=['GET'])
    def api_endpoint():
        return jsonify({
            'success': True,
            'message': 'Hello! Welcome to Microservice. To access another features, please log in.'
        })
    
    @app.route('/microservice/user/create_user', methods=['POST'])
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
    def delete_user(id):
        user = User.query.get(id)
        user.delete()
        return jsonify({
            'success': True,
            'status_code': 200
        })

    @app.route('/microservice/user', methods=['GET'])
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
    def get_user(id):
        
        user = User.query.get(id)
        email = user.email
        decryptedEmail = decrypt(email, SALT)
        return jsonify({
            'email': decryptedEmail,
            'succes': True,
            'status_code': 200
        })
       

    # @app.route('/microservice/login', methods=['POST'])
    # def login():
    #     body = request.get_json()
    #     email = body.get('email', None)
    #     password = body.get('password', None)

    #     if email == None:
    #         return jsonify({
    #             'message': 'Please Provide an Email',
    #             'status_code': 400,
    #             'success': False
    #         })
        
    #     if password == None:
    #         return jsonify({
    #             'message': 'Please Provide a Password',
    #             'status_code': 400,
    #             'success': False
    #         })
        

    #     user = verify_identity(User, email, password)
    #     return jsonify({
    #         'message': user.message,
    #         'status_code': user.status_code,
    #         'success': user.success
    #     })

    # Handle error
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'status_code': 400,
            'message': 'bad request'
        })
    
    return app