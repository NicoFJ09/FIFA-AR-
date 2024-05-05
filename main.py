import pygame
import serial
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
from Screens.home import home_screen
from Screens.start import start_screen
from Screens.info import info_screen
from Screens.top_players import top_scores_screen
from Screens.about import about_screen
#==================================================== ASSET IMPORTS ==============================

#Screen backgrounds
Hbackground = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Home_BG.png").convert_alpha(), (HWIDTH,HHEIGHT))
GTITLE =  pygame.transform.scale(pygame.image.load("Assets/Sprites/CE_SOCCER.png").convert_alpha(), (4*HWIDTH/5, HHEIGHT/10))
Mbackground = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Menu_BG.png").convert_alpha(), (MWIDTH,MHEIGHT))

#Pop up screens
Game_info_1 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Game_info_1.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))
Game_info_2 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Game_info_2.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))
Game_info_3 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Game_info_3.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))

About = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/About.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))

#Sprites
On_volume = pygame.transform.scale(pygame.image.load("Assets/Sprites/ON.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))
Off_volume = pygame.transform.scale(pygame.image.load("Assets/Sprites/OFF.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))

#Equipos
team1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/ON.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))
team2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/ON.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))
team3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/ON.png").convert_alpha(), (PAGE_WIDTH,PAGE_HEIGHT))

skin_sprites = {
    "Campeon": [team1],  # List of Samus sprites
    "Morao": [team2],  # List of Bomberman sprites
    "LSD": [team3]  # List of Kirby sprites
}


#Soundtrack
Intro_Track = "Assets/Soundtrack/Intro_Track.mp3"
Game_Track = "Assets/Soundtrack/Game_Track.mp3"
pygame.mixer.music.load(Intro_Track)
pygame.mixer.music.play(-1)  # -1 loops indefinitely
#Font
Hfont = pygame.font.Font("Assets/Font/PressStart2P.ttf",30)

#=================================================== CHECK RASPBERRY PI DETECTION =======================

def open_serial_port(port):
    try:
        Rpi = serial.Serial(port=port, baudrate=115200)
        print("Conectado")
        return Rpi
    except Exception:
        return None

def translate(Rpi):
    try:
        READ = Rpi.readline() # Esto se recibe en bytes.
        TRANSLATED = READ.decode('UTF-8') # Conversión de Byte a String
        print(TRANSLATED)
    except Exception:
        pass

Rpi = open_serial_port("COM7")

#================================================== TOP SHOOTER SCORES =================================
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

#====================================================== MAIN CODE ============================

def main():
    global selected_index, current_screen, volume, music_playing, game_section, prev_game_section, seconds
    
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

        # Update and render the current screen
        if current_screen == "HOME":
            game_section = "intro"
            home_screen(screen, Hbackground, GTITLE, Hfont, selected_index, Home_options)
        
        elif current_screen == "GAME INFO":
            game_section = "intro"
            info_screen(screen, Hbackground, Mbackground, Hfont, selected_index, Game_info_1, Game_info_2, Game_info_3)

        elif current_screen == "TOP PLAYERS":
            game_section = "intro"
            top_scores_screen(screen, Hfont, Mbackground, Hbackground)

        elif current_screen == "ABOUT":
            game_section = "intro"
            about_screen(screen, Hfont, Mbackground, Hbackground, About)

        elif current_screen == "START":
            game_section = "gameplay"
            start_screen(screen, Hfont, HWIDTH, HHEIGHT)
            if seconds>2:
                current_screen = "PLAYER_SELECT"


        elif current_screen == "PLAYER_SELECT":
            None
        # Update the display and cap the frame rate
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()