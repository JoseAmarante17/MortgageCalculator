'''
Author:Jose Amarante
Date: 5/27/2021
Purpose: A gui interface that tells you your monthly mortage payment
'''
# IMPORTS DIFFERENT MODULE
from typing import Counter
from PyQt5 import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# INITALIZES WINDOW
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(0, 0, 500, 500)
win.setWindowTitle("Mortgage Calculator")
win.setStyleSheet("background-color:white;")
win.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                   QtCore.Qt.WindowMinimizeButtonHint)
win.setFixedSize(600, 450)
win.setWindowIcon(QtGui.QIcon('folder_home.png'))


def inputs():
    # FONT
    font = QFont("Arial", 15)
    font.setItalic(True)
    # LABELS ON THE SCREEN AND TEXT BOXES
    # HEADING

    heading = QLabel(win)
    heading.setText("MORGAGE CALCULATOR     ")
    heading.setFont(font)
    heading.adjustSize()
    heading.setStyleSheet(
        "border-width: 2px; border-style: solid; border-color:none none BLACK none; color:white;Font-Weight:Bold;Background-color:#2e86c1; padding: 1px;border-radius:5px;")
    heading.move(190, 20)

    # PRICE
    label1 = QLabel(win)
    label1.setText("\t          Price $")
    label1.setFont(QFont("Arial", 12))
    label1.adjustSize()
    label1.setAlignment(QtCore.Qt.AlignRight)
    label1.move(100, 60)
    label1.setStyleSheet("color:#2e86c1;Font-Weight:Bold;")
    priceInput = QLineEdit(win)
    priceInput.setStyleSheet("color:#2e86c1;Font-Weight:Bold;Font-Size:11pt;")
    priceInput.resize(200, 30)
    priceInput.move(260, 50)
    priceInput.setText("0")

    # TERM
    label2 = QLabel(win)
    label2.setText(" \t      Term (In Years) ")
    label2.setFont(QFont("Arial", 12))
    label2.setAlignment(QtCore.Qt.AlignRight)
    label2.setStyleSheet("color:#2e86c1;Font-Weight:Bold;")
    label2.move(100, 100)
    label2.adjustSize()
    termInput = QLineEdit(win)
    termInput.setStyleSheet("color:#2e86c1;Font-Weight:Bold;Font-Size:11pt;")
    termInput.resize(200, 30)
    termInput.move(260, 100)
    termInput.setText("0")

    # INTRERST
    label3 = QLabel(win)
    label3.setText(" \t Annual Interest % ")
    label3.setFont(QFont("Arial", 12))
    label3.setAlignment(QtCore.Qt.AlignRight)
    label3.setStyleSheet("color:#2e86c1;Font-Weight:Bold;")
    label3.move(100, 150)
    label3.adjustSize()
    interestInput = QLineEdit(win)
    interestInput.resize(200, 30)
    interestInput.setStyleSheet(
        "color:#2e86c1;Font-Weight:Bold;Font-Size:11pt;")
    interestInput.move(260, 150)
    interestInput.setText("0")

    # DOWN PAYMENT
    label4 = QLabel(win)
    label4.setText(" \t\t Down Payment $ ")
    label4.setFont(QFont("Arial", 12))
    label4.setAlignment(QtCore.Qt.AlignRight)
    label4.setStyleSheet("color:#2e86c1;Font-Weight:Bold;")
    label4.adjustSize()
    label4.move(100, 200)
    downInput = QLineEdit(win)
    downInput.resize(200, 30)
    downInput.setStyleSheet("color:#2e86c1;Font-Weight:Bold;Font-Size:11pt;")
    downInput.move(260, 200)
    downInput.setText(f"{0}")

    # MONTHLY PAYMENT
    label5 = QLabel(win)
    label5.setText("\t \t\t   Monthly Payment ")
    label5.setFont(QFont("Arial", 12))
    label5.setAlignment(QtCore.Qt.AlignRight)
    label5.adjustSize()
    label5.setStyleSheet("color:#2e86c1;Font-Weight:Bold;")
    label5.move(100, 250)
    paymentOutput = QLineEdit(win)
    paymentOutput.setReadOnly(True)
    paymentOutput.resize(200, 30)
    paymentOutput.setStyleSheet(
        "color:#2e86c1;Font-Weight:Bold;Font-Size:11pt;background : rgba(70, 70, 70, 35);")
    paymentOutput.move(260, 250)
    paymentOutput.setText(f"${0:,.2f}")

    # PAYMENTS LEFT
    label6 = QLabel(win)
    label6.setText("\t \t\t      Total Payments")
    label6.setFont(QFont("Arial", 12))
    label6.setAlignment(QtCore.Qt.AlignRight)
    label6.adjustSize()
    label6.setStyleSheet("color:#2e86c1;Font-Weight:Bold;")
    label6.move(100, 300)
    left = QLineEdit(win)
    left.setReadOnly(True)
    left.resize(200, 30)
    left.setStyleSheet(
        "color:#2e86c1;Font-Weight:Bold;Font-Size:11pt;background : rgba(70, 70, 70, 35);")
    left.move(260, 300)
    left.setText("0")
    # PASSES VALUES INTO METHOD
    # BUTTONS
    button1 = QPushButton(win)
    button1.setText("Calculate")
    button1.setGeometry(200, 200, 150, 40)
    button1.move(350, 350)
    button1.clicked.connect(lambda: calc(
        priceInput, termInput, interestInput, downInput, paymentOutput,left))
    button1.setStyleSheet("QPushButton::hover"
                          "{"
                          "background-color:blue;"
                          "}"
                          "QPushButton::pressed"
                          "{"
                          "background-color:green;"
                          "}"
                          "QPushButton"
                          "{"
                          "color:white;Font-Weight:Bold;Background-color:#2e86c1;"
                          "border-radius:15px;"
                          "font-size:15pt;"
                          "}"
                          )
    button2 = QPushButton(win)
    button2.setText("Clear")
    button2.setGeometry(200, 200, 150, 40)
    button2.move(150, 350)
    button2.clicked.connect(lambda: clears(
        priceInput, termInput, interestInput, downInput, paymentOutput,left))
    button2.setStyleSheet("QPushButton::hover"
                          "{"
                          "background-color:blue;"
                          "}"
                          "QPushButton::pressed"
                          "{"
                          "background-color:green;"
                          "}"
                          "QPushButton"
                          "{"
                          "color:white;Font-Weight:Bold;Background-color:#2e86c1;"
                          "border-radius:15px;"
                          "font-size:15pt;"
                          "}"
                          )


