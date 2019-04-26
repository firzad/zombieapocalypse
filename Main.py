 # PROJECT  F.I.R.E  -  Zombie Apocalypse Beta v1.0

import pygame, sys, Functions
from TileClass import Tile
from ObjectClass import *
from Interaction import interaction
from AStar import AStar
from time import sleep


pygame.init()
pygame.mixer.init()
pygame.font.init()

pygame.mixer.music.load("Audio/zombie_theme.ogg")
pygame.mixer.music.play(-1)

SCREENWIDTH,SCREENHEIGHT = 1280,720
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)
map = pygame.image.load("Images/map.jpg")

Tile.preInit(screen, SCREENHEIGHT, SCREENWIDTH)


clock = pygame.time.Clock()
FPS = 20
totalFrames = 0

#zombie1 = Zombie-(400, 440) 			#(TileWidth*10, TileHeight*11)
survivor = Survivor(640, 360)		#(TileWidth*5, TileHeight*5)

FLAG = True

while True:

	while FLAG:
		screen.fill([0,0,0])
		Functions.displayText(screen, "ZOMBIE APOCALYPSE", 150, 100, 100, [255,255,255])
		Functions.displayText(screen, "Arrow Keys To Move Character", 310, 300, 40, [255,255,255],"monospace")
		Functions.displayText(screen, "W - A - S - D  Keys To Shoot", 300, 400, 40, [255,255,255], "monospace")
		Functions.displayText(screen, "Left Shift Key To Change Weapon", 275, 500, 40, [255,255,255],"monospace")
		Functions.displayText(screen, "Press any Key to Continue", 320, 600, 40, [255,255,255],"monospace")
		pygame.display.update()
		sleep(6)
		FLAG = False

	#screen.fill([0,0,0])
	screen.blit(map, (0, 0))

	Zombie.spawn(totalFrames, FPS)
	survivor.movement()

	Bullets.collisionLoop(screen)
	
	AStar(screen, survivor, FPS, totalFrames)

	interaction(screen, survivor) 
	
	#Tile.drawTiles(screen)
	
	survivor.draw(screen)
	Zombie.update(screen, survivor)

	Functions.displayText(screen, "H E A L T H : {0}".format(survivor.health), 10, 0, 25, )
	Functions.displayText(screen, "K I L L S : {0}".format(survivor.kills), 500, 0, 25, )
	Functions.displayText(screen, "G U N : {0}".format(Survivor.weapon[survivor.gun]), 1000, 0, 25, )
	

	#print survivor 			#Invokes __str__() method	
	#print zombie1
	
	pygame.display.flip()
	clock.tick(FPS)
	totalFrames += 1

	#Game Over Condition
	if survivor.health <= 0:
		pygame.mixer.music.stop()
		pygame.mixer.music.load("Audio/GameOver.ogg")
		sleep(2)
		pygame.mixer.music.play(0)
		screen.blit(pygame.image.load("Images/GameOver.png"), (0, 0))
		pygame.display.update()
		break

sleep(4)