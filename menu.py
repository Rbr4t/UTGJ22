import pygame
import pygame_menu

def set_difficulty(value, difficulty):
    #print(value, difficulty)
    # Do the job here !
    pass

def game_options(sounds):
    # -------------------------------------------------------------------------
    # Create menus: settings
    # -------------------------------------------------------------------------
    options_theme = pygame_menu.themes.THEME_BLUE.copy()
    options_theme.widget_margin = (0, 0)

    game_options = pygame_menu.Menu(
        height=400,
        theme=options_theme,
        title='Seaded',
        width=600
    )


    game_options.add.range_slider('Muusika', 50, (0, 100), 1, onchange=lambda x : set_volume_power(sounds, x),
                                             rangeslider_id='range_slider',
                                             value_format=lambda x: str(int(x)))
    game_options.add.toggle_switch('Mute',0)
    game_options.add.selector('Dino värv',[('roheline',0), ('roosa',1)])
    game_options.add.vertical_margin(10)
    game_options.add.vertical_margin(30)
    game_options.add.button('Tagasi', pygame_menu.events.BACK)
    return game_options

def set_volume_power(sounds, new_value):
    for sound in sounds:
        print(sound)
        sound.set_volume(new_value/100)
    pygame.mixer.music.set_volume(new_value/100)
