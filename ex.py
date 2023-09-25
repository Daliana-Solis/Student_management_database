from PyQt6.QtWidgets import QApplication, QGridLayout, QVBoxLayout, QLabel, QWidget,\
    QLineEdit

class AgeCalculator(QWidget):
    def __init__(self):
        grid = QGridLayout()
        name_label = QLabel("Name:")
        name_line_edit = QLineEdit()

        dob_label = QLabel("Date of Birth MM/DD/YYYY:")
        dob_line_edit = QLineEdit()

        #Add Widgets to the grid
        grid.addWidget(name_label, 0,0)
        grid.addWidget(name_line_edit, 0,1)
        grid.addWidget(dob_label, 1,0)
        grid.addWidget(dob_line_edit, 1,1)


age_calculator = AgeCalculator()

