import pygame
import serial
import threading
import time
import random
import sys
sys.path.append('../')
import os
from var_consts import *


#==================================================== GAME SETUP ==================================

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("FIFA LIVE ACTION")
screen = pygame.display.set_mode((HWIDTH,HHEIGHT))
clock = pygame.time.Clock()

def update_timer(start_time):
    # Get the current game time
    game_time = pygame.time.get_ticks() - start_time
    
    # Convert game time to seconds
    seconds = game_time / 1000
    
    return seconds
#==================================================== SCREEN IMPORTS =============================
#Home screens imports

from Home_Screens.home import home_screen
from Home_Screens.start import start_screen
from Home_Screens.info import info_screen
from Home_Screens.top_players import top_scores_screen
from Home_Screens.about import about_screen
from Home_Screens.team_select import team_select_screen
from Home_Screens.gamemode_select import gamemode_select_screen
from Home_Screens.players_select import players_select_screen

#Game screens imports
from Game_Screens.pregame import pregame_screen
from Game_Screens.game_constants import game_constants_screen
from Game_Screens.game_loop import gameloop_screen
#==================================================== HOME ASSET IMPORTS ==============================

#Screen backgrounds
Hbackground = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Home_BG.png").convert_alpha(), (HWIDTH,HHEIGHT))
GTITLE =  pygame.transform.scale(pygame.image.load("Assets/Sprites/CE_SOCCER.png").convert_alpha(), (4*HWIDTH/5, HHEIGHT/10))
Mbackground = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Menu_BG.png").convert_alpha(), (MWIDTH,MHEIGHT))
Ubackground = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/User_BG.png").convert_alpha(), (HWIDTH,HHEIGHT))

#Pop up Screens
Game_info_1 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Game_info_1.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))
Game_info_2 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Game_info_2.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))
Game_info_3 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Game_info_3.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))

About = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/About.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))

Gamemode_description = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Gamemode.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))

#Sprites

#Volume sprites
On_volume = pygame.transform.scale(pygame.image.load("Assets/Sprites/ON.png").convert_alpha(), (110,80))
Off_volume = pygame.transform.scale(pygame.image.load("Assets/Sprites/OFF.png").convert_alpha(), (110,80))
volume_icon = On_volume
volume_rect = volume_icon.get_rect(topleft=(10, 10))  # Adjust position as needed

#Equipos
team1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team1.png").convert_alpha(), (170,200))
team1p1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team1p1.png").convert_alpha(), (170,200))
team1p2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team1p2.png").convert_alpha(), (170,200))
team1p3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team1p3.png").convert_alpha(), (170,200))

team2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team2.png").convert_alpha(), (170,200))
team2p1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team2p1.png").convert_alpha(), (170,200))
team2p2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team2p2.png").convert_alpha(), (170,200))
team2p3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team2p3.png").convert_alpha(), (170,200))

team3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team3.png").convert_alpha(), (170,200))
team3p1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team3p1.png").convert_alpha(), (170,200))
team3p2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team3p2.png").convert_alpha(), (170,200))
team3p3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/team3p3.png").convert_alpha(), (170,200))


team_sprites = {
    "Campeon": [team1, [team1p1, "El Pete Hernández"], [team1p2,"Mr Worldwide" ], [team1p3, "Fecundo Ovario"]],  # List of campeon sprites
    "Morao": [team2, [team2p1, "Rufino Pepino"], [team2p2, "Mr Clean"], [team2p3, "DJ Mario"]],  # List of morao sprites
    "LSD": [team3, [team3p1, "Stalin"], [team3p2, "Andrew Tate"], [team3p3, "Agüero Melo"]]  # List of lsd sprites
}

# ============================================================= MAIN GAME ASSET IMPORTS ==========================================================
Field_frontal = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Field_frontal.png").convert_alpha(), (HWIDTH,HHEIGHT))
Field_lateral = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Field_lateral.png").convert_alpha(), (HWIDTH,HHEIGHT))
Field_drone = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Field_drone.png").convert_alpha(), (HWIDTH,HHEIGHT))

#Sprites
coin_gif = pygame.transform.scale(pygame.image.load("Assets/Sprites/Coin_animation.gif").convert_alpha(), (300,300))
corona = pygame.transform.scale(pygame.image.load("Assets/Sprites/Corona.gif").convert_alpha(), (300,300))
escudo = pygame.transform.scale(pygame.image.load("Assets/Sprites/Escudo.gif").convert_alpha(), (300,300))
Bola_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Brazuka.png").convert_alpha(), (160,160))
Bola_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Brazuka_rotate.png").convert_alpha(), (160,160))
Goalee=  pygame.transform.scale(pygame.image.load("Assets/Sprites/Stood_goalee.png").convert_alpha(), (162.5,235))
Goalee_left= pygame.transform.scale(pygame.image.load("Assets/Sprites/Goal_keeper_left.png").convert_alpha(), (282,120))
Goalee_right= pygame.transform.scale(pygame.image.load("Assets/Sprites/Goal_keeper_right.png").convert_alpha(), (282,120))

