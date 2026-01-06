from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired, Length, Email, DataRequired

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired

class DiagnosisForm(FlaskForm):
    patient_name = StringField("Patient Name", validators=[InputRequired()])
    age = IntegerField("Age", validators=[InputRequired()], render_kw={"placeholder": "e.g. 55"})
    race = SelectField("Race", choices=[
        ('White','White'), ('Black','Black'), ('Asian','Asian'),
        ('Hispanic','Hispanic'), ('Other','Other')
    ])
    bmi = FloatField("BMI", validators=[InputRequired()], render_kw={"placeholder": "e.g. 24.5", "type": "number", "step": "any"})
    family_history = SelectField("Family History", choices=[('0','No'), ('1','Yes')])
    psa_level = FloatField("PSA Level", validators=[InputRequired()], render_kw={"placeholder": "e.g. 4.2", "type": "number", "step": "any"})
    prostate_volume = FloatField("Prostate Volume", validators=[InputRequired()], render_kw={"placeholder": "e.g. 35.0", "type": "number", "step": "any"})
    dre_result = SelectField("DRE Result", choices=[('0','Normal'), ('1','Abnormal')])
    urinary_frequency = IntegerField("Urinary Frequency", validators=[InputRequired()])
    nocturia = IntegerField("Nocturia", validators=[InputRequired()])
    weak_urine_stream = SelectField("Weak Urine Stream", choices=[('0','No'), ('1','Yes')])
    hematuria = SelectField("Hematuria", choices=[('0','No'), ('1','Yes')])
    erectile_dysfunction = SelectField("Erectile Dysfunction", choices=[('0','No'), ('1','Yes')])
    pain_in_pelvis = SelectField("Pelvic Pain", choices=[('0','No'), ('1','Yes')])
    bone_pain = SelectField("Bone Pain", choices=[('0','No'), ('1','Yes')])
    weight_loss = SelectField("Weight Loss", choices=[('0','No'), ('1','Yes')])
    submit = SubmitField("Submit")


# from flask_wtf import FlaskForm
# from wtforms import StringField, FloatField, SelectField, SubmitField
# from wtforms.validators import DataRequired

# class DiagnosisForm(FlaskForm):
#     patient_name = StringField("Patient Name", validators=[DataRequired()])
#     age = FloatField("Age", validators=[DataRequired()])
#     psa = FloatField("PSA Level", validators=[DataRequired()])
#     gleason_score = FloatField("Gleason Score", validators=[DataRequired()])
#     tumor_volume = FloatField("Tumor Volume", validators=[DataRequired()])
#     perineural_invasion = SelectField("Perineural Invasion", choices=[('0', 'No'), ('1', 'Yes')])
#     race = SelectField("Race", choices=[
#         ('0', 'White'),
#         ('1', 'Black'),
#         ('2', 'Asian'),
#         ('3', 'Other')
#     ])
#     submit = SubmitField("Diagnose")
