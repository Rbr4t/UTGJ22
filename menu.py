import pygame
import pygame_menu

def set_difficulty(value, difficulty):
    #print(value, difficulty)
    # Do the job here !
    pass

def game_options(sounds, dinoPath):
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

    last_value = pygame.mixer.music.get_volume()

    game_options.add.range_slider('Muusika', 50, (0, 100), 1, onchange=lambda x : set_volume_power(sounds, x, last_value),
                                             rangeslider_id='range_slider',
                                             value_format=lambda x: str(int(x)))
    game_options.add.toggle_switch('Mute',0, onchange=lambda x : set_mute_power(sounds, x, last_value))
    game_options.add.selector('Dino värv',[('roheline',0), ('roosa',1)], onchange=lambda x, index : change_dino_skin(x,index,dinoPath))
    game_options.add.vertical_margin(10)
    game_options.add.vertical_margin(30)
    game_options.add.button('Tagasi', pygame_menu.events.BACK)
    return game_options

def set_volume_power(sounds, new_value, last_value):
    for sound in sounds:
        sound.set_volume(new_value/100)
    pygame.mixer.music.set_volume(new_value/100)
    last_value = new_value

def set_mute_power(sounds, muted, last_value):
    if (muted):
        for sound in sounds:
            sound.set_volume(0)
        pygame.mixer.music.set_volume(0)
    else:
        for sound in sounds:
            sound.set_volume(last_value)
        pygame.mixer.music.set_volume(last_value)

def change_dino_skin(selectedItem, isPink, DinoPath):
    print(DinoPath)
    if (isPink):
        print("pink")
        DinoPath[0] = "Kunst/Dinos/Pink/"
    else:
        print("green")
        DinoPath[0] = "Kunst/Dinos/Green/"
    print(DinoPath)