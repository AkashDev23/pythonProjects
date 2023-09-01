import colorgram

rgb_colors = []
colors = colorgram.extract('D:\Python Projects\day 18\image.jpg', 25)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)