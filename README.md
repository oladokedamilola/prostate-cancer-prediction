# Prostate Cancer Prediction System

An AI-powered diagnostic system for early detection of prostate cancer using machine learning and a web interface. The system combines synthetic dataset generation, multiple ML model evaluation, and a Flask web application for real-time diagnosis.

![Prostate Cancer Prediction System](diagnosis-page1.png)
![Prostate Cancer Prediction System](diagnosis-page2.png)

## 🎯 Features

- **Synthetic Dataset Generation**: Custom 10,000 patient records with medical heuristics
- **Multiple ML Models**: Comparative analysis of ANN, Random Forest, SVM, Decision Tree, and MLP
- **High Accuracy**: Artificial Neural Network achieves 99.75% accuracy
- **Web Application**: Flask-based interface for healthcare professionals
- **Medical Report Generation**: PDF and Word export functionality
- **Secure Authentication**: Healthcare worker registration and login system
- **Diagnosis History**: Complete record tracking for patient follow-up

## 📊 Dataset

### Dataset Characteristics
- **Size**: 10,000 synthetic patient records
- **Features**: 17 clinical parameters including age, PSA levels, symptoms, and medical history
- **Class Distribution**: 55:45 mild imbalance (reflects real-world prevalence)
- **Generation**: Medically informed heuristics with realistic feature correlations

### Features Included:
1. `patient_id` - Unique identifier
2. `age` - Patient age
3. `race` - Ethnic background
4. `bmi` - Body Mass Index
5. `family_history` - Family history of prostate cancer
6. `psa_level` - Prostate-Specific Antigen level
7. `prostate_volume` - Prostate size measurement
8. `dre_result` - Digital Rectal Exam result
9. `urinary_frequency` - Urination frequency symptom
10. `nocturia` - Nighttime urination
11. `weak_urine_stream` - Urine flow strength
12. `hematuria` - Blood in urine
13. `erectile_dysfunction` - ED symptom
14. `pain_in_pelvis` - Pelvic pain
15. `bone_pain` - Bone pain symptom
16. `weight_loss` - Unexplained weight loss
17. `diagnosis` - Target variable (0: Negative, 1: Positive)

## 🤖 Machine Learning Models

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | False Negatives | False Positives |
|-------|----------|-----------|--------|----------|-----------------|-----------------|
| **Artificial Neural Network (ANN)** | **99.75%** | **1.00** | **1.00** | **1.00** | **4** | **7** |
| Random Forest | 98.00% | 0.98 | 1.00 | 1.00 | 1 | 30 |
| Support Vector Machine (SVM) | 98.00% | 0.98 | 1.00 | 1.00 | 5 | 28 |
| Multi-Layer Perceptron (MLP) | 99.50% | 0.99 | 0.99 | 0.99 | 3 | 12 |
| Decision Tree | 97.50% | 0.97 | 0.98 | 0.98 | 2 | 35 |

### Model Selection Rationale
The **Artificial Neural Network** was selected as the production model due to:
- Highest overall accuracy (99.75%)
- Perfect recall (1.00) - critical for medical diagnosis
- Lowest combined false predictions (11 total)
- Best generalization capability on unseen data
- Superior performance across all evaluation metrics

## 🏗️ System Architecture

### Phase 1: Machine Learning Pipeline

1. **Data Generation**: Created synthetic dataset with medical heuristics
2. **Data Preprocessing**: Handled missing values, normalization, and encoding
3. **Model Training**: Evaluated multiple ML algorithms
4. **Model Evaluation**: Used accuracy, precision, recall, F1-score, and confusion matrix
5. **Model Selection**: Chose ANN based on performance metrics

### Phase 2: Web Application Development
1. **Backend**: Flask framework for server-side logic
2. **Frontend**: HTML, CSS, JavaScript for user interface
3. **User Authentication**: Secure registration and login for healthcare workers
4. **Diagnosis Module**: Input patient data and get real-time predictions
5. **Report Generation**: Export diagnosis results as PDF/Word documents
6. **Database**: Store user credentials and diagnosis history

