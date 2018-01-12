from flask import Flask, render_template, request
from model import Student, Course, searchs
from app import app

@app.route('/home', methods=['POST', 'GET'])
def home():
	if request.method == "POST":
		rows = searchs(request.form['search'])
		return render_template('searchstudent.html', rows = rows)
	else:
		return render_template('home.html')

@app.route('/studentlist')
def displayStudents():
	all_students = Student.all()
	return render_template('studentlist.html', rows = all_students)

@app.route('/courselist')
def displayCourses():
	all_courses = Course.all()
	return render_template('courselist.html', rows = all_courses)

@app.route('/addstudent', methods=['GET', 'POST'])
def adds():
    if request.method == "POST":
        student = Student(IDnum=request.form['idn'], firstName=request.form['fname'], middleName=request.form['mname'], lastName=request.form['lname'], Sex=request.form['sex'], Course=request.form['c'])
        student.add_student()
        return render_template('home.html')
    else:
    	return render_template('addstudent.html')

@app.route('/addcourse', methods=['POST', 'GET'])
def addc():
	if request.method == 'POST':
		course = Course(request.form['cid'], request.form['cname'])
		course.add_course()
		return render_template('home.html')
	else:
		return render_template('addcourse.html')

@app.route('/updatestudent', methods=['GET', 'POST'])
def updates():
	if request.method == "POST":
		student = Student(IDnum=request.form['idn'], firstName=request.form['fname'], middleName=request.form['mname'], lastName=request.form['lname'], Sex=request.form['sex'], Course=request.form['c'])
		student.update_student()
		return render_template('home.html')
	else:
		return render_template('updatestudent.html')

@app.route('/updatecourse', methods=['POST', 'GET'])
def updatec():
	if request.method == 'POST':
		course = Course(request.form['cid'], request.form['cname'])
		course.update_course()
		return render_template('home.html')
	else:
		return render_template('updatecourse.html')

@app.route('/delstudent', methods=['GET', 'POST'])
def dels():
	if request.method == "POST":
		student = Student(request.form['idn'], '', '', '', '', '')
		student.delete_student()
		return render_template('home.html')
	else:
		return render_template('delstudent.html')

@app.route('/delcourse', methods=['GET', 'POST'])
def delc():
	if request.method == "POST":
		course = Course(request.form['cid'], '')
		course.delete_course()
		return render_template('home.html')
	else:
		return render_template('delcourse.html')


if __name__ == '__main__':
	app.run(debug=True)