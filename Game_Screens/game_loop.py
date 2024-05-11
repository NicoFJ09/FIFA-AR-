from var_consts import *
import pygame
import random
import math
Whistle = "Assets/Soundtrack/Silbato_sonido.mp3"
Boo= "Assets/Soundtrack/Buu.mp3"
Cheer = "Assets/Soundtrack/Goal.mp3"


pygame.init()
pygame.mixer.init()
whistle_sound = pygame.mixer.Sound(Whistle)
boo_sound = pygame.mixer.Sound(Boo)
cheer_sound = pygame.mixer.Sound(Cheer)


def draw_target_positions(screen, blocked_positions, COLOR):
    for block_pos in blocked_positions:
        x, y, width, height = block_pos
        # Create semi-transparent surface for blocked positions
        Blocked_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        Blocked_surface.fill(COLOR)  # WINE_RED with semi-transparency
        screen.blit(Blocked_surface, (x, y))



def gameloop_screen(screen,Titlefont,Hfont, Bola_1, Goalee, Goalee_left, Goalee_right, Shootturn, seconds, selected_index, selected_option, game_reset):
    global first_enter, game_start_time, countdown_time, shoot, blocked_positions, target_position, shot_result, time_elapsed, Random_shot, Random_jump, internal_P_points, internal_E_points
    if first_enter or game_reset:

        game_start_time = seconds
        first_enter =  False
        shoot = False
        Random_shot = None
        blocked_positions= []
        target_position = None
        shot_result = ""
        internal_P_points = 0
        internal_E_points = 0
    
    time_elapsed = seconds - game_start_time

    goalee_rect= Goalee.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
    jump_rect = Goalee_right.get_rect(center=(HWIDTH//2, HHEIGHT // 2))

    if time_elapsed <  1:
        # Render and display "READY" message
        ready_text = Titlefont.render("READY", True, WINE_RED)
        ready_text_rect = ready_text.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
        screen.blit(Goalee, goalee_rect)
        screen.blit(ready_text, ready_text_rect)


    elif time_elapsed >= 1 and time_elapsed < 4:
        # Render and display countdown
        countdown_time = 3 - math.floor(time_elapsed - 1)
        countdown_text = str(countdown_time)
        countdown_surface = Titlefont.render(countdown_text, True, WINE_RED)
        countdown_rect = countdown_surface.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
        screen.blit(Goalee, goalee_rect)
        screen.blit(countdown_surface, countdown_rect)

    elif Shootturn == "YOU":
        
        if time_elapsed >= 4 and time_elapsed < 5:
            
            # Render and display "SHOOT" message
            shoot_text = Titlefont.render("SHOOT", True, WINE_RED)
            shoot_text_rect = shoot_text.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
            screen.blit(Goalee, goalee_rect)
            screen.blit(shoot_text, shoot_text_rect)
            whistle_sound.play()



        #PRE SHOT PREPARATION 
        elif time_elapsed >= 5 and time_elapsed < 8.5:

            for index, (x, y, width, height) in enumerate(goal_positions):
                position_rect = pygame.Rect(x, y, width, height)
                
                # Create semi-transparent surfaces with different colors for hover and selection
                hover_surface = pygame.Surface((width, height), pygame.SRCALPHA)
                hover_surface.fill(VIOLET_SEMITRANSPARENT)  # VIOLET with semi-transparency
                select_surface = pygame.Surface((width, height), pygame.SRCALPHA)
                select_surface.fill(WINE_RED_SEMITRANSPARENT)  # WINE_RED with semi-transparency
                
                # Check if the current position is hovered or selected
                if selected_index == index and selected_option != (x, y, width, height):
                    # Fill the hovered position with the semi-transparent hover color
                    screen.blit(hover_surface, position_rect)

                elif selected_option == (x, y, width, height):
                    # Fill the selected position with the semi-transparent select color
                    screen.blit(select_surface, position_rect)
                    shoot = True

                else:
                    # Draw other positions with default color
                    pygame.draw.rect(screen, NAVY_BLUE, position_rect, 1)

                screen.blit(Goalee, goalee_rect)

        #WHAT HAPPENS AFTER THE SHOT

        elif time_elapsed >= 8.5 and time_elapsed < 9:
            if selected_index<3:
                screen.blit(Goalee_left, jump_rect)
                
            elif selected_index>=3:
                screen.blit(Goalee_right, jump_rect)

        elif time_elapsed >= 9 and time_elapsed < 10:
            
            if shoot:
                target_position = (
                    selected_option[0] + selected_option[2] // 2 - Bola_1.get_width() // 2,  # Adjusted x-coordinate for ball centering
                    selected_option[1] + selected_option[3] // 2 - Bola_1.get_height() // 2  # Adjusted y-coordinate for ball centering
                )
                # Bot chooses from 3 possible defense lineups
                Random_lineup = random.choice([[(0, 1), (2, 3), (4, 5)], [(0, 1, 2), (3, 4, 5)], [(0, 2, 4), (1, 3, 5)]])
                # Then randomly chooses one of the options of the selected defense
                selected_blocks = random.choice(Random_lineup)

                # Get the positions of the selected blocks
                blocked_positions = [goal_positions[i] for i in selected_blocks]

                shoot = False
            

        #BALL MOVEMENT MANAGEMENT

        elif time_elapsed >= 10 and time_elapsed < 12:
            if target_position is not None and selected_option is not None:
                draw_target_positions(screen, blocked_positions, VIOLET_SEMITRANSPARENT)
                draw_target_positions(screen, [selected_option], WINE_RED_SEMITRANSPARENT)
                # Calculate fractional part of elapsed time
                fractional_time = time_elapsed - 11
                
                # Calculate current position based on elapsed time and interpolate
                current_pos = (
                    initial_ball_pos[0] + (target_position[0] - initial_ball_pos[0]) * fractional_time,
                    initial_ball_pos[1] + (target_position[1] - initial_ball_pos[1]) * fractional_time 
                )
                # Draw the ball sprite at the current position
                screen.blit(Bola_1, current_pos)

        elif time_elapsed >= 12 and time_elapsed <12.5:
            if selected_option in blocked_positions or selected_option == None :
                # Display "Failed" text in the middle of the screen using Titlefont
                failed_text = Titlefont.render("MISS!", True, WINE_RED)
                failed_text_rect = failed_text.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
                screen.blit(failed_text, failed_text_rect)
                shot_result = "MISS"
                if shoot == False:
                    boo_sound.play()
                    shoot = True
                    internal_P_points = 0

            else:
                # Display "Goal" text in the middle of the screen using Titlefont
                goal_text = Titlefont.render("GOAL!", True, WINE_RED)
                goal_text_rect = goal_text.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
                screen.blit(goal_text, goal_text_rect)
                shot_result = "GOAL"
                if shoot == False:
                    cheer_sound.play()
                    shoot = True
                    internal_P_points = 1
        
        elif time_elapsed >= 12.5 and time_elapsed <13:
            return ["switch", internal_P_points, internal_E_points]

    elif Shootturn == "ENEMY":
        if time_elapsed >= 4 and time_elapsed < 5:
            
            # Render and display "SHOOT" message
            shoot_text = Titlefont.render("DEFEND", True, WINE_RED)
            shoot_text_rect = shoot_text.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
            screen.blit(Goalee, goalee_rect)
            screen.blit(shoot_text, shoot_text_rect)
            whistle_sound.play()

    # PRE DEFENSE PREPARATION 
        elif time_elapsed >= 5 and time_elapsed < 8.5:
            Options_title = Hfont.render("SELECT YOUR DEFENSE PATTERN", True, WINE_RED)
            Options_title_rect = Options_title.get_rect(center=(HWIDTH//2, 150))
            screen.blit(Goalee, goalee_rect)
            screen.blit(Options_title, Options_title_rect)

            # Calculate the spacing between options
            spacing = 50  # Adjust the spacing as needed
            # Initial y-coordinate for the first option
            y = 200

            for i, option in enumerate(Defense_options):
                # Render the text using the Titlefont
                option_text = Hfont.render(option, True, HOT_PINK if selected_index == i and shoot== False else WINE_RED)
                # Get the rectangle for the rendered text
                option_rect = option_text.get_rect()
                # Set the top-left corner of the rectangle to the current coordinates
                option_rect.topleft = (HWIDTH - option_rect.width) // 2, y
                # Blit the text onto the screen
                screen.blit(option_text, option_rect)
                # Update the y-coordinate for the next option
                y += option_rect.height + spacing

                # Check if the selected option is pressed
                if selected_option in Defense_options and shoot == False:
                    # Print the value of the defense option
                    shoot = True

        elif time_elapsed >=9 and time_elapsed < 12:
                
                if shoot:
                    if selected_option == Defense_options[0]:
                        Defense_positions = random.choice([(0, 1, 2), (3, 4, 5)])
                    elif selected_option == Defense_options[1]:
                        Defense_positions = random.choice([(0, 1), (2, 3), (4, 5)])
                    elif selected_option == Defense_options[2]:
                        Defense_positions = random.choice([(0, 2, 4), (1, 3, 5)])

        
                    Random_shot = random.choice(goal_positions)
                    Random_jump = random.choice([Goalee_left, Goalee_right])
                    target_position = (
                    Random_shot[0] + Random_shot[2] // 2 - Bola_1.get_width() // 2,  # Adjusted x-coordinate for ball centering
                    Random_shot[1] + Random_shot[3] // 2 - Bola_1.get_height() // 2  # Adjusted y-coordinate for ball centering
                    )

                    blocked_positions = [goal_positions[i] for i in Defense_positions]
                    shoot = False

                if Random_jump != None:
                    screen.blit(Random_jump, jump_rect)
                    
                draw_target_positions(screen, blocked_positions, WINE_RED_SEMITRANSPARENT)



        #WHAT HAPPENS AFTER THE SHOT

        elif time_elapsed>=12 and time_elapsed<13:

            if target_position is not None and Random_shot is not None:
                draw_target_positions(screen, blocked_positions, WINE_RED_SEMITRANSPARENT)
                draw_target_positions(screen, [Random_shot], VIOLET_SEMITRANSPARENT)
                # Calculate fractional part of elapsed time
                fractional_time = time_elapsed - 12
                
                # Calculate current position based on elapsed time and interpolate
                current_pos = (
                    initial_ball_pos[0] + (target_position[0] - initial_ball_pos[0]) * fractional_time,
                    initial_ball_pos[1] + (target_position[1] - initial_ball_pos[1]) * fractional_time 
                )
                # Draw the ball sprite at the current position
                screen.blit(Bola_1, current_pos)


        elif time_elapsed>=13 and time_elapsed < 13.5:
            if Random_shot in blocked_positions:
                # Display "Failed" text in the middle of the screen using Titlefont
                failed_text = Titlefont.render("BLOCKED!", True, WINE_RED)
                failed_text_rect = failed_text.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
                screen.blit(failed_text, failed_text_rect)
                shot_result = "BLOCKED"
                if shoot == False:
                    cheer_sound.play()
                    shoot = True
                    internal_E_points = 0
                

            elif Random_shot not in blocked_positions or selected_option == None:
                # Display "Goal" text in the middle of the screen using Titlefont
                goal_text = Titlefont.render("GOAL!", True, WINE_RED)
                goal_text_rect = goal_text.get_rect(center=(HWIDTH//2, HHEIGHT // 2))
                screen.blit(goal_text, goal_text_rect)
                shot_result = "GOAL"
                if shoot == False:
                    boo_sound.play()
                    shoot = True
                    internal_E_points = 1
        
        elif time_elapsed >= 13.5 and time_elapsed <14:
            return ["switch", internal_P_points, internal_E_points]
            