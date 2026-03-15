# Health Mate - AI-Powered Medical Insurance Advisor

A comprehensive, modern web application for health insurance planning and medical wellness support. Health Mate uses AI and machine learning to provide personalized health insurance recommendations while offering a complete suite of healthcare tools and resources.

## 🌟 Key Features

### 🏥 Health Assessment Tools
- **BMI Calculator**: Instant body mass index calculation with health recommendations
- **Health Assessment**: Complete health profile evaluation with personalized advice
- **Symptom Checker**: AI-powered symptom analysis and guidance
- **Medication Tracker**: Manage and track your medications effectively

### 💰 Insurance Planning
- **Insurance Predictor**: ML-powered prediction of healthcare costs using Linear Regression
- **Personalized Recommendations**: Tailored insurance plans based on your health profile
- **Cost Analysis**: Detailed breakdown of expected medical expenses

### 🚑 Emergency Resources
- **Quick Access Emergency Numbers**: Indian emergency services (102, 100, 101, 1091, 1098)
- **Hospital Finder**: Instant Google Maps integration to find nearest hospitals
- **First Aid Guide**: Comprehensive CPR, choking, burns, stroke, and heart attack procedures
- **Mental Health Helplines**: 24/7 support with Tele MANAS and other services

### 🩸 Blood Bank & Donor Finder
- **Blood Bank Network**: Direct access to Indian Blood Bank database
- **Blood Group Compatibility**: Complete compatibility chart for all blood types
- **Donor Registration**: Information on becoming a blood donor
- **Emergency Blood Requests**: Quick access to blood donation resources

### 🧠 Mental Health Support ("Your Mind Matters")
- **Mood Tracker**: Interactive mood assessment with encouraging responses
- **Breathing Exercise**: Animated breathing circle for stress relief
- **Support Helplines**: 24/7 mental health helplines (Tele MANAS, AASRA, iCall)
- **Daily Affirmations**: Positive mental health messages
- **Soft UI Design**: Calming colors and smooth animations

### 📅 Appointment Booking
- **Schedule Consultations**: Book appointments with healthcare professionals
- **Multiple Departments**: General practice, cardiology, neurology, psychiatry, and more
- **Easy Management**: Track your upcoming appointments

## 🛠️ Technology Stack

- **Backend**: Flask 3.0 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3, JavaScript
- **Machine Learning**: Scikit-learn 1.3.2 (Linear Regression)
- **Data Processing**: Pandas, NumPy
- **Icons**: Font Awesome 6.4.0
- **Typography**: Poppins, Inter, Nunito (for mental health section)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Health-Mate.git
cd Health-Mate
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Flask application**
```bash
python flask_app.py
```

5. **Access the website**
Open your browser and navigate to:
```
http://localhost:5000
```

## 📋 Requirements

All dependencies are listed in `requirements.txt`:

- Flask==3.0.0
- scikit-learn==1.3.2
- pandas==2.1.4
- numpy==1.26.2
- Werkzeug==3.0.0
- Jinja2==3.1.2
- streamlit==1.28.0 (optional, for alternative UI)

Install all with:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
Health-Mate/
├── flask_app.py                 # Main Flask application
├── app.py                       # Streamlit alternative app
├── model.py                     # ML model training script
├── config.py                    # Configuration settings
├── insurance_model.pkl          # Trained Linear Regression model
├── insurance.csv                # Training dataset
├── requirements.txt             # Python dependencies
├── README.md                    # This file
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template (navbar & footer)
│   ├── home.html               # Landing page
│   ├── bmi_calculator.html     # BMI calculation tool
│   ├── health_assessment.html  # Health evaluation form
│   ├── symptom_checker.html    # AI symptom analyzer
│   ├── medication_tracker.html # Medication management
│   ├── insurance_predictor.html# Cost prediction tool
│   ├── appointments.html       # Appointment booking
│   ├── emergency.html          # Emergency resources
│   ├── blood_bank.html         # Blood bank finder
│   ├── first_aid.html          # First aid guidance
│   ├── mental_health.html      # Mental health support
│   ├── about.html              # About us page
│   ├── contact.html            # Contact information
│   └── health_records.html     # Health records tracker
│
├── static/                      # Static assets
│   ├── css/
│   │   └── style.css           # Main stylesheet (teal theme)
│   └── js/
│       └── main.js             # JavaScript utilities
│
└── venv/                        # Virtual environment (created automatically)
```

## 🚀 Running the Application

### Option 1: Flask Web Application (Recommended)
```bash
python flask_app.py
```
Visit: `http://localhost:5000`

