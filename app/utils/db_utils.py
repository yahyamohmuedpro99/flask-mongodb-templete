# functions and connection for the database
from pymongo import MongoClient
import os
from dotenv import load_dotenv , find_dotenv

# connection and database 
load_dotenv(find_dotenv())
password=os.getenv("MDB_PSWD")
MONGODB_URI = f"mongodb+srv://yahya:{password}@learncluster.mk6ma6e.mongodb.net/?retryWrites=true&w=majority&appName=LearnCluster"
DB_NAME = "Learn"

def get_db_instance():
    return MongoClient(MONGODB_URI)


def get_db_by_name(name):
    client_instance = get_db_instance()
    return client_instance[name]
