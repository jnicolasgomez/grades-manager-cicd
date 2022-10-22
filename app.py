from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from service.calculateGrades import calculateFinalGrade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class ClassGrade():
    grade = 0


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        notas = []
        notas.append(float(request.form['grade1']))
        notas.append(float(request.form['grade2']))
        notas.append(float(request.form['grade3']))
        notas.append(float(request.form['grade4']))
        ClassGrade.grade = calculateFinalGrade(notas)
        return redirect('/')
    if ClassGrade.grade:
        grade = ClassGrade.grade
        return render_template('index.html', final=grade)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
