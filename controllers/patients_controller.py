from flask import Blueprint, render_template, redirect, url_for, flash
from models.patient import Patient
from app import db

bp = Blueprint('patient', __name__)

@bp.route('/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        # Processar a adição de um novo paciente
        # ...
        flash('Patient added successfully!', 'success')
        return redirect(url_for('patient.patients'))

    all_patients = Patient.query.all()  # Listar todos os pacientes
    return render_template('patients.html', patients=all_patients)  # Crie o template patients.html
