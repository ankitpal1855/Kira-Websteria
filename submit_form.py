from flask import Flask, request, jsonify
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)

@app.route('/', methods=['POST'])
def submit_form():
    try:
        # Parse JSON data from the request
        data = request.json
        name = data['name']
        email = data['email']
        phone = data['phone']

        # Your Gmail credentials
        sender_email = "testingap1855@gmail.com"
        receiver_email = "ap349500@gmail.com"
        password = "hyrktcncbubpkrdx"

        # Email content
        subject = "Kira Websteria Submission"
        message = f"Name: {name}\n\nEmail: {email}\n\nPhone: {phone}"

        # Create MIMEText object
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Send email using SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        return jsonify({"status": "success", "message": "Mail sent successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
