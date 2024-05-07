import pygame
from var_consts import *

def team_select_screen(screen, font, Mbackground, Ubackground, team_sprites, selected_index):
    screen.blit(Ubackground, (0, 0))

    # Insert box
    skin_select_bg_rect = Mbackground.get_rect(center=(HWIDTH // 2, HHEIGHT // 2))
    screen.blit(Mbackground, skin_select_bg_rect)

    # Display title text for skin selection
    skin_title_text = "¡ESCOGE TU EQUIPO!"
    skin_title_surface = font.render(skin_title_text, True, WINE_RED)  
    skin_title_text_rect = skin_title_surface.get_rect(midtop=(HWIDTH // 2, HHEIGHT // 4))
    skin_title_text_rect.y -= skin_title_surface.get_height() 
    screen.blit(skin_title_surface, skin_title_text_rect)

    # Reference point
    invisible_rectangle = pygame.Surface((PAGE_WIDTH, PAGE_HEIGHT), pygame.SRCALPHA)
    invisible_rectangle_rect = invisible_rectangle.get_rect(center=(HWIDTH // 2, HHEIGHT // 2))

    skin_coordinates = {
        "Campeon": (252.5, 50),
        "Morao": (463.75, 200),
        "LSD": (41.25, 200)
    }

    # Blit the first sprite of each skin
    invisible_rectangle.blit(team_sprites["Campeon"][0], skin_coordinates["Campeon"])
    invisible_rectangle.blit(team_sprites["Morao"][0], skin_coordinates["Morao"])
    invisible_rectangle.blit(team_sprites["LSD"][0], skin_coordinates["LSD"])


    selected_skin = list(team_sprites.keys())[selected_index]
    selected_sprite = team_sprites[selected_skin][0]  # Get the first sprite of the selected skin
    selected_coord = skin_coordinates[selected_skin]

    # Draw a rectangle around the selected skin
    pygame.draw.rect(invisible_rectangle, VIOLET, 
                        (selected_coord[0] - 10, selected_coord[1] - 10, 
                        selected_sprite.get_width() + 20, selected_sprite.get_height() + 20), 3)
    


    screen.blit(invisible_rectangle, invisible_rectangle_rect)
    pygame.display.flip()
