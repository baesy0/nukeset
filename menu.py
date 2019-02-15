import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("bae")
m.addMenu("Draw")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")
