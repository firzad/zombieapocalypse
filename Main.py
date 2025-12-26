"""
Zombie Apocalypse - Main Game File

A 2D tile-based survival game featuring intelligent zombie AI
powered by the A* pathfinding algorithm.

Zombie Apocalypse Beta v1.0
"""

import pygame
import sys
from time import sleep

import config
import Functions
from TileClass import Tile
from ObjectClass import Zombie, Survivor, Bullets
from Interaction import interaction
from AStar import AStar


class Button:
    """Simple button class for menus."""

    def __init__(self, x, y, width, height, text, color, hover_color, text_color):
        """
        Create a button.

        Args:
            x (int): X coordinate
            y (int): Y coordinate
            width (int): Button width
            height (int): Button height
            text (str): Button text
            color (tuple): Normal button color
            hover_color (tuple): Color when mouse hovers
            text_color (tuple): Text color
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

    def draw(self, screen):
        """Draw the button on screen."""
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, config.COLOR_WHITE, self.rect, 2)  # Border

        # Calculate text width properly for centering
        font = pygame.font.SysFont("monospace", config.MENU_TEXT_SIZE)
        text_surface = font.render(self.text, True, self.text_color)
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()

        # Center text on button
        text_x = self.rect.x + (self.rect.width - text_width) // 2
        text_y = self.rect.y + (self.rect.height - text_height) // 2

        screen.blit(text_surface, (text_x, text_y))

    def check_hover(self, mouse_pos):
        """Check if mouse is hovering over button."""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_clicked):
        """Check if button was clicked."""
        return self.rect.collidepoint(mouse_pos) and mouse_clicked


class Game:
    """Main game class that manages game state and game loop."""

    def __init__(self):
        """Initialize pygame and game components."""
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        # Set up display
        self.screen = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT), 0, 32
        )
        pygame.display.set_caption(config.WINDOW_TITLE)

        # Load background map
        self.map_image = pygame.image.load(config.IMAGE_MAP)

        # Initialize tile system
        Tile.preInit(self.screen, config.SCREEN_HEIGHT, config.SCREEN_WIDTH)

        # Set up game clock
        self.clock = pygame.time.Clock()
        self.total_frames = 0

        # Create player
        self.survivor = Survivor(config.PLAYER_START_X, config.PLAYER_START_Y)

        # Game state
        self.paused = False
        self.game_start_time = None  # Will be set when game actually starts

        # Load and play background music
        pygame.mixer.music.load(config.AUDIO_THEME)
        pygame.mixer.music.set_volume(config.BACKGROUND_MUSIC_VOLUME)
        pygame.mixer.music.play(-1)  # Loop indefinitely

    def show_intro_screen(self):
        """
        Display the intro/instruction screen.

        Shows game title and controls. User can press any key to continue
        or wait for auto-start after 6 seconds.
        """
        start_time = pygame.time.get_ticks()
        waiting = True

        while waiting:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Any key press continues to game
                    waiting = False

            # Draw intro screen
            self.screen.fill(config.COLOR_BLACK)

            # Title with dramatic styling
            Functions.displayTitleText(
                self.screen,
                "ZOMBIE APOCALYPSE",
                config.INTRO_TITLE_X - 20,
                config.INTRO_TITLE_Y,
                config.INTRO_TITLE_SIZE,
                config.COLOR_RED
            )

            # Instructions
            instructions = [
                ("Arrow Keys To Move", 380, 300),
                ("Spacebar To Shoot", 380, 380),
                ("Left Shift To Change Weapon", 310, 460),
                ("Press any Key to Continue", 320, 600)
            ]

            for text, x, y in instructions:
                Functions.displayText(
                    self.screen, text, x, y,
                    config.INTRO_TEXT_SIZE,
                    config.COLOR_WHITE,
                    "monospace"
                )

            pygame.display.update()

            # Auto-continue after 6 seconds
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time > (config.INTRO_DURATION * 1000):  # Convert seconds to milliseconds
                waiting = False

            self.clock.tick(30)  # Run at 30 FPS during intro

    def show_main_menu(self):
        """
        Display the main menu.

        Returns:
            str: Action selected ('start', 'quit')
        """
        # Create buttons
        button_x = (config.SCREEN_WIDTH - config.MENU_BUTTON_WIDTH) // 2
        start_button = Button(
            button_x,
            config.MENU_BUTTONS_START_Y,
            config.MENU_BUTTON_WIDTH,
            config.MENU_BUTTON_HEIGHT,
            "START GAME",
            config.MENU_BUTTON_COLOR,
            config.MENU_BUTTON_HOVER_COLOR,
            config.MENU_BUTTON_TEXT_COLOR
        )

        quit_button = Button(
            button_x,
            config.MENU_BUTTONS_START_Y + config.MENU_BUTTON_SPACING,
            config.MENU_BUTTON_WIDTH,
            config.MENU_BUTTON_HEIGHT,
            "QUIT",
            config.MENU_BUTTON_COLOR,
            config.MENU_BUTTON_HOVER_COLOR,
            config.MENU_BUTTON_TEXT_COLOR
        )

        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = False

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True

            # Check button interactions
            start_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)

            if start_button.is_clicked(mouse_pos, mouse_clicked):
                return 'start'
            if quit_button.is_clicked(mouse_pos, mouse_clicked):
                return 'quit'

            # Draw menu
            self.screen.fill(config.COLOR_BLACK)

            # Draw title with dramatic styling
            Functions.displayTitleText(
                self.screen,
                "ZOMBIE APOCALYPSE",
                120,
                config.MENU_TITLE_Y,
                config.MENU_TITLE_SIZE,
                config.COLOR_RED
            )

            # Draw buttons
            start_button.draw(self.screen)
            quit_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

    def draw_pause_menu(self):
        """Draw the pause menu overlay."""
        # Create semi-transparent overlay
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        overlay.set_alpha(config.PAUSE_OVERLAY_ALPHA)
        overlay.fill(config.PAUSE_OVERLAY_COLOR)
        self.screen.blit(overlay, (0, 0))

        # Draw "PAUSED" title with styling
        Functions.displayTitleText(
            self.screen,
            "PAUSED",
            config.SCREEN_WIDTH // 2 - 140,
            config.PAUSE_TITLE_Y,
            config.PAUSE_TITLE_SIZE,
            config.COLOR_YELLOW
        )

        # Draw instructions
        instructions = [
            "Press ESC to Resume",
            "Press Q to Quit"
        ]

        y = config.PAUSE_INSTRUCTIONS_Y_START
        for text in instructions:
            Functions.displayText(
                self.screen,
                text,
                config.SCREEN_WIDTH // 2 - 180,
                y,
                config.PAUSE_TEXT_SIZE,
                config.COLOR_WHITE,
                "monospace"
            )
            y += config.PAUSE_INSTRUCTIONS_SPACING

        pygame.display.flip()

    def draw_hud(self):
        """
        Draw the Heads-Up Display (HUD).

        Shows health, kills, and current weapon.
        """
        # Health
        Functions.displayText(
            self.screen,
            f"H E A L T H : {self.survivor.health}",
            config.HUD_HEALTH_X,
            config.HUD_HEALTH_Y,
            config.HUD_FONT_SIZE
        )

        # Kills
        Functions.displayText(
            self.screen,
            f"K I L L S : {self.survivor.kills}",
            config.HUD_KILLS_X,
            config.HUD_KILLS_Y,
            config.HUD_FONT_SIZE
        )

        # Current weapon
        Functions.displayText(
            self.screen,
            f"G U N : {Survivor.weapon[self.survivor.gun]}",
            config.HUD_WEAPON_X,
            config.HUD_WEAPON_Y,
            config.HUD_FONT_SIZE
        )

    def handle_pause_input(self):
        """
        Handle input while game is paused.

        Returns:
            bool: True to continue paused, False to unpause
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Unpause
                    return False
                elif event.key == pygame.K_q:
                    # Quit game
                    pygame.quit()
                    sys.exit()

        return True  # Stay paused

    def update_game_state(self):
        """
        Update all game entities and logic.

        Handles zombie spawning, movement, pathfinding, and collision detection.
        """
        # Spawn zombies
        Zombie.spawn(self.total_frames, config.FPS)

        # Update player
        self.survivor.movement()

        # Update bullets and check collisions
        Bullets.collisionLoop(self.screen)

        # Run A* pathfinding for zombies
        AStar(self.screen, self.survivor, config.FPS, self.total_frames)

        # Handle user input (including pause toggle)
        self.paused = interaction(self.screen, self.survivor, self.paused)

    def render(self):
        """
        Render all game graphics to the screen.

        Draws background, entities, and HUD.
        """
        # Draw background map
        self.screen.blit(self.map_image, (0, 0))

        # Draw bullets
        for bullet in Bullets.List:
            self.screen.blit(bullet.img, (bullet.x, bullet.y))

        # Draw survivor
        self.survivor.draw(self.screen)

        # Draw zombies
        Zombie.update(self.screen, self.survivor)

        # Draw HUD
        self.draw_hud()

        # Update display
        pygame.display.flip()

    def check_game_over(self):
        """
        Check if game over condition is met.

        Returns:
            bool: True if player health is depleted, False otherwise
        """
        return self.survivor.health <= 0

    def show_game_over_screen(self):
        """
        Display the interactive game over screen with statistics and options.

        First shows the dramatic game over image, then transitions to stats/options.

        Returns:
            str: Action selected ('retry', 'menu', 'quit')
        """
        # Stop background music
        pygame.mixer.music.stop()

        # Wait a moment
        sleep(config.GAME_OVER_DELAY)

        # Play game over music
        pygame.mixer.music.load(config.AUDIO_GAME_OVER)
        pygame.mixer.music.play(0)

        # Show the dramatic game over image first
        game_over_image = pygame.image.load(config.IMAGE_GAME_OVER)
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.update()

        # Display the dramatic image for 3 seconds
        sleep(3)

        # Calculate survival time
        if self.game_start_time:
            survival_seconds = (pygame.time.get_ticks() - self.game_start_time) // 1000
            survival_minutes = survival_seconds // 60
            survival_seconds_remaining = survival_seconds % 60
            survival_time_str = f"{survival_minutes}m {survival_seconds_remaining}s"
        else:
            survival_time_str = "N/A"

        # Create buttons
        button_x = (config.SCREEN_WIDTH - config.GAMEOVER_BUTTON_WIDTH) // 2

        retry_button = Button(
            button_x,
            config.GAMEOVER_BUTTONS_START_Y,
            config.GAMEOVER_BUTTON_WIDTH,
            config.GAMEOVER_BUTTON_HEIGHT,
            "RETRY",
            config.MENU_BUTTON_COLOR,
            config.MENU_BUTTON_HOVER_COLOR,
            config.MENU_BUTTON_TEXT_COLOR
        )

        menu_button = Button(
            button_x,
            config.GAMEOVER_BUTTONS_START_Y + config.MENU_BUTTON_SPACING,
            config.GAMEOVER_BUTTON_WIDTH,
            config.GAMEOVER_BUTTON_HEIGHT,
            "MAIN MENU",
            config.MENU_BUTTON_COLOR,
            config.MENU_BUTTON_HOVER_COLOR,
            config.MENU_BUTTON_TEXT_COLOR
        )

        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = False

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True

            # Check button interactions
            retry_button.check_hover(mouse_pos)
            menu_button.check_hover(mouse_pos)

            if retry_button.is_clicked(mouse_pos, mouse_clicked):
                return 'retry'
            if menu_button.is_clicked(mouse_pos, mouse_clicked):
                return 'menu'

            # Draw game over screen
            self.screen.fill(config.COLOR_BLACK)

            # Draw "GAME OVER" title with dramatic styling
            Functions.displayTitleText(
                self.screen,
                "GAME OVER",
                config.SCREEN_WIDTH // 2 - 250,
                config.GAMEOVER_TITLE_Y,
                config.GAMEOVER_TITLE_SIZE,
                config.COLOR_RED
            )

            # Draw statistics with shadow for better visibility
            stats_x = config.SCREEN_WIDTH // 2 - 180
            y = config.GAMEOVER_STATS_START_Y

            stats = [
                f"Kills: {self.survivor.kills}",
                f"Time Survived: {survival_time_str}",
                f"Final Health: {max(0, self.survivor.health)}"
            ]

            for stat in stats:
                Functions.displayTextWithShadow(
                    self.screen,
                    stat,
                    stats_x,
                    y,
                    config.GAMEOVER_STATS_SIZE,
                    config.COLOR_WHITE,
                    (0, 0, 0),
                    "arial",
                    bold=True
                )
                y += config.GAMEOVER_STATS_SPACING

            # Draw buttons
            retry_button.draw(self.screen)
            menu_button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

        return 'quit'

    def reset_game_state(self):
        """Reset the game state for a new game."""
        # Clear all zombies and bullets
        Zombie.List.clear()
        Bullets.List.clear()

        # Reset frame counter
        self.total_frames = 0

        # Create new player
        self.survivor = Survivor(config.PLAYER_START_X, config.PLAYER_START_Y)

        # Reset pause state
        self.paused = False

        # Restart background music
        pygame.mixer.music.stop()
        pygame.mixer.music.load(config.AUDIO_THEME)
        pygame.mixer.music.set_volume(config.BACKGROUND_MUSIC_VOLUME)
        pygame.mixer.music.play(-1)

    def run(self):
        """
        Main game loop.

        Shows main menu, then runs intro screen and game loop until game over.
        Handles retry and return to main menu options.
        """
        # Main game loop - allows retry and menu returns
        while True:
            # Show main menu
            action = self.show_main_menu()

            if action == 'quit':
                return  # Exit game completely

            # Show intro screen
            self.show_intro_screen()

            # Set game start time for statistics
            self.game_start_time = pygame.time.get_ticks()

            # Main gameplay loop
            running = True
            while running:
                if self.paused:
                    # Handle pause state
                    self.draw_pause_menu()
                    self.paused = self.handle_pause_input()
                    self.clock.tick(config.FPS)  # Keep frame rate consistent
                else:
                    # Normal gameplay
                    # Update game state
                    self.update_game_state()

                    # Render everything
                    self.render()

                    # Control frame rate
                    self.clock.tick(config.FPS)
                    self.total_frames += 1

                    # Check for game over
                    if self.check_game_over():
                        running = False

            # Show game over screen and get user choice
            game_over_action = self.show_game_over_screen()

            if game_over_action == 'retry':
                # Reset game state and start new game
                self.reset_game_state()
                # Continue to show intro screen again
                continue

            elif game_over_action == 'menu':
                # Return to main menu
                self.reset_game_state()
                # Loop continues, will show main menu again
                continue

            else:  # 'quit'
                # Exit game
                return


def main():
    """Entry point for the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
