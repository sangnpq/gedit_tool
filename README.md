# GEDIT TOOL
Small format XML and JSON tool for gedit

## Environment:
- Python 2.7
- sudo apt install python-lxml
- gedit enable Manage External Tools => following the tutorial: https://wiki.gnome.org/Apps/Gedit/Plugins/ExternalTools

## Setup
- gedit -> Tools -> Manage External Tools -> Add a new tool
- Rename New Tool to Format
- Shotcut key: Anything you want, for example: Shift + Ctrl + F
- Save: Nothing
- Input: Current document
- Ouput: Replace current document
- Code: copy all from new_tool.py

## Q&A
-Q: My gedit can't enable Manage External Tools, what can I do? (Ubuntu 18.04.2):
A: Install, if it isn't already, gir1.2-gtksource-3.0 package:
    sudo apt-get install gir1.2-gtksource-3.0
   Then give your user ownership over GEdit configuration directory:
    sudo chown YOUR_USERNAME /home/YOUR_USERNAME/.config/gedit
   Open GEdit and now you should be able to use External tools plugin.

