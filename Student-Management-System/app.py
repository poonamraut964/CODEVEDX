from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)

app.secret_key = "student_secret_key"


# DATABASE CREATE
def init_db():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            age TEXT,
            course TEXT
        )
    ''')

    conn.commit()
    conn.close()


# HOME PAGE
@app.route('/')
def index():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students,
        edit_student=None
    )


# ADD STUDENT
@app.route('/add', methods=['POST'])
def add_student():

    roll = request.form['roll']
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO students(roll, name, age, course)
        VALUES (?, ?, ?, ?)
        ''',
        (roll, name, age, course)
    )

    conn.commit()
    conn.close()

    flash("Student Added Successfully!")

    return redirect('/')


# DELETE STUDENT
@app.route('/delete/<int:id>')
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    flash("Student Deleted Successfully!")

    return redirect('/')


# EDIT STUDENT
@app.route('/edit/<int:id>')
def edit_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    )

    edit_student = cursor.fetchone()

    conn.close()

    return render_template(
        "index.html",
        students=students,
        edit_student=edit_student
    )


# UPDATE STUDENT
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):

    roll = request.form['roll']
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE students
        SET roll=?, name=?, age=?, course=?
        WHERE id=?
        ''',
        (roll, name, age, course, id)
    )

    conn.commit()
    conn.close()

    flash("Student Updated Successfully!")

    return redirect('/')


if __name__ == "__main__":

    init_db()

    app.run(debug=True)
