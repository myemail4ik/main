#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random_file_test
import parther
import os
import shutil


kol_vo_test=50
pages=['https://animebest.org/anime-ab/priklyucheniya/','https://animebest.org/anime-ab/komediya/','https://animebest.org/anime-ab/drama-ab/','https://animebest.org/anime-ab/fentezi/','https://animebest.org/anime-ab/muzykalnyy/','https://animebest.org/anime-ab/news/','https://animebest.org/anime-ab/romantika-ab/','https://animebest.org/anime-ab/povsednevnost/','https://animebest.org/anime-ab/shkola/']
files=['action','comedy','drama','fantasy','musical','novelty','romantic','routine','shool',]

def dell_file(path):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path)
    shutil.rmtree(path)

i=0

for f in range(0,int(len(files))):
	parther.parther(files[f],pages[f])
i=1

i=random_file_test.update_game(kol_vo_test)
print(i)

for g in range(1,kol_vo_test):
	dell_file('output//'+str(g))
i=2
if i==2:
	import main
	main()