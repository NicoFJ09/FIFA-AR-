import pygame as pg
from var_consts import *

def pregame_screen(screen, Hfont, Field_drone, Field_lateral, Ubackground, seconds):
    global first_enter, Main_game_time
    if first_enter:
        Main_game_time = seconds
        first_enter = False
    
    time_elapsed = seconds - Main_game_time

    if time_elapsed < transition_duration:
        # Calculate the alpha value for fading out
        alpha = int(((transition_duration - time_elapsed) / transition_duration) * 255)
        Field_drone.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(Field_drone, (0, 0))
    
    elif time_elapsed < 2 * transition_duration:
        # Calculate the alpha value for fading in
        alpha = int(((time_elapsed - transition_duration) / transition_duration) * 255)
        Field_lateral.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(Field_lateral, (0, 0))
    
    elif time_elapsed < 3 * transition_duration:
        # Calculate the alpha value for fading out
        alpha = int(((2 * transition_duration - time_elapsed) / transition_duration) * 255)
        Ubackground.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(Ubackground, (0, 0))
