from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return send_file('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    print(f"Received login attempt:")
    print(f"Email: {email}")
    print(f"Password: {password}")
    return f"Login information received at backend with email {email}", 200

if __name__ == '__main__':
    print("Server starting... Navigate to http://localhost:3000 in your browser.")
    app.run(host='0.0.0.0', port=3000)
