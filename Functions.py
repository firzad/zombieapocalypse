"""
Utility Functions for Zombie Apocalypse

Contains helper functions used throughout the game.
"""

import pygame


def displayText(screen, text, x, y, size=10, color=(255, 255, 255), font_type='capture it'):
	"""
	Display text on the game screen.

	Args:
		screen: Pygame screen surface
		text: Text to display (will be converted to string)
		x (int): X coordinate
		y (int): Y coordinate
		size (int, optional): Font size. Defaults to 10.
		color (tuple, optional): RGB color. Defaults to white (255, 255, 255).
		font_type (str, optional): Font name. Defaults to 'capture it'.

	Raises:
		Exception: If there's an error rendering the font
	"""
	try:
		text = str(text)
		font = pygame.font.SysFont(font_type, size)
		text_surface = font.render(text, True, color)
		screen.blit(text_surface, (x, y))

	except Exception as e:
		print("Font Error!")
		raise e


def displayTextWithShadow(screen, text, x, y, size=10, color=(255, 255, 255), shadow_color=(0, 0, 0), font_type='arial', bold=False):
	"""
	Display text with a shadow effect for better visibility and style.

	Args:
		screen: Pygame screen surface
		text: Text to display (will be converted to string)
		x (int): X coordinate
		y (int): Y coordinate
		size (int, optional): Font size. Defaults to 10.
		color (tuple, optional): Text color. Defaults to white.
		shadow_color (tuple, optional): Shadow color. Defaults to black.
		font_type (str, optional): Font name. Defaults to 'arial'.
		bold (bool, optional): Use bold font. Defaults to False.
	"""
	try:
		text = str(text)
		font = pygame.font.SysFont(font_type, size, bold=bold)

		# Render shadow (offset by a few pixels)
		shadow_surface = font.render(text, True, shadow_color)
		screen.blit(shadow_surface, (x + 3, y + 3))

		# Render main text
		text_surface = font.render(text, True, color)
		screen.blit(text_surface, (x, y))

	except Exception as e:
		print("Font Error!")
		raise e


def displayTitleText(screen, text, x, y, size=80, color=(255, 255, 255)):
	"""
	Display large title text with dramatic styling (shadow + bold).

	Args:
		screen: Pygame screen surface
		text: Title text to display
		x (int): X coordinate
		y (int): Y coordinate
		size (int, optional): Font size. Defaults to 80.
		color (tuple, optional): Text color. Defaults to white.
	"""
	displayTextWithShadow(screen, text, x, y, size, color, (0, 0, 0), 'arial', bold=True)