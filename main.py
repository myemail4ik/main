#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime, time
import random
from PIL import Image, ImageFilter
import os
import requests
import time
from random import shuffle
import pic #pic.picture(imgage_way,img_text)
import random_list



tokenvk = "110d381ed79978477c80de7452b829c4860ba00d83fc86be21eb237b41211a8276e2e4a21847ed371cb67"

tokenvk = "7d09c12592445e951e8b5f2ddba6a2e792dd1634e9d01ecdf1b649fe818469a00ba1e570c9c839d839b97"
#tokenvk = os.environ.get('vktoken')


#prosba ='\n  не забывайте про "/", иначе бот не будет читать ваши сообщения'
hi ="привет, вот что я могу:"
commands =" \n 1) /Топ (предложит выбрать жанр и выведет топ 5 в этом жанре)\n 2) Прятки (угадай где находится Мирай) \n 3) Играть (проверь свои знания в аниме) \n 4) Тест \n 5) /Cигна (сигна от Анимагик) \n 6) Камень|Ножницы|Бумага"
top ="Выбирете жанр: \n 1) /Варя (топ 5 любимых аниме Вари) \n 2) /Драма \n 3) /Экшн \n  4) /Школа \n 5) /Комедия \n  6) /Фэнтези \n 7) /Романтика \n 8) /Повседнев (повседневность) \n 9) /Музыка (музыкальне) \n 10) /Новинки"


collvo= 10 # кол во жанров
collvoinfile = 5 # кол во аниме в одном аниме
testcolvo = 50 # кол во аниме в тесте 

romantika ="romantic.txt"
fantasy="fantasy.txt"
comedy ="comedy.txt"
whatlike ="varya.txt"
school ="shool.txt"
novelty = "novelty.txt"
drama = "drama.txt"
action = "action.txt"
routine = "routine.txt"
musical = "musical.txt"



##%%%%%%%%%%%%%%% globals %%%%%%%%%%%%%%
war_ship_commands=['морской|бой','1а','1б',"1в","1г",'2а','2б',"2в","2г",'3а','3б',"3в","3г",'4а','4б',"4в","4г"]
commas=["привет","пока","/топ","прятки","/exit","/next","тест","1","2","3","4","начать","играть","/сигна", "Камень|Ножницы|Бумага"]+war_ship_commands # all commands
levl=0 #10
oldanime =0
olddanime=0
answe=0
err=0
qe=0

testcolvo=testcolvo+1

point = [None, None]
ships_x_u = []
ships_y_u = []
ships_install = 0
bomb_point = []
ships_point = []
status=True
shot_x_u=[]
shot_y_u=[]
firs_bomb=True

# massives
map_ship_user=([[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]])

map_ship_ps=([[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]])

user_bomb_used=([[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]])

ps_bomb_used=([[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]])

# ????????????????__машинное обучение__????????????????????
massive_ob=([[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]])

massive_ob_point=([[None,None,None,None],
                    [None,None,None,None],
                    [None,None,None,None],
                    [None,None,None,None]])

#@@@@@@@@@@@@@@@@@@ def @@@@@@@@@@@@@@@@@

print("------start-------")

def find_first_word(some_str):
	for i in some_str.split("/"):
		i = i.rstrip(",")
		if i[0].isalpha():
			return i


def send(text, user): #отпр текст
	vk_session.method("messages.send",{'user_id': user, 'message': text, 'random_id':0} )

def sendmax(text,user,file,key): # текст+idd+ картинка + json
	d =0
	if file!=0:
		fistwrld =find_first_word(file)
		if fistwrld!="game":
			file ="pictures/" + str(file)
			print(str(file))
		a = vk_session.method("photos.getMessagesUploadServer")
		b = requests.post(a['upload_url'], files={'photo':open(file,'rb')}).json()
		c = vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
		d = "photo{}_{}".format(c["owner_id"], c["id"])
	keyboard=0
	if key!=0:
		keyboard=open("json/"+key,"r",encoding='utf-8').read()

	time.sleep(0.5)
	vk_session.method("messages.send",{'user_id': user, 'message': text, 'keyboard' : keyboard, 'attachment': d, 'random_id':0} )
	file =0


#------------sigma------------

