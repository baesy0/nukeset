#coding:utf8
import os
import sys
import subprocess
import nuke
import nukescripts

def browser(path):
	brws = "nautilus"
	if sys.platform == "win32":
		brws = "start"
	elif sys.platform == "darwin":
		brws = "open"
	p = subprocess.Popen([brws, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()
	if stderr:
		nuke.tprint(stderr, file=sys.stderr)
	if stdout:
		nuke.tprint(stdout)
#		os.system("%s %s" % (brws, os.path.dirname(path)))

def main():
	nodes = nuke.selectedNodes()
	if len(nodes) != 1:
		nuke.message("select one node only")
		return
	nuke.tprint(nodes[0])
	path = os.path.dirname(nodes[0]["file"].value())
	nuke.tprint(path)
	browser(path)
	return
