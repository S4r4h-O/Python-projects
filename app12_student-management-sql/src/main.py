import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QTableWidget, QWidget, QApplication, QGridLayout, QLabel, QLineEdit, 
                             QLabel, QPushButton, QMainWindow)


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student management system")
        
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.setCentralWidget(self.table)

    def load_data(self):
        self.table


app = QApplication(sys.argv)
management_system = MainWindows()
management_system.show()
sys.exit(app.exec())
