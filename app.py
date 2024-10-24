from flask import Flask, request, render_template, jsonify, redirect, url_for
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

# Credenciales EmailJS privadas en el backend
EMAILJS_SERVICE_ID = os.getenv('EMAILJS_SERVICE_ID')
EMAILJS_TEMPLATE_ID = os.getenv('EMAILJS_TEMPLATE_ID')
EMAILJS_PUBLIC_KEY = os.getenv('EMAILJS_PUBLIC_KEY')
EMAILJS_API_URL = "https://api.emailjs.com/api/v1.0/email/send"

@app.route('/')
def index():
    return render_template('contact_form.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    
    user_name = request.form['user_name']
    user_email = request.form['user_email']
    message = request.form['message']

    data = {
        'service_id': EMAILJS_SERVICE_ID,
        'template_id': EMAILJS_TEMPLATE_ID,
        'user_id': EMAILJS_PUBLIC_KEY,
        'template_params': {
            'user_name': user_name,
            'user_email': user_email,
            'message': message
        }
    }

    response = requests.post(EMAILJS_API_URL, json=data)
        
    if response.status_code == 200:
        redirect_url = url_for('index')
        print(f"Redirecting to: {redirect_url}")
        return redirect(redirect_url)
    else:
        # Error al enviar el correo
        return jsonify({"message": "Failed to send email"}), 500


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
