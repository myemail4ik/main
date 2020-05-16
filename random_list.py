from random import shuffle
import random
def randon_num(a,b):
	list_num=list(range(a,b+1))
	#print(list_num)
	len_list_num=len(list_num)+1
	#print(len_list_num)

	summ_list_num=0
	for i in list_num:
		summ_list_num = i + summ_list_num
	#print("1summ_list_num:"+str(summ_list_num))
	shuffle(list_num)
	while summ_list_num > 10:
		summ_list_num=summ_list_num/10
	#print("2summ_list_num:"+str(summ_list_num))		
	if summ_list_num > 0:
		summ_list_num =str(summ_list_num)
		len_summ_list_num= len(summ_list_num)-2
		summ_list_num=summ_list_num.replace(".",'')
	#	print ("3summ_list_num:"+str(len_summ_list_num))
		summ_list_num = summ_list_num[len_summ_list_num]
	#print("exit_out:"+str(summ_list_num))
	return int(summ_list_num)			

def massive_random(list_anime):
	len_list_anime=len(list_anime)
	print(len_list_anime)
	shuffle(list_anime)
	print (list_anime)
	random_num_return=randon_num(0,len_list_anime+1)
	random_num_return= int(random_num_return)
	list_anime = list_anime[random_num_return]
	return list_anime