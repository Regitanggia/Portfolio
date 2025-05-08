from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'rahasia'

EMAIL_PENGIRIM = 'regitaanggia25@gmail.com'
EMAIL_TUJUAN = 'regitaanggia25@gmail.com'
PASSWORD = 'ukwnooyumqdvuqcq'  # bukan password biasa!

@app.route('/')
def home():
    return redirect('/contact')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send_email():
    email_pengirim = request.form['email']
    pesan = request.form['message']

    try:
        msg = EmailMessage()
        msg.set_content(f"Pesan dari: {email_pengirim}\n\n{pesan}")
        msg['Subject'] = 'Pesan dari Website'
        msg['From'] = EMAIL_PENGIRIM
        msg['To'] = EMAIL_TUJUAN

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_PENGIRIM, PASSWORD)
            smtp.send_message(msg)

        flash('Pesan berhasil dikirim!', 'success')
    except Exception as e:
        flash(f'Gagal mengirim pesan: {e}', 'danger')

    return redirect('/contact')

if __name__ == '__main__':
    app.run(debug=True)
