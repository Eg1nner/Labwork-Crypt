from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    login = request.form['login']
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    return render_template('result.html',
                           login=login,
                           password=password,
                           hashed_password=hashed_password)

if __name__ == '__main__':
    app.run(debug=True)