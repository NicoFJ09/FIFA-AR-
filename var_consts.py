RUNNING = True
start_time = 0
seconds = 0
#RECIEVED RASPBERRY PI VALUES
data = 0
prev_pot_value=0

#Colors
WHITE=(255,255,255)
WINE_RED = (123, 3, 35)
VIOLET = (127, 0, 255)
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
selected_option = "MAIN MENU"

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

Gamemode_options = ["MANUAL", "AUTOMATIC"]
selected_gamemode = ""

game_position_index = 0

players_selection_text = ""
game_change_ready = False
game_positions = {
    "Shooter1":"",
    "Shooter2":"",
    "Goalee":""
}
