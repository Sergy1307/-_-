import pygame
import random
import time
from PIL import Image
from tkinter import messagebox as mb



size = [800, 800]
res_skale = 3
res = [k // res_skale for k in size]


camx, camy = 0, 0

window = pygame.display.set_mode(size)
screen = pygame.transform.scale(window, res)

clock = pygame.time.Clock()

slice_size = 8
one_size = 16

textures = {0: [pygame.image.load('0.png')],
			1: [pygame.image.load('1.png')],
			21: [pygame.image.load('2g.png')],
			22: [pygame.image.load('2k.png')],
			3: [pygame.image.load('3.png')],
			4: [pygame.image.load('4.png')],
			5: [pygame.image.load('5.png')],
			6: [pygame.image.load('6.png')]}
global A
A = 21
global B
B = 21
world_size_slice_x = 100//slice_size
world_size_slice_y = 100//slice_size

world_map = Image.open('world3.png').load()


def check1():
	mb.showerror(
		"",
		"Player1 wins")

def check2():
	mb.showerror(
		title="",
		message="Player2 wins")
def point_to_slice(x,y):
	one_gx, one_gy = point_to_one(x,y)[0],point_to_one(x,y)[1]
	one_x = one_gx % slice_size
	one_y = one_gy % slice_size
	slice_x = one_gx // slice_size
	slice_y = one_gy // slice_size

	if(slice_x<0 or slice_y<0) or (slice_x > world_size_slice_x - 1 or slice_y > world_size_slice_y - 1):
		return None

	return[one_x,one_y,slice_x,slice_y]
def point_to_one(x,y):
	one_x = x // one_size
	one_y = y // one_size
	return [one_x, one_y]
def slices_on_screen():
	x1 = camx // (slice_size*one_size)
	y1 = camy // (slice_size*one_size)

	x2 = (camx+res[0]) // (slice_size*one_size)
	y2 = (camy+res[1]) // (slice_size*one_size)


	x1 = min(max(x1, 0), world_size_slice_x-1)
	x2 = min(max(x2, 0), world_size_slice_x-1)

	y1 = min(max(y1, 0), world_size_slice_y-1)
	y2 = min(max(y2, 0), world_size_slice_y-1)

	result = []
	for y in range(y1, y2+1):
		for x in range(x1, x2+1):
			result.append(x+y*world_size_slice_x)

	return result



def game1_one(pos, pos1):
	global A
	global B
	k = point_to_one(*pos)
	k1 = point_to_one(*pos1)
	if (k1[0]-1<=k[0]<=k1[0]+1) and (k1[1]-1<=k[1]<=k1[1]+1):
		one_data = point_to_slice(*pos)
		one_data1 = point_to_slice(*pos1)
		slice = slices[one_data[2]+one_data[3]*world_size_slice_x]
		slice1 = slices[one_data1[2]+one_data1[3]*world_size_slice_x]


		if slice.map[one_data[0] + one_data[1] * slice_size] == 3 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 21:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 3
			pygame.display.set_caption('Player1 wins')

			check1()

			time.sleep(3)
			exit()

		if slice.map[one_data[0] + one_data[1] * slice_size] == 5 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 21:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 5
			pygame.display.set_caption('Player1 wins')

			check1()

			time.sleep(3)
			exit()






		if slice.map[one_data[0] + one_data[1] * slice_size] == 3 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 1:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 3
		if slice.map[one_data[0] + one_data[1] * slice_size] == 5 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 1:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 5


		if slice.map[one_data[0] + one_data[1] * slice_size] == 3 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 4:
			if(random.randint(1,100)%2==1):
				B-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 3
			else:
				A-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1

		if slice.map[one_data[0] + one_data[1] * slice_size] == 3 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 6:
			if(random.randint(1,100)%3==1):
				B-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 3
			else:
				A-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1

		if slice.map[one_data[0] + one_data[1] * slice_size] == 5 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 6:
			if(random.randint(1,100)%2==1):
				B-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 5
			else:
				A-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1

		if slice.map[one_data[0] + one_data[1] * slice_size] == 5 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 4:
			if(random.randint(1,100)%3!=1):
				B-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 5
			else:
				A-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1



def game2_one(pos, pos1):
	global A
	global B
	k = point_to_one(*pos)
	k1 = point_to_one(*pos1)
	if (k1[0]-1<=k[0]<=k1[0]+1) and (k1[1]-1<=k[1]<=k1[1]+1):
		one_data1 = point_to_slice(*pos1)
		one_data = point_to_slice(*pos)
		slice = slices[one_data[2]+one_data[3]*world_size_slice_x]
		slice1 = slices[one_data1[2]+one_data1[3]*world_size_slice_x]


		if slice.map[one_data[0] + one_data[1] * slice_size] == 4 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 22:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 4
			pygame.display.set_caption('Player2 wins')

			check2()

			time.sleep(3)
			exit()
		if slice.map[one_data[0] + one_data[1] * slice_size] == 6 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 22:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 6
			pygame.display.set_caption('Player2 wins')

			check2()

			time.sleep(3)
			exit()


		if slice.map[one_data[0] + one_data[1] * slice_size] == 4 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 1:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 4
		if slice.map[one_data[0] + one_data[1] * slice_size] == 6 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 1:
			slice.map[one_data[0]+one_data[1]*slice_size] = 1
			slice1.map[one_data1[0] + one_data1[1] * slice_size] = 6


		if slice.map[one_data[0] + one_data[1] * slice_size] == 4 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 3:
			if(random.randint(1,100)%2==1):
				A-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 4
			else:
				B-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1

		if slice.map[one_data[0] + one_data[1] * slice_size] == 4 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 5:
			if(random.randint(1,100)%3==1):
				A-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 4
			else:
				B-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1

		if slice.map[one_data[0] + one_data[1] * slice_size] == 6 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 5:
			if(random.randint(1,100)%2==1):
				A-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 6
			else:
				B-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1

		if slice.map[one_data[0] + one_data[1] * slice_size] == 6 and slice1.map[one_data1[0] + one_data1[1] * slice_size] == 3:
			if(random.randint(1,100)%3!=0):
				A-=1
				slice.map[one_data[0]+one_data[1]*slice_size] = 1
				slice1.map[one_data1[0] + one_data1[1] * slice_size] = 6
			else:
				B-=1
				slice.map[one_data[0] + one_data[1] * slice_size] = 1


def generate_one(x, y, slice_x, slice_y):
	one_x = (slice_x//one_size)+x
	one_y = (slice_y//one_size)+y
	if int(world_map[one_x, one_y][0]/255+world_map[one_x, one_y][1]/255+world_map[one_x, one_y][2]/255 >= 2.5):
		return 1
	if int(world_map[one_x, one_y][0]/255+world_map[one_x, one_y][1]/255+world_map[one_x, one_y][2]/255 >= 2):
		if ((random.randint(1, 100) % 3) == 1):
			return 5
		return 3
	if int(world_map[one_x, one_y][0]/255+world_map[one_x, one_y][1]/255+world_map[one_x, one_y][2]/255 >= 1.5):
		return 22

	if int(world_map[one_x, one_y][0]/255+world_map[one_x, one_y][1]/255+world_map[one_x, one_y][2]/255 >= 1):
		if (random.randint(1, 100) % 3 == 1):
			return 6
		return 4
	if int(world_map[one_x, one_y][0] / 255 + world_map[one_x, one_y][1] / 255 + world_map[one_x, one_y][2] / 255 >= 0.5):
		return 21

	return 0


class Slise:
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.map = [generate_one(x, y, self.x, self.y) for y in range(slice_size) for x in range(slice_size)]

	def render(self):
		for y in range(slice_size):
			for x in range(slice_size):
				texture = textures[self.map[x+y*slice_size]][0]
				screen.blit(texture, (self.x+x*one_size - camx, self.y+y*one_size - camy))



slices = []
for y in range(world_size_slice_y):
	for x in range(world_size_slice_x):
		slices.append(Slise(x*slice_size*one_size, y*slice_size*one_size))
pos = [0,0]
x = 0
frame = 0


while 1:
	screen.fill((0, 0, 0))
	if(B==0):
		pygame.display.set_caption('Player1 wins')

		check1()

		time.sleep(3)
		exit()

	if (A == 0):
		pygame.display.set_caption('Player2 wins')

		check2()

		time.sleep(3)
		exit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()


		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 3:
				pos = [pygame.mouse.get_pos()[0]//res_skale+camx, pygame.mouse.get_pos()[1]//res_skale+camy]
			if event.button == 1:
				pos1 = [pygame.mouse.get_pos()[0]//res_skale+camx, pygame.mouse.get_pos()[1]//res_skale+camy]
				td = point_to_slice(*pos)
				ch = slices[td[2] + td[3] * world_size_slice_x]
				if ((ch.map[td[0] + td[1] * slice_size] == 3) or (ch.map[td[0] + td[1] * slice_size] == 5)) and (x//5)%2 == 0:
					game1_one(pos,pos1)
					x += 1
				if ((ch.map[td[0] + td[1] * slice_size] == 4) or (ch.map[td[0] + td[1] * slice_size] == 6)) and (x//5)%2 == 1:
					game2_one(pos, pos1)
					x += 1


	key = pygame.key.get_pressed()
	if key[pygame.K_a]:
		camx -= 3
	if key[pygame.K_d]:
		camx += 3
	if key[pygame.K_w]:
		camy -= 3
	if key[pygame.K_s]:
		camy += 3
	if key[pygame.K_SPACE]:
		print(1)
		screen.fill((0, 0, 0))


	for i in slices_on_screen():
		slices[i].render()

	window.blit(pygame.transform.scale(screen, size), (0, 0))
	pygame.display.update()

	clock.tick(480)

	frame += 1
	if frame%10 == 0:
		pygame.display.set_caption('now: '+("Player1 " if ((x//5)%2==0) else "Player2 ")+str(A)+"/"+str(B))
		slices_on_screen()