#Soundtrack
Intro_Track = "Assets/Soundtrack/Intro_Track.mp3"
Game_Track = "Assets/Soundtrack/Game_Track.mp3"

pygame.mixer.music.load(Intro_Track)
pygame.mixer.music.play(-1)  # -1 loops indefinitely

#Font
Hfont = pygame.font.Font("Assets/Font/PressStart2P.ttf",30)
Gfont = pygame.font.Font("Assets/Font/PressStart2P.ttf",22)
Nfont = pygame.font.Font("Assets/Font/PressStart2P.ttf",15)
Titlefont = pygame.font.Font("Assets/Font/PressStart2P.ttf",60)

#=================================================== CHECK RASPBERRY PI DETECTION ====================================

serial_port = "COM8"
baud_rate = 115200

def serial_reader(ser):
    global data
    while True:
        try:
            # Read data from serial port
            data = ser.readline().decode('UTF-8').strip()
        except Exception as e:
            print(f"Error reading from serial port: {e}")

def index_map(pot_value, list_length):
    max_pot_value = 65535
    index = int(pot_value / max_pot_value * list_length)
    return min(index, list_length - 1)

def is_potentiometer_value(value):
    try:
        pot_value = int(value)
        return 0 <= pot_value <= 65535
    except ValueError:
        return False


#============================================= TOP SHOOTER SCORES ======================================
def update_top_scores(final_score):
    # Define the file path
    file_path = "Scores.txt"

    # Check if the file exists
    if os.path.exists(file_path):
        # Read existing scores from the file
        with open(file_path, 'r') as file:
            scores = [int(line.strip()) for line in file.readlines()]
    else:
        scores = []

    # Add the new score
    scores.append(final_score)

    # Sort scores in descending order
    scores.sort(reverse=True)

    # Write the scores back to the file
    with open(file_path, 'w') as file:
        for score in scores:
            file.write(str(score) + '\n')


#====================================================== MAIN CODE ========================================

