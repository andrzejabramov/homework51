from requests import get, post, put, ConnectionError
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class Our_request:
    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name

    def get_query(self):
        response = get(self.url)
        try:
            response
        except ConnectionError:
            print("Проверьте подключение к сети.")
        else:
            with open(self.file_name, "wb") as file:
                file.write(response.content)
        return response

    def get_query_param(self, params):
        response = get(self.url, params=params)
        try:
            response
        except ConnectionError:
            print("Проверьте подключение к сети.")
        else:
            with open(self.file_name, "wb") as file:
                file.write(response.content)
        return response

    def post_query(self, data):
        response = post(self.url, data)
        try:
            response
        except ConnectionError:
            print("Проверьте подключение к сети.")
        else:
            with open(self.file_name, "wb") as file:
                file.write(response.content)
        return response.status_code

    def put_query(self, data):
        response = put(self.url, data)
        try:
            response
        except ConnectionError:
            print("Проверьте подключение к сети.")
        else:
            with open(self.file_name, "wb") as file:
                file.write(response.content)
        return response.status_code


def pillow_rotate(image_file, rotate):
    try:
        with Image.open(image_file) as img:
            rotated = img.rotate(rotate)
            rotated.save('img/img1_rotate.png')
    except FileNotFoundError:
        print('Файл не найден')


def pillow_crop(image_file, crop):
    try:
        with Image.open(image_file) as img:
            cropped = img.crop(crop)
            cropped.save('img/img1_cropped.png')
    except FileNotFoundError:
        print('Файл не найден')


def pillow_format(image_file, format):
    try:
        with Image.open(image_file) as img:
            formatted = img.save('img/img1.jpeg', format)
    except FileNotFoundError:
        print('Файл не найден')


def pillow_resize(image_file, size):
    try:
        with Image.open(image_file) as img:
            resized = img.resize(size)
            resized.save('img/img1_resized.png')
    except FileNotFoundError:
        print('Файл не найден')


def pillow_watermark(image_file, text):
    try:
        with Image.open(image_file) as img:
            font = ImageFont.truetype(font='Times New Roman', size=48)
            draw_text = ImageDraw.Draw(img)
            draw_text.text((20, 20), text, font=font, fill=('#ffffff'))
            img.save('img/img1_watermark.png')
    except FileNotFoundError:
        print('Файл не найден')


def numpy_compare_img(file1, file2):
    with Image.open(file1) as left:
        left.load()

    with Image.open(file2) as right:
        right.load()

    left_array = np.asarray(left)
    right_array = np.asarray(right)

    difference_array = right_array - left_array
    difference = Image.fromarray(difference_array)
    difference.show()


def numpy_anime(file_name):
    square_animation = []
    for offset in range(0, 100, 2):
        red = np.zeros((600, 600))
        green = np.zeros((600, 600))
        blue = np.zeros((600, 600))
        red[101 + offset: 301 + offset, 101 + offset: 301 + offset] = 255
        green[200: 400, 200: 400] = 255
        blue[299 - offset: 499 - offset, 299 - offset: 499 - offset] = 255
        red_img = Image.fromarray(red).convert('L')
        green_img = Image.fromarray(green).convert('L')
        blue_img = Image.fromarray(blue).convert('L')
        square_animation.append(Image.merge('RGB', (red_img, green_img, blue_img)))
    square_animation[0].save(file_name, save_all=True, append_images=square_animation[1:])

def numpy_array():
    filedata = np.genfromtxt('text_files/numpy.txt', delimiter=',')
    filedata = filedata.astype('int32')
    return filedata