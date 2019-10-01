from PyQt5.QtWidgets import *
import sys
import mysql.connector

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

########################################################
def main():
    App = QApplication(sys.argv)
    window=Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()