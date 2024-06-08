#control the logic of handling data 

from flask import jsonify
from utils import db_utils
import bson 
def get_all_docs_from_collection(name):
    db = db_utils.get_db_by_name('classroom')
    collection = db[name]
    docs=list(collection.find())
    for doc in docs:
        doc['_id'] = str(doc['_id']) 
    print(f'------------- {docs}-------------')
    return jsonify(docs)
