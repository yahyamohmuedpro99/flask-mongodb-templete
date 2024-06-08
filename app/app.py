from flask import Flask
import pymongo
# from flask_login import LoginManager

app = Flask(__name__)

# init extensions (e.g., Flask-Login if needed)
# login_manager = LoginManager()
# login_manager.init_app(app)

# Register blueprints from routes and controllers
from routes import main_routes
app.register_blueprint(main_routes.bp)

if __name__ == "__main__":
    app.run()

