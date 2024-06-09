
class User:
    def __init__(self,username,password=None,hashed_password=None,last_login=None):
        self.username = username
        self.password = password
        self.hashed_password = hashed_password
        self.last_login = last_login


class Task:
    def __init__(self,user_id,body=None,status=None,created_at=None,updated_at=None):
        self.user_id = user_id
        self.body = body
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
    