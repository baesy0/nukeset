import nuke
import nukescripts

tb = nuke.toolbar("Nodes")
m = tb.addMenu("bae", icon="icon.png")
m.addMenu("Draw")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")
m.addCommand("Draw/slate", "nuke.createNode('slate')")
m.addCommand("Draw/slate_jonas", "nuke.createNode('slate_jonas')")


mb = menubar.addMenu("BAE")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/lazypic/nuke/issues')")
mb.addCommand("-","","")
mb.addCommand("StartPerformanceTimers", "nuke.startPerformanceTimers()")
mb.addCommand("StopPerformanceTimers", "nuke.stopPerformanceTimers()")
mb.addCommand("-","","")
# mb.addCommand("", "")

