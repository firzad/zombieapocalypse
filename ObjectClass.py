# Classes For Objects Used

import pygame
from TileClass import Tile
from random import randint


#Base Class for Characters
class Character(pygame.Rect):

	width, height = 40, 40

	def __init__(self, x, y):
		self.tx , self.ty = None, None
		pygame.Rect.__init__(self, x, y, Character.width, Character.height)

	def __str__(self):
		return str(self.getNumber())


	def setTarget(self, nextTile):
		if self.tx == None and self.ty == None:
			self.tx = nextTile.x
			self.ty = nextTile.y


	def getNumber(self):
		return ((self.x / Character.width) + Tile.Hz) + ((self.y / Character.height) * Tile.Vt)

	def getTile(self):
		return Tile.getTile(self.getNumber())



class Zombie(Character):

	List = []
	spawnTiles = (38, 42, 55, 62, 262, 533)
	originalImage = pygame.image.load("Images/zombie.png")
	health = 100

	def __init__(self, x, y):
		
		self.health = Zombie.health 
		self.vel = 4
		
		#Random Movement Speed
		r = randint(1,2) 
		if r == 1:
			self.vel = 4
		elif r ==2:
			self.vel = 8

		self.direction = 'W'
		self.img = Zombie.originalImage
		Character.__init__(self, x, y)
		Zombie.List.append(self)


	def rotate(self, direction, originalImage):

		if direction == 'N':
			if self.direction != 'N':
				self.direction = 'N'
				self.img = pygame.transform.rotate(Zombie.originalImage, 270)

		if direction == 'S':
			if self.direction != 'S':
				self.direction = 'S'
				self.img = pygame.transform.rotate(Zombie.originalImage, 90)
			
		if direction == 'E':
			if self.direction != 'E':
				self.direction = 'E'
				self.img = pygame.transform.rotate(Zombie.originalImage, 180)
			
		if direction == 'W':
			if self.direction != 'W':
				self.direction = 'W'
				self.img = Zombie.originalImage
				



	@staticmethod
	def spawn(totalFrames, FPS):

		#Set Spawning Interval of Zombies
		if totalFrames % (FPS) == 0:

			#if totalFrames % (FPS * 6) == 0:		
			#Set zombie sound interval
			q = randint(0,2)
			sounds = 	[pygame.mixer.Sound("Audio/zs1.ogg"),
						pygame.mixer.Sound("Audio/zs2.ogg"),
						pygame.mixer.Sound("Audio/zs3.ogg")]

			sound = sounds[q]
			sound.play()

			r = randint(0, len(Zombie.spawnTiles) - 1)
			spawnTileNumber = Zombie.spawnTiles[r]
			spawnNode = Tile.getTile(spawnTileNumber)
			
			Zombie(spawnNode.x, spawnNode.y)



	@staticmethod
	def update(screen, survivor):


		for zombie in Zombie.List:
			
			screen.blit(zombie.img, (zombie.x, zombie.y))

			if survivor.x % Tile.width == 0 and survivor.y % Tile.height == 0:
				if zombie.x % Tile.width == 0 and zombie.y % Tile.height == 0:
					
					tileNo = survivor.getNumber()

					N = tileNo - Tile.Vt
					S = tileNo + Tile.Vt
					E = tileNo + Tile.Hz
					W = tileNo - Tile.Hz

					NSEW = [N, S, E, W, tileNo]

					if zombie.getNumber() in NSEW:
						survivor.health -= 5
					if survivor.health <=0:
						return


					#Display Surrounding Vulnerable Tiles
					#for n in NSEW:
					#	pygame.draw.rect(screen, [66,134,12],Tile.getTile(n))



			if zombie.health <= 0:
				Zombie.List.remove(zombie)
				survivor.kills += 1

			
			#Target Already Set
			if zombie.tx != None and zombie.ty != None:

				X = zombie.x - zombie.tx
				Y = zombie.y - zombie.ty

				#Move Right
				if X < 0:
					zombie.x += zombie.vel
					zombie.rotate('E', zombie.originalImage)
				
				#Move Left
				elif X > 0:
					zombie.x -= zombie.vel
					zombie.rotate('W', zombie.originalImage)
				
				#Move Up
				if Y > 0:
					zombie.y -= zombie.vel
					zombie.rotate('N', zombie.originalImage)
				
				#Move Down
				elif Y < 0:
					zombie.y += zombie.vel
					zombie.rotate('S', zombie.originalImage)

				#Target Reached
				if X == 0 and Y == 0:
					zombie.tx, zombie.ty = None, None






