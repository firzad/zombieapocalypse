# Zombie Apocalypse

A 2D tile-based survival game built with Python and pygame, featuring intelligent zombie AI powered by the A* pathfinding algorithm.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## Overview

**Zombie Apocalypse** is a top-down survival shooter where you play as a lone survivor defending against endless waves of zombies. The game showcases classic AI pathfinding with zombies using the A* algorithm to intelligently navigate around obstacles and hunt you down.

### Key Features

- 🎮 **Professional Main Menu**: Polished title screen with clickable buttons
- 🧟 **Intelligent Enemy AI**: Zombies use A* pathfinding to navigate around walls and obstacles
- 🎯 **Intuitive Controls**: Spacebar shooting with directional movement
- 🏃 **Tile-Based Movement**: 32x18 grid system with smooth character movement
- 🔫 **Multiple Weapons**: Three weapon types with different damage profiles and fire rates
  - Pistol: Balanced damage and fire rate
  - Shotgun: High damage, slower fire rate
  - Semi-Automatic: Rapid fire, lower damage per bullet
- ⏸️ **Pause System**: Pause anytime with ESC key
- 📊 **Statistics Tracking**: Track kills, survival time, and final health
- 🔄 **Retry & Menu System**: Instant retry or return to main menu from game over
- 🎨 **Enhanced Visuals**: Dramatic text effects with shadows and bold fonts
- 🔊 **Atmospheric Audio**: Background music and zombie sound effects
- 💀 **Dramatic Game Over**: Cinematic game over sequence with stats

## Screenshots

### Gameplay
The game features a detailed map with obstacles, a heads-up display showing health, kills, and current weapon, and increasingly challenging zombie waves.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd zombieapocalypse
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install pygame directly:
   ```bash
   pip install pygame
   ```

3. **Verify assets are present**

   Ensure the following directories exist with all assets:
   - `Images/` - Game sprites and backgrounds
   - `Audio/` - Sound effects and music

## Running the Game

### Start the Game

```bash
python3 Main.py
```

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Display**: 1280x720 minimum resolution
- **RAM**: 256 MB minimum
- **Storage**: ~5 MB

## How to Play

### Game Flow

1. **Main Menu** → Click "START GAME" or "QUIT"
2. **Intro Screen** → Press any key to continue or wait 6 seconds
3. **Gameplay** → Survive against zombie waves
4. **Pause** → Press ESC anytime to pause/resume
5. **Game Over** → View stats, then choose "RETRY" or "MAIN MENU"

### Game Controls

#### Movement & Direction
- **↑ Arrow Key** - Move North (character faces north)
- **↓ Arrow Key** - Move South (character faces south)
- **→ Arrow Key** - Move East (character faces east)
- **← Arrow Key** - Move West (character faces west)

#### Combat
- **Spacebar** - Shoot in current facing direction
- Arrow keys set your facing direction, Spacebar fires!

#### Weapons
- **Left Shift** - Cycle through weapons (Pistol → Shotgun → Semi-Automatic)

#### Pause & Menu
- **ESC** - Pause/Resume game
- **Q** - Quit to desktop (while paused)

### Objective

Survive as long as possible against endless waves of zombies. Zombies spawn periodically from designated spawn points and will hunt you down using intelligent pathfinding. Each zombie you kill increases your score.

### Gameplay Tips

1. **Keep Moving**: Staying in one place allows zombies to surround you
2. **Use Obstacles**: Navigate around walls to break line of sight
3. **Face Your Target**: Move in the direction you want to shoot, then hit spacebar
4. **Weapon Selection**:
   - Use the **Pistol** for balanced gameplay
   - Switch to **Shotgun** for powerful single shots
   - Use **Semi-Automatic** when surrounded
5. **Watch Your Health**: You start with 1500 health; zombies deal 5 damage when adjacent
6. **Monitor Spawn Points**: Zombies spawn from 6 fixed locations on the map
7. **Take Breaks**: Use the pause menu (ESC) to take a breather

### Game Over Sequence

When your health reaches 0:
1. **Dramatic Game Over Image** (3 seconds) - Epic defeat screen
2. **Statistics Screen** - View your performance:
   - Total Kills
   - Time Survived (minutes:seconds)
   - Final Health
3. **Choose Your Path**:
   - **RETRY** - Jump right back into the action
   - **MAIN MENU** - Return to title screen
   - **Close Window** - Quit the game

## Technical Details

### Architecture

The game is built using an object-oriented architecture with the following components:

#### Core Classes

- **Character** (`ObjectClass.py`) - Base class for all game entities
  - Inherits from `pygame.Rect` for collision detection
  - Manages position, tile-based movement, and targeting

- **Zombie** (`ObjectClass.py`) - Enemy entity
  - Health: 100 HP
  - Speed: Random (4 or 8 pixels per frame)
  - Damage: 5 HP per frame when adjacent to player
  - Behavior: Uses A* pathfinding to chase player

- **Survivor** (`ObjectClass.py`) - Player character
  - Health: 1500 HP
  - Speed: 10 pixels per frame
  - Weapons: 3 types with different stats
  - Movement: Independent from shooting direction

- **Bullets** (`ObjectClass.py`) - Projectile system
  - Three bullet types matching weapon selection
  - Collision detection with zombies and walls
  - Automatic cleanup when off-screen

- **Tile** (`TileClass.py`) - Grid system
  - 32 columns × 18 rows = 576 tiles
  - Each tile: 40×40 pixels
  - Walkable/solid properties for collision
  - Stores A* pathfinding values (F, G, H scores)

#### Key Algorithms

