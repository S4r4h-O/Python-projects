from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrive the form informations from the form tag
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]
    return render_template("index.html")













app.run(debug=True, port=5001)
