#------------------------------------------
#----------PixelQuest v3.3.3.1-------------
#------------------------------------------

#-Created:      WED 9TH SEPTEMBER 2026-----
#-Last updated: FRI 18TH SEPTEMBER 2026----

#------------------------------------------
#-----------MODULES------------------------
#------------------------------------------
import time
import termios
import sys
import tty
import select
import random
import textwrap

#------------------------------------------ 
#-----------VARIABLES----------------------
#------------------------------------------

version = "v3.3.3.1"
player = ""
hp = 0
mp = 0
gold = 0
xp = 0
menu = ["", "", ""]
menu_pos = 0
is_menu_open = False
text = ["", "", "", "", "", ""]
grid = ["", "", "", "", "", ""]
#is_talk_open checks if the talk menu is open
is_talk_open = False
#can talk is for npcs when talking to them. sometimes you cannot talk to them as there is none nearby.
can_talk = ""
inventory = []
is_inventory_open = False
options = ["", "", "", "", "", ""]
options_pos = 0
is_options_open = False
battle_filler = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
keypress = ""
search = False
#0 is nothing, 1 is yes, 2 is no
yes = 0
#option type - is_yes - get_out_castle
option_type = ""

is_starter_menu_gameloop = False
is_gameloop = False
is_intro = False
is_map_open = False
start_story = False

talk_count = 0

#----------TIME VARIABLES------------------
delay = 0.2
actual_fps = 0
fps = 100
start_time = time.time()
frames_from_start = 0


#-----------STORY VARIABLES----------------
ruby = False
have_met_ramu_king = False

#------------------------------------------
#-----------COLOURS------------------------
#------------------------------------------
GRASS       = "\033[48;5;34m"
DARK_GRASS  = "\033[48;5;22m"
WATER       = "\033[48;5;27m"
DEEP_WATER  = "\033[48;5;18m"
LIGHT_WATER = "\033[48;5;117m"
SAND        = "\033[48;5;220m"
DESERT      = "\033[48;5;178m"
DIRT        = "\033[48;5;130m"
STONE       = "\033[48;5;240m"
DARK_STONE  = "\033[48;5;236m"
LAVA        = "\033[48;5;196m"
MAGIC       = "\033[48;5;129m"
POISON      = "\033[48;5;118m"
SNOW        = "\033[48;5;255m"
ICE         = "\033[48;5;153m"
FIRE        = "\033[48;5;208m"
GOLD        = "\033[48;5;220m"
BLACK       = "\033[48;5;0m"
MAROON      = "\033[48;5;1m"
DARK_GREEN  = "\033[48;5;2m"
OLIVE       = "\033[48;5;3m"
DARK_BLUE   = "\033[48;5;4m"
PURPLE      = "\033[48;5;5m"
TEAL        = "\033[48;5;6m"
SILVER      = "\033[48;5;7m"
GREY        = "\033[48;5;8m"
RED         = "\033[48;5;9m"
GREEN       = "\033[48;5;10m"
YELLOW      = "\033[48;5;11m"
BLUE        = "\033[48;5;12m"
MAGENTA     = "\033[48;5;13m"
CYAN        = "\033[48;5;14m"
WHITE       = "\033[48;5;15m"
DARK_GREY   = "\033[48;5;16m"
NAVY        = "\033[48;5;17m"
DARK_BLUE2  = "\033[48;5;18m"
DARK_BLUE3  = "\033[48;5;19m"
BLUE2       = "\033[48;5;20m"
BLUE3       = "\033[48;5;21m"
DARK_CYAN   = "\033[48;5;23m"
CYAN2       = "\033[48;5;24m"
DARK_TEAL   = "\033[48;5;30m"
TEAL2       = "\033[48;5;31m"
AQUA        = "\033[48;5;37m"
LIGHT_CYAN  = "\033[48;5;51m"
DARK_GREEN2 = "\033[48;5;22m"
FOREST      = "\033[48;5;28m"
GREEN2      = "\033[48;5;34m"
LIME        = "\033[48;5;46m"
LIGHT_GREEN = "\033[48;5;82m"
MINT        = "\033[48;5;121m"
DARK_RED    = "\033[48;5;52m"
RED2        = "\033[48;5;88m"
CRIMSON     = "\033[48;5;124m"
RED3        = "\033[48;5;160m"
LIGHT_RED   = "\033[48;5;203m"
SALMON      = "\033[48;5;210m"
DARK_ORANGE = "\033[48;5;130m"
BROWN       = "\033[48;5;94m"
ORANGE      = "\033[48;5;208m"
LIGHT_ORANGE = "\033[48;5;214m"
PEACH       = "\033[48;5;216m"
DARK_YELLOW = "\033[48;5;58m"
YELLOW2     = "\033[48;5;226m"
LIGHT_YELLOW = "\033[48;5;229m"
CREAM       = "\033[48;5;230m"
DARK_PURPLE = "\033[48;5;54m"
PURPLE2     = "\033[48;5;91m"
VIOLET      = "\033[48;5;129m"
LIGHT_PURPLE = "\033[48;5;177m"
LAVENDER    = "\033[48;5;183m"
DARK_PINK   = "\033[48;5;89m"
PINK        = "\033[48;5;125m"
HOT_PINK    = "\033[48;5;198m"
LIGHT_PINK  = "\033[48;5;218m"
ROSE        = "\033[48;5;211m"
DARK_BROWN  = "\033[48;5;52m"
BROWN2      = "\033[48;5;58m"
TAN         = "\033[48;5;137m"
LIGHT_BROWN = "\033[48;5;180m"
BEIGE       = "\033[48;5;223m"
SLATE       = "\033[48;5;60m"
DARK_SLATE  = "\033[48;5;59m"
LIGHT_SLATE = "\033[48;5;103m"
STEEL       = "\033[48;5;67m"
LIGHT_BLUE2 = "\033[48;5;117m"
CHARCOAL    = "\033[48;5;235m"
DARK_GREY2  = "\033[48;5;238m"
GREY2       = "\033[48;5;244m"
MEDIUM_GREY = "\033[48;5;248m"
LIGHT_GREY  = "\033[48;5;250m"
OFF_WHITE   = "\033[48;5;254m"

