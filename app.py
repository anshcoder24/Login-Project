
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check email and password here
        print(email, password)

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True , port=2000)

