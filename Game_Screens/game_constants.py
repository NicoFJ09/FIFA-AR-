from var_consts import *
import pygame
def game_constants_screen(screen,Gfont, Nfont, Field_frontal, team_sprites, selected_team, enemy_team, selected_gamemode, final_player_list, enemy_player_list, Shootturn, team_player_index, enemy_player_index, current_round):
#Main background

    screen.blit(Field_frontal, (0, 0))

    #Information box
    info_box_height = 120
    info_box_color = OVERLAY_GRAY
    info_box_rect = pygame.Rect(0, 0, HWIDTH, info_box_height)  # Adjusted for vertical orientation

    # Draw the info box
    pygame.draw.rect(screen, info_box_color, info_box_rect)

    selected_team_sprite = team_sprites[selected_team][0]
    enemy_team_sprite = team_sprites[enemy_team][0]

    # Resize images
    selected_team_sprite = pygame.transform.scale(selected_team_sprite, (85, 100))
    enemy_team_sprite = pygame.transform.scale(enemy_team_sprite, (85, 100))

    # Render text for the information to display inside the box
    Team_text = Gfont.render(f"Your team:", True, NAVY_BLUE)  
    Enemy_team_text = Gfont.render(f"Enemy team:", True, NAVY_BLUE)  

    #Current shooter text will change per turn  
    Current_shooter_text = Nfont.render(f"Current shooter: {Shootturn}", True, NAVY_BLUE)

    #Shooter and goalee names ACCORDING TO GAMEMODE AND TURN
    if selected_gamemode== "MANUAL":

        if Shootturn == "YOU":
            shooter_name_text = Nfont.render(f"Shooter name: {final_player_list[0]}", True, NAVY_BLUE)
            goalee_name_text = Nfont.render(f"Goalee name: {enemy_player_list[enemy_player_index]}", True, NAVY_BLUE)

        elif Shootturn == "ENEMY":
            shooter_name_text = Nfont.render(f"Shooter name: {enemy_player_list[enemy_player_index]}", True, NAVY_BLUE)
            goalee_name_text = Nfont.render(f"Goalee name: {final_player_list[2]}", True, NAVY_BLUE)

    elif selected_gamemode== "AUTOMATIC":

        if Shootturn == "YOU":
            shooter_name_text = Nfont.render(f"Shooter name: {final_player_list[team_player_index]}", True, NAVY_BLUE)
            goalee_name_text = Nfont.render(f"Goalee name: {enemy_player_list[enemy_player_index]}", True, NAVY_BLUE)

        elif Shootturn == "ENEMY":
            shooter_name_text = Nfont.render(f"Shooter name: {enemy_player_list[enemy_player_index]}", True, NAVY_BLUE)
            goalee_name_text = Nfont.render(f"Goalee name: {final_player_list[team_player_index]}", True, NAVY_BLUE)

    current_round_text = Gfont.render(f"Round {current_round}", True, WINE_RED)

    text_margin = 10
    # Team text rect 

    Team_text_rect = Team_text.get_rect(topleft=(10, 10))

    # Calculate the position of the sprite for the selected team
    selected_sprite_rect = selected_team_sprite.get_rect(topleft=(Team_text_rect.right, Team_text_rect.top))
    
    # Team text rect 
    Enemy_text_rect = Enemy_team_text.get_rect(topleft=(selected_sprite_rect.right + text_margin, 10))

    # Calculate the position of the sprite for the enemy team
    enemy_sprite_rect = enemy_team_sprite.get_rect(topleft=(Enemy_text_rect.right, Enemy_text_rect.top))

    current_round_text_rect = current_round_text.get_rect(topleft=(enemy_sprite_rect.right + text_margin, enemy_sprite_rect.top))

    Current_shooter_text_rect = Current_shooter_text.get_rect(topleft=(enemy_sprite_rect.right + text_margin, current_round_text_rect.bottom + text_margin ))

    shooter_name_text_rect = shooter_name_text.get_rect(topleft=(enemy_sprite_rect.right + text_margin, Current_shooter_text_rect.bottom + text_margin ))

    goalee_name_text_rect = goalee_name_text.get_rect(topleft=(enemy_sprite_rect.right + text_margin, shooter_name_text_rect.bottom + text_margin))
    
    

    # Team and enemy text and logo render 
    screen.blit(Team_text, Team_text_rect)
    screen.blit(Enemy_team_text, Enemy_text_rect)
    screen.blit(selected_team_sprite, selected_sprite_rect)
    screen.blit(enemy_team_sprite, enemy_sprite_rect)
    screen.blit(Current_shooter_text, Current_shooter_text_rect)
    screen.blit(shooter_name_text, shooter_name_text_rect)
    screen.blit(goalee_name_text, goalee_name_text_rect)
    screen.blit(current_round_text, current_round_text_rect)