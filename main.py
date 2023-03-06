# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open("D:\Downloads\srcimg.jpg")

# Call draw Method to add 2D graphics in an image
# I1 = ImageDraw.Draw(img)


# Custom font style and font size
myFontB = ImageFont.truetype('arial.ttf', 430)
myFontS = ImageFont.truetype('arial.ttf', 270) 

# Add Text to an image
# I1.text((100, 450), "0001", font=myFontB, fill=(0, 0, 0))


tim = Image.new("RGBA", (650,260), (0, 0 ,0, 0))
dr = ImageDraw.Draw(tim)
dr.text((30,0),"0001", font=myFontS, fill=(0,0,0))

tim = tim.rotate(315, expand=1)
img.paste(tim, (1030,30), tim)

# img2 = Image.open("D:\Downloads\exports\srcimg2.jpg")
#img = img.rotate(45,expand=1)
#I2 = ImageDraw.Draw(img)
#I2.text((870,340),"0001", font=myFontS, fill=(0 ,0, 0))

#img = img.rotate(315 ,expand=1)



# Save the edited image
img.save("D:\Downloads\exports\srcimg2.jpg")


