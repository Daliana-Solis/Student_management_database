import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QWidget,\
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        #Top nav bar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        #Sub items
        add_student_action = QAction("Add Student",self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)


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





app = QApplication(sys.argv)
student_mng = MainWindow()
student_mng.show()
student_mng.load_data()
sys.exit(app.exec())
