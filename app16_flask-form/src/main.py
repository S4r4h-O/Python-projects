from os import getenv
from datetime import datetime
from dotenv import load_dotenv
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "pythoncourse"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["MAIL_SERVER"] = getenv("EMAIL_SERVER")
app.config["MAIL_PORT"] = int(465)
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USERNAME"] = getenv("EMAIL_ACCOUNT")
app.config["MAIL_PASSWORD"] = getenv("EMAIL_PASSWORD")

db = SQLAlchemy(app)

mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrive the form informations from the form tag
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        email = request.form["email"]
        date = request.form["date"]
        date = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body = f"""Thank you for your submission, {first_name}.
        Here's your data: {first_name}\n{last_name}\n{date}
        """
        message = Message(subject="New Form submission",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)
        mail.send(message)

        flash(f"{first_name}, your form was submitted successfully", "success")
   
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True, port=5001)
