#Class For Manipulating Tiles

import pygame, Functions

#Tile Class Which Inherit properties of rectangles
class Tile(pygame.Rect):
	
	List = []
	width, height = 40, 40
	totalTiles = 1
	Hz, Vt = 1, 32

	#Invalids For Current Screen Spec
	invalids = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,
				39,40,43,44,52,54,56,57,59,61,63,64,68,70,71,72,75,77,78,83,86,88,89,91,95,96,104,107,110,111,113,
				114,116,118,123,125,127,128,132,139,140,150,151,152,155,157,159,160,164,166,167,171,172,174,316,
				175,176,177,178,179,180,183,184,192,193,194,195,199,201,206,210,219,222,224,229,230,231,233,419,
				234,235,238,244,246,247,248,250,251,253,254,256,258,259,260,261,270,274,276,278,288,320,352,387,
				384,416,448,480,512,544,576,33,65,97,129,161,193,225,257,289,321,353,385,417,449,545,546,547,418,
				548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,
				571,572,573,574,575,576,293,294,296,299,300,301,302,303,304,306,309,310,312,313,314,318,319,
				326,328,330,331,334,336,337,373,376,377,379,380,390,393,406,408,412,422,425,427,430,432,433,
				435,437,438,440,442,444,450,451,452,453,454,456,457,458,459,460,461,462,464,467,468,469,470,
				472,476,490,498.499,504,506,508,509,511,512,520,525,526,527,498,499,534,539,540,543,374,249)

	
	def __init__(self, x, y, Type):

		self.parent = None
		self.F, self.G, self.H = 0, 0, 0
						
		self.type = Type 			#Type: Walkable or Not
		self.number = Tile.totalTiles
		Tile.totalTiles += 1

		if Type == 'empty':
			self.walkable = True
		else:
			self.walkable = False

		pygame.Rect.__init__(self, (x, y), (Tile.width, Tile.height))

		Tile.List.append(self)

	
	#Initialize The Tiles
	@staticmethod
	def preInit(screen, SCREENHEIGHT, SCREENWIDTH):
		for y in range(0, SCREENHEIGHT, Tile.height):
			for x in range(0, SCREENWIDTH, Tile.width):
				if Tile.totalTiles in Tile.invalids:
					Tile(x, y, 'solid')
				else:
					Tile(x, y, 'empty')


	@staticmethod
	def getTile(number):
		
		for tile in Tile.List:
			if tile.number == number:
				return tile


	@staticmethod
	def drawTiles(screen):

		half = Tile.width / 2

		for tile in Tile.List:

			if not(tile.type == 'empty'):
				pygame.draw.rect(screen, [100, 50, 10], tile)	#Grey Colour For non-Empty Tiles

			#Display F, G, H Values of Tiles
			# if tile.G !=0:
			# 	Functions.displayText(screen, tile.G, tile.x, tile.y + half, color = [120, 157, 40])
			# if tile.H !=0:
			# 	Functions.displayText(screen, tile.H, tile.x + half, tile.y + half, color = [20, 67, 150])
			# if tile.F !=0:
			# 	Functions.displayText(screen, tile.F, tile.x + half, tile.y, color = [57, 177, 177])

			#Display Tile Number
			#Functions.displayText(screen, tile.number, tile.x, tile.y)
