from flask import Flask, render_template, redirect, url_for, request
import smtplib
#from email.message import EmailMessage
#import imghdr
from email.mime.text import MIMEText
#from flask_wtf import FlaskForm
#from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
#from wtforms.validators import InputRequired
import glob
#import pandas as pd
#import csv
from docx import Document

ALLOWED_EXTENSIONS = {'csv', 'html', 'htm', 'docx'}


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Innovation'
app.config['UPLOAD_FOLDER'] = r"/Users/mariondeguzman/PycharmProjects/pythonProject/static/upload_files"

def allowed_file(filename):
    return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#from email.utils import make_msgid

my_email = "hirayamanawariautomation@gmail.com"
password = "knnkyiovubzwrkwv"

@app.route('/')
def home_page():
    return render_template("homepage.html")

@app.route('/sel2', methods=["GET", "POST"])
def sel2():
    if request.method == 'GET':
        return render_template('email_template2.html')
    elif request.method == 'POST':
        email_addresses = request.form.get('email')
        email_content = request.form.get('content')
        email_subject = request.form.get('subject')
        email_list = email_addresses.split(',')
        #sel2_sending(email_list, email_subject, email_content)
        msg = MIMEText(email_content, 'plain')
        msg['From'] = my_email
        msg['To'] = ', '.join(email_list)
        msg['Subject'] = email_subject
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)
        return render_template('successful_email.html')


@app.route('/selection', methods=["GET", "POST"])
def selection_page():
    if request.method == 'GET':
        return render_template('selection_main.html')
    elif request.method == 'POST':
        if 'file1' not in request.files:
            return render_template('selection_main_error1.html')
        file1 = request.files['file1']
        filename = file1.filename
        if file1.filename == '':
            return render_template('selection_main_error1.html')
        if file1 and allowed_file(filename):
            f1 = file1
            filename = secure_filename(f1.filename)
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('selection_page2', filename1=filename))

@app.route('/selection2', methods=["GET", "POST"])
def selection_page2():
    if request.method == 'GET':
        return render_template('selection_main_success1.html')
    elif request.method == 'POST':
        if 'file2' not in request.files:
            return render_template('selection_main_error2.html')
        file2 = request.files['file2']
        filename = file2.filename
        if file2.filename == '':
            return render_template('selection_main_error2.html')
        if file2 and allowed_file(filename):
            f2 = file2
            filename = secure_filename(f2.filename)
            f2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('for_autom', filename2=filename))

@app.route('/forautom', methods=["GET", "POST"])
def for_autom():
    if request.method == 'GET':
        return render_template('selection_main_success2.html')


@app.route('/automation', methods=["GET", "POST"])
def automation_page():
    if request.method == "POST":
        doc_message = glob.glob(r"/Users/mariondeguzman/PycharmProjects/pythonProject/static/upload_files/*.docx")
        receiver = glob.glob(r"/Users/mariondeguzman/PycharmProjects/pythonProject/static/upload_files/*.csv")
        latest_file_doc = max(doc_message, key=os.path.getctime, default=0)
        latest_file_rec = max(receiver, key=os.path.getctime)
        doc_m = Document(latest_file_doc) #,encoding='latin-1' for html reading
        doc_m_txt = '\n'.join([paragraph.text for paragraph in doc_m.paragraphs])

        receiverff = []
        msg = MIMEText(doc_m_txt, 'plain')
        msg['From'] = my_email
        with open(latest_file_rec) as csvfile:
            #csv_file = csv.reader(csvfile)
            for cf in csvfile:
                receiverff.append(cf)
        new_rec = [item.strip() for item in receiverff]
        msg['To'] = ", ".join(new_rec)
        msg['Subject'] = request.form.get('subject')
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)
        return render_template('successful_email.html')

if __name__ == "__main__":
    app.run()