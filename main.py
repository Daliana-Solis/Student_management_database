import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QWidget,\
    QLineEdit, QPushButton, QMainWindow, QTableWidget

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
        self.setCentralWidget(self.table) #Central widget



    def load_data(self):
        self.table




app = QApplication(sys.argv)
student_mng = MainWindow()
student_mng.show()
sys.exit(app.exec())
