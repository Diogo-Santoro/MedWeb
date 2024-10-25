from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Armazenar a senha hasheada
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))  # Relacionar com o paciente, se necessário
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))  # Relacionar com o médico, se necessário

    patient = db.relationship('Patient', backref='user', uselist=False)  # Se um usuário está vinculado a um paciente
    doctor = db.relationship('Doctor', backref='user', uselist=False)  # Se um usuário está vinculado a um médico

    def __repr__(self):
        return f'<User {self.email}>'
