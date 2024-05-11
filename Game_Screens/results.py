import pygame
from var_consts import *
def results_screen(screen, Hfont, Mbackground, Field_frontal, current_round, Player_points, Enemy_points, seconds, game_reset):
    global player_scores, enemy_scores, first_enter, game_start_time, time_elapsed_wait # Make sure to use the global lists

    if first_enter or game_reset:
        game_start_time = seconds
        first_enter = False
    time_elapsed_wait = seconds - game_start_time   

    # Background gray coat  
    overlay = pygame.Surface((HWIDTH, HHEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_GRAY)
    screen.blit(Field_frontal, (0, 0))
    screen.blit(overlay, (0, 0))

    # Insert menu pop-up
    top_scores_BG_rect = Mbackground.get_rect(center=(HWIDTH//2, HHEIGHT//2))
    screen.blit(Mbackground, top_scores_BG_rect)

    # Display title text
    title_text = "FINAL RESULTS"
    title_surface = Hfont.render(title_text, True, WINE_RED)  
    title_text_rect = title_surface.get_rect(midtop=(HWIDTH/2, HHEIGHT/4))
    title_text_rect.y -= title_surface.get_height() 
    screen.blit(title_surface, title_text_rect)

    # Display "Amount of shots:" text
    shots_text = Hfont.render(f"Amount of shots: {current_round * 2}", True, NAVY_BLUE)
    shots_text_rect = shots_text.get_rect(midtop=(HWIDTH // 2, title_text_rect.bottom + 20))
    screen.blit(shots_text, shots_text_rect)

    # Display player and enemy points
    player_points_text = Hfont.render(f"Player Points: {Player_points}", True, NAVY_BLUE)
    player_points_rect = player_points_text.get_rect(midtop=(HWIDTH // 2, shots_text_rect.bottom + 20))
    screen.blit(player_points_text, player_points_rect)

    enemy_points_text = Hfont.render(f"Enemy Points: {Enemy_points}", True, NAVY_BLUE)
    enemy_points_rect = enemy_points_text.get_rect(midtop=(HWIDTH // 2, player_points_rect.bottom + 20))
    screen.blit(enemy_points_text, enemy_points_rect)

    # Determine final outcome
    final_result_text = ""
    if Player_points > Enemy_points:
        final_result_text = "YOU WIN!"
    elif Player_points < Enemy_points:
        final_result_text = "YOU LOSE!"
    else:
        final_result_text = "TIE!"
    
    final_result_surface = Hfont.render(final_result_text, True, WINE_RED)
    final_result_rect = final_result_surface.get_rect(midtop=(HWIDTH // 2, enemy_points_rect.bottom + 40))
    screen.blit(final_result_surface, final_result_rect)