RESET = "\033[0m"
#------------------------------------------
#-----------MAP----------------------------
#------------------------------------------
current_map = []
player_x = 20
player_y = 7
width = 16
height = 8
mapname = ""
map_height = 0
map_width = 0
start_x = 0
start_y = 0
map_x = 0
map_y = 0

ramu_castle_map = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,5,5,5,5,5,5,5,6,6,5,5,5,5,6,6,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,5,5,5,6,6,5,5,5,6,6,5,5,6,6,5,5,5,6,6,5,5,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,5,5,6,6,6,5,5,5,5,5,5,5,5,5,5,6,6,6,5,5,3,3,3,3,3,3,3,4,3,3,3],
    [3,3,3,3,3,3,3,3,3,5,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,5,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,5,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,5,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,5,5,5,5,5,5,5,5,5,5,2,2,5,5,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3],
    [3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,12,12,12,12,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3],
]

ramu_castle_map_floor_2 = [
  [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,9,9,9,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,9,8,9,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,9,8,9,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,10,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
  [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
]

world_map = [
  [ 1,  1, 11, 13, 11, 13, 11, 11, 13, 11, 1 , 13, 13, 13,  1, 13,],
  [ 1, 11,  1, 11, 13, 13, 13, 11,  1,  1, 11, 13,  1, 11,  13,  1],
  [11, 13,  5,  5,  5,  5,  5,  5,  5, 11, 13, 13, 13,  1,  13,  1],
  [13,  5,  5,  3,  3,  3,  3,  3,  5,  5, 13,  5,  5,  5,  11, 13],
  [ 1,  5,  3,  3,  2,  3,  3,  3,  3,  4,  5,  3,  3,  3,   5,  1],
  [13,  5,  4,  3,  3,  3,  4,  3,  4,  3,  3,  3,  4, 12,   5,  1],
  [ 1,  1,  5,  5,  3,  4,  5,  5,  3,  3,  3,  5,  5,  5,  13,  1],
  [ 1, 11,  1, 11,  5,  5, 13,  5,  5,  5,  5, 13, 13, 13,  13,  1],
  [ 1,  1, 11, 13, 11, 13, 11, 11, 13, 11, 1 , 13,  1,  1,  13,  1],
]

ladar = [
  [6,6,6,5,6,6,4,3,3,4,3,4,33],
  [6,5,6,6,6,6,4,4,3,3,3,3,33],
  [6,6,6,6,6,6,4,3,3,4,3,4,33],
  [5,6,6,5,6,12,3,3,3,3,4,3,33],
  [6,6,6,6,12,12,3,3,3,3,3,4,33],
  [4,3,3,3,3,4,3,3,3,3,3,3,33],
  [3,4,3,3,3,3,3,3,3,3,3,3,33],
  [33,33,33,33,33,33,33,33,33,33,33,33,33],
]

ladar_floor_1 = [
  [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
  [6,7,7,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7,6],
  [6,7,12,7,7,7,6,6,7,6,7,7,7,7,7,7,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,7,6,6,6,6,6,6,6,7,6],
  [6,6,6,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,7,7,7,7,7,7,7,7,7,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,6,6,6,6,6,6,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,6,7,6],
  [6,7,6,7,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,6,6,7,6],
  [6,7,6,6,7,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7,7,6,7,7,7,7,7,7,7,6],
  [6,7,6,6,7,6,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,7,7,7,7,7,6,7,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,7,6],
  [6,7,6,6,7,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,6,6,6,6,6,6,6,7,6,7,7,7,7,7,7,6,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,7,6],
  [6,7,6,6,6,7,6,6,7,6,7,7,7,7,7,7,6,7,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,6,7,6,7,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,6,7,6,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,7,6,7,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,7,6,7,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7,6,7,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,6,6,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,7,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,7,6,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,7,6,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,7,6,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,7,6,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,7,6,7,6,7,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,7,7,6,7,6,7,7,7,7,7,7,7,7,6,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,7,6,6,7,6,7,6,6,6,6,6,6,7,6,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,7,6,6,7,6,7,6,7,7,7,7,6,7,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,7,6,6,7,6,7,6,7,7,7,7,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,7,6,6,7,6,7,6,7,7,7,7,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,7,6,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,7,6,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,6],
  [6,7,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,6],
  [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
]

ladar_floor_2 = [
  [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,99,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6],
  [6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,6],
  [6,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66],
]

def update_map(mapname):
  global grid, player_x, player_y, width, height, map_height, map_width, is_map_open
  if is_map_open:
    #this part means that the map's height is how many things are in the list so that means that it is the map's y value
    map_height = len(mapname)
  
    #it means how many values are in the first row of mapname.
    map_width = len(mapname[0])
  
    start_x = player_x - width // 2
    start_y = player_y - height // 2
  
    grid = []
  
    for y in range(height):
      row = ""
      
      for x in range(width):
        map_x = start_x + x
        map_y = start_y + y
    
        if map_x < 0 or map_x >= map_width or map_y < 0 or map_y >= map_height:
          row += BLACK + "  " + RESET
    
          # Player
        elif map_x == player_x and map_y == player_y:
          row += CYAN + "  " + RESET 
    
        # Map
        elif mapname[map_y][map_x] == 0:
          row += GREY + "  " + RESET
        elif mapname[map_y][map_x] == 1:
          row += TEAL + "  " + RESET
        elif mapname[map_y][map_x] == 2:
          row += BROWN + "  " + RESET
        elif mapname[map_y][map_x] == 3:
          row += GRASS + "  " + RESET
        elif mapname[map_y][map_x] == 4:
          row += DARK_GRASS + "  " + RESET
        elif mapname[map_y][map_x] == 5:
          row += DARK_STONE + "  " + RESET
        elif mapname[map_y][map_x] == 6:
          row+= STONE + "  " + RESET
        elif mapname[map_y][map_x] == 7:
          row += STEEL + "  " + RESET
        elif mapname[map_y][map_x] == 8:
          row += RED + "  " + RESET
        elif mapname[map_y][map_x] == 9:
          row += GOLD + "  " + RESET
        elif mapname[map_y][map_x] == 10:
          row += MINT + "  " + RESET
        elif mapname[map_y][map_x] == 11:
          row += BLUE + "  " + RESET
        elif mapname[map_y][map_x] == 12:
          row += BROWN2 + "  " + RESET
        elif mapname[map_y][map_x] == 13:
          row += DARK_BLUE + "  " + RESET
        elif mapname[map_y][map_x] == 55:
          row += BLACK + "  " + RESET
        elif mapname[map_y][map_x] == 33:
          row += GRASS + "  " + RESET
        elif mapname[map_y][map_x] == 66:
          row += STONE + "  " + RESET
        elif mapname[map_y][map_x] == 99:
          row+=RED3 + "  " + RESET
           
    
      grid.append(row)
    
    while len(grid) < 8:
        grid.append("")
  

#------------------------------------------
#-----------ENEMIES/BATTLE-----------------
#------------------------------------------

# to add an ememy, first add name to strength_level and then add to enemy list

strength_level1 = ["slime", "blob", "banana"]
enemy_count = len(strength_level1) - 1

#enemy = [min damage, max damage, enemy_hp, gold, XP]
#  "ant": [1, 3, 6, 3, 2],
enemy_attack_list = {
  "slime": [1, 2, 5, 2, 2],
  "blob": [0, 2, 7, 3, 2],
  "banana": [1, 2, 3, 2, 1], 
}

#"attack_name": [hp done to enemy, mp used]
attack_list = {
  "punch": [2, 0],
  "kick": [3, 0]
}

#8x9 grid for enemies
slime = [
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 55, 11, 55, 55, 55, 55],
  [55, 55, 55, 11, 11, 11, 55, 55, 55],
  [55, 55, 11, 11, 11, 11, 11, 55, 55],
  [55, 55, 11, 11, 11, 11, 11, 55, 55],
  [55, 55, 11, 11, 11, 11, 11, 55, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
]

blob = [
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 55, 8, 55, 55, 55, 55],
  [55, 55, 55, 8, 8, 8, 55, 55, 55],
  [55, 55, 8, 8, 8, 8, 8, 55, 55],
  [55, 55, 8, 8, 8, 8, 8, 55, 55],
  [55, 55, 8, 8, 8, 8, 8, 55, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
]

banana = [
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 55,  2, 55, 55, 55, 55],
  [55, 55, 55,  9,  9, 55, 55, 55, 55],
  [55, 55, 55,  9,  9, 55, 55, 55, 55],
  [55, 55, 55,  9,  9,  8,  8, 55, 55],
  [55, 55, 55,  9,  9,  9,  8, 55, 55],
  [55, 55, 55, 55,  9, 55, 55, 55, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
]

hit = [
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
  [8, 8, 8, 8, 8, 8, 8, 8, 8],
]

enemy_appearances = {
  "slime": slime,
  "blob": blob,
  "banana": banana,
}

enemy_appearance = []

is_battle = False
is_enemy_vanquished = False
enemy_selected = False
enemy = ""
enemy_hp = 0
attack = ""
enemy_chance = 0


def battle():
  global is_battle, enemy_hp, enemy, enemy_count, is_enemy_vanquished, is_gameloop, attack, option_type, hp, mp, text, options_pos, gold, xp, can_talk, is_talk_open, hit, enemy_attack_list, option_type, is_menu_open, menu_pos, keypress

  for i in range(10):
    ftype("")

  text = ["", "", "", "", "", ""]
  is_enemy_vanquished = False
  if is_battle:
    options_pos = 1
    option_type = "battle"
    enemy = random.choice(strength_level1)
    enemy_hp = enemy_attack_list[enemy][2]
    
    update_enemy(enemy_appearances[enemy])

    text[0] = f"{enemy} has appeared!"
    time.sleep(1)
    clear_screen()
    clear_screen()
    print("")
    battle_menu()
    
    while is_battle:
      text = ["", "", "", "", "", ""]
      text[0] = f"{enemy}"
      text[1] = ""
      text[2] = f"HP: {enemy_hp}"
      text[3] = ""
      text[5] = ""
      
      check_keyboard()
      update_variables()

      if attack != "":
        update_enemy(hit)
        clear_screen()
        battle_menu()
        time.sleep(0.2)
        update_enemy(enemy_appearances[enemy])
        damage = attack_list[attack][0]
        mp = mp - attack_list[attack][1]
        enemy_hp -= damage
        attack = ""
        
      if enemy_hp < 1:
        is_enemy_vanquished = True

      clear_screen()
      battle_menu()
      time.sleep(1/fps)
      
      if is_enemy_vanquished:
        option_type = ""
        is_battle = False
        enemy_hp = 0
        text = ["", "", "", "", "", ""]
        ftype("Enemy gone!")
        ftype(f"You got {enemy_attack_list[enemy][3]} gold and {enemy_attack_list[enemy][4]} XP.")
        gold += enemy_attack_list[enemy][3]
        xp += enemy_attack_list[enemy][4]
        time.sleep(2)
        option_type = "default"
        keypress = ""
        can_talk = ""        # Close all menus after battle
        is_menu_open = False
        is_options_open = False
        is_talk_open = False
        is_inventory_open = False
        is_menu_open = True
        menu_pos = 1        # <-- add: always land on "Talk", not a stale position
        options_pos = 1     # <-- add: same for options
        keypress = ""

        # Flush any keystrokes buffered by the OS during battle
        # (mashed enter/arrows) so they aren't replayed as menu input
        try:
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
        except Exception:
            pass

        clear_screen()
        keypress = ""
        
        battle_filler = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    

def battle_test():
  global is_battle
  old_settings = termios.tcgetattr(sys.stdin)
  tty.setraw(sys.stdin.fileno())
  is_battle = True
  battle()

def update_enemy(enemy):
  global enemy_appearance

  if is_battle:
    start_x = 0
    start_y = 0

    enemy_appearance = []

    for y in range(8):
      row = ""

      for x in range(9):

        if enemy[y][x] == 55:
          row += BLACK + "  " + RESET
        elif enemy[y][x] == 11:
          row += BLUE + "  " + RESET
        elif enemy[y][x] == 8:
          row += RED + "  " + RESET
        elif enemy[y][x] == 9:
          row += GOLD + "  " + RESET
        elif enemy[y][x] == 2:
          row += BROWN + "  " + RESET

      enemy_appearance.append(row)

    while len(enemy_appearance) < 8:
      enemy_appearance.append("")

#------------------------------------------
#-----------VOCATIONS----------------------
#------------------------------------------
vocations = {
  #"vocation": [ATK, DEF, HPGWT, MPGWT]
  "mage": [2,5,2,6]
}

#------------------------------------------
#-----------MAIN---------------------------
#------------------------------------------

def main():
  starter_menu_gameloop()
  gameloop()

#------------------------------------------
#-----------GAME UI------------------------
#------------------------------------------

def update_gameUI():
  print(f"""
  ┌─────────────────────────────────────────────────────────────────────────┐
  |                                                                         |
  |   {grid[0]:<33}  |   ╔════════════╗  ╔════════════╗  |
  |   {grid[1]:<33}  |   ║ {player:<11}║  ║   MENU     ║  |
  │   {grid[2]:<33}  |   ╠════════════╣  ╠════════════╣  |
  │   {grid[3]:<33}  |   ║ HP: {hp:<4}   ║  ║{menu[0]:<12}║  |
  │   {grid[4]:<33}  |   ║ MP: {mp:<4}   ║  ║{menu[1]:<12}║  |
  │   {grid[5]:<33}  |   ║ Gold:{gold:<6}║  ║{menu[2]:<12}║  |
  |   {grid[6]:<33}  |   ╚════════════╝  ║            ║  |
  │   {grid[7]:<33}                      ╠════════════╣  |
  │  ╔═══════════════════════════════════════════════════╗  ║ Options    ║  |
  |  ║  Text                                             ║  ╠════════════╣  |
  |  ║     {text[0]:<46}║  ║{options[0]:<12}║  |
  |  ║     {text[1]:<46}║  ║{options[1]:<12}║  |
  |  ║     {text[2]:<46}║  ║{options[2]:<12}║  |
  |  ║     {text[3]:<46}║  ║{options[3]:<12}║  |
  |  ║     {text[4]:<46}║  ║{options[4]:<12}║  |
  |  ║     {text[5]:<46}║  ║{options[5]:<12}║  |
  |  ╚═══════════════════════════════════════════════════╝  ╚════════════╝  |
  |                                                                         |
  └─────────────────────────────────────────────────────────────────────────┘
""")

#starter menu UI update
def update_starter_menu():
  print(f"""
  ┌─────────────────────────────────────────────────────────────────────────┐
  |                                                                         |
  |   {grid[0]:<67}   |
  |   {grid[1]:<67}   |
  |   {grid[2]:<67}   |
  |   {grid[3]:<67}   |
  |   {grid[4]:<67}   |
  |   {grid[5]:<67}   |
  |                                                                         |
  |                                                                         |
  |                                                                         |
  |                                                                         |
  │  ╔═══════════════════════════════════════════════════════════════════╗  |
  |  ║  Text                                                             ║  |
  |  ║  {text[0]:<65}║  |
  |  ║  {text[1]:<65}║  |
  |  ║  {text[2]:<65}║  |
  |  ║  {text[3]:<65}║  |
  |  ║  {text[4]:<65}║  |
  |  ║  {text[5]:<65}║  |
  |  ╚═══════════════════════════════════════════════════════════════════╝  |
  └─────────────────────────────────────────────────────────────────────────┘
""")

def battle_menu():
  print(f"""
  ┌─────────────────────────────────────────────────────────────────────────┐
  |                                                                         |
  |   {grid[0]:<75} | {enemy_appearance[0]:<18} ╔════════════╗  |
  |   {grid[1]:<75} | {enemy_appearance[1]:<18} ║ {player:<11}║  |
  │   {grid[2]:<75} | {enemy_appearance[2]:<18} ╠════════════╣  |
  │   {grid[3]:<75} | {enemy_appearance[3]:<18} ║ HP: {hp:<4}   ║  |
  │   {grid[4]:<75} | {enemy_appearance[4]:<18} ║ MP: {mp:<4}   ║  |
  │   {grid[5]:<75} | {enemy_appearance[5]:<18} ║            ║  |
  |   {grid[6]:<75} | {enemy_appearance[6]:<18} ║            ║  |
  │   {grid[7]:<75}   {enemy_appearance[7]:<18} ╠════════════╣  |
  │  ╔═══════════════════════════════════════════════════╗  ║ Options    ║  |
  |  ║  Text                                             ║  ╠════════════╣  |
  |  ║     {text[0]:<46}║  ║{options[0]:<12}║  |
  |  ║     {text[1]:<46}║  ║{options[1]:<12}║  |
  |  ║     {text[2]:<46}║  ║{options[2]:<12}║  |
  |  ║     {text[3]:<46}║  ║{options[3]:<12}║  |
  |  ║     {text[4]:<46}║  ║{options[4]:<12}║  |
  |  ║     {text[5]:<46}║  ║{options[5]:<12}║  |
  |  ╚═══════════════════════════════════════════════════╝  ╚════════════╝  |
  |                                                                         |
  └─────────────────────────────────────────────────────────────────────────┘
""")

def battle_filler_screen():
  print(f"""
  ┌─────────────────────────────────────────────────────────────────────────┐
  |   {battle_filler[0]:<68}  |
  |   {battle_filler[1]:<68}  |
  |   {battle_filler[2]:<68}  |
  |   {battle_filler[3]:<68}  |
  |   {battle_filler[4]:<68}  |
  |   {battle_filler[5]:<68}  |
  |   {battle_filler[6]:<68}  |
  |   {battle_filler[7]:<68}  |
  |   {battle_filler[8]:<68}  |
  |   {battle_filler[9]:<68}  |
  |   {battle_filler[10]:<68}  |
  |   {battle_filler[11]:<68}  |
  |   {battle_filler[12]:<68}  |
  |   {battle_filler[13]:<68}  |
  |   {battle_filler[14]:<68}  |
  |   {battle_filler[15]:<68}  |
  |   {battle_filler[16]:<68}  |
  |   {battle_filler[17]:<68}  |
  |   {battle_filler[18]:<68}  |
  |   {battle_filler[19]:<68}  |
  └─────────────────────────────────────────────────────────────────────────┘
""")

  
#------------------------------------------
#----------GAMELOOP------------------------
#------------------------------------------
  
def gameloop():
  global hp, mp, gold
  #game_intro is in the castle
  game_intro()
  time.sleep(1)
  clear_screen()
  
  while is_gameloop == True:
    clear_screen()
  
    if is_battle:
      battle()
    else:
      check_keyboard()
      update_variables()
  
      if is_options_open:
        update_gameUI()
        update_map(mapname)
      elif is_talk_open:
        update_gameUI()
        update_map(mapname)
      elif is_inventory_open:
        update_gameUI()
        update_map(mapname)
      else:
        update_gameUI()
        update_map(mapname)
  
    time.sleep(1/fps)


def byebye():
  while True:
    print(" ")
    clear_screen()
    time.sleep(1/fps)

def starter_menu_gameloop():
  global is_starter_menu_gameloop, is_intro
  clear_screen()
  is_starter_menu_gameloop = True
  is_intro = True
  old_settings = termios.tcgetattr(sys.stdin)
  tty.setraw(sys.stdin.fileno())
  is_gameloop = False
  while is_starter_menu_gameloop == True:
    clear_screen()
    intro()
    check_keyboard()
    update_variables()
    update_starter_menu()
    time.sleep(1/fps)
  
#------------------------------------------
#-----------UPDATE VARIABLES---------------
#------------------------------------------

def update_variables():
  global player, hp, mp, gold, menu, menu_pos, text, options, grid, fps, keypress, is_gameloop, is_starter_menu_gameloop, is_intro, is_menu_open, is_options_open, menu_pos, options_pos, yes, option_type, is_talk_open, is_inventory_open, can_talk, inventory, player_x, player_y, mapname, is_map_open, is_battle, enemy, enemy_hp, attack, enemy_chance, battle_filler, search, ruby, have_met_ramu_king, actual_fps, start_time, frames_from_start

  #During the starter menu gameloop if keypress is not down, up, left, right, enter or backspace then the keypress is logged onto the text below.
  
  if is_starter_menu_gameloop == True:
    if keypress not in ("down", "up", "left", "right", "enter", "backspace", "space"):
      text[0] = text[0] + keypress
    if keypress == "backspace":
      text[0] = text[0][:-1]
    if keypress == "space":
      text[0] = text[0] + " "
  
    #if name is saved and the intro ends
    if keypress == "enter":
      player = text[0]
      player = player
      clear_screen()
      text[0] = ""
      update_starter_menu()
      time.sleep(1)
      grid[3] = f"Name saved! {player}"
      clear_screen()
      update_starter_menu()
      text[5] = "Loading game..."
      clear_screen()
      update_starter_menu()
      time.sleep(2)
      clear_screen()
      text = ["", "", "", "", "", ""]
      grid = ["", "", "", "", "", "", "", ""]
      is_starter_menu_gameloop = False
      is_gameloop = True
      is_intro = False

  
  if mapname == world_map:
    enemy_chance = 0
  if mapname == ramu_castle_map:
    enemy_chance = 0
  if mapname == ramu_castle_map_floor_2:
    enemy_chance = 0
  if mapname == ladar:
    enemy_chance = 0
  if mapname == ladar_floor_1:
    enemy_chance = 0
  if mapname == ladar_floor_2:
    enemy_chance = 0

  #during gameloop, the menu logic.
  if is_gameloop == True:
    
    if is_menu_open:
      menu = ["  Talk", "  Inventory", "  Options"]
      if menu_pos == 0:
        menu = ["  Talk", "  Inventory", "  Options"]
      if menu_pos == 1:
        menu = ["▶ Talk", "  Inventory", "  Options"]
      elif menu_pos == 2:
        menu = ["  Talk", "▶ Inventory", "  Options"]
      elif menu_pos == 3:
        menu = ["  Talk", "  Inventory", "▶ Options"]
      if keypress == "down":
        menu_pos = menu_pos + 1
      if keypress == "up":
        menu_pos = menu_pos - 1
      if menu_pos > 3:
        menu_pos = 1
      if menu_pos < 1:
        menu_pos = 3

    if is_options_open == True:
      menu_pos = 0
      is_menu_open = False
      if keypress == "up":
        options_pos = options_pos - 1
      if keypress == "down":
        options_pos = options_pos + 1

      if option_type == "is_yes":
        options = ["  Yes", "  No", "", "", "", ""]
        if options_pos == 0:
          options = ["  Yes", "  No", "", "", "", ""]
        if options_pos == 1:
          options = ["▶ Yes", "  No", "", "", "", ""]
        if options_pos == 2:
          options = ["  Yes", "▶ No", "", "", "", ""]
        if options_pos > 2:
          options_pos = 1
        if options_pos < 1:
          options_pos = 2
          
      if option_type == "":
        options = ["", "", "", "", "", ""]

    if not is_options_open:
      options = ["", "", "", "", "", ""]

    if not is_menu_open:
      menu = ["", "", ""]

    if keypress == "enter" and is_menu_open:

      if menu_pos == 1:
          # TALK
          is_talk_open = True
          is_inventory_open = False
          is_options_open = False

      elif menu_pos == 2:
          # INVENTORY
          is_inventory_open = True
          is_talk_open = False
          is_options_open = False
  
      elif menu_pos == 3 and option_type == "" and not is_battle:
          # OPTIONS
          ftypel()
          ftype("Options not available")
          clear_screen()
          is_options_open = False
          is_talk_open = False
          is_inventory_open = False
          is_menu_open = True
          options_pos = 1
          keypress = ""
        
      elif menu_pos == 3 and option_type != "" and not is_battle:
          # OPTIONS
          is_options_open = True
          is_talk_open = False
          is_inventory_open = False
          is_menu_open = False
          options_pos = 1
          keypress = ""

    if is_inventory_open and not is_battle:
      ftypel()
      ftype(inventory[0])
      ftype("Inventory:")
      clear_screen()
      is_inventory_open = False

    #can_talk text
    if is_talk_open and can_talk != "" and not is_battle and ruby == False:
      ftypel()
    
      for line in textwrap.wrap(can_talk, width=45):
        ftype(line)
    
      clear_screen()
      is_talk_open = False

    if is_talk_open and can_talk != "" and not is_battle and ruby == False:
      ftypel()
      ftype(can_talk)
      clear_screen()
      is_talk_open = False
        
    if keypress == "enter" and options_pos == 1 and is_options_open == True and option_type == "is_yes":
      yes = 1
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
    if keypress == "enter" and options_pos == 2 and is_options_open == True and option_type == "is_yes":
      yes = 2
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      options_pos = 0

  if is_options_open and option_type == "default" and not is_battle:
      options = ["  Door", "  Team", "  Search", "  FPS", "", ""]
      if options_pos == 0:
        options = ["  Door", "  Team", "  Search", "  FPS", "", ""]
      if options_pos == 1:
        options = ["▶ Door", "  Team", "  Search", "  FPS", "", ""]
      if options_pos == 2:
        options = ["  Door", "▶ Team", "  Search", "  FPS", "", ""]
      if options_pos == 3:
        options = ["  Door", "  Team", "▶ Search", "  FPS", "", ""]
      if options_pos == 4:
        options = ["  Door", "  Team", "  Search", "▶ FPS", "", ""]
      if options_pos > 4:
        options_pos = 1
      if options_pos < 1:
        options_pos = 4

  if keypress == "enter" and option_type == "default" and is_options_open:
    if options_pos == 1:
      ftypel()
      ftype("Sorry no door here!")
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      options_pos = 0
      keypress = ""
    elif options_pos == 2:
      ftypel()
      ftype(f"{player}: HP:{hp}, MP:{mp}, GOLD:{gold}")
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      options_pos = 0
      keypress = ""
    elif options_pos == 3:
      ftype("Searching...")
      search = True
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      keypress = ""
    elif options_pos == 4:
      ftypel()
      actual_fps = float(actual_fps)
      actual_time = time.time()
      time_elapsed = actual_time - start_time
      actual_fps = frames_from_start / time_elapsed
      ft(f"Target FPS: {fps}, True FPS: {actual_fps:.1f}")
      ft(f"Do you want to change your FPS?")
      option_type = "is_yes"
      will_continue = False
      yes = 0
      is_map_open = False
      is_options_open = True
      is_talk_open = False
      is_inventory_open = False
      menu_pos = 1
      ft("")
      text[0] = ""
      
      while will_continue == False:
        check_keyboard()
        update_variables()
        clear_screen()
        update_gameUI()
        time.sleep(1/fps)
        if yes == 1:
          yes = 0
          is_options_open = False
          option_type = ""
          ft("to?")
          ft("What would you like to change your Target FPS")
          ft("")
          will_continue_ = False
          
          while will_continue_ == False:
            check_keyboard()
            update_variables()
            clear_screen()
            update_gameUI()
            time.sleep(1/fps)
            is_menu_open = False
            newFps = fps
            if keypress == "enter":
              if text[0].isdigit():
                newFps = int(text[0])
                if newFps >= 1:
                  will_continue_ = True
                  fps = newFps
                  option_type = "default"
                  is_menu_open = True
                else:
                  text[0] = ""
                  ft("Sorry. The fps is too low.")
            if keypress == "backspace":
              text[0] = text[0][:-1]
            if keypress.isdigit():
              text[0] = text[0] + keypress
          ft(f"Target FPS: {fps}")
          newFps = 0
          will_continue = True
        if yes == 2:
          clear_screen()
          is_options_open = False
          is_map_open = True
          is_talk_open = False
          is_inventory_open = False
          is_menu_open = True
          will_continue = True
          option_type = "default"
        
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      options_pos = 1
      keypress = ""
      
  if is_map_open and not is_options_open and not is_talk_open and not is_inventory_open and not is_battle:
    # Work out where the player wants to go
    if keypress == "w":
        new_x = player_x
        new_y = player_y - 1
    elif keypress == "s":
        new_x = player_x
        new_y = player_y + 1
    elif keypress == "a":
        new_x = player_x - 1
        new_y = player_y
    elif keypress == "d":
        new_x = player_x + 1
        new_y = player_y
    else:
        new_x = player_x
        new_y = player_y

    # Check that the new position is inside the map
    if 0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[0]):
        # Check if the new position is NOT a wall
      if mapname[new_y][new_x] != 5 and mapname[new_y][new_x] != 6 and mapname[new_y][new_x] != 9:
            # Move the player
          
        player_x = new_x
        player_y = new_y
        if mapname[new_y][new_x] == 2:
          time.sleep(0.2)
          if mapname == ramu_castle_map:
            mapname = ramu_castle_map_floor_2
            player_x = 20
            player_y = 10
            enemy_chance = 0
          elif mapname == ramu_castle_map_floor_2:
            mapname = ramu_castle_map
            player_x = 20
            player_y = 7
            enemy_chance = 0
          elif mapname == world_map:
            mapname = ramu_castle_map
            player_x = 20
            player_y = 7
            enemy_chance = 0
          elif mapname == ladar:
            mapname = world_map
            player_x = 12
            player_y = 5
            enemy_chance = 10
          elif mapname == ladar_floor_1:
            mapname = ladar
            player_x = 6
            player_y = 4
            enemy_chance = 5

        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 12):
          time.sleep(0.05)
          if mapname == ramu_castle_map:
            mapname = world_map
            player_x = 5
            player_y = 6
            enemy_chance = 10
            time.sleep(0.1)
          elif mapname == world_map:
            time.sleep(0.1)
            mapname = ladar
            player_x = 10
            player_y = 6
            enemy_chance = 5
          elif mapname == ladar:
            time.sleep(0.05)
            mapname = ladar_floor_1
            player_x = 43
            player_y = 38
            enemy_chance = 5
          elif mapname == ladar_floor_1:
            mapname = ladar_floor_2
            player_x = 19
            player_y = 16
            enemy_chance = 0
        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 33):
          if mapname == ladar:
            mapname = world_map
            player_x = 12
            player_y = 5
            enemy_chance = 10
        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 66):
          if mapname == ladar_floor_2:
            mapname = world_map
            player_x = 12
            player_y = 5
            enemy_chance = 10

        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 99) and search == True:
          if mapname == ladar_floor_2:
            inventory.insert(0, "Ruby")
            time.sleep(0.5)
            ftype("Found a ruby!")
            ruby = True
            search = False
            enemy_chance = 0

        if keypress in ("w", "a", "s", "d"):
          if random.randint(1, 100) <= enemy_chance:
            for i in range(20):
              battle_filler_screen()
              battle_filler[i] = "-----------------------------------------------------------------" 
              time.sleep(0.05)
              clear_screen()
            is_battle = True
             
    update_map(mapname)
    battle_filler = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    

  if is_battle:
    if option_type == "battle":
      
      if keypress == "down":
        options_pos += 1
        

      if keypress == "up":
        options_pos -= 1

      if options_pos > 2:
        options_pos = 1

      if options_pos < 1:
        options_pos = 2
        
      options = [">Punch", " Kick", "", "", "", ""]
      if options_pos == 1:
        options = [">Punch", " Kick", "", "", "", ""]
      if options_pos == 2:
        options = [" Punch", ">Kick", "", "", "", ""]

      if keypress == "enter" and options_pos == 1:
        time.sleep(0.2)
        attack = "punch"
      if keypress == "enter" and options_pos == 2:
        time.sleep(0.2)
        attack = "kick"

  
   # Talking logic here
  if mapname == ramu_castle_map_floor_2 and mapname[player_y][player_x] == 10:
    if ruby == True and is_talk_open and keypress == "enter":
      keypress = ""
      time.sleep(1)
      can_talk = f"Well done {player}! You have finished your quest!"
      ftypel()
      ft("Do you want another quest?")
      ft("and I will also give you another quest!")
      gold += 300
      ft("In return, I will give you 300 gold!")
      ft("Thank you so much for bringing back my ruby!")
      yes = 0
      is_map_open = False
      is_options_open = True
      is_talk_open = False
      is_inventory_open = False
      menu_pos = 1
      option_type = "is_yes"
      will_continue = False
      while will_continue == False:
        check_keyboard()
        update_variables()
        clear_screen()
        update_gameUI()
        time.sleep(1/fps)
        if yes == 1:
          yes = 0
          is_options_open = False
          option_type = ""
          ftype("Great!")
          ftype("You said yes")
          will_continue = True
        if yes == 2:
          is_options_open = False
          option_type = "is_yes"
          ftype("You said no. Are you sure?")
    elif have_met_ramu_king:
      can_talk = "Go to Ladar tower to the east"
      ftypel()
      clear_screen()
      ft("the east of the castle!")
      clear_screen()
      ft("Can you go and take a look for me? Its to ")
      clear_screen()
      ft("yesterday and I could have dropped it there!")
      clear_screen()
      ft("I can't find it! I went to Ladar tower ")
      clear_screen()
    elif not have_met_ramu_king:
      ftypel()
      ft("if you can't find it.")
      clear_screen()
      ft("you try and find it for me? Come back to me")
      clear_screen()
      ft("my room and I can't find it anywhere! Can ")
      clear_screen()
      ft("Last night, my favorite ruby was taken from")
      clear_screen()
      have_met_ramu_king = True

