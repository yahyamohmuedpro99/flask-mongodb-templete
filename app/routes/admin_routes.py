
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from controllers import data_controllers
from utils import db_utils
admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/all_users/')
@jwt_required()
def get_documents():
    return jsonify({"all_users":data_controllers.find_all_docs('users')})

