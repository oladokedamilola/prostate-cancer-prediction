from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='diagnoses')
    patient_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    race = db.Column(db.String(50))
    bmi = db.Column(db.Float)
    family_history = db.Column(db.Integer)
    psa_level = db.Column(db.Float)
    prostate_volume = db.Column(db.Float)
    dre_result = db.Column(db.Integer)
    urinary_frequency = db.Column(db.Integer)
    nocturia = db.Column(db.Integer)
    weak_urine_stream = db.Column(db.Integer)
    hematuria = db.Column(db.Integer)
    erectile_dysfunction = db.Column(db.Integer)
    pain_in_pelvis = db.Column(db.Integer)
    bone_pain = db.Column(db.Integer)
    weight_loss = db.Column(db.Integer)
    result = db.Column(db.String(20))
    confidence = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
