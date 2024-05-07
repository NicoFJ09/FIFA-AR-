import pygame
import serial
import threading
import time
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
    seconds = game_time // 1000
    
    return seconds
#==================================================== SCREEN IMPORTS =============================
from Home_Screens.home import home_screen
from Home_Screens.start import start_screen
from Home_Screens.info import info_screen
from Home_Screens.top_players import top_scores_screen
from Home_Screens.about import about_screen
from Home_Screens.team_select import team_select_screen
from Home_Screens.gamemode_select import gamemode_select_screen
from Home_Screens.players_select import players_select_screen

#==================================================== ASSET IMPORTS ==============================

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
On_volume = pygame.transform.scale(pygame.image.load("Assets/Sprites/ON.png").convert_alpha(), (110,80))
Off_volume = pygame.transform.scale(pygame.image.load("Assets/Sprites/OFF.png").convert_alpha(), (110,80))

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


#Soundtrack
Intro_Track = "Assets/Soundtrack/Intro_Track.mp3"
Game_Track = "Assets/Soundtrack/Game_Track.mp3"
pygame.mixer.music.load(Intro_Track)
pygame.mixer.music.play(-1)  # -1 loops indefinitely

#Font
Hfont = pygame.font.Font("Assets/Font/PressStart2P.ttf",30)
Nfont = pygame.font.Font("Assets/Font/PressStart2P.ttf",15)

