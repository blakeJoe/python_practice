from PIL import Image, ImageFont, ImageDraw, ImageColor


def add_number(image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=150)
    color = ImageColor.colormap.get('red')
    width, height = image.size
    draw.text((width - 100, 30), '1', font=font, fill=color)
    image.save('d://result.jpg', 'jpeg')

if __name__ == '__main__':
    image = Image.open('d://t-mac.jpg')
    add_number(image)

