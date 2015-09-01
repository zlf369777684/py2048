#!/usr/bin/env python
# coding=utf-8

import random
import curses
import copy
import curses

def init():
	global mtx,screen,maxyx,startx,starty,flag
	
	mtx = [[0 for i in range(4)] for j in range(4)]
	rand = random.sample(range(16),2)
	mtx[rand[0]/4][rand[0]%4]=mtx[rand[1]/4][rand[1]%4] =2
	
	screen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)	# hide cursor
	#screen.border()
	
	maxyx = screen.getmaxyx()	 # the height and width of the screen

	starty = (maxyx[0]-len(bkg))/2		# calculate coordinate of the top left corner block so we can put the whole block at the center of screen
	startx = (maxyx[1]-len(bkg[1]))/2		

	draw_bkg()
	print_mtx()
	screen.refresh()

def draw_bkg():
	for i in range(len(bkg)):
		screen.addstr(starty+i,startx,bkg[i])
	

def print_mtx():
	ey = (len(bkg)-1)/8
	ex = (len(bkg[1])-1)/8
	for i in range(4):
		for j in range(4):
			if(mtx[i][j] != 0):
				screen.addstr(starty+ey*(2*i+1),startx+ex*(2*j+1)-len(str(mtx[i][j]))/2,str(mtx[i][j]))
	
	#screen.refresh()


def move_left():
	global moved
	for i in range(4):
		for j in range(1,4):
			if(mtx[i][j] != 0):
				temp = mtx[i][j]
				mtx[i][j] = 0
				pos_temp = j
				while(pos_temp > 0):
					pos_temp -= 1
					if(mtx[i][pos_temp] != 0):
						break
					
				if(mtx[i][pos_temp] == 0):
					mtx[i][pos_temp] = temp
				elif(mtx[i][pos_temp] == temp and flag[i][pos_temp]):
					mtx[i][pos_temp] *= 2
					flag[i][pos_temp] = False
				else:
					pos_temp += 1
					mtx[i][pos_temp] = temp
				
				if(not moved and pos_temp != j):		# check whether the final coordinate equals the original or not
					moved = True
				

def move_right():
	global moved
	for i in range(4):
		for j in range(3):
			if(mtx[i][2-j] != 0):
				temp = mtx[i][2-j]
				mtx[i][2-j] = 0
				pos_temp = 2-j
				while(pos_temp < 3):
					pos_temp += 1
					if(mtx[i][pos_temp] != 0):
						break
					
				if(mtx[i][pos_temp] == 0):
					mtx[i][pos_temp] = temp
				elif(mtx[i][pos_temp] == temp and flag[i][pos_temp]):
					mtx[i][pos_temp] *= 2
					flag[i][pos_temp] = False
				else:
					pos_temp -= 1
					mtx[i][pos_temp] = temp
					
				if(not moved and pos_temp != 2-j):		# please mind the original coordinate is 2-j
					moved = True

def move_down():
	global moved
	for i in range(3):
		for j in range(4):
			if(mtx[2-i][j] != 0):
				temp = mtx[2-i][j]
				mtx[2-i][j] = 0
				pos_temp = 2-i
				while(pos_temp < 3):
					pos_temp += 1
					if(mtx[pos_temp][j] != 0):
						break
					
				if(mtx[pos_temp][j] == 0):
					mtx[pos_temp][j] = temp
				elif(mtx[pos_temp][j] == temp and flag[pos_temp][j]):
					mtx[pos_temp][j] *= 2
					flag[pos_temp][j] = False
				else:
					pos_temp -= 1
					mtx[pos_temp][j] = temp
				
				if(not moved and pos_temp != 2-i):
					moved = True

def move_up():
	global moved
	for i in range(1,4):
		for j in range(4):
			if(mtx[i][j] != 0):
				temp = mtx[i][j]
				mtx[i][j] = 0
				pos_temp = i
				while(pos_temp > 0):
					pos_temp -= 1
					if(mtx[pos_temp][j] != 0):
						break
				
				if(mtx[pos_temp][j] == 0):
					mtx[pos_temp][j] = temp
				elif(mtx[pos_temp][j] == temp and flag[pos_temp][j]):
					mtx[pos_temp][j] *= 2
					flag[pos_temp][j] = False
				else:
					pos_temp += 1
					mtx[pos_temp][j] = temp
				
				if(not moved and pos_temp != i):
					moved = True

def add_number():
	pos = []
	for i in range(4):
		for j in range(4):
			if mtx[i][j] == 0:
				pos.append((i,j))
	if len(pos) > 0:
		rand=random.sample(pos,1)
		r_num = random.sample([2,2,2,2,4],1)	# specify the probability that 2 or 4 will appear
		mtx[rand[0][0]][rand[0][1]] = r_num[0]
			
def check_game_alive():
	for i in range(4):
		for j in range(4):
			if mtx[i][j] == 0:
				return True
			if (i > 0 and mtx[i-1][j] == mtx[i][j]) or (i < 3 and mtx[i+1][j] == mtx[i][j]) or (j > 0 and mtx[i][j-1] == mtx[i][j]) or (j < 3 and mtx[i][j+1] == mtx[i][j]):
				return True	
	return False

def game_over():
	screen.addstr(starty+len(bkg)+1,maxyx[1]/2,'game over')
	dir=chr(screen.getch())

bkg=["+-------+-------+-------+-------+",
	"|       |       |       |       |",
	"|       |       |       |       |",
	"|       |       |       |       |",
	"+-------+-------+-------+-------+",		
	"|       |       |       |       |",
	"|       |       |       |       |",
	"|       |       |       |       |",
	"+-------+-------+-------+-------+",	
	"|       |       |       |       |",
	"|       |       |       |       |",
	"|       |       |       |       |",
	"+-------+-------+-------+-------+",	
	"|       |       |       |       |",
	"|       |       |       |       |",
	"|       |       |       |       |",
	"+-------+-------+-------+-------+"	]


if __name__=='__main__':
	try:
		init()
		while(check_game_alive()):
			global moved
			dir=screen.getkey()
			moved = False			
			flag = [[True for i in range(4)] for j in range(4)]		# make sure numbers in each block can be doubled only once
			if(dir == 'q'):
				break
			elif(dir == 'a' or dir == 'j'):
				move_left()
			elif(dir == 's' or dir == 'k'):
				move_down()
			elif(dir == 'd' or dir == 'l'):
				move_right()
			elif(dir == 'w' or dir == 'i'):
				move_up()
			
			if moved:
				add_number()
				
			draw_bkg()
			print_mtx()
		
		game_over()
	except Exception,e:
		print e
	finally:
		curses.endwin()