#Survivor Object Class
class Survivor(Character):
	

	gunsImg = [	pygame.image.load("Images/pistol.png"),
				pygame.image.load("Images/shotgun.png"),
				pygame.image.load("Images/automatic.png")]

	weapon = ["PISTOL", "SHOTGUN", "SEMI-AUTOMATIC"]


	def __init__(self, x, y):

		self.health = 1500
		self.kills = 0
		self.gun = 0			#Select Gun From List
		self.direction = 'W'
		self.img = pygame.image.load("Images/survivor_w.png")
		Character.__init__(self, x, y)
		


	def draw(self, screen):
		h = self.width/2
		#pygame.draw.circle(screen, [77, 234, 156], (self.x + h, self.y + h), h)
		
		screen.blit(self.img, (self.x, self.y))
		
		img = Survivor.gunsImg[self.gun]

		if self.direction == 'W':
			screen.blit(img, (self.x, self.y + h))
		elif self.direction == 'E':
			img = pygame.transform.flip(img, True, False)
			screen.blit(img, (self.x +h, self.y + h))
		elif self.direction == 'S':
			img = pygame.transform.rotate(img, 90)
			screen.blit(img, (self.x +h, self.y + h))
		elif self.direction == 'N':
			img = pygame.transform.rotate(img, 270)
			screen.blit(img, (self.x +h, self.y - h/2))


	
	def movement(self):
		
		vel = 10
		#Target Already Set
		if self.tx != None and self.ty != None:

			X = self.x - self.tx
			Y = self.y - self.ty

			#Move Right
			if X < 0:
				self.x += vel
			
			#Move Left
			elif X > 0:
				self.x -= vel
			
			#Move Up
			if Y > 0:
				self.y -= vel
			
			#Move Down
			elif Y < 0:
				self.y += vel

			#Target Reached
			if X == 0 and Y == 0:
				self.tx, self.ty = None, None



	def rotate(self, direction):

		if direction == 'N':
			if self.direction != 'N':
				self.direction = 'N'
				self.img = pygame.image.load("Images/survivor_n.png")

		if direction == 'S':
			if self.direction != 'S':
				self.direction = 'S'
				self.img = pygame.image.load("Images/survivor_s.png")
			
		if direction == 'E':
			if self.direction != 'E':
				self.direction = 'E'
				self.img = pygame.image.load("Images/survivor_e.png")
			
		if direction == 'W':
			if self.direction != 'W':
				self.direction = 'W'
				self.img = pygame.image.load("Images/survivor_w.png")


	def getBulletType(self):

		if self.gun == 0:
			return "pistol"
		elif self.gun == 1:
			return "shotgun"
		elif self.gun == 2:
			return "automatic"
				




class Bullets(pygame.Rect):

	width, height = 7, 10
	List = []

	img = {	"pistol" : pygame.image.load("Images/pistol_b.png"),
			"shotgun" : pygame.image.load("Images/shotgun_b.png"),
			"automatic" : pygame.image.load("Images/automatic_b.png")}

	gunDmg = {	"pistol" : Zombie.health/3 + 1,
				"shotgun" : Zombie.health/2,
				"automatic" : Zombie.health/6 + 1 }


	def __init__(self, x, y, velx, vely, direction, type_):

		
		#Bullet Spacing
		try:		#Handle exceptions when the List is empty
			dx = abs(Bullets.List[-1].x - x)
			dy = abs(Bullets.List[-1].y - y)

			if dx < 50 and dy < 50 and type_ == "shotgun":
				return
			elif dx < 30 and dy < 30 and type_ == "pistol":
				return
			elif dx < 15 and dy < 15 and type_ == "automatic":
				return
		except:
			pass


		self.type = type_
		self.direction = direction
		self.velx, self.vely = velx, vely

		if direction == 'N':
			self.img = pygame.transform.rotate(Bullets.img[type_], 270)

		if direction == 'S':
			self.img = pygame.transform.rotate(Bullets.img[type_], 90)
			
		if direction == 'E':
			self.img = pygame.transform.rotate(Bullets.img[type_], 180)
			
		if direction == 'W':
			self.img = Bullets.img[type_]


		pygame.Rect.__init__(self, x, y, Bullets.width, Bullets.height)
		Bullets.List.append(self)


	

	def offScreen(self, screen):

		if self.x < 0:
			return True
		elif self.y < 0:
			return True
		elif self.x + self.width > screen.get_width():
			return True
		elif self.y + self.height > screen.get_height():
			return True
		else:
			return False


	@staticmethod
	def collisionLoop(screen):
		
		for bullet in Bullets.List:

			bullet.x += bullet.velx
			bullet.y += bullet.vely

			screen.blit(bullet.img, (bullet.x, bullet.y))

			if bullet.offScreen(screen):
				Bullets.List.remove(bullet)
				continue

			
			for zombie in Zombie.List:

				if bullet.colliderect(zombie):
					zombie.health -= Bullets.gunDmg[bullet.type]
					Bullets.List.remove(bullet)
					break


			for tile in Tile.List:

				if bullet.colliderect(tile) and not(tile.walkable):
					try:
						Bullets.List.remove(bullet)
					except:
						pass	#Bullet not in List
