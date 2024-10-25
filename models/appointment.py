from app import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'<Appointment {self.id}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}>'
