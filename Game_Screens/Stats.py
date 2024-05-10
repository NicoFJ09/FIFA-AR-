import pygame
from var_consts import *

def stats_screen(screen, Hfont, Mbackground, Field_frontal, current_round, seconds):
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

    for i in range(5):  # Assuming 5 circles
        circle_color = OVERLAY_GRAY
        pygame.draw.circle(screen, circle_color, (start_x_you + i * (circle_diameter + padding_between_circles), start_y_you + circle_diameter // 2), circle_diameter // 2)


    # Display "ENEMY" text
    enemy_text = Hfont.render("ENEMY", True, NAVY_BLUE)
    # Calculate position for "ENEMY" text and circles relative to "YOU"
    enemy_text_rect = enemy_text.get_rect(midtop=(HWIDTH // 3, you_text_rect.bottom + 120))



    screen.blit(enemy_text, enemy_text_rect)

    start_x_enemy = enemy_text_rect.right + padding_between_circles
    start_y_enemy = you_text_rect.bottom + 120 

    # Display circles for "ENEMY"
    for i in range(5):  # Assuming 5 circles
        circle_color = OVERLAY_GRAY
        pygame.draw.circle(screen, circle_color, (start_x_enemy + i * (circle_diameter + padding_between_circles), start_y_enemy + circle_diameter // 2), circle_diameter // 2)
