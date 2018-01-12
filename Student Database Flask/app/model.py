import sqlite3

sqlite = sqlite3.connect('studentdbflask.db', check_same_thread=False)

print "Database created"

sqlite.execute('CREATE TABLE IF NOT EXISTS studentdata (idnum TEXT PRIMARY KEY, firstname TEXT NOT NULL, middlename TEXT NOT NULL, lastname TEXT NOT NULL, sex TEXT NOT NULL, courseid INTEGER NOT NULL, FOREIGN KEY(courseid) REFERENCES courses(cid) ON DELETE CASCADE ON UPDATE CASCADE)')

print "Student Table created"

sqlite.execute('CREATE TABLE IF NOT EXISTS courses (cid INTEGER PRIMARY KEY, coursename TEXT NOT NULL)')

print "Course Table created"

cursor = sqlite.cursor()

class Student(object):
	def __init__(self, IDnum, firstName, middleName, lastName, Sex, Course):
		self.fname = firstName
		self.mname = middleName
		self.lname = lastName
		self.idnum = IDnum
		self.sex = Sex
		self.course = Course


	def add_student(self):
		add = [self.idnum, self.fname, self.mname, self.lname, self.sex, self.course]
		item = [self.course]
		cursor.execute('SELECT * FROM courses WHERE cid = ?', item)
		row = cursor.fetchall()
		for row in row:
			print row
		if row != []:
			cursor.execute('INSERT INTO studentdata VALUES (?, ?, ?, ?, ?, ?)', add)
			sqlite.commit()
			print "Added Successfully!"
		else:
			print "Course Invalid!"

	def update_student(self):
		update = [self.fname, self.mname, self.lname, self.sex, self.course, self.idnum]
		cursor.execute('UPDATE studentdata SET firstname = ?, middlename = ?, lastname = ?, sex = ?, courseid = ? WHERE idnum = ?', update)
		sqlite.commit()
		print "Updated Sucessfully!"

	def delete_student(self):
		delete = [self.idnum]
		cursor.execute('DELETE FROM studentdata WHERE idnum = ?', delete)
		sqlite.commit()
		print "Deleted Successfully!"


	@classmethod
	def all(cls):
		cursor.execute('SELECT * FROM studentdata')
		studentList = cursor.fetchall()
		return studentList



class Course(object):
	def __init__(self, courseid, coursename):
		self.cid = courseid
		self.cname = coursename

	def add_course(self):
		add = [self.cid, self.cname]
		cursor.execute('INSERT INTO courses VALUES (?, ?)', add)
		sqlite.commit()
		print "Added Successfully!"

	def update_course(self):
		update = [self.cname, self.cid]
		cursor.execute('UPDATE courses SET coursename = ? WHERE cid = ?', update)
		print "Updated Successfully!"

	def delete_course(self):
		delete = [self.cid]
		cursor.execute('DELETE FROM courses WHERE cid = ?', delete)

	@classmethod
	def all(cls):
		cursor.execute('SELECT * FROM courses')
		courseList = cursor.fetchall()
		return courseList


def searchs(item):
	search = [item, item, item, item, item, item]
	cursor.execute('SELECT * FROM studentdata WHERE idnum = ? OR firstname = ? OR middlename = ? OR lastname = ? OR sex = ? OR courseid = ?', search)
	searchresult = cursor.fetchall()
	return searchresult
