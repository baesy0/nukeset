#coding:utf8
import os
from PySide2.QtWidgets import *

class test(QWidget):
	def __init__(self,text):
		super(test, self).__init__()
		self.Text = text
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.layout.addWidget(QLabel(self.Text))

def main():
	blah = "hello world"
	global w
	try:
		w.close()
	except:
		pass
	w = test(blah)
	try:
		w.show()
	except:
		pass
	
