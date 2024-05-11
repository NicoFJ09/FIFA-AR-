from var_consts import *

def cinematic_screen(screen, Celebration1, Celebration2, Ubackground, seconds, game_reset):
    global first_enter, Main_game_time, time_elapsed_wait

    if first_enter or game_reset:
        Main_game_time = seconds
        first_enter = False

    time_elapsed_wait = seconds - Main_game_time

    transition_duration = 1.5 # Duration of each transition (in milliseconds)

    if time_elapsed_wait < transition_duration:
        # Calculate the alpha value for fading out
        alpha_out = int((1 - time_elapsed_wait / transition_duration) * 255)
        alpha_in = int((1 - time_elapsed_wait / transition_duration) * 255)
        Celebration1.set_alpha(alpha_out)
        Celebration2.set_alpha(alpha_in)
        screen.fill((0, 0, 0))
        screen.blit(Celebration2, (0, 0))
        screen.blit(Celebration1, (0, 0))

    elif time_elapsed_wait < 2 * transition_duration:
        # Calculate the alpha value for fading in
        alpha_in = int((time_elapsed_wait - transition_duration) / transition_duration * 255)
        alpha_out = 255 - alpha_in
        Celebration2.set_alpha(alpha_out)
        Ubackground.set_alpha(alpha_in)
        screen.blit(Ubackground, (0, 0))
        screen.blit(Celebration2, (0, 0))
    else:
        screen.blit(Ubackground, (0, 0))
    
    if time_elapsed_wait > 2*transition_duration+1:
        return "player_select"