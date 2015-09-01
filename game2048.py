#!/usr/bin/env python
# coding=utf-8

import random
import curses
import copy
import curses

def init():
	global mtx,screen,maxyx,startx,starty
	mtx=[[0 for i in range(4)] for j in range(4)]
	rand=random.sample(range(16),2)
	mtx[rand[0]/4][rand[0]%4]=mtx[rand[1]/4][rand[1]%4]=2
	
	screen=curses.initscr()
	curses.noecho()
	curses.cbreak()
	#screen.border()
	
	maxyx=screen.getmaxyx() #The height and width of the screen

	starty=(maxyx[0]-len(bkg))/2
	startx=(maxyx[1]-len(bkg[1]))/2

def drawbkg():
	for i in range(len(bkg)):
		screen.addstr(starty+i,startx,bkg[i])
	

def printmtx():
	ey=(len(bkg)-1)/8
	ex=(len(bkg[1])-1)/8
	for i in range(4):
		for j in range(4):
			screen.addch(starty+ey*(2*i+1),startx+ex*(2*j+1),str(mtx[i][j]))

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
		drawbkg()
	
		printmtx()
	
		screen.refresh()
		screen.getch()
	except Exception,e:
		print e
		
		curses.endwin()
	finally:
		curses.endwin()
