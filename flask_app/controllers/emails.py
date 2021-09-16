from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.email import Email

@app.route('/')
def load_page():
    return render_template('validator.html')

@app.route('/add_email', methods=['POST'])
def add_new_email():
    data = {
        'name' : request.form['name']
    }
    if not Email.validate_email(data):
        return redirect('/')
    Email.add_an_email(data)
    return redirect('/success')

@app.route('/success')
def show_success():
    emails = Email.get_all_emails()
    return render_template('success.html', emails = emails)