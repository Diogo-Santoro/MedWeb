from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from models.appointment import Appointment
from models.doctor import Doctor
from models.patient import Patient
from app import db

bp = Blueprint('appointment', __name__)

@bp.route('/appointments', methods=['GET', 'POST'])
@login_required
def appointments():
    # Lógica para agendar e listar consultas
    if request.method == 'POST':
        # Processar o agendamento da consulta
        # ...
        flash('Appointment scheduled successfully!', 'success')
        return redirect(url_for('appointment.appointments'))

    doctors = Doctor.query.all()  # Listar todos os médicos
    return render_template('appointments.html', doctors=doctors)  # Crie o template appointments.html
