from flask import Flask, request, render_template_string

app = Flask(__name__)

# Fake login form (No CSRF protection)
@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        email = request.form.get("email")
        return f"Password reset link sent to {email}!"
    
    return '''
        <h2>Fake Bank - Reset Password</h2>
        <form method="POST">
            <label>Email:</label>
            <input type="email" name="email">
            <input type="submit" value="Reset Password">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, port=5000)
