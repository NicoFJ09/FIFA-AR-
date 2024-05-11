

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
from Game_Screens.Stats import stats_screen
from Game_Screens.cinematic import cinematic_screen
from Game_Screens.results import results_screen
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
    "LSD": [team3, [team3p1, "Stalin"], [team3p2, "Andrew Tate"], [team3p3, "Aguero Melo"]]  # List of lsd sprites
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
Goalee=  pygame.transform.scale(pygame.image.load("Assets/Sprites/Stood_goalee.png").convert_alpha(), (162.5,235))
Goalee_left= pygame.transform.scale(pygame.image.load("Assets/Sprites/Goal_keeper_left.png").convert_alpha(), (282,120))
Goalee_right= pygame.transform.scale(pygame.image.load("Assets/Sprites/Goal_keeper_right.png").convert_alpha(), (282,120))
Celebration1 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Celebration (1).png").convert_alpha(), (HWIDTH,HHEIGHT))
Celebration2 = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Celebration (2).png").convert_alpha(), (HWIDTH,HHEIGHT))
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
def update_top_scores(scores_list, file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Read existing scores from the file
        with open(file_path, 'r') as file:
            scores = [line.strip().split(", ") for line in file.readlines()]
    else:
        scores = []


    # Dictionary to store scores by name
    scores_dict = {score[0]: int(score[1]) for score in scores}


    # Update scores or add new scores
    for score in scores_list:
        name = score[0]
        value = score[1]
        if name in scores_dict:
            scores_dict[name] += value  # If name already exists, sum the new score to the existing one
        else:
            scores_dict[name] = value   # If name doesn't exist, add it to the dictionary


    # Write the updated scores back to the file
    with open(file_path, 'w') as file:
        for name, score in scores_dict.items():
            file.write(name + ', ' + str(score) + '\n')


def add_team_stats(team_stats, file_path):
    # Dictionary to store existing team stats
    existing_stats = {}


    # Read existing team stats from the file and store them in the dictionary
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                team, label, score = line.strip().split(", ")
                existing_stats[(team, label)] = int(score)


    # Update team stats with new scores
    for team, label, score in team_stats:
        key = (team, label)
        if key in existing_stats:
            # If team and label combination already exists, add the new score to the existing score
            existing_stats[key] += score
        else:
            # If team and label combination doesn't exist, add it to the dictionary
            existing_stats[key] = score


    # Write the updated team stats back to the file
    with open(file_path, 'w') as file:
        for (team, label), score in existing_stats.items():
            file.write(f"{team}, {label}, {score}\n")
# =============================================== SCORES SORTING ======================================


def identify_team(player_name, team_sprites):
    for team, player_list in team_sprites.items():
        for player_entry in player_list[1:]:
            if player_name in player_entry:
                return team
    return None  # Return None if player not found in any team


def analyze_scores(combined_list):
    # Initialize dictionaries to store scores per player
    scores_per_player = {}
   
    # Counters for total scores and fails
    total_score = 0
    total_fail = 0


    # Iterate through the combined list
    for score, player in combined_list:
        # Count scores per player
        if score == 'SCORE':
            scores_per_player[player] = scores_per_player.get(player, 0) + 1
            total_score += 1
        # Count fails per player
        else:
            total_fail += 1


    # Create a list of sublists containing player and score count with team names
    player_scores_list = []
    for player, score_count in scores_per_player.items():
        team = identify_team(player, team_sprites)
        player_scores_list.append([player, score_count])


    # Create a list for total scores and fails with team names
    team = identify_team(player, team_sprites)
    total_scores_and_fails = [[team,'Total score', total_score], [team,'Total fail', total_fail]]




    # Return the list of player scores and total scores and fails with team names
    return player_scores_list, total_scores_and_fails




#====================================================== MAIN CODE ========================================


def main():
    global selected_index, current_screen, volume, music_playing, game_section, prev_game_section, seconds, selected_team, enemy_team, selected_gamemode, game_positions, final_player_list, game_position_index, players_selection_text, game_change_ready, data, prev_pot_value, volume_rect, volume_icon, first_enter, team_player_index, enemy_player_index, current_round, selected_option, shoot, turn_change, Shootturn, game_reset, Player_points, Enemy_points, Game_values_list, Final_scores, Final_scores_ENEMY, stats_screen_list, combined_list, combined_list_ENEMY, player_scores, total_scores_and_fails, player_scores_ENEMY, total_scores_and_fails_ENEMY






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
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        selected_index = (selected_index + 1) % len(Top_players)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        selected_index = (selected_index - 1) % len(Top_players)
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
                        if current_round == 1:
                            current_screen = "PRE_GAME"
                            selected_index = 0
                            game_change_ready = False
                        else:
                            current_screen = "MAIN_GAME"
                            selected_index = 0
                            selected_option = None
                            shoot = False
                            game_reset = True
                            first_enter = True
                            game_change_ready = False
                       


                if current_screen == "MAIN_GAME" or current_screen == "MAIN_GAME2" and not shoot:
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


                if current_screen == "RESULTS_SCREEN":
                    if event.key == pygame.K_RETURN:
                        current_screen = "HOME"


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
            top_scores_screen(screen, Hfont, Mbackground, Hbackground, selected_index)
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
            Game_values_list = gameloop_screen(screen,Titlefont,Hfont,Bola_1, Goalee, Goalee_left, Goalee_right, Shootturn, seconds, selected_index, selected_option, game_reset)
            game_reset = False
            if Game_values_list != None:
                Player_points += Game_values_list[1]
                Enemy_points += Game_values_list[2]
                Game_values_list = []
                selected_option = None
                shoot = False
                game_reset = True
                first_enter = True
                enemy_player_index = (enemy_player_index + 1) % len(enemy_player_list)
                team_player_index= (team_player_index + 1) % len(final_player_list)


                if Shootturn == "ENEMY":
                    Shootturn = "YOU"
                else:
                    Shootturn = "ENEMY"
                current_screen = "MAIN_GAME2"


        elif current_screen == "MAIN_GAME2":


            game_constants_screen(screen,Gfont,Nfont, Field_frontal, team_sprites, selected_team, enemy_team, selected_gamemode, final_player_list, enemy_player_list, Shootturn, team_player_index, enemy_player_index, current_round)
            Game_values_list= gameloop_screen(screen,Titlefont,Hfont, Bola_1, Goalee, Goalee_left, Goalee_right, Shootturn, seconds, selected_index, selected_option, game_reset)
            game_reset = False
            if Game_values_list !=None:
                turn_change = Game_values_list [0]
                Player_points += Game_values_list[1]
                Enemy_points += Game_values_list[2]
                Game_values_list = []
                selected_option = None
                shoot = False
                game_reset = True
                first_enter = True
                if Shootturn == "ENEMY":
                    Shootturn = "YOU"
                else:
                    Shootturn = "ENEMY"


                current_screen = "STATS_SCREEN"
                turn_change = None
                first_enter = True
                game_reset = True


        elif current_screen == "STATS_SCREEN":
            stats_screen_list = stats_screen(screen, Hfont, Mbackground, Field_frontal, current_round, Player_points, Enemy_points, seconds, game_reset)
            game_reset = False
            if stats_screen_list !=None:
                turn_change= stats_screen_list[0]


                if turn_change == "switch":
                    current_screen = "REPEAT_CINEMATIC"
                    turn_change = None
                    current_round +=1
                    game_reset= True
                elif turn_change == "end_screen":
                    current_screen = "RESULTS_SCREEN"
                    Final_scores, Final_scores_ENEMY = stats_screen_list[1], stats_screen_list[2]
                    print(Final_scores, Final_scores_ENEMY)
                for i, score in enumerate(Final_scores):
                    player_index = i % len(final_player_list)
                    combined_list.append([score, final_player_list[player_index]])


                for i, score in enumerate(Final_scores_ENEMY):
                    player_index = i % len(enemy_player_list)
                    combined_list_ENEMY.append([score, enemy_player_list[player_index]])
                    print(combined_list)
                    print(combined_list_ENEMY)
                    player_scores, total_scores_and_fails = analyze_scores(combined_list)
                    print(player_scores)
                    player_scores_ENEMY, total_scores_and_fails_ENEMY = analyze_scores(combined_list_ENEMY)
                    print(player_scores_ENEMY)
                    update_top_scores(player_scores, "Top_shooters.txt")
                    update_top_scores(player_scores_ENEMY, "Top_shooters.txt")
                    add_team_stats(total_scores_and_fails, "team_stats.txt")
                    add_team_stats(total_scores_and_fails_ENEMY, "team_stats.txt")
       
        elif current_screen == "REPEAT_CINEMATIC":
            turn_change = cinematic_screen(screen, Celebration1, Celebration2, Ubackground, seconds, game_reset)
            game_reset = False




            if turn_change == "player_select":
                if selected_gamemode == "MANUAL":
                    final_player_list= []
                    players_selection_text = ""
                    game_position_index = 0
                    game_change_ready = False
                    game_reset = False
                    selected_index = 1
                    current_screen = "PLAYERS_SELECT"
                    game_positions = {
                        "Shooter1":"",
                        "Shooter2":"",
                        "Goalee":""
                    }


                else:
                    current_screen = "MAIN_GAME"
                    selected_index = 0
                    selected_option = None
                    shoot = False
                    game_reset = True
                    first_enter = True
                    Game_values_list = []
                    enemy_player_index = (enemy_player_index + 1) % len(enemy_player_list)
                    team_player_index= (team_player_index + 1) % len(final_player_list)


        elif current_screen == "RESULTS_SCREEN":
            results_screen(screen, Hfont, Mbackground, Field_frontal, current_round, Player_points, Enemy_points, seconds, game_reset)
        # Update the display and cap the frame rate
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