### Technologies Used
- **Programming Language**: Python
- **Web Framework**: Flask
- **Machine Learning**: Scikit-learn, TensorFlow/Keras
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (development), MySQL (production-ready)
- **Report Generation**: ReportLab, python-docx
- **Visualization**: Matplotlib, Seaborn
- **Environment**: Jupyter Notebook, Virtual Environment (venv)

## 📱 Web Application Features

### User Flow
1. **Registration/Login**: Secure authentication for healthcare workers
2. **Diagnosis Form**: Input patient data (17 clinical features)
3. **AI Prediction**: Real-time prostate cancer risk assessment
4. **Results Display**: Clear diagnosis with confidence level
5. **Report Generation**: Downloadable PDF/Word medical reports
6. **History Tracking**: Complete diagnosis record management

### Pages
- **Home**: System introduction and navigation
- **Register/Login**: User authentication
- **Diagnosis**: Patient data input form
- **Results**: Diagnosis outcome and report options
- **History**: Previous diagnosis records

## 📈 Model Training & Evaluation

### Training Process
1. **Data Split**: 80% training, 20% testing
2. **Preprocessing**: MinMax scaling, one-hot encoding
3. **Training**: 5-fold cross-validation
4. **Hyperparameter Tuning**: Grid search for optimal parameters
5. **Evaluation**: Comprehensive metrics analysis

### Key Technical Decisions
1. **Synthetic Data**: Overcame limitations of public datasets (size, imbalance, privacy)
2. **ANN Architecture**: 3 hidden layers with dropout regularization
3. **Feature Engineering**: Medical domain knowledge integration
4. **Class Weighting**: Addressed mild class imbalance
5. **Early Stopping**: Prevented overfitting during training

## 🏥 Clinical Relevance

### Medical Impact
- **Early Detection**: Identifies high-risk patients for further testing
- **Reduced False Negatives**: Critical for life-threatening conditions
- **Decision Support**: Assists healthcare professionals in diagnosis
- **Standardization**: Consistent evaluation across different practitioners

### Limitations & Considerations
- **Not a Replacement**: Supplementary tool, not replacement for medical professionals
- **Synthetic Data**: While realistic, may not capture all real-world variability
- **Feature Limitations**: Limited to 17 clinical parameters
- **Validation Required**: Clinical trials needed for real-world validation


## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/oladokedamilola/prostate-cancer-prediction.git
cd prostate-cancer-prediction
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up the database**
```bash
python init_db.py
```

5. **Run the application**
```bash
python app.py
```

6. **Access the web application**
```
Open browser and navigate to: http://localhost:5000
```

### Dependencies (requirements.txt)
```txt
flask==2.3.3
tensorflow==2.13.0
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
imbalanced-learn==0.10.1
reportlab==4.0.4
python-docx==0.8.11
```

## 🔬 Future Enhancements

1. **Real Clinical Data Integration**: Partner with healthcare institutions
2. **Advanced ML Techniques**: Ensemble methods, deep learning architectures
3. **Mobile Application**: iOS/Android apps for on-the-go diagnosis
4. **API Development**: REST API for third-party integration
5. **Multi-language Support**: Global accessibility for diverse regions
6. **Admin Dashboard**: Analytics and monitoring interface
7. **Predictive Analytics**: Treatment outcome prediction
8. **Telemedicine Integration**: Video consultation features

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Damilola Oladoke**
- GitHub: [@oladokedamilola](https://github.com/oladokedamilola)
- LinkedIn: [Damilola Oladoke](https://linkedin.com/in/oladokedamilola)
- Portfolio: [damilolaoladoke.com](https://github.com/oladokedamilola/portfolio.html)

## 🙏 Acknowledgments

- Medical professionals for domain expertise guidance
- Open-source community for ML libraries and tools
- Research papers on prostate cancer detection methodologies
- Healthcare AI innovation initiatives
- Academic advisors and mentors

---

**⚠️ Medical Disclaimer:** This system is a decision support tool and NOT a replacement for professional medical diagnosis, advice, or treatment. Always consult qualified healthcare providers for medical concerns. The synthetic dataset is for research purposes only and does not contain real patient data.
```

