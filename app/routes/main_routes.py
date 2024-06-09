
from flask import Blueprint, json, jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity
from marshmallow import ValidationError
from controllers.data_controllers import save_task,check_owend,get_id_from_username,update_user_task
from models.schemas import TasksSchema
api_bp = Blueprint('bp', __name__)

@api_bp.route('/add_task/', methods=['POST'])
@jwt_required()
def add_task():
    try:
        username = get_jwt_identity()
        task = TasksSchema().load(request.get_json())
        save_task(task,username)
        return jsonify({"msg":"task added"})
    except ValidationError as e:
        return jsonify({"error":e.messages}),400
    except Exception as e:
        return jsonify({"error":"internal server error"})

@api_bp.route('/update_task/<task_id>/', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    task_id=request.args.get('task_id')
    user_id=get_id_from_username(get_jwt_identity())
    
    updated_data=TasksSchema().load(request.get_json())

    #check that the user has permission to update this task 
    # check that the user own this task 
    if check_owend(task_id,user_id):
        updated_task=update_user_task(task_id,updated_data)
        return json.dumps(updated_task,default=str)
    return jsonify({"error":"you not allowed to update this task is not yours bro :("})
        



