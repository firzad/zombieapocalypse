# Screenshots Directory

This directory contains screenshots and GIFs for the main README.md file.

## Required Files

### Gameplay GIF (Featured at top of README)

**gameplay.gif** - Animated GIF showing 5-10 seconds of gameplay
- This will be the first thing visitors see on the README
- Should show exciting gameplay with multiple zombies
- Include shooting, movement, and zombie pathfinding
- Recommended size: 800px wide
- Keep file size under 5MB if possible

### Screenshots

Take the following screenshots and save them to this directory:

### 1. main_menu.png
- Launch the game
- Capture the main menu screen with START GAME and QUIT buttons
- **Resolution**: 1280x720

### 2. gameplay.png
- Start a new game
- Play for 30-60 seconds to spawn some zombies
- Make sure the HUD is visible (Health, Kills, Gun)
- Capture during active gameplay with zombies on screen
- **Resolution**: 1280x720

### 3. pause_menu.png
- During gameplay, press ESC to pause
- Capture the pause overlay with "PAUSED" text
- Should show "Press ESC to Resume" and "Press Q to Quit"
- **Resolution**: 1280x720

### 4. game_over.png
- Let the zombies kill your character (health reaches 0)
- Wait for the dramatic game over image to pass (3 seconds)
- Capture the statistics screen showing:
  - GAME OVER title
  - Kills count
  - Time Survived
  - Final Health
  - RETRY and MAIN MENU buttons
- **Resolution**: 1280x720

## How to Take Screenshots

### macOS
- Press `Cmd + Shift + 4` and select the game window
- Or press `Cmd + Shift + 3` for full screen

### Windows
- Press `Win + Shift + S` to select area
- Or use the Print Screen key

### Linux
- Use `gnome-screenshot` or your DE's screenshot tool
- Or press Print Screen key

## Tips for Best Results

- Take screenshots at full resolution (1280x720)
- Capture during interesting moments (multiple zombies, active combat)
- Make sure UI elements are clearly visible
- Use PNG format for best quality
- Rename files exactly as specified above

## How to Create the Gameplay GIF

### Option 1: Screen Recording + Conversion (Recommended)

1. **Record gameplay** (5-10 seconds of action):
   - **macOS**: Use QuickTime Player (File → New Screen Recording) or Screenshot app (Cmd+Shift+5)
   - **Windows**: Use Xbox Game Bar (Win+G) or OBS Studio
   - **Linux**: Use `recordmydesktop`, SimpleScreenRecorder, or OBS Studio

2. **Convert video to GIF**:
   - Online: Upload to [ezgif.com](https://ezgif.com/video-to-gif) or [cloudconvert.com](https://cloudconvert.com/mp4-to-gif)
   - Command line with ffmpeg:
     ```bash
     ffmpeg -i gameplay.mp4 -vf "fps=15,scale=800:-1:flags=lanczos" -loop 0 gameplay.gif
     ```

### Option 2: Direct GIF Recording

- **macOS**: Use [Gifox](https://gifox.io/) or [LICEcap](https://www.cockos.com/licecap/)
- **Windows**: Use [ScreenToGif](https://www.screentogif.com/) or [LICEcap](https://www.cockos.com/licecap/)
- **Linux**: Use [Peek](https://github.com/phw/peek) or [LICEcap](https://www.cockos.com/licecap/)

### GIF Recording Tips

- Keep the recording to 5-10 seconds for reasonable file size
- Show exciting action: shooting zombies, being chased, weapon switching
- Make sure the game runs at full 60 FPS during recording
- Try to keep the final GIF under 5MB (may need to reduce fps or size)
- Preview the GIF before adding it to ensure smooth playback