### Option 2: Streamlit Dashboard
```bash
streamlit run app.py
```

## 🤖 Machine Learning Model

The insurance cost prediction uses a **Linear Regression** model trained on health and demographic data:

**Features:**
- Age
- Gender (Male/Female)
- BMI (Body Mass Index)
- Number of Dependents
- Smoker Status
- Region

**Output:** Predicted annual insurance cost

To retrain the model:
```bash
python model.py
```

## 🎨 Theme & Design

- **Color Scheme**: Professional teal (#26A69A) with soft blues
- **Design Pattern**: Modern, healthcare-focused UI
- **Responsive**: Fully mobile-friendly design
- **Accessibility**: WCAG 2.1 compliant color contrast and navigation

## 🚀 Deployment Options

### Option 1: PythonAnywhere (Free)
1. Create account at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload files via Web tab
3. Configure WSGI file to point to `flask_app.py`
4. Set working directory and reload web app

### Option 2: Render (Free Tier)
1. Create account at [Render](https://render.com)
2. Connect GitHub repository
3. Create new Web Service
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn flask_app:app`

### Option 3: Heroku
1. Install Heroku CLI
2. Create `Procfile`:
```
web: gunicorn flask_app:app
```
3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Option 4: Docker (Self-Hosted)
1. Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "flask_app.py"]
```
2. Build and run:
```bash
docker build -t health-mate .
docker run -p 5000:5000 health-mate
```

## 📊 Features in Detail

### Insurance Cost Predictor
- Input health metrics and demographics
- AI analyzes data using trained ML model
- Receives personalized cost estimate and plan recommendations

### Health Assessment
- Comprehensive medical history questionnaire
- Personalized health advice based on responses
- Risk assessment for common conditions

### Symptom Checker
- Describe your symptoms
- AI provides initial guidance (not a diagnosis)
- Recommends seeking professional medical care when needed

### Mental Health Support
- Mood tracking with emotional intelligence
- Guided breathing exercises for stress relief
- Access to 24/7 helplines (Tele MANAS, AASRA, iCall)

### Appointment Booking
- Schedule consultations across multiple departments
- Track upcoming appointments
- Easy cancellation and rescheduling

## 🔐 Privacy & Security

- **Data Protection**: All user data is encrypted
- **HTTPS Ready**: Supports secure connections
- **No Third-Party Storage**: Data stored locally
- **Compliance**: Follows healthcare data guidelines

## 🐛 Known Issues & Limitations

- Machine learning model trained on US insurance data (adapt for your region)
- Symptom checker is for informational purposes only, not medical diagnosis
- Requires internet for Google Maps integration (hospital finder)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 💬 Support & Contact

For issues, feature requests, or questions:

- **GitHub Issues**: [Report bugs here](https://github.com/your-username/Health-Mate/issues)
- **Email**: support@healthmate.care
- **Emergency Helpline**: 102 (India)

## 👥 Credits

**Special Thanks** to contributors and the open-source community for tools and libraries used.

## 📈 Future Enhancements

- [ ] Multi-language support (Hindi, regional languages)
- [ ] Mobile app (React Native/Flutter)
- [ ] Advanced ML models (Random Forest, XGBoost)
- [ ] Integration with real insurance providers
- [ ] Video consultation feature
- [ ] Payment gateway integration
- [ ] User authentication and accounts
- [ ] Health record cloud sync

## ⚠️ Disclaimer

Health Mate is an informational platform and does NOT provide medical advice. Always consult licensed healthcare professionals for medical concerns. The AI recommendations are for guidance only and should not replace professional medical consultation.

---

**Last Updated**: March 2026  
**Version**: 1.0.0