#------------------------------------------
#-----------UTILITIES----------------------
#------------------------------------------

#ttype is typewriter type for short. It types characters one by one with a pause of 0.05 seconds between each one.
def ttype(type):
  for i in range(len(type)):
    print(type[i], end="", flush = True)
    time.sleep(0.05)

#clear_screen clears the terminal screen.
def clear_screen():
  global frames_from_start
  print("\033[2J\033[H", end="")
  frames_from_start += 1

#ftype a line
def ftypel():
  ftype("---------------------------")

#adding text in the grid place.
def ftype(type):
  global text
  clear_screen()
  text.insert(0, type)
  text.pop()
  time.sleep(delay)
  update_gameUI()
  

#it is ftype but with a delay, ftyped
def ftyped(type):
  global text, delay
  clear_screen()
  text.insert(0, type)
  text.pop()
  update_gameUI()

def ft(type):
  clear_screen()
  global text
  text.insert(0, type)
  text.pop()
  time.sleep(0.05)
  update_gameUI()
  
#check_keyboard checks the keyboard after every key input.
def check_keyboard():
  global keypress
  keypress = ""
  
  if select.select([sys.stdin], [], [], 0)[0]:
    key = sys.stdin.read(1)
    if key == "\x1b":
      key += sys.stdin.read(2)
    #key = up, down, left, right, enter, backspace, space
    if key == "\x1b[A":
      keypress = "up"
    elif key == "\x1b[B":
      keypress = "down"
    elif key == "\x1b[D":
      keypress = "left"
    elif key == "\x1b[C":
      keypress = "right"
    elif key in ("\n", "\r"):
      keypress = "enter"
    elif key in ("\x7f", "\x08"):
      keypress = "backspace"
    elif key == " ":
      keypress = "space"
    #key = a, b, c, d, e, ... z
    elif key.isalpha():
      keypress = key.lower()
    elif key.isdigit():
      keypress = key

