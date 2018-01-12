import sqlite3

#model
class Student (object):
    def __init__(self, firstName, middleName, lastName, IDNum, Course, db_file, option, search):
        self.fname = firstName
        self.mname = middleName
        self.lname = lastName
        self.idnum = IDNum
        self.course = Course
        self.opt = option
        self.srch = search
        self.matchrow = []
        try:
            self.conn = sqlite3.connect(db_file)
        except Exception as e:
            print(e)

        self.create_table_db_sorted = """ CREATE TABLE IF NOT EXISTS studentdata_sorted (
                                        id text PRIMARY KEY,
                                        firstname text NOT NULL,
                                        middlename text NOT NULL,
                                        lastname text NOT NULL,
                                        course text NOT NULL
                                        ); """
        
        create_table_db = """ CREATE TABLE IF NOT EXISTS studentdata (
                                        id text PRIMARY KEY,
                                        firstname text NOT NULL,
                                        middlename text NOT NULL,
                                        lastname text NOT NULL,
                                        course text NOT NULL
                                        ); """
        if self.conn is not None:
            try:
                self.c = self.conn.cursor()
                self.c.execute(create_table_db)

            except Exception as e:
                print(e)

    def update_data(self):
        updatedata = [self.idnum, self.fname, self.mname, self.lname, self.course, self.srch]
        self.c.execute("UPDATE studentdata SET id = ?, firstname = ?, middlename = ?, lastname = ?, course = ? WHERE id = ?", updatedata)
        self.conn.commit()

    def insert_data(self):
        insertdata = [self.idnum, self.fname, self.mname, self.lname, self.course]
        self.c.execute("INSERT OR IGNORE INTO studentdata VALUES (?, ?, ?, ?, ?)", insertdata)
        self.conn.commit()

    def search_data(self):
        if self.opt == 1:
        	self.c.execute("SELECT * FROM studentdata WHERE id = ?", (self.srch,))
        	self.rows = self.c.fetchall()
        	for self.row in self.rows:
        		self.matchrow.append(self.row)
        elif self.opt == 2:
        	namelist = [self.srch, self.srch, self.srch]
        	self.c.execute("SELECT * FROM studentdata WHERE firstname = ? OR middlename = ? OR lastname = ?", namelist)
        	self.rows = self.c.fetchall()
        	for self.row in self.rows:
        		self.matchrow.append(self.row)
        elif self.opt == 3:
            self.c.execute("SELECT * FROM studentdata WHERE course = ?", (self.srch,))
            self.rows = self.c.fetchall()
            for self.row in self.rows:
            	self.matchrow.append(self.row)
        return self.matchrow

    def delete_data(self):
    		self.c.execute("DELETE FROM studentdata WHERE id = ?", (self.srch,))
    		self.conn.commit()
    def check(self):
        for self.row in self.c.execute("SELECT * FROM studentdata"):
            print self.row

    def clear_table(self):
        self.c.execute("DROP TABLE IF EXISTS studentdata")

    def sort(self):
        self.c.execute(self.create_table_db_sorted)
        self.c.execute("SELECT * FROM studentdata ORDER BY id")
        self.rows = self.c.fetchall()
        for self.row in self.rows:
        	self.c.execute("INSERT INTO studentdata_sorted VALUES (?,?,?,?,?)", (self.row))
        self.conn.commit()
        self.c.execute("DROP TABLE IF EXISTS studentdata")
        self.c.execute("ALTER TABLE studentdata_sorted RENAME TO studentdata")

    def showall(self):
    	self.c.execute("SELECT * FROM studentdata")
    	self.rows = self.c.fetchall()
    	self.complete = []
    	for self.row in self.rows:
    		self.complete.append(self.row)
    	return self.complete