# functions and connection for the database
from pymongo import MongoClient
import os
from app import app
from flask_bcrypt import Bcrypt
from config import MONGODB_URI,DB_NAME
bycrypt = Bcrypt(app)

def get_client():
    return MongoClient(MONGODB_URI)

def get_db(name=DB_NAME):
    client_instance = get_client()
    return client_instance[name]

def get_collection(name:str,db=DB_NAME):
    db=get_db(db)
    return db[name]

def hash_password(password):
    return bycrypt.generate_password_hash(password)
    
