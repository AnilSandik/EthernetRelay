# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 15:17:13 2017

@author: Asus
"""

import sys
import time
import iprelay_gui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import socket


class Iprelay(QMainWindow,iprelay_gui.Ui_MainWindow):
    
    
    def __init__(self,parent=None):
        super(Iprelay,self).__init__(parent)
        self.setupUi(self)
        self.buttonLED1.clicked.connect(self.doled)
        self.buttonLED2.clicked.connect(self.doled)
        self.buttonLED3.clicked.connect(self.doled)
        self.buttonLED4.clicked.connect(self.doled)
        self.buttonLED5.clicked.connect(self.doled)
        self.buttonLED6.clicked.connect(self.doled)
        self.buttonLED7.clicked.connect(self.doled)
        self.buttonLED8.clicked.connect(self.doled)
        self.buttonConnect.clicked.connect(self.init)
        self.com = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.com.settimeout(5)
        self.groupBox.setEnabled(False)
        #self.com.connect(("10.70.24.34",23))
        
     
    def init(self):
        self.com.connect(("192.168.1.26",23))
        self.buttonConnect.setEnabled(False)
        self.groupBox.setEnabled(True)
        
    def doled(self):
        a = self.sender().objectName()
        
        if a=='buttonLED1':
            print "LED1 state is changed"
            self.com.send("Q\n")
        elif a=='buttonLED2':
            print "LED2 state is changed"
            self.com.send("W\n")
        elif a=='buttonLED3':
            print "LED3 state is changed"
            self.com.send("E\n")
        elif a=='buttonLED4':
            print "LED4 state is changed"
            self.com.send("R\n")
        elif a=='buttonLED5':
            print "LED5 state is changed"
            self.com.send("T\n")  
        elif a=='buttonLED6':
            print "LED6 state is changed"
            self.com.send("Y\n")    
        elif a=='buttonLED7':
            print "LED7 state is changed"
            self.com.send("U\n")
        elif a=='buttonLED8':
            print "LED8 state is changed"
            self.com.send("I\n")
 
        
app=QApplication(sys.argv)
form=Iprelay()
form.show()
app.exec_()
