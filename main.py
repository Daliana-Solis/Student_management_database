import sys
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QWidget,\
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout,\
    QComboBox
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        #Top nav bar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")


        #Sub items
        add_student_action = QAction("Add Student",self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        search_name = QAction("Search", self)
        edit_menu_item.addAction(search_name)
        search_name.triggered.connect(self.search)


        #Table
        self.table = QTableWidget()
        self.table.setColumnCount(4) #4 columns in our table
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False) #Hide vertical numbers for each row
        self.setCentralWidget(self.table) #Central widget



    def load_data(self):
        #Connect with sql database
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students") #extract from DB
        self.table.setRowCount(0) #Resets table, loads data as fresh

        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for colmn_num, data in enumerate(row_data):
                self.table.setItem(row_num, colmn_num, QTableWidgetItem(str(data)))
        connection.close()


    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        #Name Widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        #Course Widget
        self.course_name = QComboBox()
        courses = ["Biology", 'Math', "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        #Add Phone
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        #Submit button
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor() #adding
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?,?,?)",
                       (name, course, mobile))

        connection.commit() #Apply the sql statement
        cursor.close()
        connection.close()

        student_mng.load_data() #Reload data table showing update (new student)


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        #Add Phone
        self.search_student = QLineEdit()
        self.search_student.setPlaceholderText("Name")
        layout.addWidget(self.search_student)

        #Submit button
        button = QPushButton("Search")
        button.clicked.connect(self.search_name)
        layout.addWidget(button)

        self.setLayout(layout)

    def search_name(self):
        name = self.search_student.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM student WHERE name = ?" (name,))
        rows = list(result)
        items = student_mng.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            student_mng.table.item(item.row(),1).setSelected(True)

        cursor.close()
        connection.close()





app = QApplication(sys.argv)
student_mng = MainWindow()
student_mng.show()
student_mng.load_data()
sys.exit(app.exec())
