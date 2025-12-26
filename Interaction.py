"""
Player Interaction Handler for Zombie Apocalypse

Processes keyboard and mouse input for player movement and shooting.
"""

import pygame
import sys

import config
from TileClass import Tile
from ObjectClass import Bullets


def interaction(screen, survivor, paused=False):
	"""
	Handle all player input and interactions.

	Args:
		screen: Pygame screen surface
		survivor: Player character
		paused (bool): Current pause state

	Returns:
		bool: New pause state
	"""

	#Mouse Pointer Coordinates
	Mpos = pygame.mouse.get_pos()
	Mx = Mpos[0] // Tile.width
	My = Mpos[1] // Tile.height



	for event in pygame.event.get():

		#For Window close button
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		#Handle ESC key for pause
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				return not paused  # Toggle pause state

		#Create Solid Tiles: Mouse Click
		if event.type == pygame.MOUSEBUTTONDOWN:
			for tile in Tile.List:
				if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.height):
					tile.type = 'solid'
					tile.walkable = False
					break

		#Switch between guns
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LSHIFT:
				survivor.gun += 1
				survivor.gun %= 3


	#Character Movement
	keys = pygame.key.get_pressed()

	# Movement with arrow keys (also sets facing direction)
	if keys[pygame.K_UP]:
		futureTileNumber = survivor.getNumber() - Tile.Vt

		#Prevent Out Of Bounds Movement If Exits Are Provided
		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('N')

	if keys[pygame.K_DOWN]:
		futureTileNumber = survivor.getNumber() + Tile.Vt

		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('S')

	if keys[pygame.K_RIGHT]:
		futureTileNumber = survivor.getNumber() + Tile.Hz

		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('E')

	if keys[pygame.K_LEFT]:
		futureTileNumber = survivor.getNumber() - Tile.Hz

		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('W')

	# Shooting with spacebar in current facing direction
	if keys[pygame.K_SPACE]:
		if survivor.direction == 'N':
			Bullets(survivor.centerx, survivor.centery, 0, -config.BULLET_SPEED, 'N', survivor.getBulletType())
		elif survivor.direction == 'S':
			Bullets(survivor.centerx, survivor.centery, 0, config.BULLET_SPEED, 'S', survivor.getBulletType())
		elif survivor.direction == 'E':
			Bullets(survivor.centerx, survivor.centery, config.BULLET_SPEED, 0, 'E', survivor.getBulletType())
		elif survivor.direction == 'W':
			Bullets(survivor.centerx, survivor.centery, -config.BULLET_SPEED, 0, 'W', survivor.getBulletType())

	return paused  # Return unchanged pause state
