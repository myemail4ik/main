import functions_parther
import time

global filter_
filter_=['None','Регистрация на сайте','Вход на сайт','']



def parther(name,page):
	path_file_html = str(name) + ".html"
	path_file_txt = "top/" + str(name) + ".txt"


	functions_parther.dell_file(path_file_txt)
	print('Dell file...')
	time.sleep(2)

	functions_parther.download_page(page,path_file_html)
	print('Download...')
	time.sleep(2)

	anime=functions_parther.main_parther_filter(filter_,path_file_html,path_file_txt)
	print(anime)
	print('Спизжено...')
	time.sleep(2)

	functions_parther.dell_file(path_file_html)
	print('Dell file html...')

	time.sleep(2)

	functions_parther.write_in_file(anime,path_file_txt)
	print("Writing...")

'''
page='https://animebest.org/anime/romantika/'
name='index'


parther(name,page)'''