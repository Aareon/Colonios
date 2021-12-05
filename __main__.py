# Start the game
# included in pythonista
from scene import *
from ui import *

# python std
from pathlib import Path
from random import randint, seed

# project modules
from lib.game import Game
from lib.interface import Interface

HERE_FP = Path(__file__).parent

if __name__ == "__main__":
    iface = Interface()
  
    iface.run()
