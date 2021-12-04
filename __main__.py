# Start the game
# included in pythonista
from scene import *
from ui import *

# python std
from pathlib import Path
from random import randint, seed

# project modules
from lib import game
from interface import Interface

HERE_FP = Path(__file__).parent

if __name__ == "__main__":
    iface = Interface()
    game_inst = game.Game()
  
    iface.run(game_inst)
