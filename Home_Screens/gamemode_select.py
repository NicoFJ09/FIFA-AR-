import pygame
from var_consts import *
def gamemode_select_screen(screen, font, Mbackground, Ubackground,Gamemode_description, Gamemode_options, selected_index):

    screen.blit(Ubackground, (0, 0))

    # Insert box
    gamemode_select_bg_rect = Mbackground.get_rect(center=(HWIDTH // 2, HHEIGHT // 2))
    screen.blit(Mbackground, gamemode_select_bg_rect)

    gamemode_select_description = Gamemode_description.get_rect(center=(HWIDTH // 2, HHEIGHT // 2))
    screen.blit(Gamemode_description, gamemode_select_description)
    # Title text separated in 2 lines

    gamemode_title_text_line1 = "ESCOGE TU MODALIDAD"
    gamemode_title_text_line2 = "DE JUEGO"

    gamemode_title_surface_line1 = font.render(gamemode_title_text_line1, True, WINE_RED)  
    gamemode_title_surface_line2 = font.render(gamemode_title_text_line2, True, WINE_RED)  

    gamemode_title_text_rect_line1 = gamemode_title_surface_line1.get_rect(midtop=(HWIDTH // 2, HHEIGHT // 4))
    gamemode_title_text_rect_line2 = gamemode_title_surface_line2.get_rect(midtop=(HWIDTH // 2,  gamemode_title_text_rect_line1.bottom+15))

    screen.blit(gamemode_title_surface_line1, gamemode_title_text_rect_line1)
    screen.blit(gamemode_title_surface_line2, gamemode_title_text_rect_line2)

    # Render sub-title texts
    sub_title_surfaces = [font.render(option, True, NAVY_BLUE) for option in Gamemode_options]

    # Calculate total width of all sub-titles
    total_width = sum(surface.get_width() for surface in sub_title_surfaces)

    # Calculate horizontal spacing between sub-titles
    spacing = (HWIDTH - total_width - 500) // (len(Gamemode_options) + 1)  # Subtract 500 for the spacing on each side

    # Initial x-coordinate for the first sub-title
    x_coordinate = spacing + 250  # Add 250 for the left-side spacing

    # Calculate the y-coordinate for the second line of text to ensure symmetry
    y_coordinate_line2 = gamemode_title_text_rect_line2.bottom + 30

    # Blit sub-title texts
    for index, surface in enumerate(sub_title_surfaces):
        sub_title_rect = surface.get_rect(midtop=(x_coordinate + surface.get_width() // 2, y_coordinate_line2))
        
        # Change color if the index matches selected_index
        if index == selected_index:
            surface = font.render(Gamemode_options[index], True, VIOLET)  # Change to color when selected 
        
        screen.blit(surface, sub_title_rect)
        x_coordinate += surface.get_width() + spacing
