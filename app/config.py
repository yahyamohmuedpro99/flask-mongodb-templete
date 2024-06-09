from flask_jwt_extended import JWTManager
from app import app
from dotenv import load_dotenv , find_dotenv
import os
load_dotenv(find_dotenv())

app.config['SECRET_KEY'] = os.getenv('SECREATE_KEY')
# Set token expiration times
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 15*60  # 15 min
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 7 * 24 * 60 * 60  # 7 days

jwt=JWTManager(app)
#set the secret key
# init extensions (e.g., Flask-Login if needed)
# login_manager = LoginManager()
# login_manager.init_app(app)
#set the secret key


# connection to database 
password=os.getenv("MDB_PSWD")
MONGODB_URI = f"mongodb+srv://yahya:{password}@learncluster.mk6ma6e.mongodb.net/?retryWrites=true&w=majority&appName=LearnCluster"
DB_NAME = "tasker"