#------------------------------------------
#-----------INTRO - STORYLINE--------------
#------------------------------------------
#intro is where player gets its variable name

def intro():
  global text, is_intro
  if is_intro:
    grid[1] = "Please choose a name for your character"
    grid[0] = f"Welcome to PixelQuest {version}" 
    time.sleep(1/fps)
    clear_screen()

def game_intro():
  global hp, mp, gold, is_menu_open, menu_pos, yes, option_type, is_options_open, options_pos, can_talk, delay, inventory, mapname, is_map_open, talk_count, grid
  delay = 0.01
  grid = ["", "", "", "", "", "", "", ""]
  is_map_open = False
  for i in range(7):
    time.sleep(delay)
    ftype("")
  hp = 10
  mp = 0
  gold = 10
  ft("Do you want to go on a quest?")
  is_gameloop = True
  time.sleep(delay)
  mapname = ramu_castle_map
  is_map_open = True
  update_map(mapname)
  ftypel()
  yes = 0
  is_menu_open = False
  is_options_open = True
  menu_pos = 1
  option_type = "is_yes"
  while yes == 0:
    check_keyboard()
    update_variables()
    clear_screen()
    update_gameUI()
    time.sleep(1/fps)
  if yes == 1:
    yes = 0
    is_options_open = False
    option_type = ""
    ftype("Great!")
    ftype("You said yes")
    time.sleep(delay*10)
  if yes == 2:
    yes = 0
    is_options_open = False
    option_type = ""
    ft("Goodbye.")
    ftype("You said no.")
    print("Bye!")
    time.sleep(1)
    sys.exit()
  can_talk = f"Try going to the king!"
  option_type = "default"
  talk_count = 0
  
main()

