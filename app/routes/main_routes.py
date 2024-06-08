
from flask import Blueprint
from controllers import data_controllers
bp = Blueprint('bp', __name__)

@bp.route('/documents')
def get_documents():
    return data_controllers.get_all_docs_from_collection('student_collections')