def signa(textim,idd):
	if len(textim)<21:
		text="Лови сигну от Анимагик))"
		pic.picture("pictures/signa.jpg",textim,idd)
		time.sleep(1)
		file = str(idd)+'.jpg'
		a = vk_session.method("photos.getMessagesUploadServer")
		b = requests.post(a['upload_url'], files={'photo':open(file,'rb')}).json()
		c = vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
		d = "photo{}_{}".format(c["owner_id"], c["id"])
		keyboard=0
		keyboard=open("json/main.json","r",encoding='utf-8').read()

		time.sleep(1)
		vk_session.method("messages.send",{'user_id': idd, 'message': text, 'keyboard' : keyboard, 'attachment': d, 'random_id':0} )
		time.sleep(2)
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), (str(idd)+'.jpg'))
		os.remove(path)
	else:
		sendmax("Много букв",idd,0,"main.json")

def stone_scissors_paper(response,bot_answer):
	out="False_stone_scissors_paper"
	if response == "камень" and bot_answer=="ножницы" and response!= bot_answer:
		out="True_stone_scissors_paper"

	if response == "бумага" and bot_answer=="камень" and response!= bot_answer:
		out="True_stone_scissors_paper"

	if response == "ножницы" and bot_answer=="бумага" and response!= bot_answer:
		out="True_stone_scissors_paper"
	if response == bot_answer:
		out="null_stone_scissors_paper"

	return out


"""
def signa1(err,idd,response):
	signa_response=''
	if len(response)>6:
		for s in range (6):
		    signa_response = signa_response + response[s]
		    print(signa_response)

	if signa_response=="/сигна":
		signa_response = response.replace("/сигна",'')
		signa_response = str(signa_response)
		print(signa_response)
		if signa_response[0]==" ":
			signa_response= signa_response[1:]
		print(signa_response[0])
		if len(signa_response)<=18:	
			signa(signa_response,idd)
		else:
			sendmax("Слишком длинный текст",idd,0,"main.json")	
		err = 0
	return err		
"""

###war_ship
# functions_math
def printMatrix ( matrix ):
   for i in range ( len(matrix) ):
      for j in range ( len(matrix[i]) ):
          print ( "{:4d}".format(matrix[i][j]), end = "" )
      print ()

def read_file_pop_learn(path):
	out=[]
	file_read = open(str(path), 'r', encoding="UTF-8")
	for line in file_read.readlines():
		out.append(line.replace('\n',''))
	file_read.close()
	print("pop_point:\n"+str(out))
	return out

def pop_in_map_point():
	massive_pop= read_file_pop_learn("learn_ship_point_in_war_ship.txt")
	massive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
	for i in massive_pop:
		massive.remove(int(i))
	print(massive)
	return massive

def point_plus(map,x,y):
    map[x][y]=1
    return map

def point_minus(map,x,y):
    map[x][y]=0
    return map

def user_bomb(map,x,y):
    point=[0,0]
    point[0]=int(x)
    point[1]=int(y)
    if map[point[0]][point[1]]==1:
        map[point[0]][point[1]]=2
    return map

def chek_win(map):
    g=0
    len_map=int(len(map))
    for i in range(0,len_map):
        for j in map[i]:
            if j==1:
                g=g+1
    if g==0:
        out=True
    else:
        out=False
    return  out

def bot_bomb(map,x,y):
    if map[x][y]==1:
        map[x][y]=2
    return map

def ps_automatick_bomb_cell(map_point,first):
    try:
        if first==True:
            map_point = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random_point=random.choice(map_point)
        map_point.remove(random_point)
        return [random_point,map_point]

    except:
        return [1,[1]]




