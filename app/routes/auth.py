from flask import Blueprint, jsonify,request
from marshmallow import  ValidationError
from controllers.data_controllers import is_exist_in, save_user
from models.schemas import UserSchema
from datetime import datetime as dt
from flask_jwt_extended import create_access_token,create_refresh_token, get_jwt_identity, jwt_required
from utils.db_utils import bycrypt, get_collection

auth = Blueprint('auth', __name__)

@auth.route('/signup/', methods=['POST'])
def signup():
    user = UserSchema().load(request.get_json())
    try:
        # Use deserialized data from UserSchema.load
        user = UserSchema().load(request.get_json())
        user['created_at'] = dt.now()
        user['last_login'] = dt.now()

        # Save user in database
        try:
            inserted_user = save_user(user)
            print('another try')
            if not inserted_user: 
                return jsonify({"error": "Failed to save user"}), 400
            
            #generate access and refresh tokens
            access_token=create_access_token(identity=user['username'])
            refersh_token=create_refresh_token(identity=user['username'])
            print("after creating access token")
            return jsonify({"accesse_token":access_token,"refersh_token":refersh_token}), 201
        except Exception as e:  # Catch database insertion errors
            print(f"Error saving user: {e}")
            return jsonify({"error": "Internal server error"}), 500

    except ValidationError as err:
        return jsonify({"error": "Invalid username or password"}), 400

@auth.route('/signin/', methods=['POST'])
def signin():
    try:
        user=UserSchema().load(request.get_json())

        #check if user exists or not 
        if is_exist_in(user['username'],'users') :
            #if user exist 
            u=get_collection('users').find_one({'username':user['username']})
            if bycrypt.check_password_hash(u['password'],user['password']):
                #generate access and refresh tokens
                access_token=create_access_token(identity=user['username'])
                refersh_token=create_refresh_token(identity=user['username'])
                return jsonify({"accesse_token":access_token,"refersh_token":refersh_token}), 201
        
        return jsonify({"error":"check password or username"}),400
    
    except ValidationError as err:
        print(f"Error on retriveing user : {err}")
        return jsonify({"error": "Internal server error"}), 500

# create endpoint to generate access token from refresh token
@auth.route('/refresh/', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token), 200
