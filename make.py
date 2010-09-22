from bbfreeze import Freezer
import os
import sys
import shutil

## This will build a standalone exe version of the app
## Run on any windows machine, no python install necessary.


install_root = "target"
install_path = "steamgamefaqs"

# clean the target directory
if os.path.isdir(install_root):
    shutil.rmtree(install_root)

# The project needs to be built first
# (This seems REALLY cludgy)
sys.argv.append("build")
import setup

# This is also pretty cludgy, but I can't get bbfreeze to find all my 
# dependencies, so I have to explicitly set them here:
f = Freezer(os.path.join(install_root,install_path), includes=(
        "steamgamefaqs",
        "setuptools",
        "pylons",
        "pyquery",
        "anydbm",
        "dbhash",
        "paste",
        "paste.script",
        "Queue",
        "BaseHTTPServer",
        "xml.dom.minidom",
        "commands",
        "new",
        "xmlrpclib",
        "HTMLParser",
        "decimal",
        "json"))

f.addScript(os.path.join("scripts","go.py"))
f()

shutil.copyfile("development.ini",os.path.join(install_root,install_path,"app.ini"))
shutil.copyfile(os.path.join("scripts","run_server.bat"), os.path.join(install_root,"run_server.bat"))
