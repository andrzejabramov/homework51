from classes import Our_request, pillow_rotate, pillow_crop, pillow_format, pillow_resize, pillow_watermark, \
    numpy_compare_img, numpy_anime, numpy_array

url_get = 'https://i.pinimg.com/736x/0d/b1/3c/0db13cca84e4d85919c2679324ef0c9f.jpg'
file = 'img/img1.png'

params = {"ll": "37.677751,55.757718",
          "spn": "0.016457,0.00619",
          "l": "map"}
url_map = "https://static-maps.yandex.ru/1.x/"
file_map = 'img/map.png'

url_post = 'https://jsonplaceholder.typicode.com/posts'
file_post = 'text_files/text_post.txt'

url_put = 'https://jsonplaceholder.typicode.com/posts/1'
file_put = 'text_files/text_put.txt'

data_post={
    "userId": 12,
    "title": "my test post",
    "body": "message in body 1",
    "photo": ['image1.png', 'image2.jpg', 'image3.pdf']
}

data_put={
    "userId": 12,
    "title": "my test post",
    "body": "message in body 2",
    "photo": ['image4.png', 'image5.jpg', 'image6.pdf']
}


#Создаем экземпляры класса с примерами библиотеки requests:
request = Our_request(url_get, file)
request_map = Our_request(url_map, file_map)
request_post = Our_request(url_post, file_post)
request_put = Our_request(url_put, file_put)


if __name__ == '__main__':
    #Метод экземпляра класса для примера работы метода get без параметров
    img = request.get_query()
    print(img)
    # Метод экземпляра класса для примера работы метода get с параметрами
    img_map = request_map.get_query_param(params)
    print(img_map)
    # Метод экземпляра класса для примера работы метода post для добавления данных на тестовом сервере
    text_post = request_post.post_query(data_post)
    # Метод экземпляра класса для примера работы метода put для изменения данных на тестовом сервере
    text_put = request_put.put_query(data_put)
    #методы и функции библиотеки pillow:
    #метод поворота изображения
    pillow_rotate('img/img1.png', 45)
    #метод обрезки изображения
    pillow_crop('img/img1.png', (0, 0, 300, 300))
    #метод изменения формата файла изображения
    pillow_format('img/img1.png', 'jpeg')
    #метод изменения размера изображения
    pillow_resize('img/img1.png', (200, 200))
    #метод наложения водяных знаков на изображение
    pillow_watermark('img/img1.png', 'Urban univercity')
    #методы и функции библиотеки numpy
    #метод сравнения двух изображений для поиска отличий
    numpy_compare_img('img/img1.png', 'img/img1_watermark.png')
    #метод создания анимации из изображения
    numpy_anime('gif/anime.gif')
    #один из методов обработки числовых массивов
    print(f'результат функции:\n{numpy_array()}')