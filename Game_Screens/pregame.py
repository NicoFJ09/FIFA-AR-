import pygame as pg
from var_consts import *
import random

# Randomly select text once
text_choice = random.choice(["Escudo: Tu turno", "Corona: Turno del contrincante"])

def pregame_screen(screen, Hfont, Field_drone, Field_lateral, Ubackground, coin_gif, corona, escudo, seconds):
    global first_enter, Main_game_time, text_choice
    if first_enter:
        Main_game_time = seconds
        first_enter = False

    time_elapsed = seconds - Main_game_time

    transition_duration = 1.5 # Duration of each transition (in milliseconds)
    countdown_duration = 3  # Duration of the countdown (in seconds)

    if time_elapsed < transition_duration:
        # Calculate the alpha value for fading out
        alpha_out = int((1 - time_elapsed / transition_duration) * 255)
        alpha_in = int((1 - time_elapsed / transition_duration) * 255)
        Field_drone.set_alpha(alpha_out)
        Field_lateral.set_alpha(alpha_in)
        screen.fill((0, 0, 0))
        screen.blit(Field_lateral, (0, 0))
        screen.blit(Field_drone, (0, 0))

    elif time_elapsed < 2 * transition_duration:
        # Calculate the alpha value for fading in
        alpha_in = int((time_elapsed - transition_duration) / transition_duration * 255)
        alpha_out = 255 - alpha_in
        Field_lateral.set_alpha(alpha_out)
        Ubackground.set_alpha(alpha_in)
        screen.blit(Ubackground, (0, 0))
        screen.blit(Field_lateral, (0, 0))
    else:
        screen.blit(Ubackground, (0, 0))
        
        if time_elapsed < (2 * transition_duration) + (countdown_duration):
            # Countdown text
            countdown_time = countdown_duration - int((time_elapsed - (2 * transition_duration)))
            countdown_text = "DECIDIENDO QUIEN COMIENZA: {}".format(countdown_time)
            text_surface = Hfont.render(countdown_text, True, WINE_RED)
            text_rect = text_surface.get_rect(center=(HWIDTH // 2, 50))
            screen.blit(text_surface, text_rect)
            gif_rect = coin_gif.get_rect(center=(HWIDTH // 2, HHEIGHT // 2 + 50))
            screen.blit(coin_gif, gif_rect)
        else:
            # Blit the selected sprite directly
            if "Escudo" in text_choice:
                escudo_rect = escudo.get_rect(center=(HWIDTH // 2, HHEIGHT // 2 + 50))
                screen.blit(escudo, escudo_rect)

                text_surface = Hfont.render(text_choice, True, WINE_RED)
                text_rect = text_surface.get_rect(center=(HWIDTH // 2, 50))
                screen.blit(text_surface, text_rect)
            
                Firstplayer = "YOU"
                
            else:
                escudo_rect = corona.get_rect(center=(HWIDTH // 2, HHEIGHT // 2 + 50))
                screen.blit(corona, escudo_rect)

                text_surface = Hfont.render(text_choice, True, WINE_RED)
                text_rect = text_surface.get_rect(center=(HWIDTH // 2, 50))
                screen.blit(text_surface, text_rect)

                Firstplayer = "ENEMY"

        # Wait for 1 second before returning Firstplayer
        if time_elapsed > (2 * transition_duration) + (countdown_duration) + 1:  
            return Firstplayer
