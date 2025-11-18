import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from Application.Application import Application

app = Application()

app.build()
app.run()

