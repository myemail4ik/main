#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil, os
import random
import time

def update_game(collvo):

	collvo=collvo+1
	list_names=list(range(1,collvo))
	list_names_shuffle=list(range(1,collvo))
	random.shuffle(list_names_shuffle)
	print(list_names_shuffle)



	path='./output/'
	shutil.rmtree(path)
	time.sleep(1)
	os.makedirs("output")

	time.sleep(1)
			
	for i in list_names:
		try:
			b=list_names_shuffle[i-1]
			i=str(i)
			b=str(b)
			os.mkdir('./output/'+i)
			shutil.copyfile('./game/'+b+'/picture.jpg','./output/'+i+'/picture.jpg')
			shutil.copyfile('./game/'+b+'/question.txt','./output/'+i+'/question.txt')
			print("copy_out:"+b+"/"+i)
			time.sleep(0.05)
		except OSError:
			print("err_copy_out")	

	time.sleep(1)


	path='./game/'
	shutil.rmtree(path)
	time.sleep(1)
	os.makedirs('game')

	time.sleep(1)
	for i in list_names:
		try:
			i=str(i)
			os.mkdir('./game/'+i)
			shutil.copyfile('./output/'+i+'/picture.jpg','./game/'+i+'/picture.jpg')
			shutil.copyfile('./output/'+i+'/question.txt','./game/'+i+'/question.txt')
			print("copy_game:"+i)
			time.sleep(0.05)
		except OSError:
			print("err_copy_game")	


	time.sleep(1)

	print("DONE")
	return 1