def main():
    global selected_index, current_screen, volume, music_playing, game_section, prev_game_section, seconds, selected_team, enemy_team, selected_gamemode, game_positions, final_player_list, game_position_index, players_selection_text, game_change_ready, data, prev_pot_value, volume_rect, volume_icon, first_enter, team_player_index, enemy_player_index, current_round, selected_option, shoot

    while RUNNING:
        # Check Music Toggle Option
        if game_section != prev_game_section:
            prev_game_section = game_section
            music_playing = False
            if game_section == "gameplay":
                start_time =pygame.time.get_ticks()

        if game_section == "gameplay":
            seconds = update_timer(start_time)

        if volume:
            # Condition 1: Music Toggle ON
            if not music_playing and game_section == "intro":
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Intro_Track)
                pygame.mixer.music.play(-1)  # -1 loops indefinitely

            # Condition 2: Music Toggle OFF
            elif not music_playing and game_section == "gameplay":
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Game_Track)
                pygame.mixer.music.play(-1)  # -1 loops indefinitely
            music_playing = True

            # Volume Control
            pygame.mixer.music.set_volume(0.5)

        else:
            # Handle volume mute
            if music_playing:
                pygame.mixer.music.stop()
                music_playing = False

        # =========================== EVENT MANAGEMENT ===============================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Universal volume toggle
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_m:
                    volume = not volume
            # Home screen controls
                elif current_screen == "HOME":
                    
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        selected_index = (selected_index - 1) % len(Home_options)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        selected_index = (selected_index + 1) % len(Home_options)
                    elif event.key == pygame.K_RETURN:
                        current_screen = Home_options[selected_index]
                        selected_index = 0
                # Game info controls
                elif current_screen == "GAME INFO":
                    
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        selected_index = (selected_index + 1) % len(Info_options)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        selected_index = (selected_index - 1) % len(Info_options)
                    elif event.key == pygame.K_RETURN:
                        current_screen = "HOME"
                        selected_index = 0
                # Top_scores controls
                elif current_screen == "TOP PLAYERS":
                    
                    if event.key == pygame.K_RETURN:
                        current_screen = "HOME"
                        selected_index = 0
                # About controls
                elif current_screen == "ABOUT":
                    
                    if event.key == pygame.K_RETURN:
                        current_screen = "HOME"
                        selected_index = 0

                # Team select controls
                elif current_screen == "TEAM_SELECT":

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        selected_index = (selected_index + 1) % len(team_sprites)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        selected_index = (selected_index - 1) % len(team_sprites)
                    elif event.key == pygame.K_RETURN:
                        selected_key = list(team_sprites.keys())[selected_index]
                        selected_team = selected_key
                        enemy_options = list(team_sprites.keys())
                        enemy_options.remove(selected_team)
                        enemy_team = random.choice(enemy_options)
                        enemy_player_list = [team_sprites[enemy_team][1][1],team_sprites[enemy_team][2][1], team_sprites[enemy_team][3][1]]
                        current_screen = "GAMEMODE_SELECT"
                        selected_index = 0

                # Gamemode select controls: manual or automatic
                elif current_screen == "GAMEMODE_SELECT":

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        selected_index = (selected_index + 1) % len(Gamemode_options)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        selected_index = (selected_index - 1) % len(Gamemode_options)
                    elif event.key == pygame.K_RETURN:
                        selected_gamemode = Gamemode_options[selected_index]
                        if selected_gamemode == "MANUAL":
                            current_screen = "PLAYERS_SELECT"
                            selected_index = 1
                        elif selected_gamemode == "AUTOMATIC":
                            final_player_list = [team_sprites[selected_team][1][1],team_sprites[selected_team][2][1], team_sprites[selected_team][3][1]]
                            current_screen = "PRE_GAME"
                            selected_index = 0

                elif current_screen == "PLAYERS_SELECT":
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        selected_index = min(selected_index + 1, len(team_sprites[selected_team]) - 1)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        selected_index = max(selected_index - 1, 1)
                    elif event.key == pygame.K_RETURN and not game_change_ready:
                        # Get the player name
                        selected_player = team_sprites[selected_team][selected_index][1]

                        # Check if the player is already assigned to a position
                        if selected_player in game_positions.values():
                            players_selection_text = f"Player {selected_player} is already assigned to a position."
                        else:
                            # Assign the player to the current position
                            positions = list(game_positions.keys())
                            position = positions[game_position_index]
                            game_positions[position] = selected_player
                            final_player_list.append(selected_player)
                            # Move to the next position index
                            game_position_index = (game_position_index + 1) % len(game_positions)

                            players_selection_text = f"Assigned {selected_player} to {position}"
                            # Check if all positions are assigned
                            if game_position_index == 0:
                                game_change_ready = True

                    elif event.key == pygame.K_RETURN and game_change_ready:
                        current_screen = "PRE_GAME"

                if current_screen == "MAIN_GAME" and not shoot:
                    if Shootturn == "YOU":
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            selected_index = (selected_index + 1) % len(goal_positions)
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            selected_index = (selected_index - 1) % len(goal_positions)
                        elif event.key == pygame.K_RETURN:
                            selected_option = goal_positions[selected_index]
                            shoot = True

                    if Shootturn == "ENEMY" and not shoot:
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            selected_index = (selected_index + 1) % len(Defense_options)
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            selected_index = (selected_index - 1) % len(Defense_options)
                        elif event.key == pygame.K_RETURN:
                            selected_option = Defense_options[selected_index]
                            shoot = True


        # ========================================= CURRENT SCREEN RENDERING =============================================

        
        if current_screen == "HOME":
            game_section = "intro"
            home_screen(screen, Hbackground, GTITLE, Hfont, selected_index, Home_options)
            screen.blit(volume_icon, volume_rect)
        
        elif current_screen == "GAME INFO":
            game_section = "intro"
            info_screen(screen, Hbackground, Mbackground, Hfont, selected_index, Game_info_1, Game_info_2, Game_info_3)
            screen.blit(volume_icon, volume_rect)

        elif current_screen == "TOP PLAYERS":
            game_section = "intro"
            top_scores_screen(screen, Hfont, Mbackground, Hbackground)
            screen.blit(volume_icon, volume_rect)

        elif current_screen == "ABOUT":
            game_section = "intro"
            about_screen(screen, Hfont, Mbackground, Hbackground, About)
            screen.blit(volume_icon, volume_rect)

        elif current_screen == "START":
            game_section = "gameplay"
            start_screen(screen, Hfont, HWIDTH, HHEIGHT)
            if seconds>1.5:
                current_screen = "TEAM_SELECT"
                selected_index = 0

        elif current_screen == "TEAM_SELECT":
            team_select_screen(screen, Hfont, Mbackground, Ubackground, team_sprites, selected_index)
            screen.blit(volume_icon, volume_rect)
            
        elif current_screen == "GAMEMODE_SELECT":
            gamemode_select_screen(screen, Hfont, Mbackground, Ubackground, Gamemode_description, Gamemode_options, selected_index)
            screen.blit(volume_icon, volume_rect)

        elif current_screen == "PLAYERS_SELECT":
            players_select_screen(screen, Hfont, Nfont, Mbackground, Ubackground, team_sprites, selected_index,selected_team, players_selection_text)
            screen.blit(volume_icon, volume_rect)
            
        elif current_screen == "PRE_GAME":
            Shootturn = pregame_screen(screen, Hfont, Field_drone, Field_lateral, Ubackground,coin_gif, corona, escudo, seconds)
            if Shootturn == "ENEMY" or Shootturn == "YOU":
                current_screen = "MAIN_GAME"
                first_enter = True
                selected_index = 0
        
        elif current_screen == "MAIN_GAME":
            game_constants_screen(screen,Gfont,Nfont, Field_frontal, team_sprites, selected_team, enemy_team, selected_gamemode, final_player_list, enemy_player_list, Shootturn, team_player_index, enemy_player_index, current_round)
            gameloop_screen(screen,Titlefont,Hfont, selected_gamemode,Bola_1, Bola_2, Goalee, Goalee_left, Goalee_right, Shootturn, seconds, current_round, selected_index, selected_option)
        # Update the display and cap the frame rate
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()