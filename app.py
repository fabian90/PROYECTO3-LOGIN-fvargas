from flask import Flask, request, render_template,redirect, url_for
from dotenv import load_dotenv
from db import db
from flask_restful import Api,Resource
from flask_login import LoginManager, login_required, login_user
from models.user import User
from Router.heladeriaRouter import heladeria_bp
import os

app = Flask(__name__)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

    secret_key = os.urandom(24)

# Configurar la base de datos u otras configuraciones
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = secret_key   
# Crear una instancia de SQLAlchemy como Singleton

api= Api(app)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' 
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user
    return None
app.register_blueprint(heladeria_bp)
with app.app_context():
        # from Controllers.controller import Controlador
        db.create_all()

        # Registrar blueprint del controlador
        # app.register_blueprint(Controlador)


# Ruta para mostrar la lista de perros
# Rutas
# @app.route('/')
# def index():
#     return "¡Bienvenido a la aplicación de Heladeria!"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    #     return render_template("login.html")
    # else:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:

            login_user(user)
            return redirect(url_for('heladeria.index'))
        return render_template('no_autorizado.html')       
    return render_template("login.html")

# api.add_resource(Controlador,'/consulta_nombre')
if __name__ == '__main__':
    app.run(debug=True)