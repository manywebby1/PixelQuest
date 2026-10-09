#------------------------------------------
#----------PixelQuest v3.4.6.2-------------
#------------------------------------------

#-Created:      WED 9TH SEPTEMBER 2026-----
#-Last updated: THU 1ST OCTOBER 2026-------

#PixelQuest v3-----------------------------
#PixelQuest v3.2.1 - Audio test - removed
#in v3.2.2
#
#PixelQuest v3.2.2 - Extra map additions
#and code additions
#
#PixelQuest v3.2.3 - Battle additions, 
#battle_filler added.
#
#PixelQuest v3.2.4 - Fixed battle bugs and 
#changed teleportation xy coordinates
#
#PixelQuest v3.2.5 - battle()
#v3.2.5.1 - Added battle monster sprites
#v3.2.5.2 - Added hit animation
#v3.2.5.3 - Fixed some battle bugs
#
#PixelQuest v3.3.0 - battle()
#v3.3.0.1 - All bugs fixed! + new features
#Working battle system with map and 1 quest
#but quest not finished. 
#v3.3.0.2 - battle() + fixes!
#v3.3.0.3 - can_talk + textwrap
#
#PixelQuest - v3.3.1 - Quest 1
#v3.3.1.0 - made ladar floor 1 map
#v3.3.1.1 - fixed inventory and ladar floor
#2 and added ruby
#v3.3.1.2 - made king say that player 
#finished their first quest
#v3.3.1.3 - fixed bug where it says sorry
#no door here all the time
#
#PixelQuest - v3.3.2 - FPS
#v3.3.2.1 - Added FPS functionalities into
#the menu
#
#PixelQuest - v3.3.3 - Do you want to go on
#a quest?
#v3.3.3.1 - Added no feature
#
#PixelQuest - v3.3.4 - Added Saving feature
#v3.3.4.1 - Added saving feature
#v3.3.4.2 - Fixed line 1289 - met ramu king
#
#PixelQuest - v3.3.5 - Added inventory
#v3.3.5.1 - Inventory functions
#v3.3.5.2 - Major inventory update
#v3.3.5.3 - When items are eqipped, they 
#turn green.
#
#PixelQuest - v3.4.1 - Fixed Bugs
#v3.4.1.1 - Fixed all bugs, gameloop(), 
#game_intro, added break.
#
#PixelQuest - v3.4.2 - Can_talk fixes
#v3.4.2.1 - Fixed try going to king text.
#
#PixelQuest - v3.4.3 - Added page 2 to 
#options - "default"
#v3.4.3.1 - Added page 2 to "default"
#v3.4.3.2 - Edited page to of "default"
#
#PixelQuest - v3.4.4 - Added Twilight town
#v3.4.4.1 - Added twilight town
#v3.4.4.2 - Added map_name variable
#v3.4.4.3 - Fixed battle enemy damage
#
#PixelQuest - v3.4.5 - Added if hp >= 0 in 
#battle.
#v3.4.5.1 - Added hp >= 0 functionality
#v3.4.5.2 - Added attack names for enemies
#
#PixelQuest - v3.4.6 - Added usable items
#v3.4.6.1 - Added usable items like Green
#herb and green leaf
#v3.4.6.2 - Fixed inn bugs
#
#
#
#NOTES: add more attacks and make the enemy
#attack as well





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
import base64
import pickle

#------------------------------------------ 
#-----------VARIABLES----------------------
#------------------------------------------

version = "v3.4.6.2"
menu = ["", "", ""]
menu_pos = 0
is_menu_open = False
text = ["", "", "", "", "", ""]
grid = ["", "", "", "", "", ""]
#is_talk_open checks if the talk menu is open
is_talk_open = False
#can talk is for npcs when talking to them. sometimes you cannot talk to them as there is none nearby.
can_talk = ""
inventory = ["Plain Clothes", "Dull Sword", "", "", "", "", "", "", "", ""]
inv_txt = ["", "", "", ""]
choosing = False
arrow = ["", "", "", "", "", "", "", "", "", ""]
is_inventory_open = False
options = ["", "", "", "", "", ""]
options_pos = 0
options_page = 1
is_options_open = False
battle_filler = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
keypress = ""
search = False
#0 is nothing, 1 is yes, 2 is no
yes = 0
#option type - is_yes - get_out_castle
option_type = ""
map_name = ""

is_starter_menu_gameloop = False
is_gameloop = False
is_intro = False
is_map_open = False
start_story = False

talk_count = 0
old_settings = termios.tcgetattr(sys.stdin)

moves_per_page = 3   # near enemy_selected / attack / etc.
move_page = 0

buyable = []

#----------TIME VARIABLES------------------
delay = 0.2
actual_fps = 0
fps = 100
start_time = time.time()
frames_from_start = 0

#-----------CHARACTER VARIABLES------------
ATK = 1
DEF = 1
base_ATK = 1
base_DEF = 1
player = ""
hp = 0
hp = int()
mp = 0
mp = int()
gold = 0
gold = int()
xp = 0
lvl = 1
max_hp = 10
max_mp = 2
hp = 10
mp = 2
gold = 30

#For main character
next_lvl = [
  [10,15,20,25,30,35,40,50,57,60,70,75,130,140,150,160,170,180,190,200,220,240,260,280,300,330,360,390,420,460,1000000000000],#XP to next level
  [1,2,2,3,4,5,6,7,8,9,10,11,13,14,15,17,18,19,20,21,22,24,26,28,30,31,33,34,36,37,40,41],#ATK
  [1,2,2,3,5,6,8,9,9,10,11,12,13,14,16,17,19,20,21,22,24,25,26,29,31,32,33,34,35,36,38,40],#DEF
  [10,11,12,14,15,17,19,20,21,23,24,26,28,30,31,33,34,35,37,38,39,41,42,43,45,47,49,50,51,53,55,57,59,60],#HP
  [2,2,3,5,6,7,8,9,10,11,12,12,12,13,14,15,16,17,18,19,20,21,22,23,23,24,25,26,27,28,29,30,31,31,32,33,34,35,36,37,38,39,40,41,42],#MP
]

