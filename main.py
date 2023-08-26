# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

start = 1
end = 9999
output = "D:\Downloads\exports\srcimg {0:04d}.jpg"


for i in range (start,end + 1):
        img = Image.open("D:\Downloads\srcimg.jpg")

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)


        # Custom font style and font size
        myFontB = ImageFont.truetype('arial.ttf', 430)
        myFontS = ImageFont.truetype('arial.ttf', 270) 

        # Add Text to an image
        I1.text((100, 450), "{0:04d}".format(i), font=myFontB, fill=(0, 0, 0))

        # Create a new image, add the text on a transparent background, rotate the "new image" and paste it onto the original image
        img2 = Image.new("RGBA", (650,260), (0, 0 ,0, 0))
        I2 = ImageDraw.Draw(img2)
        I2.text((30,0),"{0:04d}".format(i), font=myFontS, fill=(0,0,0))

        img2 = img2.rotate(315, expand=1)
        img.paste(img2, (1030,30), img2)


        # Save the edited image
        img.save(output.format(i))




