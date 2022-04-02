import pygame
import pygame_menu

def set_difficulty(value, difficulty):
    #print(value, difficulty)
    # Do the job here !
    pass

def game_options():
    # -------------------------------------------------------------------------
    # Create menus: settings
    # -------------------------------------------------------------------------
    game_options = pygame_menu.themes.THEME_BLUE.copy()
    game_options.widget_margin = (0, 0)

    game_options = pygame_menu.Menu(
        height=400,
        theme=game_options,
        title='Seaded',
        width=600
    )

    game_options.add.range_slider('Muusika', 50, (0, 100), 1,
                                             rangeslider_id='range_slider',
                                             value_format=lambda x: str(int(x)))
    game_options.add.selector('Dino värv',[('roheline',0), ('roosa',1)])
    game_options.add.vertical_margin(10)
    game_options.add.toggle_switch('Mute',0)
    game_options.add.vertical_margin(30)
    game_options.add.button('Tagasi', pygame_menu.events.BACK)
    return game_options
