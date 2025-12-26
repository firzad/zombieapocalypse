#Utility Functions Used

import pygame


#Function to Display Text in Game Window
def displayText(screen, text, x, y, size = 10, color = (255, 255, 255), font_type = 'capture it'):

	try:
		text = str(text)
		font = pygame.font.SysFont(font_type, size)
		text = font.render(text, True, color)
		screen.blit(text, (x, y))

	except Exception as e:
		print("Font Error!")
		raise e