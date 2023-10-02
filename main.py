import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QGridLayout, QLineEdit, QMainWindow,QPushButton,QTableWidget
from PyQt6.QtGui import QAction
import sys
# from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Student Management System")


        # MENU BAR
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&help")

        add_student_action = QAction("Add Student",self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About",self)
        help_menu_item.addAction(about_action)

        # MAIN WINDOW
        self.table = QTableWidget() 
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id","Name","Course","Mobile"))
        self.setCentralWidget(self.table)
    


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())