def calc(priceInput, termInput, interestInput, downInput, paymentOutput,left):
    # INPUT VARIABLES
    price = float(priceInput.text())
    term = int(termInput.text())
    interest = eval(interestInput.text())
    downPyt = eval(downInput.text())

    # CALCULATIONS
    priceAfterDown = price - downPyt
    interest = ((interest/12)/100)
    termLoan = term*12
    total = 0
    time=0
    # FINALY CALC
    try:
        total = priceAfterDown * interest * \
            (((1+interest)**termLoan)/(((1+interest)**termLoan)-1))
        time = priceAfterDown/ total
    except:
        if price == 0:
            # INITS MESSAGE BOX
            messageBox()

        elif term == 0:
            messageBox()

        elif interest == 0:
            messageBox()

        elif downPyt == 0:
            messageBox()
        else:
            print("")

    paymentOutput.setText((f"${format(total, ',.2f')}"))
    # NUMBER OF PAYMENTS LEFT

    left.setText(f"{time:.0f}")



def clears(priceInput, termInput, interestInput, downInput, paymentOutput,left):
    priceInput.setText("0")
    termInput.setText("0")
    interestInput.setText("0")
    downInput.setText("0")
    paymentOutput.setText(f"${0:,.2f}")
    left.setText("0")


def messageBox():
    # INITS MESSAGE BOX
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    # CONTENTS OF MESSAGE BOX
    msg.setWindowTitle("Important Information")
    msg.setText("Invalid Information")
    msg.setInformativeText("Please Fill out All fields")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()


def main():
    inputs()
    win.show()
    sys.exit(app.exec())


main()
