from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from io import BytesIO
from . import db
from .models import User, Diagnosis
from .forms import LoginForm, RegisterForm, DiagnosisForm
from .utils import preprocess_and_predict, generate_docx_report
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return redirect(url_for('main.login'))

@main.route('/home')
@login_required
def home():
    return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(
            email=form.email.data,
            password=hashed,
            first_name=form.first_name.data,
            last_name=form.last_name.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully! Please login.", "success")
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        flash("Invalid username or password.", "danger")
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('main.login'))

RACE_ENCODING = {
    'White': 4,
    'Black': 0,
    'Asian': 1,
    'Hispanic': 2,
    'Other': 3
}

@main.route('/diagnose', methods=['GET', 'POST'])
@login_required
def diagnose():
    form = DiagnosisForm()
    if form.validate_on_submit():
        label, confidence = preprocess_and_predict(request.form)
        diagnosis = Diagnosis(
            user_id=current_user.id,
            patient_name=form.patient_name.data,
            age=form.age.data,
            race=form.race.data,
            bmi=form.bmi.data,
            family_history=int(form.family_history.data),
            psa_level=form.psa_level.data,
            prostate_volume=form.prostate_volume.data,
            dre_result=int(form.dre_result.data),
            urinary_frequency=form.urinary_frequency.data,
            nocturia=form.nocturia.data,
            weak_urine_stream=int(form.weak_urine_stream.data),
            hematuria=int(form.hematuria.data),
            erectile_dysfunction=int(form.erectile_dysfunction.data),
            pain_in_pelvis=int(form.pain_in_pelvis.data),
            bone_pain=int(form.bone_pain.data),
            weight_loss=int(form.weight_loss.data),
            result=label,
            confidence=confidence
        )
        db.session.add(diagnosis)
        db.session.commit()

        return render_template("result.html",
            name=diagnosis.patient_name,
            symptoms={
                "Age": diagnosis.age,
                "Race": diagnosis.race,
                "BMI": diagnosis.bmi,
                "Family History": diagnosis.family_history,
                "PSA Level": diagnosis.psa_level,
                "Prostate Volume": diagnosis.prostate_volume,
                "DRE Result": diagnosis.dre_result,
                "Urinary Frequency": diagnosis.urinary_frequency,
                "Nocturia": diagnosis.nocturia,
                "Weak Urine Stream": diagnosis.weak_urine_stream,
                "Hematuria": diagnosis.hematuria,
                "Erectile Dysfunction": diagnosis.erectile_dysfunction,
                "Pain in Pelvis": diagnosis.pain_in_pelvis,
                "Bone Pain": diagnosis.bone_pain,
                "Weight Loss": diagnosis.weight_loss
            },
            result=label,
            confidence=round(confidence * 100, 2),
            record_id=diagnosis.id
        )
    return render_template("diagnose.html", form=form)

@main.route('/history')
@login_required
def history():
    diagnoses = Diagnosis.query.filter_by(user_id=current_user.id).order_by(Diagnosis.created_at.desc()).all()

    # Add .symptoms dictionary manually to each record
    for d in diagnoses:
        d.symptoms = {
            "Age": d.age,
            "Race": d.race,
            "BMI": d.bmi,
            "Family History": d.family_history,
            "PSA Level": d.psa_level,
            "Prostate Volume": d.prostate_volume,
            "DRE Result": d.dre_result,
            "Urinary Frequency": d.urinary_frequency,
            "Nocturia": d.nocturia,
            "Weak Urine Stream": d.weak_urine_stream,
            "Hematuria": d.hematuria,
            "Erectile Dysfunction": d.erectile_dysfunction,
            "Pain in Pelvis": d.pain_in_pelvis,
            "Bone Pain": d.bone_pain,
            "Weight Loss": d.weight_loss,
        }

    return render_template("history.html", diagnoses=diagnoses)

@main.route('/download/<format>/<int:record_id>')
@login_required
def download_result(format, record_id):
    diagnosis = Diagnosis.query.get_or_404(record_id)
    if diagnosis.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('main.history'))

    context = {
        'name': diagnosis.patient_name,
        'symptoms': {
            'Age': diagnosis.age,
            'Race': diagnosis.race,
            'BMI': diagnosis.bmi,
            'Family History': diagnosis.family_history,
            'PSA Level': diagnosis.psa_level,
            'Prostate Volume': diagnosis.prostate_volume,
            'DRE Result': diagnosis.dre_result,
            'Urinary Frequency': diagnosis.urinary_frequency,
            'Nocturia': diagnosis.nocturia,
            'Weak Urine Stream': diagnosis.weak_urine_stream,
            'Hematuria': diagnosis.hematuria,
            'Erectile Dysfunction': diagnosis.erectile_dysfunction,
            'Pain in Pelvis': diagnosis.pain_in_pelvis,
            'Bone Pain': diagnosis.bone_pain,
            'Weight Loss': diagnosis.weight_loss,
        },
        'result': diagnosis.result,
        'confidence': diagnosis.confidence,
        'timestamp': diagnosis.created_at.strftime("%Y-%m-%d %H:%M"),
    }

    if format == 'pdf':
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        # Branding header
        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, height - 60, "Lassa Fever Diagnosis Report")

        # Add patient name and timestamp
        p.setFont("Helvetica", 12)
        p.drawString(50, height - 90, f"Patient Name: {context['name']}")
        p.drawString(50, height - 110, f"Date: {context['timestamp']}")

        # Add diagnosis result
        p.setFont("Helvetica-Bold", 13)
        p.drawString(50, height - 140, f"Diagnosis Result: {context['result']}")

        p.setFont("Helvetica", 12)
        p.drawString(50, height - 160, f"Confidence Score: {context['confidence']}%")

        # Add symptom details
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, height - 190, "Symptom Inputs:")

        p.setFont("Helvetica", 11)
        y = height - 210
        for label, value in context['symptoms'].items():
            p.drawString(70, y, f"{label}: {value}")
            y -= 18
            if y < 50:
                p.showPage()
                y = height - 50

        p.showPage()
        p.save()
        buffer.seek(0)

        return send_file(buffer, mimetype='application/pdf',
                         download_name=f"{diagnosis.patient_name}_diagnosis.pdf",
                         as_attachment=True)

    elif format == 'docx':
        docx_file = generate_docx_report(context)
        return send_file(docx_file, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                         download_name=f"{diagnosis.patient_name}_diagnosis.docx",
                         as_attachment=True)

    flash("Invalid download format.", "danger")
    return redirect(url_for('main.history'))

# Error Handlers
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@main.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403

@main.app_errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500
