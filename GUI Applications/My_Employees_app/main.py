from PyQt5.QtWidgets import *
import sys
import sqlite3
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic, Qt



con = sqlite3.connect('employees.db')
cur = con.cursor()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450,150,750,600)
        self.UI()
        
        self.show()

    def UI(self):
        self.main_design()
        self.layouts()


    def main_design(self):
        self.employeeList=QListWidget()
        self.btnNew = QPushButton('New')
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate = QPushButton('Update')
        self.btnDelete = QPushButton('Delete')


    def layouts(self):
        ############# LAYOUTS #################
        self.mainLayout= QHBoxLayout()
        self.leftLayout= QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()

        ############# ADDING CHILD TO MAIN LAYOUT #################
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout,40)
        self.mainLayout.addLayout(self.rightMainLayout,60)
        ############# ADDING WIDGETS TO LAYOUT #################
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)


        ############# SETTING MAIN WINDOW LAYOUT #################

        self.setLayout(self.mainLayout)

    def addEmployee(self):
        self.newEmployee = AddEmployee() # that part of code transfer us to new Window ( new windows is created as new class)
        # self.close()


class AddEmployee(QMainWindow, QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('add_employee.ui', self) # adding UI from designer.exe
        
        self.setWindowTitle("Add Employees")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        
    
    def mainDesign(self):
        self.imgAdd.setPixmap(QPixmap('icons/person.png'))
        self.nameEntry.setPlaceholderText('Enter Employee Name')
        self.surnameEntry.setPlaceholderText('Enter Employee Surname')
        self.phoneEntry.setPlaceholderText('Enter Employee Phone Number')
        self.emailEntry.setPlaceholderText('Enter Employee email')
    




########################################################
def main():
    App = QApplication(sys.argv)
    window=Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()