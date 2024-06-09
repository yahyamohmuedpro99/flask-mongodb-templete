#control the logic of handling data 

import datetime
from flask import jsonify
from pymongo import ReturnDocument
from utils.db_utils import get_collection, hash_password
import bson 
from models.schemas import TasksSchema, UserSchema

def is_exist_in(name,collection):
    collection=get_collection(collection)
    # return Name or None if not exist
    if collection.find_one({"username":name}):
        return True
    return False

def find_all_docs(collection:str):
    collection=get_collection(collection)
    docs=list(collection.find())
    schema = UserSchema(many=True)
    
    return schema.dump(docs)


def save_user(user:UserSchema):
    # check if username is exist before create new one 
    if is_exist_in(user['username'],"users"):
        return jsonify({"error":"username already exists"}),400
    #hash passwords 
    user['password'] = hash_password(user['password'])
    user_collection = get_collection('users')
    return user_collection.insert_one(user)


def save_task(task:TasksSchema,username):
    user_id=get_id_from_username(username)
    task_collection = get_collection('tasks')
    task['user_id'] = user_id
    task_collection.insert_one(task)

def get_id_from_username(username):
    user_collection = get_collection('users')
    user = user_collection.find_one({'username': username})
    if not user:
        raise ValueError(f"User with username {username} not found")
    return str(user['_id'])

def check_owend(task_id,user_id):
    task_collection=get_collection('tasks')
    task=task_collection.find_one({'task_id':task_id})
    return str(task['user_id'])==user_id

def update_user_task(task_id,updated_data):
    try:
        task_collection=get_collection('tasks')

        #update task
        updated_task=task_collection.find_one_and_update(
            {"task_id":task_id}, #find by task_id
            {'$set':updated_data}, # only update the data provided
            return_document=ReturnDocument.AFTER
            )
        return updated_task
    except ValueError as e:
        return jsonify({"error":e.message})
    except Exception as e:
        return jsonify({"error":e.message})