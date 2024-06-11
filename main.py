import os
import eel
from evo_back.features import *
from evo_back.command import *

def start():

    eel.init("evo_front")

    playEvoSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)
