# Notes made during chapter 21 of Automate the Boring Stuff With Python
# 2025-12-09

# %% colours ------------------------------------------------------------------

from PIL import ImageColor

# case insensitive
ImageColor.getcolor('RED', 'RGBA')
ImageColor.getcolor('magenta', 'RGBA')
ImageColor.getcolor('CornFlowerBlue', 'RGBA')

# all colour names
list(ImageColor.colormap)

# %% image manipulation -------------------------------------------------------

from PIL import Image

img = Image.open('D:/Python Projects/000 start.png')
img.show()

img.size
img.width
img.height
img.filename
img.format
img.format_description

# discard transparency
img = img.convert('RGB')
# format is automatic based on extension
img.save('D:/Python Projects/000 start.jpg')
# crop
# img.crop((first_horizontal, first_vertical, first_excl_horizontal, first_excl_vertical))
# copy
img2 = img.copy()

# new image
img2 = Image.new('RGB', (img.width, img.height))
# past onto new
img2.paste(img, (0,0))
img2.save('D:/Python Projects/000 start.jpg')

# PIL copy & paste do not use clipboard

# resize
width,height = img.size
img2 = img.resize((int(0.7 * width), int(0.7 * height)))
img2 = img.resize((width, height + 100))

# rotate - crops instead of resizing
img.rotate(90)
img.rotate(20)
# rotate - expanding
img.rotate(90, expand = True)
img.rotate(20, expand = True)
# flip - requires direction
img.transpose(Image.FLIP_LEFT_RIGHT)
img.transpose(Image.FLIP_TOP_BOTTOM)

# %% pixel editing ------------------------------------------------------------

a_colour = img.getpixel((10,10))

for x in range(int(img.width / 3)):
    for y in range(int(img.height / 3)):
        img.putpixel((3*x,3*y), a_colour)

img.show()

# %% drawing shapes -----------------------------------------------------------

from PIL import Image, ImageDraw

img = Image.new('RGBA', (200, 200), 'white')

draw = ImageDraw.Draw(img)
draw.line([(0,0), (199,199)], 'grey')
draw.rectangle((10,20,15,25), fill = 'blue')
draw.ellipse((105,105,155,135), fill = 'red', outline = 'orange', width = 4)

img.show()

# %% graphs -------------------------------------------------------------------

import matplotlib.pyplot as plt

# data
x_values = [0,1,2,3,4,5]
y_values1 = [23,34,65,56,12,32]
y_values2 = [24,36,57,64,11,31]

# line plot by default
plt.plot(x_values, y_values1)
plt.plot(x_values, y_values2)
plt.show()
# plot.savefig('filename.png')

# scatter
plt.scatter(x_values, y_values1)
plt.scatter(x_values, y_values2)
plt.show()

# bar chart
keys = ["A", "B", "C", "D"]
values = [10,20,60,30]
plt.bar(keys, values)
plt.show()

# pie chart
plt.pie(values, labels = keys, autopct='%.1f%%') # % accuracy
plt.show()

# %% graphs advanced ----------------------------------------------------------

import matplotlib.pyplot as plt

# data
x_values = [0,1,2,3,4,5]
y_values1 = [23,34,65,56,12,32]
y_values2 = [24,36,57,64,11,31]

plt.plot(x_values, y_values1, marker = 'o', color = 'b', label = "Line 1")
plt.plot(x_values, y_values2, marker = 's', color = 'r', label = "Line 2")
plt.legend()
plt.xlabel("The X-axis")
plt.ylabel("The Y-axis")
plt.title("The title")
plt.grid(True)
plt.show()

# %%
