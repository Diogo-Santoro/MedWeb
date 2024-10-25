from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from controllers.auth_controller import bp as auth_bp
from controllers.appointments_controller import bp as appointments_bp
from controllers.doctors_controller import bp as doctors_bp
from controllers.patients_controller import bp as patients_bp

# Inicializando o banco de dados
db = SQLAlchemy()

# Inicializando o Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'  # Altere para uma chave segura
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Inicializando o LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # O nome da função de login no seu controlador de autenticação

# Definindo a função user_loader
@login_manager.user_loader
def load_user(user_id):
    from models.user import User  # Importando o modelo User aqui
    return User.query.get(int(user_id))

# Registrando os blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(appointments_bp, url_prefix='/appointments')
app.register_blueprint(doctors_bp, url_prefix='/doctors')
app.register_blueprint(patients_bp, url_prefix='/patients')

# Resto da configuração do seu aplicativo...

if __name__ == '__main__':
    app.run(debug=True)
