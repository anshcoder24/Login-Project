
from flask import Flask, render_template,request,flash,redirect,url_for

app = Flask(__name__)

app.config["SECRET_KEY"]="768jsh87ysjkh87sbjsr65s"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email=="admin@gmail.com" and password=="admin@123":
            flash("Login Success")
            return render_template("index.html")
        else:
            flash("Login Details is Invalid.")
            return render_template("login.html")

    return render_template("login.html")
@app.route("/profile")
def profile():
    return render_template("profile.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        print(fullname, email, password)

        return redirect(url_for("login"))

    return render_template("register.html")
    return "<h2>Register page</h2>"
@app.route("/logout")
def logout():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True , port=2000)

