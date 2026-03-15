"""
Health Mate - Modern Medical Insurance Advisor Web Application
Flask Backend Application
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import numpy as np
import pickle
import os
from datetime import datetime
import json

app = Flask(__name__)
# Use environment variable for secret key (secure for production)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

# Load the health insurance model
try:
    with open('insurance_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Helper function to calculate BMI
def calculate_bmi(height_cm, weight_kg):
    """Calculate BMI from height and weight"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# Helper function to get BMI category
def get_bmi_category(bmi):
    """Return BMI category and health advice"""
    if bmi < 18.5:
        return {
            'category': 'Underweight',
            'color': '#17a2b8',
            'advice': 'Consider consulting a nutritionist for a healthy weight gain plan.',
            'icon': 'fa-arrow-down'
        }
    elif 18.5 <= bmi < 25:
        return {
            'category': 'Normal Weight',
            'color': '#28a745',
            'advice': 'Great! Maintain your healthy lifestyle.',
            'icon': 'fa-check-circle'
        }
    elif 25 <= bmi < 30:
        return {
            'category': 'Overweight',
            'color': '#ffc107',
            'advice': 'Consider a balanced diet and regular exercise.',
            'icon': 'fa-exclamation-triangle'
        }
    else:
        return {
            'category': 'Obese',
            'color': '#dc3545',
            'advice': 'Please consult a healthcare provider for personalized advice.',
            'icon': 'fa-exclamation-circle'
        }

@app.route('/')
def home():
    """Home page route"""
    return render_template('home.html')

@app.route('/bmi-calculator')
def bmi_calculator():
    """BMI Calculator page"""
    return render_template('bmi_calculator.html')

