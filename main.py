import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QGridLayout, QLineEdit, QMainWindow,QPushButton,QTableWidget, QTableWidgetItem,QDialog,QComboBox
from PyQt6.QtGui import QAction
import sys,sqlite3
# from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Student Management System")


        # MENU BAR
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction("Add Student",self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About",self)
        help_menu_item.addAction(about_action)

        search_action = QAction("Search",self)
        search_action.triggered.connect(self.lookup)
        edit_menu_item.addAction(search_action)

        # MAIN WINDOW
        self.table = QTableWidget() 
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id","Name","Course","Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
    
    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def lookup(self):
        search_dialog = SearchDialog()
        search_dialog.exec()


class InsertDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        # student name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Enter Name")   
        layout.addWidget(self.student_name)

        # courses
        self.course_option = QComboBox()
        courses = ["Astronomy","Biology","Chemistry","Art","Social Sciences","Math"]
        self.course_option.addItems(courses)
        layout.addWidget(self.course_option)

        # phone
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("add phone no.")   
        layout.addWidget(self.phone)

        # execute button
        button = QPushButton("Add Record")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_option.itemText(self.course_option.currentIndex())
        phone = self.phone.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students(name,course,mobile) VALUES (?,?,?)",(name,course,phone))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


class SearchDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()

        search_input = QLineEdit()
        search_input.setPlaceholderText("type name to search..")

        search_button = QPushButton("Search")

        layout.addWidget(search_input)
        layout.addWidget(search_button)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())


