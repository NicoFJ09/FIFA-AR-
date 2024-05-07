import pygame
from var_consts import *

def players_select_screen(screen, Hfont, font, Mbackground, Ubackground, team_sprites, selected_index, selected_team, players_selection_text):

    screen.blit(Ubackground, (0, 0))

    # Insert box
    skin_select_bg_rect = Mbackground.get_rect(center=(HWIDTH // 2, HHEIGHT // 2))
    screen.blit(Mbackground, skin_select_bg_rect)

    # Display title text for skin selection
    skin_title_text = "¡ESCOGE TUS POSICIONES!"
    skin_title_surface = Hfont.render(skin_title_text, True, WINE_RED)  
    skin_title_text_rect = skin_title_surface.get_rect(midtop=(HWIDTH // 2, HHEIGHT // 4))
    skin_title_text_rect.y -= skin_title_surface.get_height() 
    screen.blit(skin_title_surface, skin_title_text_rect)

    # Blit text right below the existing title text
    additional_text = "NO PUEDES REPETIR SELECCION DE JUGADOR"
    additional_surface = font.render(additional_text, True, NAVY_BLUE)
    additional_rect = additional_surface.get_rect(midtop=(HWIDTH // 2, skin_title_text_rect.bottom + 10))  # Adjust the Y position as needed
    screen.blit(additional_surface, additional_rect)

    # Blit text right below the existing title text
    announcement_text = players_selection_text
    announcement_surface = font.render(announcement_text, True, NAVY_BLUE)
    announcement_rect = announcement_surface.get_rect(midtop=(HWIDTH // 2, additional_rect.bottom + 10))  # Adjust the Y position as needed
    screen.blit(announcement_surface, announcement_rect)


    # Reference point
    player = pygame.Surface((PAGE_WIDTH, PAGE_HEIGHT), pygame.SRCALPHA)
    player_rect = player.get_rect(center=(HWIDTH // 2, HHEIGHT // 2))

    skin_coordinates = {
        "player1": (252.5, 75),
        "player2": (463.75, 225),
        "player3": (41.25, 225)
    }

    # Blit the first sprite of each skin
    player.blit(team_sprites[selected_team][1][0], skin_coordinates["player1"])
    player.blit(team_sprites[selected_team][2][0], skin_coordinates["player2"])
    player.blit(team_sprites[selected_team][3][0], skin_coordinates["player3"])

    # Increase Y value by the size of the player sprites for text positioning
    sprite_height = team_sprites[selected_team][1][0].get_height()  # Assuming all sprites have the same height

    # Blit text for each player manually, adjusted to the reference point
    player1_text = font.render(team_sprites[selected_team][1][1], True, NAVY_BLUE)
    text_width = player1_text.get_width()
    player.blit(player1_text, (skin_coordinates["player1"][0] + (team_sprites[selected_team][1][0].get_width() - text_width) / 2, skin_coordinates["player1"][1] + sprite_height + 10))

    player2_text = font.render(team_sprites[selected_team][2][1], True, NAVY_BLUE)
    text_width = player2_text.get_width()
    player.blit(player2_text, (skin_coordinates["player2"][0] + (team_sprites[selected_team][2][0].get_width() - text_width) / 2, skin_coordinates["player2"][1] + sprite_height + 10))

    player3_text = font.render(team_sprites[selected_team][3][1], True, NAVY_BLUE)
    text_width = player3_text.get_width()
    player.blit(player3_text, (skin_coordinates["player3"][0] + (team_sprites[selected_team][3][0].get_width() - text_width) / 2, skin_coordinates["player3"][1] + sprite_height + 10))

    # Draw outline around the selected player
    outline_color = VIOLET
    outline_width = 2
    if selected_index == 1:
        selected_player_rect = pygame.Rect(skin_coordinates["player1"], team_sprites[selected_team][1][0].get_size())
        pygame.draw.rect(player, outline_color, selected_player_rect, outline_width)
    elif selected_index == 2:
        selected_player_rect = pygame.Rect(skin_coordinates["player2"], team_sprites[selected_team][2][0].get_size())
        pygame.draw.rect(player, outline_color, selected_player_rect, outline_width)
    elif selected_index == 3:
        selected_player_rect = pygame.Rect(skin_coordinates["player3"], team_sprites[selected_team][3][0].get_size())
        pygame.draw.rect(player, outline_color, selected_player_rect, outline_width)

    screen.blit(player, player_rect)