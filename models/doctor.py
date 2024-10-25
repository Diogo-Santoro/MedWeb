from app import db

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String(500))  # E.g., "2024-10-30 09:00-11:00"
    
    appointments = db.relationship('Appointment', backref='doctor')
    user = db.relationship('User', backref='doctor', uselist=False)  # Relacionamento com o usuário

    def __repr__(self):
        return f'<Doctor {self.name}, Specialty: {self.specialty}>'
