from flask import Blueprint, render_template, redirect, url_for, flash
from models.doctor import Doctor
from app import db

bp = Blueprint('doctor', __name__)

@bp.route('/doctors', methods=['GET', 'POST'])
def doctors():
    if request.method == 'POST':
        # Processar a adição de um novo médico
        # ...
        flash('Doctor added successfully!', 'success')
        return redirect(url_for('doctor.doctors'))

    all_doctors = Doctor.query.all()  # Listar todos os médicos
    return render_template('doctors.html', doctors=all_doctors)  # Crie o template doctors.html
