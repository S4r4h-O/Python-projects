import sys
import sqlite3
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QTableWidget, QTableWidgetItem, QWidget, QApplication, QGridLayout, QLabel, QLineEdit, 
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
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        
        self.table.setRowCount(0)
        # Row data is the columns of the table (tuples)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            # Data are the values of each column (tuples)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()


app = QApplication(sys.argv)
management_system = MainWindows()
management_system.show()
management_system.load_data()
sys.exit(app.exec())
