from PyQt5.QtWidgets import *
import sys, os
import sqlite3
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic, Qt
from PIL import Image


con = sqlite3.connect('employees.db')
cur = con.cursor()
defaultImg = 'person.png'
person_id = None
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
        self.displayFirstRecord()

    def main_design(self):
        self.setStyleSheet('font-size:14pt;font-family:Arial Bold;')
        self.employeeList=QListWidget()
        self.employeeList.itemClicked.connect(self.singleCLick)
        self.btnNew = QPushButton('New')
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updateEmployee)
        self.btnDelete = QPushButton('Delete')
        self.btnDelete.clicked.connect(self.deleteEmployee)
        
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

    def displayFirstRecord(self):
        query = 'SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1'
        employee = cur.execute(query).fetchone()
        
        img=QLabel()
        img.setPixmap(QPixmap('images/'+employee[5]))
        name=QLabel(employee[1])
        surname=QLabel(employee[2])
        phone=QLabel(employee[3])
        email=QLabel(employee[4])
        address=QLabel(employee[6])

        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow('',img)
        self.leftLayout.addRow('Name:',name)
        self.leftLayout.addRow('Surame:',surname)
        self.leftLayout.addRow('Phone:',phone)
        self.leftLayout.addRow('Email:',email)
        self.leftLayout.addRow('Address:',address)

    def singleCLick(self):

        for i in reversed(range(self.leftLayout.count())):
            widget = self.leftLayout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()

        employee = self.employeeList.currentItem().text()
        id = employee.split('-')[0]
        query=('SELECT * FROM employees WHERE id = ?') # question mark is for variable
        person = cur.execute(query,(id,)).fetchone()  # single item tuple = (1,)

        img=QLabel()
        img.setPixmap(QPixmap('images/'+person[5]))
        name=QLabel(person[1])
        surname=QLabel(person[2])
        phone=QLabel(person[3])
        email=QLabel(person[4])
        address=QLabel(person[6])

        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow('',img)
        self.leftLayout.addRow('Name:',name)
        self.leftLayout.addRow('Surame:',surname)
        self.leftLayout.addRow('Phone:',phone)
        self.leftLayout.addRow('Email:',email)
        self.leftLayout.addRow('Address:',address)

    def deleteEmployee(self):
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text() # outputts current value from QListWidget as string 
            ids = person.split('-')[0]
            mbox = QMessageBox.question(self, 'Warning','Are you sure to delete this person?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    
                    query = f'DELETE FROM employees WHERE id = {ids}'
                    cur.execute(query)
                    con.commit()
                    QMessageBox.information(self, 'Deleted!!','Person has been deleted')
                    self.close()
                    self.main = Main()
                except:
                    QMessageBox.information(self, 'Warning!!','Person has not been deleted')
        else:
            QMessageBox.information(self,'Warning!!!', 'Please select a person to delete')

    def updateEmployee(self):
        global person_id
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text()
            person_id = person.split('-')[0]
            print(person_id)
            self.updateWindow=UpdateEmployee()
            self.close()

        else:
            QMessageBox.information(self, 'Info','Please selcet person to update')    

class UpdateEmployee(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('update_employee.ui', self) # adding UI from designer.exe
        
        self.setWindowTitle("Update Employees")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        self.getPerson()
        self.mainDesign()
        

    def getPerson(self):
        global person_id

        query = f'SELECT * FROM employees WHERE id = {person_id}'
        employee = cur.execute(query).fetchone()
        print(employee)
        self.name = employee[1]
        self.surname = employee[2]
        self.phone = employee[3]
        self.email = employee[4]
        self.image = employee[5]
        self.address = employee[6]

    def mainDesign(self):
        
        self.imgAdd.setPixmap(QPixmap(f'images/{self.image}'))
        self.nameEntry.setText(self.name)
        self.surnameEntry.setText(self.surname)
        self.phoneEntry.setText(self.phone)
        self.emailEntry.setText(self.email)
        self.addressEditor.setPlainText(self.address)
        self.imgButton.clicked.connect(self.uploadImage)
        self.addButton.clicked.connect(self.updateEmployee )

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
    
    def updateEmployee(self):
        global defaultImg
        global person_id

        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText()

        if (name and surname and phone != ""):
            try:
                query="UPDATE employees set name =?, surname=?, phone=?,email=?,img=?,address=? WHERE id=?"
                cur.execute (query,(name,surname,phone,email,img,address,person_id))

                
                con.commit()
                QMessageBox.information(self,'Success', 'Person has been updated')
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self,'Warning', 'Person has NOT been updated')    
        else:
            QMessageBox.information(self,'Warning', 'Fields Can not be empty')

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