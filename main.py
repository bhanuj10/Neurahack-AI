from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users[email] = password
        return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/file_drop', methods=['GET', 'POST'])
def file_drop():
    if request.method == 'POST':
        # Handle file drop here
        file = request.files['file']
        # Save the file or process it
        return redirect(url_for('file_drop_result'))
    return render_template('file_drop.html')

@app.route('/file_drop_result')
def file_drop_result():
    return render_template('file_drop_result.html')

if __name__ == '__main__':
    app.run(debug=True)
