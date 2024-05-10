RUNNING = True
#Time variables
start_time = 0
seconds = 0
Main_game_time = 0


#RECIEVED RASPBERRY PI VALUES
data = 0
prev_pot_value=0

#Colors
WHITE=(255,255,255)
WINE_RED = (123, 3, 35)
WINE_RED_SEMITRANSPARENT = (123, 3, 35, 128)
VIOLET = (127, 0, 255)
VIOLET_SEMITRANSPARENT = (127, 0, 255, 128)
NAVY_BLUE = (0, 0, 128)
OVERLAY_GRAY = (128,128,128,128)

#Screen dimensions
HWIDTH=1200
HHEIGHT=900

MWIDTH = 900
MHEIGHT = 675

PAGE_WIDTH = 675
PAGE_HEIGHT = 450


#Game section conditional
game_section= "intro"
prev_game_section = None
#Home screen
current_screen = "HOME"
selected_index = 0


#Game variables
volume = True
game_section = "intro"
music_playing = True

#Index management 
Initial_entry = True
Home_options = ["START", "GAME INFO", "TOP PLAYERS", "ABOUT"]
Info_options = ["1/3", "2/3", "3/3"]

#Gameplay constants

selected_team =""
enemy_team = ""

Gamemode_options = ["MANUAL", "AUTOMATIC"]
selected_gamemode = ""

game_position_index = 0
final_player_list = []
players_selection_text = ""
game_change_ready = False
game_positions = {
    "Shooter1":"",
    "Shooter2":"",
    "Goalee":""
}

#PREGAME VARIABLES
first_enter = True
transition_duration = 2
Shootturn = ""

# GAME VARIABLES
team_player_index = 0
enemy_player_index = 0
current_round = 1
game_start_time = 0
countdown_time=3

goal_positions = [
    (162, 120, 149, 378),
    (311, 120, 149, 378),
    (460, 120, 149, 378),
    (609, 120, 149, 378),
    (758, 120, 149, 378),
    (907, 120, 149, 378)
]

Defense_options = ["3 lateral blocks", "2 lateral blocks", "3 separated blocks"]

initial_ball_pos = (504,804)
selected_option = None
target_position = None
blocked_positions= []
shoot = False
shot_result = ""