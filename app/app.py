from flask import Flask
from flask_jwt_extended import JWTManager
# from flask_login import LoginManager
app = Flask(__name__)
# Register blueprints from routes and controllers
from routes import main_routes,auth,admin_routes
app.register_blueprint(main_routes.api_bp,prefix="/api")
app.register_blueprint(auth.auth, url_prefix='/auth')
app.register_blueprint(admin_routes.admin_bp, url_prefix='/admin')

if __name__ == "__main__":
    app.run(debug=True)

