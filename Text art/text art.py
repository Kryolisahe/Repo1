from PIL import Image,ImageDraw

#opening and showing the image
img=Image.open("mickey.jpg")
img.show()

#resizing and maintaing aspect ratio
width,height=img.size
aspect_ratio=height/width
new_width=80
#height resizing using aspect ratio
#divided be 2 to reduce the pixels size and not disturbing the clarity of image
new_height=(aspect_ratio * new_width * 0.50)

#converting new_height to integer as new width is also integer
img=img.resize((new_width,int(new_height)))

#converting to grayscale
img=img.convert("L")

#getting pixel details
pixels=img.getdata()

#replacing each pixel with a character
char=['#','&','@','%','?','!',':',';',',','.',' ']
newpixels=""
for pixela in pixels:
    pixels=char[pixela//25]#each intensity is of 25 
    newpixels+=pixels
    #"@ % &"

#splitting strings of char into multiple strings of length
#equal to new width and height

newpixels_count=len(newpixels)
final_image=""

for index in range(0,newpixels_count,new_width):
    row=newpixels[index:(index+new_width)]
    final_image+="\n"+row

#printing image on screen
print(final_image)

#creating a jpg image file
img=Image.new('RGB',(1000,1000),(255,255,255))
draw=ImageDraw.Draw(img)
draw.text((0,0),final_image,(0,0,0))
img.show()
img.save("image.jpg")

with open("ascii_image.text","w") as f:
    f.write(final_image)
    