#-----------STORY VARIABLES----------------
ruby = False
have_met_ramu_king = False
is_first_island_completed = False

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
TEXT_RED    = "\033[38;5;9m"
TEXT_GREEN  = "\033[38;5;10m"
TEXT_YELLOW = "\033[38;5;11m"
TEXT_BLUE   = "\033[38;5;12m"
TEXT_GOLD   = "\033[38;5;220m"
TEXT_WHITE  = "\033[38;5;15m"

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
  [ 1,  1, 11, 13, 11, 13, 11, 11, 13, 11, 1 , 13, 13, 13,   1, 13, 11, 11, 13,  1, 13, 11],
  [ 1, 11,  1, 11, 13, 13, 13, 11,  1,  1, 11, 13,  1, 11,  13,  1,  1, 13, 13, 11,  1, 13],
  [11, 13,  5,  5,  5,  5,  5,  5,  5, 11, 13, 13, 13,  1,   5,  5,  1,  1, 11, 13, 11, 11],
  [13,  5,  5,  3,  3,  3,  3,  3,  5,  5,  5,  5,  5,  5,   3,  3,  5,  5,  1, 11, 11,  1],
  [ 1,  5,  3,  2,  3,  3,  3,  3,  3,  4,  3,  3,  3,  3,   3,  3,  4,  5,  1,  1, 13, 13],
  [13,  1,  5,  3,  3,  3,  3,  3,  4,  3,  3,  3,  4, 12,   4,  3,  3,  3,  5,  1, 11, 13],
  [13,  5,  3,  3,  4,  3,  4,  3,  3,  3,  3,  3,  4,  4,   3,  3,  3,  4,  3,  5,  1, 11],
  [13, 11,  5,  3,  3,  3,  3,  3,  3,  3,  5,  5,  5,  5,   3,  3,  3,  4,  3,  5, 13,  1],
  [13, 13,  5,  3,  3,  3,  3,  3,  3,  5, 11, 13, 13, 11,   5,  3,  3,  3,  3,  3,  5, 11],
  [13, 11,  5,  3,  3,  3,  4,  3,  4,  5, 11,  1,  1, 11,   5,  3,  3,  4,  3,  5,  1,  1],
  [13,  5,  4,  3,  3,  3,  3,  3,  3,  3,  5,  5,  5,  5,   3,  3,  3,  3, 14,  5,  1, 13],
  [ 1,  1,  5,  3,  3,  4,  3,  3,  3,  3,  3,  3,  3,  3,   3,  3,222, 14,  5, 13,  1, 11],
  [ 1,  1, 11,  5,  3,  3,  5,  5,  3,  3,  3,  4,  3,  3,  14, 14, 14, 14,  5, 11,  1, 11],
  [ 1, 11,  1, 11,  5,  5, 13,  5,  5,  4,  5,  3,  3, 14,  14,  5,  5,  5, 11, 13, 13,  1],
  [ 1,  1, 11, 13, 11, 13, 11, 11,  5,102,  5,  5,  5,  5,  13,  1, 13, 13, 11,  1, 11,  1],
  [ 1,  1, 11, 13, 11, 13, 11, 11,  5,101,  5, 13, 13, 13,   1, 13, 11, 11, 13,  1, 13, 11],
  [ 1, 11,  1, 11, 13, 13, 13, 11,  1,  1, 11, 13,  1, 11,  13,  1,  1, 13, 13, 11,  1, 13],
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

