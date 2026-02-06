from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)
app.app_context().push()

class Employee(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(200),nullable = False)
    email = db.Column(db.String(500), nullable = False)

@app.route("/")
def home():
    employee = Employee(name = "Diksha Sharma",email = "dikshasharma@gmail.com")
    db.session.add(employee)
    db.session.commit()
    allemployee = Employee.query.all()
    return render_template('index.html',allemployee = allemployee)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
