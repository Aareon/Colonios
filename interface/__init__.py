# Interface module
from ui import *
from pathlib import Path

HERE_FP = Path(__file__).parent
ROOT_FP = HERE_FP.parent


class MainMenu(View):

    def new_game_pressed(self, sender):
        self.superview.new_game()
    
    def quit(self, sender):
        self.trans_view = View()
        self.trans_view.background_color = '#2a2a2a'
        self.trans_view.alpha = 0.8
        self.trans_view.frame = self.superview.frame
        
        self.alert_view = load_view(str(HERE_FP / 'ui/alert'))
        self.superview.add_subview(self.trans_view)
        self.superview.add_subview(self.alert_view)
        self.alert_view.center = self.superview.frame.center()
        self.alert_view.wait_modal()
    
    def close_alert(self, sender):
        self.superview.remove_subview(self.alert_view)
        self.superview.remove_subview(self.trans_view)
    
    def quit(self, sender):
        self.superview.quit()


class NewGame(View):
    def __init__(self):
        super().__init__()
        
        self.iface = None
        
        self.menu_opt_seed = load_view(str(HERE_FP / 'menu_option_seed'))
        self.menu_opt_seed.width = self['scrollview1']['view2'].width
        
        self.menu_opt_map_size = load_view(str(HERE_FP / 'ui/menu_option_map_size'))
        self.menu_opt_map_size.width = self['scrollview1']['view2'].width

        self['scrollview1']['view1'].add_subview(self.menu_opt_map_size)

        self['scrollview1']['view2'].add_subview(self.menu_opt_seed)
    
    def back_pressed(self, sender):
        self.iface.bring_to_front(self.main_menu)
    
    def next_pressed(self, sender):
        self.iface.new_with_options({})
    
    def generate_new_seed(self, sender=None):
        with open(HERE_FP / 'words.txt') as f:
            words = f.read().splitlines()
            word = words[randint(0, len(words)-1)]
            if sender is None:
                return word
            else:
                sender.superview['view2']['seed_field']
    
    def toggle_map_size(self, sender):
        idx = sender.selected_index
        if idx == 1:
            sender.superview['textfield1'].text = '64'
            sender.superview['textfield2'].text = '64'


class Interface(View):
    def __init__(self):
        super().__init__()

        self.main_menu = load_view(str(HERE_FP / 'main_menu'))
        self.main_menu.iface = self
        self.add_subview(self.main_menu)
        
        self.new_game_menu = load_view(str(HERE_FP / 'new_game'))
        self.new_game_menu.iface = self
        
        self.add_subview(self.new_game_menu)

    
    def run(self):
        self.main_menu.bring_to_front()
        self.present('fullscreen', hide_title_bar=False)
    
    def new_game_pressed(self, sender):
        self.new_game_menu.bring_to_front()
    
    def quit(self):
        self.close()
    
    def new_with_options(self, opts):
        self.game = SceneView(frame=(0,0,*get_screen_size()))
        self.game.scene = Game()
        
        self.toolbar = load_view('ui/toolbar')
        self.add_subview(self.game)
        self.add_subview(self.toolbar)
    
    def show_game_settings(self, sender):
        self.game_settings = load_view('ui/game_settings')
        self.game_settings.center = self.frame.center()
        self.add_subview(self.game_settings)
    
    def quit_pressed(self, sender):
        self.remove_subview(self.game_settings)
        self.remove_subview(self.toolbar)
        self.remove_subview(self.game)
        self.game.close()
    
    def close_pressed(self, sender):
        self.remove_subview(self.game_settings)