twilight_town = [
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,15,15,15,15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,15,15,15,302,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,15,15,15,15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,15,15,15,15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,15,151,152,301,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,15,15,15,15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
  [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
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
        elif mapname[map_y][map_x] == 14:
          row += SAND + "  " + RESET
        elif mapname[map_y][map_x] == 222:
          row += DARK_BROWN + "  " + RESET
        elif mapname[map_y][map_x] == 15:
          row += DARK_BROWN + "  " + RESET
        elif mapname[map_y][map_x] == 151:
          row += DARK_BROWN + "IN" + RESET
        elif mapname[map_y][map_x] == 152:
          row += DARK_BROWN + "N " + RESET

        #NPCs
        elif mapname[map_y][map_x] == 301:
          row += BLUE + "  " + RESET
        elif mapname[map_y][map_x] == 302:
          row += BLUE + "  " + RESET

        #special story blocks
        elif mapname[map_y][map_x] == 101:
          row += STONE + "  " + RESET
        elif mapname[map_y][map_x] == 102:
          row += GRASS + "  " + RESET
           
    
      grid.append(row)
    
    while len(grid) < 8:
        grid.append("")
  

#------------------------------------------
#-----------ENEMIES/BATTLE-----------------
#------------------------------------------

# to add an ememy, first add name to strength_level and then add to enemy list
strength_level = 1
strength_level1 = ["slime", "blob", "banana"]
strength_level2 = ["blobby", "banana"]
strength_level3 = ["wet_banana", "banana", "blobby"]
enemy_count_str_lvl = ""
if strength_level == 1:
  enemy_count_str_lvl = len(strength_level1)
if strength_level == 2:
  enemy_count_str_lvl = len(strength_level2)
  
enemy_count = enemy_count_str_lvl - 1

current_category = ""

#enemy = [min damage, max damage, enemy_hp, gold, XP, ["move names"]]
#  "ant": [1, 3, 6, 3, 2],
enemy_attack_list = {
  "slime": [1, 2, 5, 2, 2, ["wobble", "slimy"]],
  "blob": [0, 2, 7, 3, 2, ["wobble", "blob"]],
  "banana": [1, 2, 3, 2, 1, ["slip", "rotten smell"]], 
  "blobby": [1,4,5,9,3, ["wobbly wobble", "wobble wobble"]],
  "wet_banana": [2,4,7,5,5, ["slip", "wet slip"]],
}

#"attack_name": [hp done to enemy, mp used, lvl unlocked, type]
attack_list = {
  "punch": [2, 0, 1, "physical"],
  "kick": [3, 0, 1, "physical"],
  "fireball": [5,1,1, "fire"],
  "fire": [3,1,0, "fire"],
  "bang": [7,2,2, "fire"],
  "heal": [0,0,1,"heal"],
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

wet_banana = [
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 55,  2, 55, 55, 55, 55],
  [55, 55, 55,  9,  9, 55, 55, 55, 55],
  [55, 55, 55,  9,  9, 55, 55, 55, 55],
  [55, 55, 55,  9,  9,  1,  1, 55, 55],
  [55, 55, 55,  9,  9,  1,  1, 55, 55],
  [55, 55, 55, 55,  9, 55, 55, 55, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
]

blobby = [
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
  [55, 55, 55, 11, 11, 11, 55, 55, 55],
  [55, 55, 11, 11,  9, 11, 11, 55, 55],
  [55, 55, 11, 11, 11,  9, 11, 55, 55],
  [55, 11,  9, 11, 11, 11, 11, 11, 55],
  [55, 55, 55, 55, 55, 55, 55, 55, 55],
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
  "blobby": blobby,
}

enemy_appearance = []

is_battle = False
is_enemy_vanquished = False
enemy_selected = False
enemy = ""
enemy_hp = 0
attack = ""
enemy_chance = 0
dam = 0

def battle():
  global is_battle, enemy_hp, enemy, enemy_count, is_enemy_vanquished, is_gameloop, attack, option_type, hp, mp, text, options_pos, gold, xp, can_talk, is_talk_open, hit, enemy_attack_list, option_type, is_menu_open, menu_pos, keypress, is_options_open, is_inventory_open, mapname, player_x, player_y, max_hp, gold, player_x, player_y
  for i in range(10):
    ftype("")

  is_menu_open = False        # <-- add
  is_options_open = False     # <-- add
  is_talk_open = False        # <-- add
  is_inventory_open = False 

  text = ["", "", "", "", "", ""]
  is_enemy_vanquished = False
  if is_battle:
    options_pos = 1
    option_type = "battle"
    if strength_level == 1:
      enemy = random.choice(strength_level1)
    elif strength_level == 2:
      enemy = random.choice(strength_level2)
    elif strength_level == 3:
      enemy = random.choice(strength_level3)
      
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

      if enemy_hp <= 1:
        is_enemy_vanquished = True

      if hp <= 0:
        clear_screen()
        black_screen()
        time.sleep(2)
        typewriter("You died.", 0.1)
        time.sleep(2)
        is_battle = False
        mapname = ramu_castle_map
        gold = gold//2
        player_x = 20
        player_y = 10
        hp = max_hp
        mp = max_mp
        menu_pos = 1
        options_pos = 1
        keypress = ""
        clear_screen()
        break

      if attack != "":
        if attack == "heal":
          hp += 10
          mp -= 1
          if hp >= max_hp:
            hp = max_hp

        else:
          update_enemy(hit)
          clear_screen()
          battle_menu()
          time.sleep(0.2)
          update_enemy(enemy_appearances[enemy])
          damage = round(attack_list[attack][0] + ATK * 0.45)
          if damage < 1:
            damage = 1
          mp = mp - attack_list[attack][1]
          enemy_hp -= damage
          text = ["", "", "", "", "", ""]
          text[0] = f"You used {attack} and did {damage} damage!"
          clear_screen()
          battle_menu()
          time.sleep(1.5)
          
          dam = round(random.randint(enemy_attack_list[enemy][0], enemy_attack_list[enemy][1]) - DEF/3)
  
          if (enemy_attack_list[enemy][1]//2) > dam:
            dam = enemy_attack_list[enemy][1]//2
          
          if dam <= 1:
            dam = 1
            
          hp -= dam
          text = ["", "", "", "", "", ""]
          enemy_attack = random.choice(enemy_attack_list[enemy][5])
          text[0] = f"{enemy} used {enemy_attack} and did {dam} damage."
          clear_screen()
          battle_menu()
          dam = 0
          time.sleep(1.5)

      clear_screen()
      battle_menu()
      attack = ""
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
        is_map_open = True
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

        for i in range(10):
          ft("")
        
        battle_filler = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

def battle_test():
  global is_battle, old_settings
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
        elif enemy[y][x] == 1:
          row += TEAL + "  " + RESET

      enemy_appearance.append(row)

    while len(enemy_appearance) < 8:
      enemy_appearance.append("")

#------------------------------------------
#-----------INVENTORY----------------------
#------------------------------------------
#[ATK + , DEF +, equip/item, item type, +hp/+mp,gold cost] 
items = {
  "Plain Clothes": [0,1,"equip",5],
  "Copper Shield": [0,3,"equip",15],
  
  "Dull Blade": [1,0,"equip",10],
  "Copper Blade": [1.5,0,"equip",14],
  "Tin Blade": [1.7,0,"equip",19],
  "Dull Sword": [2,0,"equip",21],
  
  "Ruby": [0,0,"item","story"],
  
  "Green Herb": [0,0,"item","herb",20,10],
  "Orange Herb": [0,0,"item","herb",30,20],
  
  "Green Leaf": [0,0,"item","leaf",5,10],
  "Orange Leaf": [0,0,"item","leaf",10,15],
}

equipped = ["", "", ""]

inventory_item = 0
is_eqipped = False

def open_inventory():
  global is_inventory_open, keypress, arrow_pos, arrow_char, is_options_open, is_talk_open, is_inventory_open, is_menu_open, menu_pos, arrow, inv_txt, inventory, inventory_item, ATK, DEF, is_eqipped
  
  arrow_char = "▶"
  arrow[0] = arrow_char
  arrow_pos = 0
  inventory_item = find_len_inventory()
  
  while is_inventory_open:
    check_keyboard()
    update_variables()
    time.sleep(1/fps)
    
    for i in range(len(inventory)):
      base = inventory[i].replace(TEXT_GREEN, "").replace(RESET, "").strip()
      if base != "" and base in equipped:
        inventory[i] = TEXT_GREEN + f"{base:<67}" + RESET
      else:
        inventory[i] = base

    clear_screen()
    inventory_screen()
    
    if keypress == "up":
      arrow_pos -= 1
      keypress = ""
    if keypress == "down":
      arrow_pos += 1
      keypress = ""
    if keypress == "left":
      is_inventory_open = False
      keypress = ""
    if keypress == "enter":
      item = inventory[arrow_pos].replace(TEXT_GREEN, "").replace(RESET, "").strip()
      inventory_selected(item)
      keypress = ""
      
    if inventory_item == 0:
      arrow_pos = 0
    elif arrow_pos > inventory_item - 1:
      arrow_pos = 0
    elif arrow_pos < 0:
      arrow_pos = inventory_item - 1

    arrow = ["", "", "", "", "", "", "", "", "", ""]
    arrow[arrow_pos] = arrow_char

    inventory_item = find_len_inventory()
        
  is_options_open = False
  is_talk_open = False
  is_inventory_open = False
  is_menu_open = True
  menu_pos = 1
  options_pos = 1
  keypress = ""

def inventory_selected(item):
  global inv_txt, inventory_item, keypress, ATK, DEF, is_eqipped
  inv_txt[0] = f"What would you like to do with the {item}?"
  inv_txt[1] = "▶ Equip/Use"
  inv_txt[2] = "  Unequip"
  inv_txt[3] = "  Throw away"

  inventory_loop = True
  inv_txt_pos = 1
  keypress = ""
  
  while inventory_loop == True:
    check_keyboard()
    time.sleep(1/fps)
    clear_screen()
    inventory_screen()
    if keypress == "up":
      inv_txt_pos -= 1
      keypress = ""
    if keypress == "down":
      inv_txt_pos += 1
      keypress = ""
    if inv_txt_pos == 1:
      inv_txt[1] = "▶ Equip/Use"
      inv_txt[2] = "  Unequip"
      inv_txt[3] = "  Throw away"
    if inv_txt_pos == 2:
      inv_txt[1] = "  Equip/Use"
      inv_txt[2] = "▶ Unequip"
      inv_txt[3] = "  Throw away"
    if inv_txt_pos == 3:
      inv_txt[1] = "  Equip/Use"
      inv_txt[2] = "  Unequip"
      inv_txt[3] = "▶ Throw away"
    if inv_txt_pos > 3:
      inv_txt_pos = 1
    if inv_txt_pos < 1:
      inv_txt_pos = 3
    if keypress == "enter":
      if inv_txt_pos == 1:
        if equipped[0] != "" and equipped[1] != "" and equipped[2] != "":
          inv_txt = ["", "", "", ""]
          inv_txt[0] = "Sorry you cannot equip more."
          time.sleep(0.5)
          inv_txt = ["", "", "", ""]
          inventory_loop = False
        else:
          if items[item][2] == "equip":
            add_to_equip(item)
          elif items[item] [2] == "item":
            print(f"Using {item}")
            use_item(item)
          
          if is_eqipped == False:
            ATK += items[item][0]
            DEF += items[item][1]
            inv_txt = ["", "", "", ""]
            inv_txt[0] = f"{item} is equipped!"
            time.sleep(0.5)
            inv_txt = ["", "", "", ""]
            inventory_loop = False
          else:
            inventory_loop = False
            is_eqipped = False
      if inv_txt_pos == 2:
        remove_from_equip(item)
        ATK -= items[item][0]
        DEF -= items[item][1]
        inv_txt = ["", "", "", ""]
        inv_txt[0] = f"{item} is unequipped!"
        time.sleep(0.5)
        inv_txt = ["", "", "", ""]
        inventory_loop = False
      if inv_txt_pos == 3:
        remove_from_inventory(item)
        inv_txt = ["", "", "", ""]
        inv_txt[0] = f"{item} is thrown away."
        time.sleep(0.5)
        inv_txt = ["", "", "", ""]
        inventory_loop = False
  
def use_item(item):
  global hp, mp
  if items[item][3] == "herb":
    hp += items[item][4]
    remove_from_inventory(item)
    ftype(f"HP: +{items[item][4]}")
    ftype(f"HP: {hp}, MP: {mp}")
  elif items[item][3] == "leaf":
    mp += items[item][4]
    remove_from_inventory(item)
    ftype(f"MP: +{items[item][4]}")
    ftype(f"HP: {hp}, MP: {mp}")

def buy_item(shop_type):
  global buyable
  if shop_type == "defence":
    buyable = ["Plain Clothes", "Copper Shield"]
  elif shop_type == "weapons":
    buyable = ["Dull Blade", "Copper Blade", "Tin Blade", "Dull Sword"]
  elif shop_type == "items":
    buyable = ["Green Herb", "Green Leaf"]
  else:
    ftype("Cannot buy right now. Check buy_item(shop_type)")
  buying(buyable)

def buying(buyable):
  global choosing, item_count, is_menu_open, is_options_open, menu_pos, option_type, options_pos, talk_count
  
  choosing = True
  item_count = 0
  
  for item in buyable:
    item_count += 1

  is_menu_open = False
  is_options_open = True
  menu_pos = 1
  option_type = "buying"
    
  while choosing:
    
    clear_screen()
    update_variables()
    check_keyboard()
    update_gameUI()
    time.sleep(1/fps)
      
  option_type = "default"
  options_pos = 1
  is_options_open = False
  talk_count = 0
  buyable = []
  
def add_to_inventory(thing):
  global inventory
  
  for i in range(len(inventory)):
    if inventory[i] == "":
      inventory[i] = thing
      break

def add_to_equip(thing):
  global equipped, is_eqipped

  if thing in equipped:
    inv_txt = ["", "", "", ""]
    inv_txt[0] = f"Sorry, but your item is already equipped."
    is_eqipped = True
  
  else:
    for i in range(len(equipped)):
      if equipped[i] == "":
        equipped[i] = thing
        break

def remove_from_inventory(thing):
  global inventory
  if thing in inventory:
    inventory.remove(thing)
    inventory.append("")

def remove_from_equip(thing):
  global equipped
  if thing in equipped:
    equipped.remove(thing)
    equipped.append("")

def find_len_inventory():
  global inventory
  inventory_item = 0
  for i in range(10):
    if inventory[i] != "":
      inventory_item += 1
    if inventory[i] == "":
      inventory_item = inventory_item

  return inventory_item
  
#------------------------------------------
#-----------INN----------------------------
#------------------------------------------
def rest_at_inn(gold_amount):
  global hp, mp, max_mp, max_hp, gold, is_options_open, option_type, options_pos, is_menu_open, menu_pos, yes
  ftype(f"Do you want to rest at the inn for {gold_amount}G?")
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
      ftype("Great! Goodnight!")
      if gold >= gold_amount:
        gold -= gold_amount
        time.sleep(delay*10)
        option_type = "default"
        options_pos = 1
        hp = max_hp
        mp = max_mp
        for i in range(2):
          black_screen()
          time.sleep(1)
        ftype(f"{player} HP: {hp}, MP: {mp}")
        break
      else:
        yes = 0
        ftype("Not enough Gold!")
        break
    elif yes == 2:
      yes = 0
      is_options_open = False
      option_type = ""
      ftype("Bye!")
      break

  option_type = "default"
  is_menu_open = True
  is_options_open = False
  menu_pos = 1

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
  │   {grid[5]:<33}  |   ║ G:{gold:<9}║  ║{menu[2]:<12}║  |
  |   {grid[6]:<33}  |   ║ Lvl: {lvl:<6}║  ║            ║  |
  │   {grid[7]:<33}      ╚════════════╝  ╠════════════╣  |
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
  global current_category
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
  │  ╔═══════════════════════════════════════════════════╗  ║ {current_category.capitalize():<11}║  |
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

def black_screen():
  print("")
  
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

def inventory_screen():
  print(f"""
  ┌─────────────────────────────────────────────────────────────────────────┐
  |                                                                         |
  |   {player:<10}                                                            |
  |   {arrow[0]:<1}{inventory[0]:<67}  |
  |   {arrow[1]:<1}{inventory[1]:<67}  |
  |   {arrow[2]:<1}{inventory[2]:<67}  |
  |   {arrow[3]:<1}{inventory[3]:<67}  |
  |   {arrow[4]:<1}{inventory[4]:<67}  |
  |   {arrow[5]:<1}{inventory[5]:<67}  |
  |   {arrow[6]:<1}{inventory[6]:<67}  |
  |   {arrow[7]:<1}{inventory[7]:<67}  |
  |   {arrow[8]:<1}{inventory[8]:<67}  |
  |   {arrow[9]:<1}{inventory[9]:<67}  |
  |                                                                         |
  │  ╔═══════════════════════════════════════════════════════════════════╗  |
  |  ║  Text                                                             ║  |
  |  ║  {inv_txt[0]:<65}║  |
  |  ║  {inv_txt[1]:<65}║  |
  |  ║  {inv_txt[2]:<65}║  |
  |  ║  {inv_txt[3]:<65}║  |
  |  ╚═══════════════════════════════════════════════════════════════════╝  |
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
    if is_battle:
      battle()
    else:
      check_keyboard()
      update_variables()
      update_map(mapname)     # build the map first
      clear_screen()
      update_gameUI()         # then draw it
  
    time.sleep(1/fps)


def byebye():
  while True:
    print(" ")
    clear_screen()
    time.sleep(1/fps)

def starter_menu_gameloop():
  global is_starter_menu_gameloop, is_intro, mapname
  mapname = ramu_castle_map
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
  global player, hp, mp, gold, menu, menu_pos, text, options, grid, fps, keypress, is_gameloop, is_starter_menu_gameloop, is_intro, is_menu_open, is_options_open, menu_pos, options_pos, yes, option_type, is_talk_open, is_inventory_open, can_talk, inventory, player_x, player_y, mapname, is_map_open, is_battle, enemy, enemy_hp, attack, enemy_chance, battle_filler, search, ruby, have_met_ramu_king, actual_fps, start_time, frames_from_start, save, is_first_island_completed, xp, ATK, DEF,lvl, strength_level, moves_per_page, move_page, current_category, base_ATK, base_DEF, max_hp, max_mp, options_page, buyable

  if is_battle:
    is_menu_open = False

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
    strength_level = 1
    map_name = "world_map"
  if mapname == ramu_castle_map:
    enemy_chance = 0
    strength_level = 1
    map_name = "ramu_castle_map"
  if mapname == ramu_castle_map_floor_2:
    enemy_chance = 0
    strength_level = 1
    map_name = "ramu_castle_map_floor2"
  if mapname == ladar:
    enemy_chance = 5
    strength_level = 1
    map_name = "ladar"
  if mapname == ladar_floor_1:
    enemy_chance = 10
    strength_level = 2
    map_name = "ladar_floor_1"
  if mapname == ladar_floor_2:
    enemy_chance = 0
    strength_level = 2
    map_name = "ladar_floor_2"
  if mapname == twilight_town:
    enemy_chance = 0
    strength_level = 2
    map_name = "twilight_town"

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

      if option_type == "save_load":
        options = ["  Save", "  Load", "", "", "", "  Back"]
        if options_pos == 0:
          options = ["  Save", "  Load", "", "", "", "  Back"]
        if options_pos == 1:
          options = ["▶ Save", "  Load", "", "", "", "  Back"]
        if options_pos == 2:
          options = ["  Save", "▶ Load", "", "", "", "  Back"]
        if options_pos == 3:
          options = ["  Save", "  Load", "", "", "", "▶ Back"]
        if options_pos > 3:
          options_pos = 1
        if options_pos < 1:
          options_pos = 3

      if option_type == "buying":
        buying_count = len(buying) - 1

        for items in buying:
          if options_pos == items:
            buying[options_pos] = buying[options_pos].insert(options_pos,"▶")
            buy_item = str(buying[options_pos])
                           
          for i in buying_count:
            buying[i+1] = buying[i+1].insert(0," ")

        if options_pos > (len(buying)-1):
          options_pos = 0
        if options_pos < 0:
          options_pos = len(buying) - 1
          
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
          is_menu_open = False
          keypress = ""
          open_inventory()
  
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

    if keypress == "enter" and option_type == "buying":
      if gold > items[buy_item][3]:
        add_to_inventory(buy_item)
        gold -= items[buy_item][3]
      else:
        ftype("Sorry. You do not have enough money...")
        
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

  if is_options_open and option_type == "default" and not is_battle and options_page == 1:
      options = ["  Door", "  Team", "  Search", "  FPS", "", "  Next Page"]
      if options_pos == 0:
        options = ["  Door", "  Team", "  Search", "  FPS", "", "  Next Page"]
      if options_pos == 1:
        options = ["▶ Door", "  Team", "  Search", "  FPS", "", "  Next Page"]
      if options_pos == 2:
        options = ["  Door", "▶ Team", "  Search", "  FPS", "", "  Next Page"]
      if options_pos == 3:
        options = ["  Door", "  Team", "▶ Search", "  FPS", "", "  Next Page"]
      if options_pos == 4:
        options = ["  Door", "  Team", "  Search", "▶ FPS", "", "  Next Page"]
      if options_pos == 5:
        options = ["  Door", "  Team", "  Search", "  FPS", "", "▶ Next Page"]
      if options_pos > 5:
        options_pos = 1
      if options_pos < 1:
        options_pos = 5
  elif is_options_open and option_type == "default" and not is_battle and options_page == 2:
    
      options = ["  Progress", "  Back", "", "", "", "  Previous"]
      if options_pos == 1:
        options = ["▶ Progress", "  Back", "", "", "", "  Previous"]
      if options_pos == 2:
        options = ["  Progress", "▶ Back", "", "", "", "  Previous"]
      if options_pos == 3:
        options = ["  Progress", "  Back", "", "", "", "▶ Previous"]

      if options_pos > 3:
        options_pos = 1
      if options_pos < 1:
        options_pos = 3

  if keypress == "enter" and option_type == "save_load" and is_options_open:
    if options_pos == 1:
      save = 1
    if options_pos == 2:
      save = 2
    if options_pos == 3:
      save = 0

  if keypress == "enter" and option_type == "default" and is_options_open and options_page == 1:
    if options_pos == 1:
      ftypel()
      ftype("Sorry no door here!")
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      options_pos = 0
      keypress = ""
    elif options_pos == 2:
      count = 0
      for i in range(3):
        if equipped[i] == "":
          count = count
        else:
          count += 1

      if count == 0:
        ftypel()
        ft(f"Nothing equipped.")
        ft(f"ATK: {ATK}, DEF: {DEF}")
        ftype(f"{player}: HP:{hp}, MP:{mp}, GOLD:{gold}")
      else:
        ftypel()
        ft(f"Equipped: {equipped[0]}, {equipped[1]}, {equipped[2]}")
        ft(f"ATK: {ATK}, DEF: {DEF}")
        ftype(f"{player}: HP:{hp}, MP:{mp}, GOLD:{gold}")
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      options_pos = 0
      keypress = ""
      
    elif options_pos == 3:
      ftypel()
      ftype(f"{map_name}")
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
          is_map_open = True
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

    elif options_pos == 5:
      options_page += 1
      options_pos = 1
      keypress = ""

  if keypress == "enter" and option_type == "default" and is_options_open and options_page == 2:
    if options_pos == 2:
      is_options_open = False
      is_map_open = True
      is_talk_open = False
      is_inventory_open = False
      is_menu_open = True
      will_continue = True
      option_type = "default"
      menu_pos = 1
      options_pos = 1
      options_page = 1
      
    elif options_pos == 3:
      options_page -= 1
      options_pos = 1

    elif options_pos == 1:
      load_or_save()
      
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
      if mapname[new_y][new_x] == 101 and not is_first_island_completed and search == True:
        player_x = player_x
        player_y = player_y
        ftypel()
        ft("Harbour not discovered")
        search = False
        # Check if the new position is NOT a wall
      elif mapname[new_y][new_x] != 5 and mapname[new_y][new_x] != 6 and mapname[new_y][new_x] != 9 and mapname[new_y][new_x] != 15:
          
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
          elif mapname == twilight_town:
            mapname = world_map
            player_x = 16
            player_y = 12

        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 12):
          time.sleep(0.05)
          if mapname == ramu_castle_map:
            mapname = world_map
            player_x = 4
            player_y = 5
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

        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 222):
          if mapname == world_map:
            mapname = twilight_town
            player_x = 17
            player_y = 24
            enemy_chance = 0

        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 99) and search == True:
          if mapname == ladar_floor_2:
            add_to_inventory("Ruby")
            time.sleep(0.5)
            ftype("Found a ruby!")
            ruby = True
            search = False
            enemy_chance = 0
            
        if (0 <= new_y < len(mapname) and 0 <= new_x < len(mapname[new_y]) and mapname[new_y][new_x] == 99) and is_first_island_completed == True and mapname == world_map and search == True: 
          ftypel()
          ft("This is a harbour")
          clear_screen()
          search = False

    if keypress in ("w", "a", "s", "d"):
      if random.randint(1, 100) <= enemy_chance:
        for i in range(20):
          battle_filler_screen()
          battle_filler[i] = "-----------------------------------------------------------------" 
          time.sleep(0.05)
          clear_screen()
        is_battle = True
        option_type = "battle"
           
        update_map(mapname)
        battle_filler = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    
  if is_battle:
      move_names = [name for name, stats in attack_list.items() if stats[2] <= lvl]
  
      # Group into categories, preserving first-seen order
      categories = []
      grouped = {}
      for name in move_names:
        cat = attack_list[name][3]
        if cat not in grouped:
          grouped[cat] = []
          categories.append(cat)
        grouped[cat].append(name)
  
      # Build a flat list of pages: each page is (category_name, chunk_of_moves)
      pages = []
      for cat in categories:
        cat_moves = grouped[cat]
        for i in range(0, len(cat_moves), moves_per_page):
          pages.append((cat, cat_moves[i:i + moves_per_page]))
  
      total_pages = max(len(pages), 1)
  
      if keypress == "right":
        move_page += 1
        options_pos = 1
      if keypress == "left":
        move_page -= 1
        options_pos = 1
      if move_page >= total_pages:
        move_page = 0
      if move_page < 0:
        move_page = total_pages - 1
  
      if pages:
        current_category, page_moves = pages[move_page]
      else:
        current_category, page_moves = "", []
  
      if keypress == "down":
        options_pos += 1
      if keypress == "up":
        options_pos -= 1
      if options_pos > len(page_moves):
        options_pos = 1
      if options_pos < 1:
        options_pos = len(page_moves) if page_moves else 1
  
      options = ["", "", "", "", "", ""]
  
      for i, move_name in enumerate(page_moves):
        label = move_name.capitalize()
        if options_pos == i + 1:
          options[i] = f">{label}"
        else:
          options[i] = f" {label}"
  
      if keypress == "enter" and page_moves and 1 <= options_pos <= len(page_moves):
        chosen_move = page_moves[options_pos - 1]
        mp_cost = attack_list[chosen_move][1]
        if mp >= mp_cost:
          time.sleep(0.2)
          attack = chosen_move
        else:
          ftype("Not enough MP!")

  if mapname == world_map and mapname[player_y][player_x] == 102 and search == True:
    ftypel()
    ft("You found something")
    search = False
  
   # Talking logic here

  if mapname == twilight_town and mapname[player_y][player_x] == 301 and is_talk_open:
    is_talk_open = False
    ftypel()
    rest_at_inn(15)

  if mapname == twilight_town and mapname[player_y][player_x] == 302 and is_talk_open:
    is_talk_open = False
    ftypel()
    buy_item("weapons")
    
  if mapname == ramu_castle_map_floor_2 and mapname[player_y][player_x] == 10:
    if not have_met_ramu_king and is_talk_open:
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
      is_talk_open = False
    
    elif ruby == True and is_talk_open and keypress == "enter" and have_met_ramu_king:
      keypress = ""
      time.sleep(1)
      can_talk = f"Well done {player}! You have finished your quest!"
      ftypel()
      ft("Do you want another quest?")
      ft("and I will also give you another quest!")
      gold += 300
      ft("In return, I will give you 300 gold!")
      ft("Thank you so much for bringing back my ruby!")
      remove_from_inventory("Ruby")
      remove_from_equip("Ruby")
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
          ftype("Ok. Now go and explore the rest of the island!")
          ftype("Great!")
          ftype("You said yes")
          will_continue = True
          is_map_open = True
        if yes == 2:
          is_options_open = False
          option_type = "is_yes"
          ftype("You said no. Are you sure?")
          is_map_open = True
    elif have_met_ramu_king and not is_first_island_completed and is_talk_open:
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
      is_talk_open = False
      is_map_open = True

  if xp > next_lvl[0][lvl-1]:
    lvl += 1
    xp = 0
    max_hp = next_lvl[3][lvl-1]
    max_mp = next_lvl[4][lvl-1]
    hp = max_hp
    mp = max_mp
    base_ATK = next_lvl[1][lvl-1]
    base_DEF = next_lvl[2][lvl-1]
    ATK = base_ATK + sum(items[e][0] for e in equipped if e in items)
    DEF = base_DEF + sum(items[e][1] for e in equipped if e in items)
    ft(f"You are now level {lvl}!")
    ft(f"HP: {hp}  MP: {mp}")
    ft(f"ATK: {ATK}  DEF: {DEF}")

  if is_talk_open and can_talk != "" and not is_battle and ruby == False:
      ftypel()
    
      for line in textwrap.wrap(can_talk, width=45):
        ftype(line)
    
      clear_screen()
      is_talk_open = False
 
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

def typewriter(text, delay):
  for i in text:
    print(text[i], end="")
    time.sleep(delay)

def invt(type):
  clear_screen()
  global inv_txt
  text.insert(0,type)
  text.pop()
  time.sleep(0.05)
  inventory_screen()

def load_or_save():
  global save, is_menu_open, is_options_open, option_type
  ft("Do you want to save or load a game?")
  ftypel()
  save = -1
  is_menu_open = False
  is_options_open = True
  option_type = "save_load"
  
  while save == -1:
    check_keyboard()
    update_variables()
    clear_screen()
    update_gameUI()
    time.sleep(1/fps)
    is_menu_open = False
    is_options_open = True
    option_type = "save_load"
    
    if save == 1:
      clear_screen()
      saving()
    if save == 2:
      clear_screen()
      decode()
    if save == 0:
      is_options_open = False
      options_pos = 1
      menu_pos = 1
      is_menu_open = True
      option_type = "default"
      break

def saving():
  global player, hp, mp, gold, xp, ATK, DEF, lvl, menu, menu_pos, is_menu_open, text, grid, is_talk_open, inventory, is_inventory_open, options, options_pos, is_options_open, keypress, search, yes, option_type, is_starter_menu_gameloop, is_gameloop, is_intro, is_map_open, start_story, talk_count, actual_fps, fps, ruby, have_met_ramu_king, is_battle, is_enemy_vanquished, enemy_selected, enemy, enemy_hp, attack, enemy_chance, current_map, player_x, player_y, mapname, map_height, map_width, start_x, start_y, map_x, map_y, save, max_hp, max_mp, base_ATK, base_DEF
  ft("Do you want to save and quit?")
  ftypel()
  yes = 0
  is_menu_open = False
  is_options_open = True
  option_type = "is_yes"
  while yes == 0:
    check_keyboard()
    update_variables()
    clear_screen()
    update_gameUI()
    time.sleep(1/fps)
    is_menu_open = False
    is_options_open = True
    option_type = "is_yes"
    
    if yes == 2:
      yes = 0
      is_options_open = False
      option_type = ""
      ftype("Great!")
      ftype("You said no!")
      time.sleep(delay*10)
      is_options_open = False
      is_menu_open = True
      menu_pos = 1
      keypress = ""
      game_intro()
    if yes == 1:
      yes = 0
      is_options_open = False
      option_type = ""
      ft("Goodbye.")
      time.sleep(1)
      clear_screen()
      reset_terminal()
      will_save = input("Do you want to save your game? Yes/No\n")
      if will_save in ("Yes", "yes", "y", "maybe", "of course", "mhm", "ya", "ye", "yess", "yesss", "yaha", "yah", "Y"):
        print("Remember to copy and paste!")
        time.sleep(3)
        clear_screen()
        save_game()
        time.sleep(15)

      else:
        print("Here is the save code anyway:")
        time.sleep(3)
        clear_screen()
        save_game()
      print("Bye!")
      time.sleep(1)
      sys.exit()

  save = -1

def reset_terminal():
    global old_settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
  
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
      
def decode():
  global player, hp, mp, gold, xp, ATK, DEF, menu, menu_pos, is_menu_open
  global text, grid, is_talk_open, inventory, is_inventory_open
  global options, options_pos, is_options_open, keypress, search, yes
  global option_type, is_starter_menu_gameloop, is_gameloop, is_intro
  global is_map_open, start_story, talk_count, actual_fps, fps
  global ruby, have_met_ramu_king, is_battle, is_enemy_vanquished
  global enemy_selected, enemy, enemy_hp, attack, enemy_chance
  global current_map, player_x, player_y, mapname
  global map_height, map_width, start_x, start_y, map_x, map_y
  global start_time, frames_from_start, save, lvl, max_hp, max_mp, base_ATK, base_DEF
  
  reset_terminal()
  
  saveKey = pickle.loads(base64.b64decode(input("Enter the save code: ")))

  player = saveKey[0]
  hp = saveKey[1]
  mp = saveKey[2]
  gold = saveKey[3]
  xp = saveKey[4]
  menu = saveKey[5]
  menu_pos = saveKey[6]
  is_menu_open = saveKey[7]
  text = saveKey[8]
  grid = saveKey[9]
  is_talk_open = saveKey[10]
  inventory = saveKey[11]
  is_inventory_open = saveKey[12]
  options = saveKey[13]
  options_pos = saveKey[14]
  is_options_open = saveKey[15]
  keypress = saveKey[16]
  search = saveKey[17]
  yes = saveKey[18]
  option_type = saveKey[19]
  is_starter_menu_gameloop = saveKey[20]
  is_gameloop = saveKey[21]
  is_intro = saveKey[22]
  is_map_open = saveKey[23]
  start_story = saveKey[24]
  talk_count = saveKey[25]
  actual_fps = saveKey[26]
  fps = saveKey[27]
  ruby = saveKey[28]
  have_met_ramu_king = saveKey[29]
  is_battle = saveKey[30]
  is_enemy_vanquished = saveKey[31]
  enemy_selected = saveKey[32]
  enemy = saveKey[33]
  enemy_hp = saveKey[34]
  attack = saveKey[35]
  enemy_chance = saveKey[36]
  current_map = saveKey[37]
  player_x = saveKey[38]
  player_y = saveKey[39]
  mapname = saveKey[40]
  map_height = saveKey[41]
  map_width = saveKey[42]
  start_x = saveKey[43]
  start_y = saveKey[44]
  map_x = saveKey[45]
  map_y = saveKey[46]
  ATK = saveKey[47]
  DEF = saveKey[48]
  lvl = saveKey[49]
  max_hp = saveKey[50] 
  max_mp = saveKey[51] 
  base_ATK = saveKey[52] 
  base_DEF = saveKey[53]

  old_settings = termios.tcgetattr(sys.stdin)
  tty.setraw(sys.stdin.fileno())

  print("Loaded!")

  save = -1
  
  frames_from_start = 0

  start_time = time.time()
  is_gameloop = True
  gameloop()

def save_game():
  global player, hp, mp, gold, xp, menu, menu_pos, is_menu_open, text, grid, is_talk_open, inventory, is_inventory_open, options, options_pos, is_options_open, keypress, search, yes, option_type, is_starter_menu_gameloop, is_gameloop, is_intro, is_map_open, start_story, talk_count, actual_fps, fps, ruby, have_met_ramu_king, is_battle, is_enemy_vanquished, enemy_selected, enemy, enemy_hp, attack, enemy_chance, current_map, player_x, player_y, mapname, map_height, map_width, start_x, start_y, map_x, map_y, ATK, DEF,lvl,max_hp, max_mp, base_ATK, base_DEF
  
  saveKey = [player, hp, mp, gold, xp, menu, menu_pos, is_menu_open, text, grid, is_talk_open, inventory, is_inventory_open, options, options_pos, is_options_open, keypress, search, yes, option_type, is_starter_menu_gameloop, is_gameloop, is_intro, is_map_open, start_story, talk_count, actual_fps, fps, ruby, have_met_ramu_king, is_battle, is_enemy_vanquished, enemy_selected, enemy, enemy_hp, attack, enemy_chance, current_map, player_x, player_y, mapname, map_height, map_width, start_x, start_y, map_x, map_y, ATK, DEF,lvl,max_hp, max_mp, base_ATK, base_DEF]

  encoded = base64.b64encode(pickle.dumps(saveKey)).decode()

  print(encoded)

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
  ft("Do you want to go on a quest?")
  is_gameloop = True
  time.sleep(delay)
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
      option_type = "default"
      options_pos = 1
      break
    if yes == 2:
      yes = 0
      is_options_open = False
      option_type = ""
      saving()
      time.sleep(1)
      sys.exit()
  can_talk = f"Try going to the king!"
  option_type = "default"
  talk_count = 0
main()

