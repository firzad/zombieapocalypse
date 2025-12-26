"""
Object Classes for Zombie Apocalypse

Contains all game entity classes: Character, Zombie, Survivor, and Bullets.
"""

import pygame
from random import randint, choice

import config
from TileClass import Tile


class Character(pygame.Rect):
	"""
	Base class for all game characters (Player and Zombies).

	Inherits from pygame.Rect for built-in collision detection and positioning.
	Manages tile-based movement and targeting.
	"""

	width, height = config.TILE_WIDTH, config.TILE_HEIGHT

	def __init__(self, x, y):
		"""
		Initialize character at given position.

		Args:
			x (int): X coordinate in pixels
			y (int): Y coordinate in pixels
		"""
		self.tx, self.ty = None, None  # Target coordinates for movement
		pygame.Rect.__init__(self, x, y, Character.width, Character.height)

	def __str__(self):
		"""Return string representation (tile number)."""
		return str(self.getNumber())

	def setTarget(self, nextTile):
		"""
		Set the target tile for character to move towards.

		Args:
			nextTile (Tile): The tile to move to
		"""
		if self.tx is None and self.ty is None:
			self.tx = nextTile.x
			self.ty = nextTile.y

	def getNumber(self):
		"""
		Get the tile number of the character's current position.

		Returns:
			int: Tile number in the grid
		"""
		return ((self.x // Character.width) + Tile.Hz) + ((self.y // Character.height) * Tile.Vt)

	def getTile(self):
		"""
		Get the Tile object the character is currently on.

		Returns:
			Tile: The tile at character's current position
		"""
		return Tile.getTile(self.getNumber())



class Zombie(Character):
	"""
	Zombie enemy class.

	Zombies spawn at designated points, use A* pathfinding to chase the player,
	and deal damage when adjacent.
	"""

	List = []
	spawnTiles = config.ZOMBIE_SPAWN_TILES
	originalImage = pygame.image.load(config.IMAGE_ZOMBIE)
	base_health = config.ZOMBIE_HEALTH

	def __init__(self, x, y):
		"""
		Create a new zombie at the given position.

		Args:
			x (int): X coordinate in pixels
			y (int): Y coordinate in pixels
		"""
		self.health = Zombie.base_health

		# Random movement speed selection
		self.vel = choice(config.ZOMBIE_SPEEDS)

		self.direction = 'W'
		self.img = Zombie.originalImage
		Character.__init__(self, x, y)
		Zombie.List.append(self)


	def rotate(self, direction, originalImage):
		"""
		Rotate zombie sprite to face the given direction.

		Args:
			direction (str): Direction to face ('N', 'S', 'E', 'W')
			originalImage: Base zombie image to rotate
		"""

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
		"""
		Spawn new zombies at designated spawn points.

		Args:
			totalFrames (int): Total frames elapsed since game start
			FPS (int): Frames per second
		"""
		# Spawn a zombie every second (every FPS frames)
		if totalFrames % FPS == 0:
			# Play random zombie spawn sound
			sound_path = choice(config.AUDIO_ZOMBIE_SPAWN)
			sound = pygame.mixer.Sound(sound_path)
			sound.set_volume(config.SFX_VOLUME)
			sound.play()

			# Select random spawn tile
			spawnTileNumber = choice(Zombie.spawnTiles)
			spawnNode = Tile.getTile(spawnTileNumber)

			# Create new zombie
			Zombie(spawnNode.x, spawnNode.y)



	@staticmethod
	def update(screen, survivor):
		"""
		Update all zombies - render them and check for player collision.

		Args:
			screen: Pygame screen surface
			survivor (Survivor): Player character to check collision with
		"""


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
						survivor.health -= config.ZOMBIE_DAMAGE
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






class Survivor(Character):
	"""
	Player character class.

	The survivor can move in 4 directions, shoot in 4 directions,
	and switch between three weapons.
	"""

	gunsImg = [
		pygame.image.load(config.IMAGE_PISTOL),
		pygame.image.load(config.IMAGE_SHOTGUN),
		pygame.image.load(config.IMAGE_AUTOMATIC)
	]

	weapon = config.WEAPON_NAMES

	def __init__(self, x, y):
		"""
		Create the player character.

		Args:
			x (int): Starting X coordinate
			y (int): Starting Y coordinate
		"""
		self.health = config.PLAYER_HEALTH
		self.kills = 0
		self.gun = 0  # Current weapon index (0=pistol, 1=shotgun, 2=auto)
		self.direction = 'W'
		self.img = pygame.image.load(config.IMAGE_SURVIVOR_W)
		Character.__init__(self, x, y)
		


	def draw(self, screen):
		"""
		Draw the survivor and current weapon to the screen.

		Args:
			screen: Pygame screen surface
		"""
		h = self.width // 2

		# Draw survivor sprite
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
			screen.blit(img, (self.x +h, self.y - h//2))


	def movement(self):
		"""Move the survivor towards the target tile if one is set."""
		vel = config.PLAYER_SPEED
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
		"""
		Rotate the survivor sprite to face the given direction.

		Args:
			direction (str): Direction to face ('N', 'S', 'E', 'W')
		"""
		if direction == 'N':
			if self.direction != 'N':
				self.direction = 'N'
				self.img = pygame.image.load(config.IMAGE_SURVIVOR_N)

		if direction == 'S':
			if self.direction != 'S':
				self.direction = 'S'
				self.img = pygame.image.load(config.IMAGE_SURVIVOR_S)

		if direction == 'E':
			if self.direction != 'E':
				self.direction = 'E'
				self.img = pygame.image.load(config.IMAGE_SURVIVOR_E)

		if direction == 'W':
			if self.direction != 'W':
				self.direction = 'W'
				self.img = pygame.image.load(config.IMAGE_SURVIVOR_W)


	def getBulletType(self):
		"""
		Get the bullet type string for the current weapon.

		Returns:
			str: Bullet type ("pistol", "shotgun", or "automatic")
		"""
		if self.gun == 0:
			return "pistol"
		elif self.gun == 1:
			return "shotgun"
		elif self.gun == 2:
			return "automatic"
				




class Bullets(pygame.Rect):
	"""
	Bullet/projectile class.

	Handles all bullet types with different damage values and fire rates.
	"""

	width, height = config.BULLET_WIDTH, config.BULLET_HEIGHT
	List = []

	img = {
		"pistol": pygame.image.load(config.IMAGE_PISTOL_BULLET),
		"shotgun": pygame.image.load(config.IMAGE_SHOTGUN_BULLET),
		"automatic": pygame.image.load(config.IMAGE_AUTOMATIC_BULLET)
	}

	gunDmg = {
		"pistol": config.PISTOL_DAMAGE,
		"shotgun": config.SHOTGUN_DAMAGE,
		"automatic": config.AUTOMATIC_DAMAGE
	}


	def __init__(self, x, y, velx, vely, direction, type_):
		"""
		Create a new bullet.

		Args:
			x (int): Starting X coordinate
			y (int): Starting Y coordinate
			velx (int): X velocity (pixels per frame)
			vely (int): Y velocity (pixels per frame)
			direction (str): Direction bullet is traveling ('N', 'S', 'E', 'W')
			type_ (str): Bullet type ("pistol", "shotgun", "automatic")
		"""
		# Enforce bullet spacing based on weapon type (fire rate limiting)
		try:
			if Bullets.List:  # Check if list is not empty
				dx = abs(Bullets.List[-1].x - x)
				dy = abs(Bullets.List[-1].y - y)

				if dx < config.SHOTGUN_SPACING and dy < config.SHOTGUN_SPACING and type_ == "shotgun":
					return
				elif dx < config.PISTOL_SPACING and dy < config.PISTOL_SPACING and type_ == "pistol":
					return
				elif dx < config.AUTOMATIC_SPACING and dy < config.AUTOMATIC_SPACING and type_ == "automatic":
					return
		except (IndexError, AttributeError):
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
		"""
		Check if bullet has moved off screen.

		Args:
			screen: Pygame screen surface

		Returns:
			bool: True if bullet is off screen, False otherwise
		"""
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
		"""
		Update all bullets and check for collisions.

		Args:
			screen: Pygame screen surface
		"""

		for bullet in Bullets.List:

			bullet.x += bullet.velx
			bullet.y += bullet.vely

			# Note: Bullets are now rendered in Main.render() method
			# This method only updates positions and checks collisions

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
