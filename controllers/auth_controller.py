from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    from models.user import User  # Importação interna para evitar circularidade
    from models.doctor import Doctor
    from models.patient import Patient
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            # Verifica se o usuário é médico ou paciente
            if user.doctor:
                return redirect(url_for('doctors.dashboard'))  # Redireciona para a dashboard do médico
            elif user.patient:
                return redirect(url_for('patients.dashboard'))  # Redireciona para a dashboard do paciente
        else:
            flash('Login Failed. Check your username and password.', 'danger')

    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
