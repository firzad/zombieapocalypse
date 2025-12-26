# Interaction Processes


import pygame, sys
from TileClass import Tile
from ObjectClass import Bullets


def interaction(screen, survivor):

	#Mouse Pointer Coordinates
	Mpos = pygame.mouse.get_pos()
	Mx = Mpos[0] // Tile.width
	My = Mpos[1] // Tile.height



	for event in pygame.event.get():

		#For Window close button
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

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

	if keys[pygame.K_UP]:
		futureTileNumber = survivor.getNumber() - Tile.Vt

		#Prevent Out Of Bounds Movement If Exits Are Provided
		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('N')
				#survivor.y -= survivor.height 

	if keys[pygame.K_DOWN]:
		futureTileNumber = survivor.getNumber() + Tile.Vt

		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('S')
				#survivor.y += survivor.height

	if keys[pygame.K_RIGHT]:
		futureTileNumber = survivor.getNumber() + Tile.Hz

		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('E')
				#survivor.x += survivor.width

	if keys[pygame.K_LEFT]:
		futureTileNumber = survivor.getNumber() - Tile.Hz

		if futureTileNumber in range(1, Tile.totalTiles + 1):
			futureTile = Tile.getTile(futureTileNumber)
			if futureTile.walkable:
				survivor.setTarget(futureTile)
				survivor.rotate('W')
				#survivor.x -= survivor.width


	if keys[pygame.K_w]:
		survivor.rotate('N')
		Bullets(survivor.centerx, survivor.centery, 0, -10, 'N', survivor.getBulletType())

	elif keys[pygame.K_s]:
		survivor.rotate('S')
		Bullets(survivor.centerx, survivor.centery, 0, 10, 'S', survivor.getBulletType())

	elif keys[pygame.K_d]:
		survivor.rotate('E')
		Bullets(survivor.centerx, survivor.centery, 10, 0, 'E', survivor.getBulletType())

	elif keys[pygame.K_a]:
		survivor.rotate('W')
		Bullets(survivor.centerx, survivor.centery, -10, 0, 'W', survivor.getBulletType())
	

