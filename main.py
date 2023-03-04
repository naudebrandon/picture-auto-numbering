# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open("D:\Downloads\srcimg.jpg")

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)


# Custom font style and font size
myFontB = ImageFont.truetype('arial.ttf', 430)
myFontS = ImageFont.truetype('arial.ttf', 270) 

# Add Text to an image
I1.text((100, 450), "0001", font=myFontB, fill=(0, 0, 0))

# Save the edited image
img.save("D:\Downloads\exports\srcimg2.jpg")

img2 = Image.open("D:\Downloads\exports\srcimg2.jpg")
I2 = ImageDraw.Draw(img2)
I2.text((1000,250),"0001", font=myFontS, fill=(0 ,0, 0))
img2.rotate(I2,330,expand=1)




