from PyQt5.QtWidgets import *
import sys, os
import sqlite3
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic, Qt
from PIL import Image



con = sqlite3.connect('employees.db')
cur = con.cursor()
defaultImg = 'person.png'
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
        self.getEmployee()

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
        self.close()

    def getEmployee(self):
        query = 'SELECT id, name, surname FROM employees'
        employees = cur.execute(query).fetchall()
        
        for employee in employees:
            self.employeeList.addItem(str(employee[0])+'-'+employee[1]+' '+employee[2])

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

    def closeEvent (self, event):
        self.main = Main()  
    
    def mainDesign(self):
        self.imgAdd.setPixmap(QPixmap('icons/person.png'))
        self.nameEntry.setPlaceholderText('Enter Employee Name')
        self.surnameEntry.setPlaceholderText('Enter Employee Surname')
        self.phoneEntry.setPlaceholderText('Enter Employee Phone Number')
        self.emailEntry.setPlaceholderText('Enter Employee email')
        self.imgButton.clicked.connect(self.uploadImage)
        self.addButton.clicked.connect(self.addEmployee )
    
    def uploadImage(self):
        global defaultImg
        size = (128,128)
        # getOpenFileName from QFileDialog give us path to file as a string 
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '','Image Files (*.jpg *.png)')
        if ok:
            
            # code below allow to retreive file name from path. 
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size) # resize image 
            img.save(f'images/{defaultImg}')
    
    def addEmployee(self):
        global defaultImg
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText()

        if (name and surname and phone != ""):
            try:
                query = 'INSERT INTO employees (name, surname, phone, email, img, address) VALUES(?,?,?,?,?,?)'
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self,'Success', 'Person has been added')
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self,'Warning', 'Person has NOT been added')    
        else:
            QMessageBox.information(self,'Warning', 'Fields Can not be empty')

########################################################
def main():
    App = QApplication(sys.argv)
    window=Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()