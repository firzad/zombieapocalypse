"""
Game Configuration File

Contains all constants and configuration values for Zombie Apocalypse.
Modify these values to tweak game balance and behavior.
"""

# Screen Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_TITLE = "Zombie Apocalypse"

# Game Performance
FPS = 60  # Frames per second (increased from 20 for smoothness)

# Tile System
TILE_WIDTH = 40
TILE_HEIGHT = 40
GRID_COLUMNS = 32  # SCREEN_WIDTH // TILE_WIDTH
GRID_ROWS = 18     # SCREEN_HEIGHT // TILE_HEIGHT

# Player Settings
PLAYER_START_X = 640  # Center of screen
PLAYER_START_Y = 360  # Center of screen
PLAYER_HEALTH = 1500
PLAYER_SPEED = 200  # Pixels per second (was 10 pixels/frame * 20 FPS)

# Zombie Settings
ZOMBIE_HEALTH = 100
ZOMBIE_DAMAGE = 5  # Damage per frame when adjacent
ZOMBIE_SPAWN_INTERVAL = 1.0  # Spawn every N seconds
ZOMBIE_SPEEDS = [80, 160]  # Pixels per second (was [4, 8] * 20 FPS)

# Weapon Settings - Damage values
PISTOL_DAMAGE = ZOMBIE_HEALTH // 3 + 1      # ~34 damage (3 shots to kill)
SHOTGUN_DAMAGE = 100                          # 100 damage (1 shot to kill - powerful!)
AUTOMATIC_DAMAGE = ZOMBIE_HEALTH // 6 + 1    # ~17 damage (6 shots to kill)

# Weapon Settings - Fire Rate (time-based in seconds)
# Time delay between shots for each weapon
PISTOL_FIRE_RATE = 0.3      # Medium fire rate - 0.3 second delay between shots
SHOTGUN_FIRE_RATE = 0.6     # Slowest fire rate - 0.6 second delay (high damage)
AUTOMATIC_FIRE_RATE = 0.08  # Fastest fire rate - 0.08 second delay (low damage)

# Bullet Settings
BULLET_SPEED = 500  # Pixels per second - faster than player for better visuals
BULLET_WIDTH = 7
BULLET_HEIGHT = 10

# A* Pathfinding Settings
PATHFINDING_UPDATE_INTERVAL = 0.05  # Update paths every 0.05 seconds (20 times per second)

# Audio Settings
BACKGROUND_MUSIC_VOLUME = 0.7  # 0.0 to 1.0
SFX_VOLUME = 0.5  # 0.0 to 1.0

# UI Settings
INTRO_DURATION = 6  # Seconds to show intro screen
GAME_OVER_DELAY = 2  # Seconds before showing game over screen
GAME_OVER_DISPLAY_TIME = 4  # Seconds to show game over before exit

# Colors (RGB)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)

# HUD Settings
HUD_FONT_SIZE = 25
HUD_HEALTH_X = 10
HUD_HEALTH_Y = 0
HUD_KILLS_X = 500
HUD_KILLS_Y = 0
HUD_WEAPON_X = 1000
HUD_WEAPON_Y = 0

# Intro Screen Settings
INTRO_TITLE_SIZE = 100
INTRO_TEXT_SIZE = 40
INTRO_TITLE_X = 150
INTRO_TITLE_Y = 100
INTRO_INSTRUCTIONS_Y_START = 300
INTRO_INSTRUCTIONS_SPACING = 100

# Asset Paths
PATH_AUDIO = "Audio/"
PATH_IMAGES = "Images/"

# Audio Files
AUDIO_THEME = PATH_AUDIO + "zombie_theme.ogg"
AUDIO_GAME_OVER = PATH_AUDIO + "GameOver.ogg"
AUDIO_ZOMBIE_SPAWN = [
    PATH_AUDIO + "zs1.ogg",
    PATH_AUDIO + "zs2.ogg",
    PATH_AUDIO + "zs3.ogg"
]

# Image Files
IMAGE_MAP = PATH_IMAGES + "map.jpg"
IMAGE_GAME_OVER = PATH_IMAGES + "GameOver.png"
IMAGE_ZOMBIE = PATH_IMAGES + "zombie.png"

IMAGE_SURVIVOR_N = PATH_IMAGES + "survivor_n.png"
IMAGE_SURVIVOR_S = PATH_IMAGES + "survivor_s.png"
IMAGE_SURVIVOR_E = PATH_IMAGES + "survivor_e.png"
IMAGE_SURVIVOR_W = PATH_IMAGES + "survivor_w.png"

IMAGE_PISTOL = PATH_IMAGES + "pistol.png"
IMAGE_SHOTGUN = PATH_IMAGES + "shotgun.png"
IMAGE_AUTOMATIC = PATH_IMAGES + "automatic.png"

IMAGE_PISTOL_BULLET = PATH_IMAGES + "pistol_b.png"
IMAGE_SHOTGUN_BULLET = PATH_IMAGES + "shotgun_b.png"
IMAGE_AUTOMATIC_BULLET = PATH_IMAGES + "automatic_b.png"

# Weapon Names
WEAPON_NAMES = ["PISTOL", "SHOTGUN", "SEMI-AUTOMATIC"]

# Zombie Spawn Tiles (tile numbers where zombies can spawn)
ZOMBIE_SPAWN_TILES = (38, 42, 55, 62, 262, 533)

# Pause Menu Settings
PAUSE_OVERLAY_COLOR = (0, 0, 0)  # Black
PAUSE_OVERLAY_ALPHA = 128  # Semi-transparent (0-255)
PAUSE_TITLE_SIZE = 80
PAUSE_TEXT_SIZE = 40
PAUSE_TITLE_Y = 250
PAUSE_INSTRUCTIONS_Y_START = 400
PAUSE_INSTRUCTIONS_SPACING = 60

# Main Menu Settings
MENU_TITLE_SIZE = 100
MENU_TITLE_Y = 150
MENU_BUTTON_WIDTH = 400
MENU_BUTTON_HEIGHT = 70
MENU_BUTTON_SPACING = 90
MENU_BUTTONS_START_Y = 350
MENU_BUTTON_COLOR = (50, 50, 50)  # Dark gray
MENU_BUTTON_HOVER_COLOR = (100, 100, 100)  # Lighter gray
MENU_BUTTON_TEXT_COLOR = (255, 255, 255)  # White
MENU_TEXT_SIZE = 35

# Game Over Screen Settings
GAMEOVER_TITLE_SIZE = 90
GAMEOVER_TITLE_Y = 100
GAMEOVER_STATS_SIZE = 35
GAMEOVER_STATS_START_Y = 250
GAMEOVER_STATS_SPACING = 50
GAMEOVER_BUTTONS_START_Y = 480
GAMEOVER_BUTTON_WIDTH = 350
GAMEOVER_BUTTON_HEIGHT = 70
