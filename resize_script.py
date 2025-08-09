from PIL import Image

img = Image.open('assets\images\galaga_spaceship.png')
img = img.resize((64, 64))
img.save('small_galaga_spaceship.png')