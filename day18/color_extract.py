import colorgram

color_pallette = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in color_pallette:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)

