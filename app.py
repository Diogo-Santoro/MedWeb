from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Inicializa as extensões
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Cria a aplicação Flask
    app = Flask(__name__)
    
    # Configuração da aplicação
    app.config.from_object(Config)
    
    # Inicializa as extensões
    db.init_app(app)
    login_manager.init_app(app)

    # Registra os blueprints
    from controllers.auth_controller import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from controllers.appointments_controller import bp as appointments_bp
    app.register_blueprint(appointments_bp, url_prefix='/appointments')

    from controllers.doctors_controller import bp as doctors_bp
    app.register_blueprint(doctors_bp, url_prefix='/doctors')

    from controllers.patients_controller import bp as patients_bp
    app.register_blueprint(patients_bp, url_prefix='/patients')

    # Cria o banco de dados se não existir
    with app.app_context():
        db.create_all()

    return app

# Executa a aplicação
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
