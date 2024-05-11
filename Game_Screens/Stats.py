import pygame
from var_consts import *
# Initialize lists to store player and enemy scores for each round
player_scores = ["","","","",""]

enemy_scores = ["","","","",""]



def stats_screen(screen, Hfont, Mbackground, Field_frontal, current_round, Player_points, Enemy_points, seconds, game_reset):
    global player_scores, enemy_scores, first_enter, game_start_time, time_elapsed_wait # Make sure to use the global lists

    if first_enter or game_reset:
        game_start_time = seconds
        first_enter =  False
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
    title_text = "CURRENT STATISTICS"
    title_surface = Hfont.render(title_text, True, WINE_RED)  
    title_text_rect = title_surface.get_rect(midtop=(HWIDTH/2, HHEIGHT/4))
    title_text_rect.y -= title_surface.get_height() 
    screen.blit(title_surface, title_text_rect)

    # Display "Amount of shots:" text
    shots_text = Hfont.render(f"Amount of shots: {current_round * 2}", True, NAVY_BLUE)
    shots_text_rect = shots_text.get_rect(midtop=(HWIDTH // 2, title_text_rect.bottom + 20))
    screen.blit(shots_text, shots_text_rect)

    # Update player and enemy scores based on the current round
    if current_round >=5:
        player_scores[current_round - 1] = "SCORE" if Player_points > 0 else "FAIL"
        enemy_scores[current_round - 1] = "SCORE" if Enemy_points > 0 else "FAIL"
        return ["end_screen", player_scores, enemy_scores]
    if current_round >= 1:
        player_scores[current_round - 1] = "SCORE" if Player_points > 0 else "FAIL"
        enemy_scores[current_round - 1] = "SCORE" if Enemy_points > 0 else "FAIL"

    # Display circles for "YOU"
    circle_diameter = 20  # Adjust as needed
    padding_between_circles = 30  # Adjust as needed
    # Display "YOU" text
    you_text = Hfont.render("YOU", True, NAVY_BLUE)
    you_text_rect = you_text.get_rect(midtop=(HWIDTH // 3, title_text_rect.bottom + 120))
    screen.blit(you_text, you_text_rect)

    # Display circles for "YOU"
    start_x_you = you_text_rect.right + padding_between_circles
    start_y_you = title_text_rect.bottom + 120  # Adjust vertical position as needed

    for i, score in enumerate(player_scores):  # Display scores for each round
        circle_color = GREEN if score == "SCORE" else RED if score == "FAIL" else OVERLAY_GRAY
        pygame.draw.circle(screen, circle_color, (start_x_you + i * (circle_diameter + padding_between_circles), start_y_you + circle_diameter // 2), circle_diameter // 2)

    # Display "ENEMY" text
    enemy_text = Hfont.render("ENEMY", True, NAVY_BLUE)
    # Calculate position for "ENEMY" text and circles relative to "YOU"
    enemy_text_rect = enemy_text.get_rect(midtop=(HWIDTH // 3, you_text_rect.bottom + 120))
    screen.blit(enemy_text, enemy_text_rect)

    start_x_enemy = enemy_text_rect.right + padding_between_circles
    start_y_enemy = you_text_rect.bottom + 120 

    # Display circles for "ENEMY"
    for i, score in enumerate(enemy_scores):  # Display scores for each round
        circle_color = GREEN if score == "SCORE" else RED if score == "FAIL" else OVERLAY_GRAY
        pygame.draw.circle(screen, circle_color, (start_x_enemy + i * (circle_diameter + padding_between_circles), start_y_enemy + circle_diameter // 2), circle_diameter // 2)

    if time_elapsed_wait >  1.5:
        return ["switch", player_scores, enemy_scores]
    