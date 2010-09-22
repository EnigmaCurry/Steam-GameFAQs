from paste.script.command import run
import shlex

run(shlex.split("serve app.ini"))

