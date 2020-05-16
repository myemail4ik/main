from bs4 import BeautifulSoup
from requests import request
import os

class Parther_clss(object):
    def __init__(self,path_file_html,filter_l):
        self.path_file_html=path_file_html
        self.filter_=filter_l


    def soup_parth(self):
        anime_input=[]
        html = open(self.path_file_html, encoding='utf8').read()
        soup = BeautifulSoup(html, 'lxml')

        div=soup.find_all('a')

        for a in div:
            link=a.get('title')
            link=str(link)
            if link not in self.filter_:
                anime_input.append(link+'\n')
        return anime_input


class Filters(object):

    def __init__(self,anime,path_txt,path_html):
        self.anime=anime
        self.path_txt=path_txt
        self.path_html=path_html


    def filter_see(self):
    #anime.pop(0)
        number=0
        anime=self.anime
        for i in anime:
            number=number+1
            if 'Смотреть ' in i:
                anime.pop(number-1)

        return anime


    def filter_duble(self):
        anime_out=[]
        for i in range(1,int(len(self.anime))):
            if self.anime[i]==self.anime[i-1]:
                anime_out.append(self.anime[i])
        return anime_out



    def filter_replay(self):
        anime_out=[]
        for i in self.anime:
            if i not in anime_out:
                anime_out.append(i)
        return anime_out




def write_in_file(anime,path_file_txt):
    len_anime=len(anime)
    number_line=0
    my_file = open(path_file_txt, "w",encoding = 'utf-8')
    for i in range(len_anime):
        number_line=number_line+1
        my_file.write(str(number_line)+') '+ anime[i])
    my_file.close()



def main_parther_filter(filter_l,path_file_html,path_file_txt):
    parther=Parther_clss(path_file_html,filter_l)
    anime=parther.soup_parth()


    filter_anime=Filters(anime,path_file_txt,path_file_html)
    anime=filter_anime.filter_see()


    anime_l=filter_anime.filter_duble()

    filter_anime=Filters(anime_l,path_file_txt,path_file_html)
    anime=filter_anime.filter_replay()

    return anime


def  download_page(page,path_file_html):
    page_txt = request('GET', page).text
    with open(path_file_html, 'w', encoding='utf-8') as f:
        f.write(page_txt)


def dell_file(path_file):
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path_file)
        os.remove(path)
    except Exception:
        pass
