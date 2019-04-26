# A* Path Finding Algorithm

import pygame
from ObjectClass import *
from TileClass import Tile


def AStar(screen, survivor, FPS, totalFrames):

	#Surroundind Nodes in 8 Directions
	N = -32
	S = 32
	E = 1
	W = -1

	NW = -33
	NE = -31
	SE = 33
	SW = 31

	half = Tile.width / 2

	#Reset F,G,H Values: Zombie Blocked By Walls
	for tile in Tile.List:
		tile.parent = None
		tile.F, tile.G, tile.H = 0, 0, 0


	def blockyPath(surroundingTiles, diagonals, surTile):
		if surTile.number not in diagonals:
			surroundingTiles.append(surTile)

		return surroundingTiles


	#Get List of Surrounding Nodes
	def getSurroundingTiles(baseNode):
		
		array = (
				(baseNode.number + N),
				(baseNode.number + NE),
				(baseNode.number + E),
				(baseNode.number + SE),
				(baseNode.number + S),
				(baseNode.number + SW),
				(baseNode.number + W),
				(baseNode.number + NW)
				)

		#print array


		surroundingTiles = []

		baseNumber = baseNode.number
		diagonals = [baseNumber + NE, baseNumber + NW, baseNumber + SE, baseNumber + SW]

		for tileNumber in array:

			surTile = Tile.getTile(tileNumber)

			if tileNumber not in range(1,Tile.totalTiles + 1):
				continue

			if surTile.walkable and surTile not in closedList:
				
				#For Diagonal Movements
				#surroundingTiles.append(surTile)	
				
				#For Blocky Movement
				surroundingTiles = blockyPath(surroundingTiles, diagonals, surTile) 

		return surroundingTiles


	#Calculate G Value: Bottom Left
	def G(tile):
		
		diff = tile.number - tile.parent.number

		if diff in (N, S, E, W): #Straights = +10
			tile.G = tile.parent.G + 10

		elif diff in (NE, NW, SE, SW): #Diagonals = +14
			tile.G = tile.parent.G + 14


	#Calculate H Value: Bottom Right
	def H():
		
		for tile in Tile.List:
			tile.H = 10 * (abs(tile.x - survivor.x) + abs(tile.y - survivor.y)) / Tile.width


	#Calculate F Value: Top Right
	def F(tile):
		#F = G + H    =>  A* Algorithm
		tile.F = tile.G + tile.H


	#Update the Lists
	def swap(tile):
		openList.remove(tile)
		closedList.append(tile)


	#Get Lowest F-Value Tile
	def getLFT():
		
		Fvals = []

		for tile in openList:
			Fvals.append(tile.F)

		revOpenList = openList[::-1]

		for tile in revOpenList:
			if tile.F == min(Fvals):
				return tile



	#Calculate New Possible G Values
	def moveToGCost(LFT, tile):

		GVal = 0
		diff = LFT.number - tile.number

		if diff in (N, S, E, W): #10
			GVal = LFT.G + 10

		elif diff in (NE, NW, SE, SW): #14
			GVal = LFT.G + 14

		return GVal



	#Recursive function to estimate the path
	def loop():

		LFT = getLFT()
		#Draw The Tree Path
		#pygame.draw.line(screen, [0, 255, 255], [LFT.parent.x + half, LFT.parent.y + half], [LFT.x + half, LFT.y + half] ) 

		swap(LFT)
		surroundingNodes = getSurroundingTiles(LFT)


		for node in surroundingNodes:

			if node not in openList:
				openList.append(node)
				node.parent = LFT


			#Perform G Check - Avoid ZigZag Paths
			elif node in openList:

				calG = moveToGCost(LFT, node)

				if calG < node.G:
					node.parent = LFT
					G(node)
					F(node)



		if openList == [] or survivor.getTile() in closedList:
			return

		for node in openList:
			G(node)
			F(node)

			#Draw The Tree Path
			#pygame.draw.line(screen, [255, 0, 0], [node.parent.x + half, node.parent.y + half], [node.x + half, node.y + half] )


		loop()



	#Perform A-Star Algorithm for each Zombie
	for zombie in Zombie.List:

		#Improve Performance
		if zombie.tx != None or zombie.ty != None:
			continue

		openList = []
		closedList = []

		zombieTile = zombie.getTile()
		openList.append(zombieTile)

		surroundingNodes = getSurroundingTiles(zombieTile)

		for node in surroundingNodes:
			node.parent = zombieTile
			openList.append(node)

		swap(zombieTile)

		H()

		for node in surroundingNodes:
			G(node)
			F(node)
			
			#Draw The Tree Path
			#pygame.draw.line(screen, [255, 0, 0], [node.parent.x + half, node.parent.y + half], [node.x + half, node.y + half] )


		loop()


		#Store The Path Tiles
		returnTiles = []

		parent = survivor.getTile()

		while True:

			returnTiles.append(parent)
			parent = parent.parent

			if parent == None:
				break

			if parent.number == zombieTile.number:
				break


		#Draw The Calculated Path Using Small Blue Circles
		#for tile in returnTiles:
		#	pygame.draw.circle(screen, [34, 95, 200], [tile.x + half, tile.y + half], 5)


		#Move Zombies - Chase The Player
		if len(returnTiles) > 1:
			nextTile = returnTiles[-1]
			zombie.setTarget(nextTile)




