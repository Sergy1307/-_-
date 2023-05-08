import pygame
import random
from PIL import Image

pygame.init()

size = [800, 800]
res_skale = 2
res = [k // res_skale for k in size]

cam_x, cam_y = 0, 0

window = pygame.display.set_mode(size)
screen = pygame.transform.scale(window, res)

clock = pygame.time.Clock()

chunk_size = 8
tile_size = 16

textures = {0: [pygame.image.load('0.png')],
			1: [pygame.image.load('1.png')],
			2: [pygame.image.load('2.png')],
			3: [pygame.image.load('3.png')],
			4: [pygame.image.load('4.png')],
			5: [pygame.image.load('5.png')],
			6: [pygame.image.load('6.png')]}

en = []
fr = []

world_size_chunk_x = 100//chunk_size
world_size_chunk_y = 100//chunk_size

world_map = Image.open('world3.png').load()
#world_map1 = Image.open('world1.png').load()
#world_map = world_map1.copy()
#world_map = world_map.resize((world_size_chunk_x,world_size_chunk_y), Image.LANCZOS )
#world_map = world_map.load()


def point_to_chunk(x,y):
	tile_gx, tile_gy = point_to_tile(x,y)[0],point_to_tile(x,y)[1]
	tile_x = tile_gx % chunk_size
	tile_y = tile_gy % chunk_size
	chunk_x = tile_gx // chunk_size
	chunk_y = tile_gy // chunk_size

	if(chunk_x<0 or chunk_y<0) or (chunk_x > world_size_chunk_x - 1 or chunk_y > world_size_chunk_y - 1):
		return None

	return[tile_x,tile_y,chunk_x,chunk_y]
def point_to_tile(x,y):
	tyle_x = x // tile_size
	tyle_y = y // tile_size
	return [tyle_x, tyle_y]
def chunks_on_screen():
	x1 = cam_x // (chunk_size*tile_size)
	y1 = cam_y // (chunk_size*tile_size)

	x2 = (cam_x+res[0]) // (chunk_size*tile_size)
	y2 = (cam_y+res[1]) // (chunk_size*tile_size)


	x1 = min(max(x1, 0), world_size_chunk_x-1)
	x2 = min(max(x2, 0), world_size_chunk_x-1)

	y1 = min(max(y1, 0), world_size_chunk_y-1)
	y2 = min(max(y2, 0), world_size_chunk_y-1)

	result = []
	for y in range(y1, y2+1):
		for x in range(x1, x2+1):
			result.append(x+y*world_size_chunk_x)

	return result



def game1_tile(pos, pos1):
	k = point_to_tile(*pos)
	k1 = point_to_tile(*pos1)
	if (k1[0]-1<=k[0]<=k1[0]+1) and (k1[1]-1<=k[1]<=k1[1]+1):
		tile_data = point_to_chunk(*pos)
		tile_data1 = point_to_chunk(*pos1)
		chunk = chunks[tile_data[2]+tile_data[3]*world_size_chunk_x]
		chunk1 = chunks[tile_data1[2]+tile_data1[3]*world_size_chunk_x]


		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 3 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 1:
			chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
			chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 3
		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 5 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 1:
			chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
			chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 5


		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 3 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 4:
			if(random.randint(1,100)%2==1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 3
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1

		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 3 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 6:
			if(random.randint(1,100)%3==1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 3
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1

		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 5 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 6:
			if(random.randint(1,100)%2==1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 5
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1

		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 5 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 4:
			if(random.randint(1,100)%3!=1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 5
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1



def game2_tile(pos, pos1):
	k = point_to_tile(*pos)
	k1 = point_to_tile(*pos1)
	if (k1[0]-1<=k[0]<=k1[0]+1) and (k1[1]-1<=k[1]<=k1[1]+1):
		tile_data1 = point_to_chunk(*pos1)
		tile_data = point_to_chunk(*pos)
		chunk = chunks[tile_data[2]+tile_data[3]*world_size_chunk_x]
		chunk1 = chunks[tile_data1[2]+tile_data1[3]*world_size_chunk_x]


		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 4 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 1:
			chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
			chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 4
		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 6 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 1:
			chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
			chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 6


		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 4 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 3:
			if(random.randint(1,100)%2==1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 4
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1

		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 4 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 5:
			if(random.randint(1,100)%3==1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 4
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1

		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 6 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 5:
			if(random.randint(1,100)%2==1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 6
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1

		if chunk.map[tile_data[0] + tile_data[1] * chunk_size] == 6 and chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] == 3:
			if(random.randint(1,100)%3!=1):
				chunk.map[tile_data[0]+tile_data[1]*chunk_size] = 1
				chunk1.map[tile_data1[0] + tile_data1[1] * chunk_size] = 6
			else:
				chunk.map[tile_data[0] + tile_data[1] * chunk_size] = 1


def generate_tile(x, y, chunk_x, chunk_y):
	tile_x = (chunk_x//tile_size)+x
	tile_y = (chunk_y//tile_size)+y
	if int(world_map[tile_x, tile_y][0]/255+world_map[tile_x, tile_y][1]/255+world_map[tile_x, tile_y][2]/255 >= 2.5):
		return 1
	if int(world_map[tile_x, tile_y][0]/255+world_map[tile_x, tile_y][1]/255+world_map[tile_x, tile_y][2]/255 >= 1.5):
		fr.append([tile_x,tile_y,chunk_x,chunk_y])
		if (random.randint(1, 100) % 3 == 1):
			return 5
		return 3
	if int(world_map[tile_x, tile_y][0]/255+world_map[tile_x, tile_y][1]/255+world_map[tile_x, tile_y][2]/255 >= 0.5):
		en.append([tile_x,tile_y,chunk_x,chunk_y])
		if (random.randint(1, 100) % 3 == 1):
			return 6
		return 4
	return 0
class Chunk:
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.map = [generate_tile(x, y, self.x, self.y) for y in range(chunk_size) for x in range(chunk_size)]

	def render(self):
		for y in range(chunk_size):
			for x in range(chunk_size):
				texture = textures[self.map[x+y*chunk_size]][0]
				screen.blit(texture, (self.x+x*tile_size - cam_x, self.y+y*tile_size - cam_y))



chunks = []
for y in range(world_size_chunk_y):
	for x in range(world_size_chunk_x):
		chunks.append(Chunk(x*chunk_size*tile_size, y*chunk_size*tile_size))
pos = [0,0]
x = 1
frame = 0
while 1:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 3:
				pos = [pygame.mouse.get_pos()[0]//res_skale+cam_x, pygame.mouse.get_pos()[1]//res_skale+cam_y]
				print(pos)
			if event.button == 1:
				pos1 = [pygame.mouse.get_pos()[0]//res_skale+cam_x, pygame.mouse.get_pos()[1]//res_skale+cam_y]
				td = point_to_chunk(*pos)
				ch = chunks[td[2] + td[3] * world_size_chunk_x]
				if ((ch.map[td[0] + td[1] * chunk_size] == 3) or (ch.map[td[0] + td[1] * chunk_size] == 5)) and x == 1:
					game1_tile(pos,pos1)
					x = 0
					#cam_y = 0
				if ((ch.map[td[0] + td[1] * chunk_size] == 4) or (ch.map[td[0] + td[1] * chunk_size] == 6)) and x == 0:
					game2_tile(pos, pos1)
					x = 1
					#cam_y = 1000


	key = pygame.key.get_pressed()
	if key[pygame.K_a]:
		cam_x -= 3
	if key[pygame.K_d]:
		cam_x += 3
	if key[pygame.K_w]:
		cam_y -= 3
	if key[pygame.K_s]:
		cam_y += 3

	for i in chunks_on_screen():
		chunks[i].render()

	window.blit(pygame.transform.scale(screen, size), (0, 0))
	pygame.display.update()
	clock.tick(480)

	frame += 1
	if frame%100 == 0:
		pygame.display.set_caption('FPS: '+str(round(clock.get_fps())))
		chunks_on_screen()