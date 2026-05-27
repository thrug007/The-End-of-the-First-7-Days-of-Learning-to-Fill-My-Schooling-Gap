from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
from pickle import load,dump
def play():
    f=open("eleve.dat","ab")
    ch=w.ch.text()
    n=w.n.text()
    e=dict()
    i=w.tab.rowCount()
    i=w.li.count()
    if verif(ch)==True and verif(n)==True:
        w.tab.insertRow(i)
        w.tab.setItem(i,0,QTableWidgetItem(ch))
        w.tab.setItem(i,1,QTableWidgetItem(n))
        e["nom"]=ch
        e["id"]=crt(ch)
        dump(e,f)
        w.li.addItem(crt(ch))
    f.close()
def crt(ch):
    return conv(ord(ch[0])+w.li.count(),16)
#i realised if i letted cript the same as it was in free1 it two peoples has the same name they will have the same id 
def conv(x,a):
    c=""
    while x!=0:
        if a==16:
            if x%a>9:
                c=chr(ord("A")+(x%a)-10)+c
                x=x//a
            else:
                c=str(x%a)+c
                x=x//a
        else:
            c=str(x%a)+c
            x=x//a
    return c
        
        
        
        
def verif(ch):
    i=0
    test=True
    while i<len(ch) and test==True:
        if "A"<=ch[i].upper()<="Z" or "0"<=ch[i].upper()<="9":
            i=i+1
        else:
            test=False
    return test
app = QApplication([])
w = loadUi ("free1v1.5.ui")
w.show()
w.bt1.clicked.connect (play)
app.exec()
