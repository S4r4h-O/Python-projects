import sys
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (QComboBox, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QApplication, QGridLayout, 
                             QLabel, QLineEdit, QLabel, QPushButton, QMainWindow, QToolBar)


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student management system")
        self.setMinimumSize(800, 600)

        # Add tabs
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        # Add actions to each tab 
        add_student_action = QAction(QIcon("assets/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert_student)
        file_menu_item.addAction(add_student_action)

        search_students_action = QAction(QIcon("assets/search.png"), "Search names", self)
        search_students_action.triggered.connect(self.search_student)
        edit_menu_item.addAction(search_students_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_students_action)

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

    def insert_student(self):
        dialog = InsertDialog()
        dialog.exec()

    def search_student(self):
        dialog = SearchDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert student data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
       
        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile widget 
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText((self.course_name.currentIndex()))
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", 
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        management_system.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search for a name")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.search_name = QLineEdit()
        self.search_name.setPlaceholderText("Name")
        layout.addWidget(self.search_name)

        button = QPushButton("Search")
        button.clicked.connect(self.search_students_db)
        layout.addWidget(button)

        self.setLayout(layout)

    def search_students_db(self):
        name = self.search_name.text()
        pattern = f"%{name}%"
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name LIKE ?", (pattern,))
        rows = list(result)
        print(rows)
        items = management_system.table.findItems(name, Qt.MatchFlag.MatchContains)
        for item in items:
            print(item)
            management_system.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


app = QApplication(sys.argv)
management_system = MainWindows()
management_system.show()
management_system.load_data()
sys.exit(app.exec())
