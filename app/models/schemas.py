from marshmallow import Schema , fields
from enum import Enum

# ---------------------------------------------------------
# ----------------------- Enums,struct --------------------------
# ---------------------------------------------------------
# class TaskStatus(Enum):
#     started = "started"
#     workingon = "workingon"
#     finished = "finished"
#     paused = "paused"




# ---------------------------------------------------------
# ----------------------- Schema --------------------------
# ---------------------------------------------------------

class UserSchema(Schema):
    id = fields.Method("get_objectid_str")
    username=fields.Str(required=True)
    password=fields.Str(required=True)
    last_login=fields.DateTime(required=False)
    created_at = fields.DateTime(required=False)

    def get_objectid_str(self, obj):
        return str(obj['_id'])

class TasksSchema(Schema):
    user_id=fields.Str(required=False)
    body=fields.Str(required=True)
    status=fields.Str(required=False, default="started")