#=================================================== CHECK RASPBERRY PI DETECTION =======================

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
    global selected_index, current_screen, volume, music_playing, game_section, prev_game_section, seconds, selected_team, selected_gamemode, game_positions, game_position_index, players_selection_text, game_change_ready, data, prev_pot_value
    
    try:
        ser = serial.Serial(serial_port, baud_rate)
        print("Serial port connected")
    except Exception as e:
        print(f"Error opening serial port: {e}")
        return
    
    # Create and start serial reader thread
    serial_thread = threading.Thread(target=serial_reader, args=(ser,), daemon=True)
    serial_thread.start()

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

            volume_icon = On_volume if volume else Off_volume
            volume_rect = volume_icon.get_rect(topleft=(10, 10))  # Adjust position as needed
            #Universal volume toggle

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_m:
                volume = not volume

            # ======================= HOME SCREEN CONTROLS =======================================
        if current_screen == "HOME":
            if is_potentiometer_value(data):
                current_pot_value = int(data)
                # Check if the current potentiometer value is different from the previous one
                if current_pot_value != prev_pot_value:
                    selected_index = index_map(current_pot_value, len(Home_options))
                    prev_pot_value = current_pot_value  # Update the previous potentiometer value
            elif data == "BUTTON_PRESS":
                current_screen = Home_options[selected_index]
                selected_index = 0
                time.sleep(0.1)

        # ======================= GAME INFO CONTROLS =======================================
        elif current_screen == "GAME INFO":
            if is_potentiometer_value(data):
                current_pot_value = int(data)
                # Check if the current potentiometer value is different from the previous one
                if current_pot_value != prev_pot_value:
                    selected_index = index_map(current_pot_value, len(Info_options))
                    prev_pot_value = current_pot_value  # Update the previous potentiometer value
            elif data == "BUTTON_PRESS":
                current_screen = "HOME"
                selected_index = 0
                time.sleep(0.1)

        # ======================= TOP PLAYERS CONTROLS =======================================

        elif current_screen == "TOP PLAYERS":
            if data == "BUTTON_PRESS":
                current_screen = "HOME"
                selected_index = 0
                time.sleep(0.1)

        # ======================= ABOUT CONTROLS =======================================
        elif current_screen == "ABOUT":
            if data == "BUTTON_PRESS":
                current_screen = "HOME"
                selected_index = 0
                time.sleep(0.1)


        # ======================= TEAM SELECT CONTROLS =======================================
        elif current_screen == "TEAM_SELECT":
            if is_potentiometer_value(data):
                current_pot_value = int(data)
                # Check if the current potentiometer value is different from the previous one
                if current_pot_value != prev_pot_value:
                    selected_index = index_map(current_pot_value, len(team_sprites))
                    prev_pot_value = current_pot_value  # Update the previous potentiometer value
            elif data == "BUTTON_PRESS":
                selected_key = list(team_sprites.keys())[selected_index]
                selected_team = selected_key
                current_screen = "GAMEMODE_SELECT"
                selected_index = 0
                time.sleep(0.1)

        # ======================= GAMEMODE SELECT CONTROLS: MANUAL OR AUTOMATIC=======================================
        elif current_screen == "GAMEMODE_SELECT":

            if is_potentiometer_value(data):
                current_pot_value = int(data)
                # Check if the current potentiometer value is different from the previous one
                if current_pot_value != prev_pot_value:
                    selected_index = index_map(current_pot_value, len(Gamemode_options))
                    prev_pot_value = current_pot_value  # Update the previous potentiometer value

            elif data == "BUTTON_PRESS":
                selected_gamemode = Gamemode_options[selected_index]
                if selected_gamemode == "MANUAL":
                    current_screen = "PLAYERS_SELECT"
                    selected_index = 0
                    time.sleep(0.1)
                elif selected_gamemode == "AUTOMATIC":
                    current_screen = "MAIN_GAME"
                    selected_index = 0
                    time.sleep(0.1)

        elif current_screen == "PLAYERS_SELECT":
            if is_potentiometer_value(data):
                current_pot_value = int(data)
                if current_pot_value != prev_pot_value:
                    # Adjust the selected index based on the potentiometer value
                    selected_index = min(index_map(current_pot_value, len(team_sprites[selected_team])) + 1, len(team_sprites[selected_team]))  # Ensure it starts from 1
                    selected_index = min(selected_index, 3)
                    print(selected_index)
                    prev_pot_value = current_pot_value  # Update the previous potentiometer value
            elif data == "BUTTON_PRESS" and not game_change_ready:
                time.sleep(0.1)
                # Get the player name
                selected_player = team_sprites[selected_team][selected_index ][1]

                # Check if the player is already assigned to a position
                if selected_player in game_positions.values():
                    players_selection_text = f"{selected_player} is already assigned to a position."
                else:
                    # Assign the player to the current position
                    positions = list(game_positions.keys())
                    position = positions[game_position_index]
                    game_positions[position] = selected_player
                    
                    # Move to the next position index
                    game_position_index = (game_position_index + 1) % len(game_positions)

                    players_selection_text = f"Assigned {selected_player} to {position}"
                    # Check if all positions are assigned
                    if game_position_index == 0:
                        game_change_ready = True
                
            elif data == "BUTTON_PRESS" and game_change_ready:
                current_screen = "MAIN_GAME"
                selected_index = 0
                time.sleep(0.1)




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
            if seconds>2:
                current_screen = "TEAM_SELECT"

        elif current_screen == "TEAM_SELECT":
            team_select_screen(screen, Hfont, Mbackground, Ubackground, team_sprites, selected_index)
            screen.blit(volume_icon, volume_rect)
            
        elif current_screen == "GAMEMODE_SELECT":
            gamemode_select_screen(screen, Hfont, Mbackground, Ubackground, Gamemode_description, Gamemode_options, selected_index)
            screen.blit(volume_icon, volume_rect)

        elif current_screen =="PLAYERS_SELECT":
            players_select_screen(screen, Hfont, Nfont, Mbackground, Ubackground, team_sprites, selected_index,selected_team, players_selection_text)
            screen.blit(volume_icon, volume_rect)
        elif current_screen =="MAIN_GAME":
            start_screen(screen, Hfont, HWIDTH, HHEIGHT)
        
        
        # Update the display and cap the frame rate
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()