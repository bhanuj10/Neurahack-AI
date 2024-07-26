from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import time
from threading import Thread
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
# Dummy user data
users = {"bhanuj@aimavericks.com": "password"}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            return redirect(url_for('file_drop'))
        else:
            return "Invalid credentials"
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():############    need some adjust accordingly
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users[email] = password
        return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/file_drop', methods=['GET', 'POST'])
def file_drop():
    for i in os.listdir('uploads'):
        os.remove('uploads/'+i)
    if request.method == 'POST':
        # Handle file drop here
        file = request.files['file']
        # Save the file or process it
    
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        return redirect(url_for('file_drop_result'))
    return render_template('file_drop.html')

@app.route('/file_drop_result',methods=['GET','POST'])
def file_drop_result():
    if request.method =='POST':
        return render_template('file_drop_result.html')    
    return render_template('file_drop_result.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    if not os.path.exists('static/results'):
        os.makedirs('static/results')
    app.run(debug=False)
