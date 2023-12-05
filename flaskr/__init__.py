from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from models import (
    setup_db,
    User
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

        if email == None and password == None:
            abort(400)
        
        try:
            user = User(email, password)
            user.insert()
            return jsonify({
                'email': email,
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

        if request.method == 'PATCH':
            if email != None:
                user.email = email
            if password != None:
                user.password = password
        
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
        email = user.email
        user.delete()
        return jsonify({
            'deleted_user': email,
            'success': True,
            'status_code': 200
        })

    @app.route('/microservice/user', methods=['GET'])
    def get_all_user():
        
        users = User.query.all()
        all_users = []
        for user in users:
            all_users.append({
                "email" : user.email
            })
        return jsonify({
            'users': all_users,
            'success': True,
            'status_code': 200
        })

    @app.route('/microservice/user/<int:id>', methods=['GET'])
    def get_user(id):
        try:
            user = User.query.get(id)
            return jsonify({
                'email': user.email,
                'succes': True,
                'status_code': 200
            })
        except:
            abort(400)


    # Handle error
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'status_code': 400,
            'message': 'bad request'
        })
    
    return app