from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Predefined correct credentials
CORRECT_USERNAME = 'admin'
CORRECT_PASSWORD = 'harsha123'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return redirect(url_for('success'))
    else:
        message = 'Login unsuccessful'
        return render_template('login.html', message=message)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
