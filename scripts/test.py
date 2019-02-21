#coding:utf8
import os
import nuke
from PySide2.QtWidgets import *

class WriteFormat(QWidget):
	def __init__(self):
		super(WriteFormat, self).__init__()
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")
		
		# event
		self.ok.clicked.connect(self.pushOK)
		self.cancel.clicked.connect(self.close)

		# layout
		layout = QGridLayout()
		layout.addWidget(self.cancel, 1, 0)
		layout.addWidget(self.ok,1 ,1)
		self.setLayout(layout)

		# node list
		self.linkOrder = []


	def genReformat(self):
		reformat = nuke.nodes.Reformat()
		reformat["box_fixed"].setValue(True)
		reformat["type"].setValue("to box")
		reformat["box_width"].setValue(int(nuke.selectedNode()["formate"].value().width()))
		reformat["box_height"].setValue(int(nuke.selectedNode()["formate"].value().height()))
		self.linkOrder.append(reformat)


	def genWrite(self):
		write = nuke.nodes.Write()
		dirname, basename = os.path.split(nuke.root().name())
		filename, notuse = os.path.splitext(basename)
		ext = str(self.ext.currentText())
		write["file_type"].setValue(ext[1:])
		write["file"].setValue("%s/out/%s/%s.####%s" % (dirname, filename, filename, ext))
		write["create_directories"].setValue(True)
		self.linkOrder.append(write)

	def linkNodes(self):
		"""
		linkOrder 노드 순서대로 노드를 연결, 생성한다.
		"""
		tail = nuke.selectedNode()
		for n in self.linkOrder:
			n.setInput(0, tail)
			tail = n
		
	def pushOK(self):
		"""
		OK버튼을 누르면 노드를 생성한다.
		"""
		self.genWrite()
		self.linkNodes()
		self.close()
			

def checkCondition():
	if nuke.root().name() == "Root":
		nuke.message("파일을 저장해주세요.")
		return

	if len(nuke.selectedNodes()) != 1:
		nuke.message("노드를 하나만 선택하세요")
		return

def main():
	checkCondition()
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = MakeWrite()
	try:
		customApp.show()
	except:
		pass


