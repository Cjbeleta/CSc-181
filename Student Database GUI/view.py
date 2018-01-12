from Tkinter import *
from model import *

connector = sqlite3.connect('studentdb.db')

#database
database = 'studentdb'

#view and controller

class mainWindow(object):

    def __init__(self):
        self.main = Tk()
        self.main.title("Student Database")
        self.main.minsize(width = 100, height = 50)
        self.searchOption = IntVar()
        self.searchOption.set(1)
        self.entrySearch = Entry(self.main)
        self.entrySearch.pack(side = LEFT)
        self.fn = None
        self.mn = None
        self.ln = None
        self.idn = None
        self.co =None
        self.sel_id = None
        self.Search = None
        colNum = 0
        for mode in ["ID Number", "Name", "Course"]:
            colNum = colNum + 1
            button = Radiobutton(
                self.main,
                text = mode,
                variable = self.searchOption,
                value = colNum,
                indicatoron = 1
                ).pack(side = LEFT)
        self.buttonSearch = Button(
            self.main,
            text = "Search",
            command = self.search).pack(side = LEFT)
        self.buttonAdd = Button(
            self.main,
            text = "Add Student",
            command = self.add).pack(side = LEFT)
        self.buttonSort = Button(
        	self.main,
        	text = "Sort by ID Number",
        	command = self.sortdb).pack(side = LEFT)
        self.displayAll = Button(
        	self.main,
        	text = "Student List",
        	command = self.displayStudents).pack(side = LEFT)

    def sortdb(self):
    	self.studentSort = Student(" ", " ", " ", " ", " ", database, " ", " ")
    	self.studentSort.sort()

    def displayStudents(self):
    	self.show = Tk()
    	self.show.title("Student List")
    	self.show.minsize(width = 300, height = 200)
    	self.listAll = Listbox(self.show)
    	self.listAll.pack(fill = X)
    	self.listAll.insert(0, "ID Number     Name     Course")
    	self.studentDisplay = Student(" ", " ", " ", " ", " ", database, " ", " ")
    	self.completeList = self.studentDisplay.showall()
    	for self.row in self.completeList:
    		self.listAll.insert(END, self.row)

    def add(self):
        self.add = Tk()
        self.add.title("Add Student")
        self.add.minsize(width = 250, height = 150)
        self.add.maxsize(width = 250, height = 300)
        self.labelFN = Label(self.add,
            text = "First Name: ").pack()
        self.entryFN = Entry(self.add)
        self.entryFN.pack()
        self.labelMN = Label(self.add,
            text = "Middle Name: ").pack()
        self.entryMN = Entry(self.add)
        self.entryMN.pack()
        self.labelLN = Label(self.add,
            text = "Last Name: ").pack()
        self.entryLN = Entry(self.add)
        self.entryLN.pack()
        self.labelIDN = Label(self.add,
            text = "ID Number: ").pack()
        self.entryIDN = Entry(self.add)
        self.entryIDN.pack()
        self.labeC = Label(self.add,
            text = "Course: ").pack()
        self.entryC = Entry(self.add)
        self.entryC.pack()
        self.addbutton = Button(self.add,
            text = "Add", command = self.getEntriesAndAdd).pack()

    def getEntriesAndAdd(self):
        self.fn = self.entryFN.get()
        self.mn = self.entryMN.get()
        self.ln = self.entryLN.get()
        self.idn = self.entryIDN.get()
        self.co = self.entryC.get()
        self.studentAdd = Student(self.fn, self.mn, self.ln, self.idn, self.co, database, self.searchOption.get(), self.Search)
        self.studentAdd.insert_data()
        #self.studentAdd.check()
        self.add.destroy()

    def update(self):
        print "Heyyyy"
        self.update = Tk()
        self.update.title("Update Student Data")
        self.update.minsize(width = 250, height = 150)
        self.update.maxsize(width = 250, height = 300)

        self.labelFN = Label(self.update,
            text = "First Name: ").pack()
        self.entryNewFN = Entry(self.update)
        self.entryNewFN.pack()
        self.labelNewMN = Label(self.update,
            text = "Middle Name: ").pack()
        self.entryNewMN = Entry(self.update)
        self.entryNewMN.pack()
        self.labelNewLN = Label(self.update,
            text = "Last Name: ").pack()
        self.entryNewLN = Entry(self.update)
        self.entryNewLN.pack()
        self.labelNewIDN = Label(self.update,
            text = "ID Number: ").pack()
        self.entryNewIDN = Entry(self.update)
        self.entryNewIDN.pack()
        self.labeNewC = Label(self.update,
            text = "Course: ").pack()
        self.entryNewC = Entry(self.update)
        self.entryNewC.pack()

        self.updatebutton = Button(self.update,
            text = "Update", command = self.getUpdates).pack()

    def search(self):
        self.search = Tk()
        self.search.title("Search Student")
        self.search.minsize(width = 350, height = 150)
        self.Search = self.entrySearch.get()
        self.studentSearch = Student(" ", " ", " ", " ", " ", database, self.searchOption.get(), self.Search)
        self.list = Listbox(self.search, selectmode = SINGLE)
        self.list.pack(fill = X)
        self.updateButton = Button(self.search, text = "Update Student Data", command = self.update).pack(side = LEFT)
        self.deleteButton = Button(self.search, text = "Delete Student", command = self.delete).pack(side = LEFT)
        self.closeButton = Button(self.search, text = "Close", command = self.destroySearchWindow).pack(side = LEFT)
        self.list.insert(0, "ID Number   Name   Course")
        for self.element in self.studentSearch.search_data():
        	self.list.insert(END, self.element)
        if self.list.get(1) == []:
        	self.list.insert(1, "NO MATCH FOUND")
        else:
        	self.list.select_set(1)
        	self.list.bind("<<ListboxSelect>>", self.setSelID)

    def destroySearchWindow(self):
    	self.search.destroy()

    def setSelID(self, event):
    	self.selected = self.list.curselection()
    	self.sel_id = self.list.get(self.selected)

    def getUpdates(self):
        self.fn = self.entryNewFN.get()
        self.mn = self.entryNewMN.get()
        self.ln = self.entryNewLN.get()
        self.idn = self.entryNewIDN.get()
        self.co = self.entryNewC.get()
        self.studentUpdate = Student(self.fn, self.mn, self.ln, self.idn, self.co, database, self.searchOption.get(), self.sel_id[0])
        self.studentUpdate.update_data()
        self.update.destroy()

    def delete(self):
    	self.studentDelete = Student(" ", " ", " ", " ", " ", database, " ", self.sel_id[0])
    	self.studentDelete.delete_data()
    	self.list.delete(0, END)
        self.search.destroy()


    def display(self):
        self.main.mainloop()