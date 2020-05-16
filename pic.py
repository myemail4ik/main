from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps, ImageFilter
import textwrap

def convert_pase(input_text):
	input_text=str(input_text)
	if '_' in input_text:
		input_text= input_text.replace("_"," ")
		print(input_text)
	return input_text		



def picture(imgage_way,img_text,idd):
	string=0
	#img_text=convert_pase(img_text)
	img=Image.open(imgage_way)
	text1=img_text
	if len(img_text)>5:
		wrapper =textwrap.TextWrapper(width=7)
		text1 =wrapper.fill(text=img_text) 

	f = font = ImageFont.truetype(r'animagick.ttf', 200)
	txt=Image.new('L', (1500,730))
	d = ImageDraw.Draw(txt)
	d.text( (20, 20),text1,  font=f, fill=255)
	w=txt.rotate(106,  expand=1)


	img.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (-150,-595),  w)
	
	img_c= img.filter(ImageFilter.SMOOTH)
	img_c.save(str(idd)+'.jpg')



def picture_game_guess(image_code,idd):
	image_code= str(image_code)
	mirai_picture =Image.open("pictures/mirai.png")
	background = Image.open("pictures/background.png")

	mirai_picture = mirai_picture.resize((1224,888))
	#mirai_picture=mirai_picture.rotate(100,  expand=1)

	mirai_pos_x=0
	mirai_pos_y=0
	if image_code=='1':
		mirai_pos_x=180
		mirai_pos_y=300

	if image_code=='2':
		mirai_pos_x=2100
		mirai_pos_y=300

	if image_code=='3':
		mirai_pos_x=4300
		mirai_pos_y=300	

	background.paste(mirai_picture, (mirai_pos_x, mirai_pos_y),  mirai_picture)
	background=background.convert('RGB')
	background.save("pictures/"+str(idd)+".jpg")


#picture("pictures/signa.jpg","Doctor___S",11111)