**A* Pathfinding** (`AStar.py`)
- Calculates optimal path from each zombie to the player
- Accounts for walls and obstacles
- Updates every frame for real-time response
- Uses Manhattan distance heuristic
- Supports blocky (4-directional) or diagonal movement

**Movement System**
- Tile-based targeting with smooth interpolation
- Prevents out-of-bounds movement
- Collision detection with solid tiles
- Independent movement and shooting directions

**Spawn System**
- 6 predefined spawn locations across the map
- Zombies spawn every second (20 frames at 20 FPS)
- Random spawn point selection
- Random zombie speed variation

### File Structure

```
zombieapocalypse/
│
├── Main.py              # Entry point, game loop
├── ObjectClass.py       # Character, Zombie, Survivor, Bullets classes
├── TileClass.py         # Tile-based grid system
├── Interaction.py       # User input handling
├── AStar.py             # A* pathfinding algorithm
├── Functions.py         # Utility functions (text display)
│
├── Images/              # Visual assets
│   ├── map.jpg                    # Game background
│   ├── survivor_n/s/e/w.png       # Player sprites (4 directions)
│   ├── zombie.png                 # Enemy sprite
│   ├── pistol/shotgun/automatic.png         # Weapon sprites
│   ├── pistol_b/shotgun_b/automatic_b.png   # Bullet sprites
│   └── GameOver.png               # Game over screen
│
├── Audio/               # Sound assets
│   ├── zombie_theme.ogg     # Background music (loops)
│   ├── zs1.ogg              # Zombie spawn sound 1
│   ├── zs2.ogg              # Zombie spawn sound 2
│   ├── zs3.ogg              # Zombie spawn sound 3
│   └── GameOver.ogg         # Game over music
│
├── Extras/              # Additional character sprites
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Performance Characteristics

- **Frame Rate**: 20 FPS (configurable in `Main.py`)
- **Screen Resolution**: 1280×720 (configurable)
- **A* Calculations**: Performed per zombie per frame (optimized with early exit)
- **Zombie List**: Dynamic (grows as more zombies spawn)

### Weapon Statistics

| Weapon          | Damage per Hit | Fire Rate | Bullet Speed | Best Use Case          |
|-----------------|----------------|-----------|--------------|------------------------|
| Pistol          | 34 HP          | Medium    | 10 px/frame  | Balanced gameplay      |
| Shotgun         | 50 HP          | Slow      | 10 px/frame  | High-damage single shots |
| Semi-Automatic  | 17 HP          | Fast      | 10 px/frame  | Crowd control          |

*Note: Zombie health is 100 HP*

## Development History

### Version History

**Version 2.0** (Current - 2025)
- 🎮 **Complete UI Overhaul**:
  - Professional main menu with clickable buttons
  - Interactive pause menu with ESC key
  - Enhanced game over screen with stats and options
- 🎯 **Improved Controls**:
  - Spacebar shooting system (replaced WASD)
  - Directional movement with arrow keys
  - Intuitive facing direction system
- 🎨 **Visual Enhancements**:
  - Dramatic text shadows and bold fonts
  - Color-coded titles (red for dramatic effect)
  - Enhanced button hover effects
- 📊 **Statistics System**:
  - Time survived tracking (minutes:seconds)
  - Kill counter
  - Final health display
- 🔄 **Game Loop**:
  - Retry functionality
  - Return to main menu option
  - Complete game flow cycle
- 🐛 **Bug Fixes**:
  - Fixed bullet rendering issue
  - Fixed intro screen event handling
  - Improved text centering on buttons

**Beta v1.0** (Original)
- Initial tile-based game implementation (32×18 grid)
- Arrow key movement for player
- A* pathfinding for zombie AI
- Three weapon types
- Health and scoring system
- Audio integration

**Legacy Version**
- Developed in Python 2.7
- Migrated to Python 3.8+ (2025)
- Updated syntax for modern Python compatibility

### Migration & Refactoring Notes

This project was originally developed for Python 2.7 and has undergone extensive modernization:

**Python 3 Migration:**
- Updated exception handling syntax (`except Exception, e:` → `except Exception as e:`)
- Converted print statements to function calls (`print "text"` → `print("text")`)
- Changed division operators for integer results (`/` → `//` in 8 locations)
- Updated pygame to version 2.6.1+

**Code Refactoring:**
- Created `config.py` for centralized configuration
- Implemented OOP structure with Game class
- Added comprehensive docstrings to all modules
- Separated rendering from game logic
- Created reusable Button class for UI elements
- Added utility functions for enhanced text rendering

### Technologies
- **Python** - Programming language
- **pygame** - Game development library
- **A* Algorithm** - Pathfinding implementation

### Assets
- Game sprites and artwork
- Sound effects and music
- Map design

## License

This project is available under the MIT License.

## Troubleshooting

### Common Issues

**Game won't start**
- Verify Python 3.8+ is installed: `python3 --version`
- Ensure pygame is installed: `pip3 install pygame`
- Check that `Images/` and `Audio/` directories exist

**Missing assets error**
- Verify all image files are present in `Images/`
- Verify all audio files are present in `Audio/`
- Check file permissions

**Audio not playing**
- Ensure your system supports .ogg format
- Check system volume settings
- Verify pygame mixer initialized correctly

**Poor performance**
- Adjust FPS in `Main.py` (line 26)
- Reduce zombie spawn rate
- Close other resource-intensive applications

**Import errors**
- Ensure all Python files are in the same directory
- Check for typos in import statements
- Verify no circular dependencies

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Future Development

See `IMPROVEMENTS.md` for a comprehensive list of planned features and potential enhancements.

## Contact

For questions, suggestions, or bug reports, please open an issue on the project repository.

---

**Enjoy surviving the zombie apocalypse!** 🧟‍♂️🔫
