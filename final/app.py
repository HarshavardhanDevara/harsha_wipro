from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite://app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Doctor Model
class Doctor(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String, nullable=False)
    available_slots = db.Column(db.PickleType, nullable=False)
    on_leave = db.Column(db.Boolean, default=False)

# Patient Model
class Patient(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.String, nullable=False)

# Appointment Model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.String, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.String, db.ForeignKey('doctor.id'), nullable=False)
    time_slot = db.Column(db.String, nullable=False)

# Home Route (Fixes 404 Issue)
@app.route('/')
def home():
    return "Doctor Appointment API is running!"

# Register Doctor
@app.route('/register_doctor', methods=['POST'])
def register_doctor():
    data = request.json
    if Doctor.query.get(data['doctor_id']):
        return jsonify({"success": False, "message": "Doctor ID already exists!"})

    new_doctor = Doctor(
        id=data['doctor_id'],
        name=data['name'],
        specialty=data['specialty'],
        available_slots=data['available_slots']
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({"success": True, "message": "Doctor registered successfully!"})

# Register Patient
@app.route('/register_patient', methods=['POST'])
def register_patient():
    data = request.json
    if Patient.query.get(data['patient_id']):
        return jsonify({"success": False, "message": "Patient ID already exists!"})

    new_patient = Patient(
        id=data['patient_id'],
        name=data['name'],
        age=data['age'],
        contact=data['contact']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"success": True, "message": "Patient registered successfully!"})

#Book Appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.json
    doctor = Doctor.query.get(data['doctor_id'])
    
    if not doctor:
        return jsonify({"success": False, "message": "Doctor not found!"})
    
    if data['time_slot'] not in doctor.available_slots:
        return jsonify({"success": False, "message": "Time slot not available!"})

    existing_appointment = Appointment.query.filter_by(doctor_id=data['doctor_id'], time_slot=data['time_slot']).first()
    if existing_appointment:
        return jsonify({"success": False, "message": "Time slot already booked!"})

    new_appointment = Appointment(
        patient_id=data['patient_id'],
        doctor_id=data['doctor_id'],
        time_slot=data['time_slot']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"success": True, "message": "Appointment booked successfully!"})

#Get Doctor's Appointments
@app.route('/get_appointments/<doctor_id>', methods=['GET'])
def get_appointments(doctor_id):
    appointments = Appointment.query.filter_by(doctor_id=doctor_id).all()
    return jsonify([{"patient_id": a.patient_id, "doctor_id": a.doctor_id, "time_slot": a.time_slot} for a in appointments])

# Cancel Appointment
@app.route('/cancel_appointment', methods=['POST'])
def cancel_appointment():
    data = request.json
    appointment = Appointment.query.filter_by(patient_id=data['patient_id'], doctor_id=data['doctor_id'], time_slot=data['time_slot']).first()

    if not appointment:
        return jsonify({"success": False, "message": "Appointment not found!"})

    db.session.delete(appointment)
    db.session.commit()
    return jsonify({"success": True, "message": "Appointment cancelled successfully!"})

# Run App & Create Tables
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
