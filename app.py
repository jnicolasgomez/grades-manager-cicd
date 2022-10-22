from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from service.calculateGrades import calculateFinalGrade, setGrade, getGrade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class ClassGrade(db.Model):
    grade = 0
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        notas = []
        notas.append(float(request.form['grade1']))
        notas.append(float(request.form['grade2']))
        notas.append(float(request.form['grade3']))
        notas.append(float(request.form['grade4']))
        ClassGrade.grade = calculateFinalGrade(notas)
        print(ClassGrade.grade)
        return redirect('/')
    if ClassGrade.grade:
        print('hello')
        return render_template('index.html', final = ClassGrade.grade)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)