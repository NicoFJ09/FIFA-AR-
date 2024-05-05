import pygame
from var_consts import *
def about_screen(screen, Hfont, Mbackground, Hbackground, About):

    #Background gray coat  
    overlay = pygame.Surface((HWIDTH, HHEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_GRAY)
    screen.blit(Hbackground,(0,0))
    screen.blit(overlay,(0,0))

    #Insert menu pop-up
    about_BG_rect = Mbackground.get_rect(center=(HWIDTH//2, HHEIGHT//2))
    screen.blit(Mbackground,about_BG_rect)

    # Display title text
    title_text = "MEET THE DEVELOPERS!"
    title_surface = Hfont.render(title_text, True, NAVY_BLUE) 
    title_text_rect = title_surface.get_rect(midtop=(HWIDTH/2, HHEIGHT/4))
    title_text_rect.y -= title_surface.get_height() 
    screen.blit(title_surface, title_text_rect)

    #Insert about image
    page_x = (HWIDTH - PAGE_WIDTH) // 2
    page_y = (HHEIGHT - PAGE_HEIGHT) // 2

    screen.blit(About, (page_x+1, page_y+1))