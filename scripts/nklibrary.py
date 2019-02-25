#coding:utf8
import os
import nuke
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class NKLibrary(QWidget):
	def __init__(self):
		super(NKLibrary, self).__init__()
		#variable
		self.libpath = os.getenv("NUKE_PATH")+"/nk/"
		self.appname = "Nuke Library"
		self.version = "v0.1"
		#widget
		self.nklist = QListWidget()
		self.addNKList()
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")
		#layout
		layout = QVBoxLayout()
		layout.addWidget(self.nklist)
		layout.addWidget(self.ok)
		layout.addWidget(self.cancel)
		self.setWindowTitle(self.appname+" "+self.version)
		self.setLayout(layout)
		#event
		self.ok.clicked.connect(self.pushOK)
		self.cancel.clicked.connect(self.close)
		self.nklist.itemClicked.connect(self.itemClick)
		
	def pushOK(self):
		nuke.nodePaste(self.libpath+self.currentItem)
		self.close()
	

	def itemClick(self, item):
		self.currentItem = item.text()
		nuke.tprint(self.currentItem)

	def addNKList(self):
		nkpath = os.getenv("NUKE_PATH") + "/nk"
		if not os.path.exists(nkpath):
			nuke.message(nkpath + "경로가 존재하지 않습니다")
		for i in os.listdir(nkpath):
			base, ext = os.path.splitext(i)
			if ext != ".nk":
				continue
			self.nklist.addItem(QListWidgetItem(i))


def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = NKLibrary()
	try:
		customApp.show()
	except:
		pass