def ps_automatick_bomb(random_cell):
    map_point = ([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

    for j in range(int(len(map_point))):
        for g in range(int(len(map_point[j]))):
            if random_cell== map_point[j][g] and map_point[j][g] != 0:
                point=[g,j]
                return point


def user_bombs_used_mapper(user_bomb_used,x,y):
    user_bomb_used[x][y]=1
    print("user_bomb_used:")
    printMatrix(user_bomb_used)
    return user_bomb_used


def ps_bombs_used_mapper(ps_bomb_used,x,y):
    ps_bomb_used[x][y]=1
    print("ps_bomb_used:")
    printMatrix(ps_bomb_used)
    return ps_bomb_used

def creater_ship_ps(map_ship_ps):
	random_point=[None,None,None]
	# generator_random_seed
	now = datetime.now()
	random_data=int(str(now.hour)+str(now.minute)+str(now.second)+str(now.day))
	while random_data>random.randint(0,3000):
		random_data=random_data-int(random.randint(0,1000))
	random.seed(int(random_data))

	# generator_point
	map_point = pop_in_map_point()
	for i in range(0,3):
		random_point[i] = random.choice(map_point)
		map_point.remove(random_point[i])
	#----on_map
	for map_for in range (0,3):
		map_point = ([[1, 2, 3, 4],
					  [5, 6, 7, 8],
					  [9, 10, 11, 12],
					  [13, 14, 15, 16]])

		for j in range(int(len(map_point))):
			for g in range(int(len(map_point[j]))):
				if random_point[map_for] == map_point[j][g] and map_point[j][g] != 0:
					map_ship_ps[g][j] = 1
	printMatrix(map_ship_ps)
	return map_ship_ps

def converter_letters_to_numbers(letter):
	letter=letter.upper()
	letters=['А','Б','В','Г']
	i=0
	for g in letters:
		if g==letter:
			letter=str(i)
			break
		i=i+1
	print(letter)
	return int(letter)

def convert_to_number(point):
	map_point = ([[1, 2, 3, 4],
				  [5, 6, 7, 8],
				  [9, 10, 11, 12],
				  [13, 14, 15, 16]])

	return map_point[point[0]][point[1]]


# functions_math
# functions graffick
'''
def paste_ship(x, y, map):
	obj = Image.open('ship.jpg')
	obj = obj.resize((40, 35), Image.ANTIALIAS)
	map.paste(obj, (x, y))
	return map
'''

def paste_ship(x, y, map):
	obj = Image.open('pictures/ship.png')
	obj = obj.resize((54, 35), Image.ANTIALIAS)
	map.paste(obj, (x-4, y), obj)
	return map


def paste_krest(x, y, map):
	obj = Image.open('pictures/krest.png')
	obj = obj.resize((50, 35), Image.ANTIALIAS)
	map.paste(obj, (x-4, y), obj)
	return map


def paste_bomb(x, y, map):
	obj = Image.open('pictures/bomb.png')
	obj = obj.resize((55, 45), Image.ANTIALIAS)
	map.paste(obj, (x-4, y-7), obj)
	return map


def converter_to_map(number,letter):
	if number!= None and letter!= None:
		x = [45,89,133,176]
		y = [3,42,81,120]
		x_pos=x[letter]
		y_pos=y[number]
		point=[x_pos,y_pos]
		return point



def mapper(map_ship_user,ps_bomb_used,idd):
	map_u = Image.open('pictures/map.jpg')
	#add user ships
	for i in range(0,4):
		for g in range(0,4):
			if map_ship_user[i][g]==1:
				point=[i,g]
				print(point)
				p=converter_to_map(point[0],point[1])
				map_u=paste_ship(p[0], p[1], map_u)
	#add bombs_user_map--------------------
	for i in range(0,4):
		for g in range(0,4):
			if ps_bomb_used[i][g]==1 and map_ship_user[i][g]==1 or map_ship_user[i][g]==2:
				point=[i,g]
				print(point)
				p=converter_to_map(point[0],point[1])
				map_u=paste_krest(p[0], p[1], map_u)

			if ps_bomb_used[i][g] == 1 and map_ship_user[i][g]==0:
				point = [i, g]
				print(point)
				p = converter_to_map(point[0], point[1])
				map_u = paste_bomb(p[0], p[1], map_u)

	map_u.save("pictures/"+str(idd)+"user_map_ship.jpg")


def mapper_ps_map(user_bomb_used,map_ship_ps,idd):
	map_p = Image.open('pictures/map.jpg')
	for i in range(0,4):
		for g in range(0,4):
			if user_bomb_used[i][g]==1 and map_ship_ps[i][g]==1 or map_ship_ps[i][g]==2 :
				point=[i,g]
				print(point)
				p=converter_to_map(point[0],point[1])
				map_p=paste_krest(p[0], p[1], map_p)

			if user_bomb_used[i][g] == 1 and map_ship_ps[i][g] == 0:
				point = [i, g]
				print(point)
				p = converter_to_map(point[0], point[1])
				map_p = paste_bomb(p[0], p[1], map_p)
	map_p.save("pictures/"+str(idd)+"ps_map_ship.jpg")


def dell_file(path):
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path)
	os.remove(path)

def merging_pictures_war_ship(map_p_1,map_p_2,idd):
	map_1 = Image.open('pictures/'+str(idd)+str(map_p_1))
	map_2=Image.open('pictures/'+str(idd)+str(map_p_2))
	area=Image.open('pictures/area_war_ship.png')
	area.paste(map_1, (0, 0))
	area.paste(map_2, (218, 0))
	area.save('pictures/'+str(idd)+'output_maps_war_ship.png')

# машинное обучение----------------
class Learn_war_ship(object):
	def __init__(self,massive_ob,massive_ob_point,path_learn_file):
		self.path_learn_file = str(path_learn_file)
		self.massive_ob_point=massive_ob_point
		self.hod_number=1
		self.massive_ob=massive_ob

	def in_game(self,point):
		self.position=point
		self.massive_ob[self.position[0]][self.position[1]]=self.hod_number
		self.massive_ob_point[self.position[0]][self.position[1]]=point
		self.hod_number = self.hod_number + 1

	def numbers_lower(self):
		printMatrix(self.massive_ob)
		self.point=([])
		status=0
		while status <16:
			for j in range(4):
				for g in range(4):
					if self.massive_ob[j][g]==status and self.massive_ob[j][g]!=0:
						self.point.append([j,g])
						self.massive_ob[j][g]=0
			status=status+1

	def pop_massive_function(self):
		line=0
		try:
			file_output = open(self.path_learn_file, 'w')
			for i in self.point:
				if line<3:
					file_output.write(str(convert_to_number(i))+"\n")
					line=line+1
			file_output.close()
		except:
			pass

	def cleaner(self):
		print("Clean...")
		self.massive_ob_point=([[None,None,None,None],
								[None,None,None,None],
								[None,None,None,None],
								[None,None,None,None]])
		self.massive_ob=([[0,0,0,0],
						  [0,0,0,0],
						  [0,0,0,0],
						  [0,0,0,0]])
		self.hod_number = 1
		self.position=[None,None]
		self.point=None

#--------------------------------

def topchick(failname): # открытите текст файла /топ
	f = open(failname, "r",encoding = 'utf-8')
	data = f.read()
	f.close()
	return data



def test(testcolvo): # массив теста тест
	r = list(range(1,testcolvo))
	shuffle(r)
	return r




def randnumanime(): # играть
	randomnum1=random.randint(1,testcolvo)
	print("randomnum1:"+str(randomnum1))

	b = list(range(1,testcolvo))
	shuffle(b)
	print("b="+str(b))
	randomnum = str(b[int(randomnum1-2)])

	if randomnum == 39:
		randomnum = randomnum - 2
	if randomnum == 1 or 2:
		randonumber = 4

	print(str(randomnum))
	r = list(range(1,testcolvo))
	shuffle(r)
	print("r="+str(r))
	randomnum = int(randomnum)
	randompi = str(r[randomnum-2])
	print("out: "+str(randompi))
	return randompi




def game_gener(randompic): # чтение ответа и отправка теста или игра
	way_game = "game/"+randompic+"/question.txt"
	print(way_game)
	with open(way_game, 'r', encoding='utf-8') as f:
		answer_ques = f.read().splitlines()
	f.close()
	answer = answer_ques[0]
	print("ответ:" + str(answer))
	question = open(way_game, 'r', encoding='utf-8')
	questions= question.read()
	questions =questions[1 : ]
	picture =way_game = "game/"+randompic+"/picture.jpg"
	picture = str(picture)
	time.sleep(1)
	sendmax("Варианты ответов \n"+questions,idd, picture,"test.json")
	return answer

def game_check(resp,ansver,json): # свериться правильный ли ответ в тест или играть
	checkstatus = 2
	testmark="err"
	if resp=="1":
		if resp == ansver:
			testmark ="Правильно"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ryght.jpg",json)
		if resp!= ansver:
			testmark ="Упс, ошибочка"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ron.png",json)

	if resp=="2":
		if resp == ansver:
			testmark ="Правильно"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ryght.jpg",json)
		if resp!= ansver:
			testmark ="Упс, ошибочка"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ron.png",json)


	if resp=="3":
		if resp == ansver:
			testmark ="Правильно"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ryght.jpg",json)
		if resp!= ansver:
			testmark ="Упс, ошибочка"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ron.png",json)

	if resp=="4":
		if resp == ansver:
			testmark ="Правильно"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ryght.jpg",json)
		if resp!= ansver:
			testmark ="Упс, ошибочка"
			checkstatus = 1
			print(testmark)
			sendmax(testmark,idd,"ron.png",json)
	return checkstatus


def error(err, commas,response, signa_err): # ошибки
	summerr=0
	err=0

	for numbererr in range(int(len(commas))):
		print("err_for:"+str(numbererr))
		if response!= commas[numbererr]:
			summerr= summerr+1

	print(str(len(commas))+"sum_err:"+str(summerr))

	if summerr == int(len(commas)):
		print("sum_err:"+str(summerr))
		err=1
	summerr=0

	if signa_err==True:
		err=0

	return err

#----------------------top----------------



def top_mess(resp,top,err): # топ
	levl =0
	if resp=="/романтика":
		sendmax(top,idd,0,"top.json")
		textin =topchick("top/"+romantika)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0

	if resp=="/новинки":
		sendmax(top,idd,0,"top.json")
		textin =topchick("top/"+novelty)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0


	if resp=="/драма":
		sendmax(top,idd,0,"top.json")
		textin = topchick("top/"+drama)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0


	if resp=="/экшн":
		sendmax(top,idd,0,"top.json")
		textin = topchick("top/"+action)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0


	if resp=="/школа":
		sendmax(top,idd,0,"top.json")
		textin = topchick("top/"+school)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0


	if resp=="/варя":
		sendmax(top,idd,0,"top.json")
		textin = topchick("top/"+whatlike)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0


	if resp=="/комедия":
		sendmax(top,idd,0,"top.json")
		textin = topchick("top/"+comedy)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0

	if resp=="/фэнтези":
		sendmax(top,idd,0,"top.json")
		textin= topchick("top/"+fantasy)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0

	if resp=="/повседнев":
		sendmax(top,idd,0,"top.json")
		textin =topchick("top/"+routine)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0

	if resp=="/повседневность":
		sendmax(top,idd,0,"top.json")
		textin =topchick("top/"+routine)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0

	if resp=="/музыка":
		sendmax(top,idd,0,"top.json")
		textin =topchick("top/"+ musical)
		resp= resp.replace("/","")
		send(resp + ": \n" + textin, idd)
		err =0
	return err



#--------------------------------

vk_session=vk_api.VkApi(token=tokenvk)

session_api=vk_session.get_api
longpoll = VkLongPoll(vk_session)

while True:
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			print(str(event.user_id))
			print("new message: "+ str(datetime.strftime(datetime.now(), "%H:%M:%S")))
			print("text: "+str(event.text))
			idd = event.user_id
			response = event.text.lower()
			if response[0]==" ":
				response[0]=''
			user = vk_session.method("users.get", {"user_ids": idd})
			name_idd = user[0]['first_name']
			#############################################

			if event.to_me:
				signa_err=False
				if levl == 9 and response!="/сигна":
					signa(response,idd)
					signa_err=True
					levl=0
					err=0

				response= response.replace(" ","")

				err = error(err, commas, response, signa_err)
				print("err_exit:"+str(err))

				if response=="пока":
					sendmax("Пока;)",idd,"bay.jpg","hiafterbay.json")
					levl=0
					err=0


				if response=="привет" or response=="назад":
					sendmax(hi+"\n"+commands,idd,"hi.jpg","main.json")
					levl=0
					err=0

				if response=="начать":
					sendmax(hi+"\n"+commands,idd,"hi.jpg","main.json")
					levl=0
					err=0


				if response == "/сигна":
					print("signa_levl_9")
					sendmax("Введите текст",idd,0,0)
					levl=9
					err=0


				#-------------------------------------------------

				if response=="камень|ножницы|бумага":
					number_figer=["камень","ножницы","бумага"]
					shuffle(number_figer)
					number_figer=number_figer[1]
					number_figer=str(number_figer)
					answer= str(number_figer)
					print("answer_bot: "+str(number_figer))
					time.sleep(1)
					sendmax("Попробуй обыграй меня)",idd,0,"stone_paper_scissors.json")
					err=0
					levl=10

				if levl==10 and response!= "камень|ножницы|бумага" :
					number_figer=stone_scissors_paper(response,number_figer)
					if number_figer=="True_stone_scissors_paper":
						sendmax("Да ну тебя, плохая игра",idd,"mirai_right.jpg","main.json")
						levl=0
						err=0

					if number_figer=="False_stone_scissors_paper":
						sendmax("Я выиграла) Я загадывала " + answer+")",idd,"mirai_ron.png","main.json")
					err=0
					levl=0
					if number_figer=="null_stone_scissors_paper":
						sendmax("Ничья...",idd,"mirai_ron_nech.png","main.json")
					err=0
					levl=0


				if response =="играть":
					err=0
					print(str(oldanime)+"|||"+str(olddanime))
					numberanime=randnumanime()
					if numberanime == olddanime or oldanime:
						numberanime=randnumanime()
						print(str(oldanime)+"|||"+str(olddanime))
					olddanime = oldanime
					oldanime = numberanime
					time.sleep(1)
					levl =2
					answe = game_gener(numberanime)





				if levl ==2:
					err=0
					levl = game_check(response,answe,"main.json")


				#--------------------------topcommand----------------------
				if response=="тест":
					mark = 0
					levl=3
					err=0
					massiveanimetest = test(testcolvo)
					print(len(massiveanimetest))
					print(massiveanimetest[1])
					print(massiveanimetest)
					firstqe = str(massiveanimetest[0])
					secondqe = str(massiveanimetest[1])
					therdqe = str(massiveanimetest[2])
					fourthqe =str(massiveanimetest[3])
					fifthqe =str(massiveanimetest[4])
					sendmax("№1",idd,0,0)
					answertest = game_gener(firstqe)

				if response=="/next" and qe==1:
					levl=4
					sendmax("№2",idd,0,0)
					answertest = game_gener(secondqe)

				if response=="/next" and qe==2:
					levl=5
					sendmax("№3",idd,0,0)
					answertest = game_gener(therdqe)

				if response=="/next" and qe==3:
					levl=6
					sendmax("№4",idd,0,0)
					answertest = game_gener(fourthqe)
				if response=="/next" and qe==4:
					levl=7
					sendmax("№5",idd,0,0)
					answertest = game_gener(fifthqe)




				if levl == 3:
					err=0
					levl = game_check(response,answertest,"test5.json")
					if response==answertest:
						mark = mark+1
					qe=1
					levl = 3

				if levl == 4:
					err=0
					levl = game_check(response,answertest,"test5.json")
					if response==answertest:
						mark = mark+1
					qe=2
					levl = 4

				if levl == 5:
					err=0
					levl = game_check(response,answertest,"test5.json")
					if response==answertest:
						mark = mark+1
					qe=3
					levl = 5

				if levl == 6:
					err=0
					levl = game_check(response,answertest,"test5.json")
					if response==answertest:
						mark = mark+1
					qe=4
					levl = 6

				if levl == 7:
					err=0
					levl = game_check(response,answertest,"balltest5.json")
					if response==answertest:
						mark = mark+1
					levl = 7
					qe=0


				if response =="/балл":
					sendmax(str(mark)+"/5",idd,0,"main.json")
					if mark==5:
						sendmax("Ты ответил привильно на все 5 вопросов)",idd,"prise.png","main.json")
					levl = 0
					mark=0
					qe=0


				if response=="/exit":
					qe=0
					levl = 0
					mark=0
					sendmax(hi+"\n"+commands,idd,"hi.jpg","main.json")
					try:
						learner_1 = Learn_war_ship(massive_ob, massive_ob_point)
						learner_1.cleaner()
					except:
						pass

				#-------------------------------------




				if response=="морской|бой":
					levl=11
					out = ps_automatick_bomb_cell(None, True)
					point = out[0]
					return_automatick_ps_bomb = ps_automatick_bomb(out[0])
					mapper(map_ship_user, ps_bomb_used,idd)
					map_p = Image.open('pictures/map.jpg')
					map_p.save("pictures/"+str(idd)+"ps_map_ship.jpg")
					sendmax("Расположи 3 корабля", idd, str(idd)+"user_map_ship.jpg", "war_ship.json")

				if status == False or levl == 0:
					try:
						dell_file('pictures/' + str(idd) + 'user_map_ship.jpg')
						dell_file('pictures/' + str(idd) + "ps_map_ship.jpg")
						dell_file('pictures/' + str(idd) + 'output_maps_war_ship.png')
					except:
						print(None)

					map_ship_user = ([[0, 0, 0, 0],
									  [0, 0, 0, 0],
									  [0, 0, 0, 0],
									  [0, 0, 0, 0]])

					map_ship_ps = ([[0, 0, 0, 0],
									[0, 0, 0, 0],
									[0, 0, 0, 0],
									[0, 0, 0, 0]])

					user_bomb_used = ([[0, 0, 0, 0],
									   [0, 0, 0, 0],
									   [0, 0, 0, 0],
									   [0, 0, 0, 0]])

					ps_bomb_used = ([[0, 0, 0, 0],
									 [0, 0, 0, 0],
									 [0, 0, 0, 0],
									 [0, 0, 0, 0]])

					point = [None, None]
					ships_x_u = []
					ships_y_u = []
					ships_install = 0
					bomb_point = []
					ships_point = []
					status = True
					shot_x_u = []
					shot_y_u = []
					firs_bomb = True


				if levl==11 and response!='морской|бой' and ships_install<3:
					try:
						resp = list(response)
						print(resp)
						print("введите координату корабля: " + str(ships_install + 1))
						point=[0,0]
						try:
							point[0] = int(resp[0])
						except:
							point[0]=1

						print(str(point[0]) + str(resp[1]).upper())
						if str(point[0]) + str(resp[1]) in war_ship_commands:
							point[1] = converter_letters_to_numbers(resp[1]) + 1
							if str(point[0]) + str(point[1]) not in ships_point:
								map_ship_user = point_plus(map_ship_user, int(point[0]) - 1, int(point[1]) - 1)
								ships_point.append(str(point[0]) + str(point[1]))
								ships_install = ships_install + 1
								print(ships_point)
								mapper(map_ship_user, ps_bomb_used,idd)
							else:
								print("вы устанавливаете корабли на одну и туже клетку")

						else:
							print("вы debil")
						if ships_install<3:
							sendmax("Расположи 3 корабля", idd, str(idd) + 'user_map_ship.jpg', "war_ship.json")

					except:
						err=1


				if ships_install==3 and levl==11:
					map_ship_ps=creater_ship_ps(map_ship_ps)
					levl=12
					mapper(map_ship_user, ps_bomb_used,idd)
					merging_pictures_war_ship('user_map_ship.jpg', "ps_map_ship.jpg", idd)

					learner = Learn_war_ship(massive_ob, massive_ob_point,'learn_ship_point_in_war_ship.txt')
					learner.cleaner()

					sendmax("Огонь!!!", idd, str(idd) + 'output_maps_war_ship.png', "war_ship.json")


				#  series war
				if levl==12 and list(response)!=resp:
					try:
						resp=[10230231012,834789348903,4782347890234789234]
						new_point_bomb_user = False
						if new_point_bomb_user == False and status==True:
							point = [0, 0]
							resp_1 = list(response)
							print(resp_1)
							point[0] = int(resp_1[0])-1
							point[1] = converter_letters_to_numbers(resp_1[1])
							print(point)
							# ================ graffick
							user_bomb_used = user_bombs_used_mapper(user_bomb_used, point[0], point[1])
							mapper_ps_map(user_bomb_used, map_ship_ps,idd)
							##================ math

							if int(len(resp_1))>2:
								levl=0
								status=False
								err=1
								
							if str(point[0]) + str(point[1]) not in bomb_point:
								learner.in_game([point[0], point[1]])
								bomb_point.append(str(point[0]) + str(point[1]))
								new_point_bomb_user = True

							map_ship_ps = user_bomb(map_ship_ps, point[0], point[1])

							print("map_ship_user: ")
							printMatrix(map_ship_user)
							print("-----------------------------")
							print('map_ships_ps: ')
							printMatrix(map_ship_ps)

							win_user = chek_win(map_ship_ps)
							if win_user == True:
								print("User_win")
								sendmax("Баака((", idd, str(idd)+'ps_map_ship.jpg', 0)
								sendmax(hi+"\n"+commands, idd,'hi.jpg', 'main.json')
								status=False
								levl=0
								learner.numbers_lower()
								learner.pop_massive_function()
								learner.cleaner()


							if status == True and new_point_bomb_user == True:
								point_p = [None, None]
								print("strelat_ps")
								point = out[0]
								print(point)
								print('out_point: ' + str(return_automatick_ps_bomb[0] + 1) + '/' + str(return_automatick_ps_bomb[1] + 1))
								print("---------")
								map_ship_user = bot_bomb(map_ship_user, return_automatick_ps_bomb[0],
														 return_automatick_ps_bomb[1])

								##================ graffick

								ps_bomb_used = ps_bombs_used_mapper(ps_bomb_used, return_automatick_ps_bomb[0],
																	return_automatick_ps_bomb[1])
								mapper(map_ship_user, ps_bomb_used,idd)

								##================ graffick

								out = ps_automatick_bomb_cell(out[1], False)
								return_automatick_ps_bomb = ps_automatick_bomb(out[0])

								print("map_ship_user: ")
								printMatrix(map_ship_user)
								print("-----------------------------")
								print('map_ships_ps: ')
								printMatrix(map_ship_ps)

								win_ps = chek_win(map_ship_user)
								if win_ps == True and levl==12:
									print("Ps_win")
									sendmax("Я затопила все твои корабли))", idd, str(idd)+'user_map_ship.jpg', 0)
									sendmax(hi+"\n"+commands, idd, 'hi.jpg', 'main.json')
									status=False
									levl=0
									learner.cleaner()
					except:
						err=1

					if levl == 12:
						print("strelat")
						err = 0
						merging_pictures_war_ship('user_map_ship.jpg', "ps_map_ship.jpg", idd)
						sendmax("Огонь!!!", idd, str(idd)+'output_maps_war_ship.png', "war_ship.json")


				if status == False or levl == 0:
					try:
						dell_file('pictures/' + str(idd) + 'user_map_ship.jpg')
						dell_file('pictures/' + str(idd) + "ps_map_ship.jpg")
						dell_file('pictures/' + str(idd) + 'output_maps_war_ship.png')
					except:
						print(None)

					map_ship_user = ([[0, 0, 0, 0],
									  [0, 0, 0, 0],
									  [0, 0, 0, 0],
									  [0, 0, 0, 0]])

					map_ship_ps = ([[0, 0, 0, 0],
									[0, 0, 0, 0],
									[0, 0, 0, 0],
									[0, 0, 0, 0]])

					user_bomb_used = ([[0, 0, 0, 0],
									   [0, 0, 0, 0],
									   [0, 0, 0, 0],
									   [0, 0, 0, 0]])

					ps_bomb_used = ([[0, 0, 0, 0],
									 [0, 0, 0, 0],
									 [0, 0, 0, 0],
									 [0, 0, 0, 0]])

					point = [None, None]
					ships_x_u = []
					ships_y_u = []
					ships_install = 0
					bomb_point = []
					ships_point = []
					status = True
					shot_x_u = []
					shot_y_u = []
					firs_bomb = True



				if response=="прятки":
					list_variant=list(range(1,4))
					true_result = 1
					true_result = random_list.massive_random(list_variant)
					print("true_result_game_guess ответ:" + str(true_result))
					true_result = str(true_result)
					sendmax("Угадай где Мирай",idd,"background.jpg","game_guess.json")
					levl=8
					err =0


				if levl == 8 and true_result == response and response !="прятки":
					sendmax("Правильно", idd, str(true_result)+".jpg", "main.json")
					levl=0
					err=0

				if levl == 8 and true_result!= response  and response !="прятки":
					print("ron_game")
					sendmax("Упс, ошибочка(", idd, str(true_result)+".jpg", "main.json")
					levl=0
					err=0


				if response=="/топ":
					print(response)
					sendmax(top,idd,0,"top.json")
					err =0

				err=top_mess(response,top,err)

				if err == 1:
					sendmax('ERROR  Я не знаю такую команду((',idd,"error.jpg","main.json")
					err=0

					try:
						dell_file('pictures/' + str(idd) + 'user_map_ship.jpg')
						dell_file('pictures/' + str(idd) + "ps_map_ship.jpg")
						dell_file('pictures/' + str(idd) + 'output_maps_war_ship.png')
					except:
						print(None)

					map_ship_user = ([[0, 0, 0, 0],
									  [0, 0, 0, 0],
									  [0, 0, 0, 0],
									  [0, 0, 0, 0]])

					map_ship_ps = ([[0, 0, 0, 0],
									[0, 0, 0, 0],
									[0, 0, 0, 0],
									[0, 0, 0, 0]])

					user_bomb_used = ([[0, 0, 0, 0],
									   [0, 0, 0, 0],
									   [0, 0, 0, 0],
									   [0, 0, 0, 0]])

					ps_bomb_used = ([[0, 0, 0, 0],
									 [0, 0, 0, 0],
									 [0, 0, 0, 0],
									 [0, 0, 0, 0]])

					point = [None, None]
					ships_x_u = []
					ships_y_u = []
					ships_install = 0
					bomb_point = []
					ships_point = []
					status = True
					shot_x_u = []
					shot_y_u = []
					firs_bomb = True