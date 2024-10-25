from app import db

class Patient(db.Model):
    __tablename__ = 'patients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    medical_history = db.Column(db.Text)

    appointments = db.relationship('Appointment', backref='patient')

    def __repr__(self):
        return f'<Patient {self.name}>'
