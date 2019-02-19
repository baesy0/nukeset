#coding:utf8
import os
import nuke

def main():
	nuke.message("""$USER : %s\n
					$OCIO : %s\n
					$NUKE_PATH : %s\n
					$NUKE_FONT_PATH : %s"""
					% (os.environ['USER'],
					os.environ['OCIO'],
					os.environ['NUKE_PATH'],
					os.environ['NUKE_FONT_PATH'])
				)


