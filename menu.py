import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("bae", icon="icon.png")
m.addMenu("Draw")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")
m.addMenu("Slate")
m.addCommand("Slate/slate", "nuke.createNode('slate')")
