from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
# Make sure QTableWidgetItem is added here ^
from random import randint
from pickle import load,dump
def play():
    ch=w.name.text()
    if verif(ch)==True:
        w.li.addItem(ch)
def select():
    f=open("enre.dat","ab")
    e=dict()
    if w.li.currentItem() != None:
        i=w.tab.rowCount()
        w.tab.insertRow(i)
        w.tab.setItem(i,0,QTableWidgetItem(w.li.currentItem().text()))
        x=generateid()
        w.tab.setItem(i,1,QTableWidgetItem(x))
        e["name"]=w.li.currentItem().text()
        e["id"]=x
        dump(e,f)
    f.close()
def generateid():
    c=""
    for i in range(11):
        if randint(1,2)==1:
            c=c+str(randint(0,9))
        else:
            c=c+chr(randint(ord("A"),ord("Z")))
    return c
    
def verif(ch):
    if len(ch)>1:
        return True
    else:
        return False
def res():
    w.name.clear()
    w.id.setText("generated id")
    w.li.clear()
    w.tab.clear()
    f=open("enre.dat","wb")
    f.close()
app = QApplication([])
w = loadUi ("lol.ui")
w.show()
w.add.clicked.connect (play)
w.res.clicked.connect (res)
w.se.clicked.connect (select)
app.exec()
