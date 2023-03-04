# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open("D:\Downloads\srcimg.jpg")

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('arial.ttf', 430)
 
# Add Text to an image
I1.text((100, 450), "0001", font=myFont, fill =(0, 0, 0))
  
# Save the edited image
img.save("D:\Downloads\exports\srcimg2.jpg")
