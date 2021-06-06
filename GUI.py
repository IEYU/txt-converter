from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow, QLabel, QLineEdit, QMessageBox, QWidget, QPushButton
import sys

import os
from pathlib import Path
import subprocess
                    
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Txt Decoder'
        self.left = 600
        self.right = 300
        self.height = 300
        self.width = 300
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.width, self.height)
        
        self.button1 = QPushButton('Single File', self)
        self.button2 = QPushButton('Multiple Files', self)
        self.button1.resize(200,70)
        self.button2.resize(200,70)
        self.button1.move(50,50)
        self.button2.move(50,150)
        
        self.button1.clicked.connect(self.single)
        self.button2.clicked.connect(self.multi)
        self.show()
    
    def single(self):
        
        self.textbox = QLineEdit(self)
        self.textbox.move(50,20)
        self.textbox.resize(200,40)
        
        file, result = QInputDialog.getText(self, "Single File Mode", "Enter the file name:")
        if result:
            file += '.txt'
        
        decoded = file[:-4] + ' decoded'
        
        os.system('iconv -c -f GB2312 -t UTF-8 %s >> %s' % (file, file[:-4]))
        os.makedirs(decoded)
        os.system("mv %s '%s'" % (file[:-4],decoded))
    
    def multi(self):    
        self.textbox = QLineEdit(self)
        self.textbox.move(50,20)
        self.textbox.resize(200,40)
        
        folder, result = QInputDialog.getText(self, "Multiple File Mode", "Enter the name of the folder that contains all the files:")
                
        folder_path = os.path.abspath(folder)
        os.chdir(folder_path)

        new_dir = 'the decoded files'

        file_list = [elem for elem in os.listdir(folder_path) if ".txt" in elem]

        os.makedirs(new_dir)
        for elem in file_list:
            new_name = str(elem)[:-4]
            os.system('iconv -c -f GB2312 -t UTF-8 %s >> %s' % (elem, (elem[:-4])))
            os.system("mv %s '%s'" % (elem[:-4], new_dir))
        
app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
