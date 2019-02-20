#coding:utf8
import nuke
from PySide2.QtWidgets import *

class MakeWrite(QWidget):
	formats = ["2048x1152", "1920x1080", "2048x872"]
	exts = [".exr", ".dpx", ".jpg", ".mov"]

	def __init__(self):
		super(MakeWrite, self).__init__()
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")
		self.ext = QComboBox()
		self.ext.addItems(self.exts)
		self.fm = QComboBox()
		self.fm.addItems(self.formats)
		self.reformat = QCheckBox("&reformat", self)
		self.reformat.setChecked(True)
		self.slate = QCheckBox("&slate", self)
		self.slate.setChecked(True)
		self.tail = nuke.selectedNode()

		# event
		self.ok.clicked.connect(self.bt_ok)
		self.fm.currentIndexChanged.connect(self.indexChanged)
		self.cancel.clicked.connect(self.close)

		# layout
		layout = QGridLayout()
		layout.addWidget(self.reformat, 0, 0)
		layout.addWidget(self.fm, 0, 1)
		layout.addWidget(QLabel("Master Ext"), 1, 0)
		layout.addWidget(self.ext, 1, 1)
		layout.addWidget(self.slate, 2, 0)
		layout.addWidget(self.cancel, 3, 0)
		layout.addWidget(self.ok, 3,1)
		self.setLayout(layout)

	def indexChanged(self):
		self.reformatSize = self.fm.currentText()

	def bt_ok(self):
		if self.reformat.isChecked():
			reformat = nuke.nodes.Reformat()
			reformat["box_fixed"].setValue(True)
			reformat["type"].setValue("to box")
			width, height = self.fm.currentText().split("x")
			reformat["box_width"].setValue(int(width))
			reformat["box_height"].setValue(int(height))
#			reformat.setInput(0,self.tail)
#			self.tail = reformat
		if self.slate.isChecked():
			slate = nuke.nodes.slate()
#			slate.setInput(0, self.tail)
#			self.tail = slate

# write노드에 옵션 안들어가는 거 해결하기!
		write = nuke.nodes.Write()
		write["file_type"].setValue(self.ext.currentText[1:])
		write["file"].setValue("/test/test/####"+self.ext.currentText())
		write["create_directories"].setValue(True)
#		write.setInput(0, self.tail)


		self.close()

"""
	timecode = nuke.nodes.AddTimeCode()
	timecode["startcode"].setValue("01:00:00:00")
	timecode["useFrame"].setValue(True)
	timecode["frame"].setValue(1001)
	timecode.setInput(0, reformat)

	slate = nuke.nodes.slate()
	slate.setInput(0, timecode)

	w = nuke.nodes.Write()
	w["file_type"].setValue("exr")
	w["file"].setValue("/test/test.####.exr")
	w["create_directories"].setValue(True)
	w.setInput(0, slate)
"""
def main():
	nodes = nuke.selectedNodes()
	if len(nodes) != 1:
		nuke.message("노드를 하나만 선택하세요")
		return

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


