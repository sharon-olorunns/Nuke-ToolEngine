import nuke
import os

import ToolEngine.src.toolengine as toolengine
import ToolEngine.src.toolhelper as helper

logo = os.path.normpath(os.path.join(os.path.dirname(__file__), "ToolEngine", "img", "logo.png"))

# build menu
te_menu = nuke.menu("Nodes").addMenu("ToolEngine", icon=logo)
te_menu.addCommand("reload", helper.reload_tools_menu, "Alt+R")
te_menu.addCommand("add toolset...", toolengine.add_toolset)
te_menu.addCommand("settings...", toolengine.show_settings)
te_menu.addCommand("info...", toolengine.show_info)
te_menu.addSeparator()

# load the tools
helper.load_tools()

