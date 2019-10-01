''' 
01/10/2019 
Slawomir Sowa 

Application was created as a part of course Python GUI Programming Using PYQT5 from Udemy.
Simple Game Rock Paper Scissors 

'''


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

Textfont = QFont('Times', 16)
buttonsFont = QFont('Arial', 14)
computerScore = 0
playerScore = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Rock Papers Scissors Game')
        self.setGeometry(250,100,500,500)
        self.UI()

    def UI(self):

        ######### Scores #######

        self.scoreComputerText = QLabel('Computer Score : ', self)
        self.scoreComputerText.move(30,20)
        self.scoreComputerText.setFont(Textfont)
        self.scorePlayerText = QLabel('Your Score : ', self)
        self.scorePlayerText.move(300,20)
        self.scorePlayerText.setFont(Textfont)

        ######### BUTTONS ################
        btnStart = QPushButton('start', self)
        btnStart.move(160, 250)
        btnStart.clicked.connect(self.start) 

        btnStop = QPushButton('stop', self)
        btnStop.move(250, 250)
        btnStop.clicked.connect(self.stop)
   
        ######### Images #######
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap('images/paper.png'))
        self.imageComputer.move(60,80)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap('images/rock.png'))
        self.imagePlayer.move(300,80)

        self.imageGame = QLabel(self)
        self.imageGame.setPixmap(QPixmap('images/game.png'))
        self.imageGame.move(230,120)

        ######### TIMER #######
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.play)

        self.show()

    def play(self):
        # randint generates random numbers 
        self.rndComputer = randint(1,3)
        self.rndPlayer = randint(1,3)
        print (self.rndComputer,self.rndPlayer ) # print numbers in terminal 

        # by if elif else statement we assign images to numbers 
        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap('images/rock.png'))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap('images/paper.png'))
        else:
            self.imageComputer.setPixmap(QPixmap('images/scissors.png'))

        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap('images/rock.png'))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap('images/paper.png'))
        else:
            self.imagePlayer.setPixmap(QPixmap('images/scissors.png'))


    def start(self):
        self.timer.start()

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()   

        if self.rndComputer == 1 and self.rndPlayer == 1:
            mbox=QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer== 1 and self.rndPlayer == 2:
            mbox=QMessageBox.information(self,"Information","You Win")
            playerScore +=1
            self.scorePlayerText.setText("Your Score:{}".format(playerScore))
        elif self.rndComputer == 1 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore +=1
            self.scoreComputerText.setText("Computer Score:{}".format(computerScore))

        elif self.rndComputer == 2 and self.rndPlayer ==1:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score:{}".format(computerScore))
        elif self.rndComputer == 2 and self.rndPlayer ==2:
            mbox=QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer == 2 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score:{}".format(playerScore))

        elif self.rndComputer == 3 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score:{}".format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer ==2:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score:{}".format(computerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "Draw Game")

        if computerScore == 3 or playerScore ==3 :
            mbox=QMessageBox.information(self,"Information","Game Over")
            sys.exit()

def main():
    App = QApplication(sys.argv)
    window = Window()
    
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()