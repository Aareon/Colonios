from ui import *

from pathlib import Path
from random import randint, seed

HERE_FP = Path(__file__).parent
IFACE_FP = HERE_FP / "interface/"

# All `.pyui` files were generated using the UI editor built-in to Pythonista


class MainMenu(View):
  """Custom class in main_menu.pyui"""
    def __init__(self):
        super().__init__()


class Interface(View):
    """Master view and interface controller for the game"""
    def __init__(self, game_inst):
        super().__init__()

        self.game_inst = game_inst

        self.main_menu = ui.load_view(str(IFACE_FP / "main_menu"))
        self.new_game_menu = ui.load_view(str(IFACE_FP / "new_game"))
        self.toolbar = ui.load_view(str(IFACE_FP / "toolbar"))
    
    def run(self):
        self.present('fullscreen', hide_title_bar=True if DEBUG else False)
    
    def show_menu(self, menu):
        # menu is a view as loaded in `self.__init__`
        if menu not in self.subviews:
            self.add_subview(menu)
        else:
            self.bring_to_front(menu)
    
    def new_game(self, opts: Dict):
        self.game_view = SceneView(frame=(0, 0, *ui.get_screen_size()))
        self.game_inst.iface = self
        self.add_subview(self.game_view)

        self.add_subview(self.toolbar)

    def quit(self):
        self.close()
