import pygame
from var_consts import *
def info_screen(screen, Hbackground, Mbackground, Hfont, selected_index, Game_info_1, Game_info_2, Game_info_3):
    
    #Background gray coat  
    overlay = pygame.Surface((HWIDTH, HHEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_GRAY)
    screen.blit(Hbackground,(0,0))
    screen.blit(overlay,(0,0))

    #Insert menu pop-up

    info_BG_rect = Mbackground.get_rect(center=(HWIDTH//2, HHEIGHT//2))
    screen.blit(Mbackground,info_BG_rect)

    page_x = (HWIDTH - PAGE_WIDTH) // 2
    page_y = (HHEIGHT - PAGE_HEIGHT) // 2


    # Display title text
    title_text = "GAME MANUAL"
    title_surface = Hfont.render(title_text, True, NAVY_BLUE)  
    title_text_rect = title_surface.get_rect(midtop=(HWIDTH/2, HHEIGHT/4))
    title_text_rect.y -= title_surface.get_height() 
    screen.blit(title_surface, title_text_rect)

    #Page select
    if Info_options[selected_index] == "1/3":
        screen.blit(Game_info_1, (page_x+1, page_y+1))
    if Info_options[selected_index] == "2/3":
        screen.blit(Game_info_2, (page_x+1, page_y+1))
    if Info_options[selected_index] == "3/3":
        screen.blit(Game_info_3, (page_x+1, page_y+1))

    #Page number display
    index_text = Info_options[selected_index]
    index_surface = Hfont.render(index_text, True, (NAVY_BLUE))
    index_rect = index_surface.get_rect(bottomleft=(info_BG_rect.left, info_BG_rect.bottom))
    screen.blit(index_surface, index_rect)