@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi_route():
    """API endpoint to calculate BMI"""
    try:
        data = request.get_json()
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        
        bmi = calculate_bmi(height, weight)
        bmi_data = get_bmi_category(bmi)
        bmi_data['bmi'] = bmi
        bmi_data['age'] = age
        
        return jsonify({'success': True, 'data': bmi_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/health-assessment')
def health_assessment():
    """Health Assessment page"""
    return render_template('health_assessment.html')

@app.route('/submit-assessment', methods=['POST'])
def submit_assessment():
    """API endpoint to process health assessment"""
    try:
        data = request.get_json()
        
        # Store assessment in session
        session['health_assessment'] = data
        
        # Generate health advice based on conditions
        advice = []
        
        age = int(data.get('age', 0))
        weight = float(data.get('weight', 0))
        height = float(data.get('height', 0))
        conditions = data.get('conditions', [])
        smoking = data.get('smoking', 'no')
        alcohol = data.get('alcohol', 'no')
        exercise = data.get('exercise', 'none')
        
        bmi = calculate_bmi(height, weight) if height > 0 and weight > 0 else 0
        
        # Generate personalized advice
        if age > 50 and 'Heart Disease' in conditions:
            advice.append({
                'type': 'warning',
                'title': 'Cardiovascular Health',
                'message': 'Regular cardiovascular check-ups are important. Consider a low-fat diet and mild physical activity.'
            })
        
        if 'Diabetes' in conditions:
            advice.append({
                'type': 'warning',
                'title': 'Diabetes Management',
                'message': 'Proper diet, exercise, and regular blood sugar monitoring is critical. Avoid high-sugar foods.'
            })
        
        if bmi > 30:
            advice.append({
                'type': 'warning',
                'title': 'Weight Management',
                'message': 'Your BMI suggests obesity. A balanced diet and regular physical activity are important.'
            })
        
        if smoking == 'yes':
            advice.append({
                'type': 'danger',
                'title': 'Smoking Cessation',
                'message': 'Smoking is harmful. Consider quitting to reduce health risks significantly.'
            })
        
        if alcohol == 'yes':
            advice.append({
                'type': 'warning',
                'title': 'Alcohol Consumption',
                'message': 'Excessive alcohol can lead to liver damage. Moderation is key.'
            })
        
        if exercise == 'none':
            advice.append({
                'type': 'info',
                'title': 'Physical Activity',
                'message': 'Regular exercise is essential for overall health. Start with light activities.'
            })
        
        if not advice:
            advice.append({
                'type': 'success',
                'title': 'Good Health',
                'message': 'Your health profile looks stable. Continue maintaining a healthy lifestyle!'
            })
        
        return jsonify({'success': True, 'advice': advice})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/insurance-predictor')
def insurance_predictor():
    """Insurance Cost Predictor page"""
    return render_template('insurance_predictor.html')

@app.route('/predict-insurance', methods=['POST'])
def predict_insurance():
    """API endpoint to predict insurance cost"""
    try:
        if model is None:
            return jsonify({'success': False, 'error': 'Model not loaded'})
        
        data = request.get_json()
        
        # Extract features
        age = int(data['age'])
        sex = 1 if data['sex'] == 'male' else 0
        bmi = float(data['bmi'])
        children = int(data['children'])
        smoker = 1 if data['smoker'] == 'yes' else 0
        region = int(data.get('region', 0))
        
        # Create feature array
        features = np.array([[age, sex, bmi, children, smoker, region]])
        
        # Predict
        prediction = model.predict(features)[0]
        
        # Generate insurance recommendations based on prediction
        recommendations = []
        
        if prediction < 5000:
            recommendations = [
                {'name': 'Basic Health Plan', 'premium': '$150/month', 'coverage': 'Basic coverage with essential benefits'},
                {'name': 'Standard Plan', 'premium': '$250/month', 'coverage': 'Comprehensive coverage with preventive care'}
            ]
        elif prediction < 15000:
            recommendations = [
                {'name': 'Standard Plus Plan', 'premium': '$350/month', 'coverage': 'Enhanced coverage with specialist visits'},
                {'name': 'Premium Plan', 'premium': '$500/month', 'coverage': 'Extensive coverage with minimal copays'}
            ]
        else:
            recommendations = [
                {'name': 'Premium Plus Plan', 'premium': '$600/month', 'coverage': 'Maximum coverage with chronic condition management'},
                {'name': 'Platinum Plan', 'premium': '$800/month', 'coverage': 'Complete coverage with zero deductible'}
            ]
        
        return jsonify({
            'success': True,
            'predicted_cost': round(prediction, 2),
            'recommendations': recommendations
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/appointments')
def appointments():
    """Appointments page"""
    return render_template('appointments.html')

@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    """API endpoint to book an appointment"""
    try:
        data = request.get_json()
        
        # In a real application, save to database
        # For now, just return success
        appointment = {
            'id': datetime.now().strftime('%Y%m%d%H%M%S'),
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'date': data['date'],
            'time': data['time'],
            'department': data['department'],
            'doctor': data.get('doctor', 'To be assigned'),
            'reason': data.get('reason', ''),
            'status': 'Pending'
        }
        
        return jsonify({'success': True, 'appointment': appointment})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/health-records')
def health_records():
    """Health Records page"""
    return render_template('health_records.html')

@app.route('/symptom-checker')
def symptom_checker():
    """Symptom Checker page"""
    return render_template('symptom_checker.html')

@app.route('/check-symptoms', methods=['POST'])
def check_symptoms():
    """API endpoint to check symptoms"""
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        
        # Simple symptom analysis (in real app, use medical AI)
        analysis = {
            'severity': 'moderate',
            'possible_conditions': [],
            'recommendations': []
        }
        
        symptom_keywords = ' '.join(symptoms).lower()
        
        if 'fever' in symptom_keywords and 'cough' in symptom_keywords:
            analysis['possible_conditions'].append('Common Cold or Flu')
            analysis['recommendations'].append('Rest and stay hydrated')
            analysis['recommendations'].append('Monitor temperature')
        
        if 'chest pain' in symptom_keywords or 'breathing' in symptom_keywords:
            analysis['severity'] = 'high'
            analysis['possible_conditions'].append('Respiratory or Cardiac Issue')
            analysis['recommendations'].append('Seek immediate medical attention')
        
        if 'headache' in symptom_keywords:
            analysis['possible_conditions'].append('Tension Headache or Migraine')
            analysis['recommendations'].append('Rest in a quiet, dark room')
        
        if not analysis['possible_conditions']:
            analysis['possible_conditions'].append('General discomfort')
            analysis['recommendations'].append('Monitor symptoms and consult a doctor if they persist')
        
        return jsonify({'success': True, 'analysis': analysis})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/medication-tracker')
def medication_tracker():
    """Medication Tracker page"""
    return render_template('medication_tracker.html')

@app.route('/health-resources')
def health_resources():
    """Health Resources and Education page"""
    return render_template('health_resources.html')

@app.route('/emergency')
def emergency():
    """Emergency Information page"""
    return render_template('emergency.html')

@app.route('/blood_bank')
def blood_bank():
    """Blood Bank & Donor Finder page"""
    return render_template('blood_bank.html')

@app.route('/first_aid')
def first_aid():
    """First Aid Guide page"""
    return render_template('first_aid.html')

@app.route('/mental_health')
def mental_health():
    """Mental Health Support page"""
    return render_template('mental_health.html')

@app.route('/about')
def about():
    """About Us page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """API endpoint to handle contact form submission"""
    try:
        data = request.get_json()
        # In real app, send email or save to database
        return jsonify({'success': True, 'message': 'Thank you for contacting us. We will respond shortly.'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Get port from environment variable (for deployment) or use 5000 for local
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
