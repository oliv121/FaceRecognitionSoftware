import face_recognition
from PIL import Image, ImageDraw


# Нахождение лиц на фото
def face_search(img_path):
    img = face_recognition.load_image_file(img_path)
    faces_locations = face_recognition.face_locations(img)  # Массив с координатами лиц
    pil_img = Image.fromarray(img)                          # Пиллоу изображения для дальнейшей работы с ним
    draw1 = ImageDraw.Draw(pil_img)

    for (top, right, bottom, left) in faces_locations:
        # Рисуем прямоугольник на найденных лицах
        draw1.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=2)

    del draw1
    pil_img.save("images/new_img.jpg")

    return faces_locations


# Обрезка лиц с изображения и их кодировка
def cut_face(faces_locations, img_path):
    img = face_recognition.load_image_file(img_path)
    count = 0
    faces_encoding = []

    for face_location in faces_locations:
        top, right, bottom, left = face_location
        face_img = img[top:bottom, left:right]
        pil_img = Image.fromarray(face_img)
        pil_img.save(f"images/{count}_face_img.jpg")
        img_face = face_recognition.load_image_file(f"images/{count}_face_img.jpg")
        faces_encoding.append(face_recognition.face_encodings(img_face)[0])
        count += 1

    return count, faces_encoding


# Сравнение кодировок лиц
def face_compar(face1_encodings, face2_encodings):
    result = face_recognition.compare_faces([face1_encodings], face2_encodings)

    return result


# Кодируем лица с которыми будем сравнивать
def encoding_database():
    faces_encoding = []
    for number in range(15):
        img = face_recognition.load_image_file(f"images/faces_database/face{number}.jpg")
        faces_encoding.append(face_recognition.face_encodings(img)[0])

    return faces_encoding


# Основная функция
def face_rec(img_path):
    database_encoding = encoding_database()
    faces_locations = face_search(img_path)
    people_number, faces_encodings = cut_face(faces_locations, img_path)
    person_name = []
    for i in range(people_number):
        for j in range(15):
            flag = face_compar(faces_encodings[i], database_encoding[j])

            if flag == [True]:
                if j == 0:
                    person_name.append('Дейенерис Таргариен')
                    person_name.append('Эмилия Кларк')
                elif j == 1:
                    person_name.append('Джон Сноу')
                    person_name.append('Кит Хэрингтон')
                elif j == 2:
                    person_name.append('Серсея Ланнистер')
                    person_name.append('Лина Хиди')
                elif j == 3:
                    person_name.append('Тирион Ланнистер')
                    person_name.append('Питэр Динклэйдж')
                elif j == 4:
                    person_name.append('Джейме Ланнистер')
                    person_name.append('Николай Костер-Вальдау')
                elif j == 5:
                    person_name.append('Эддард Старк')
                    person_name.append('Шон Бин')
                elif j == 6:
                    person_name.append('Робб Старк')
                    person_name.append('Ричард Мэдден')
                elif j == 7:
                    person_name.append('Бран Старк')
                    person_name.append('Исаак Хемпсмид-Райт')
                elif j == 8:
                    person_name.append('Санса Старк')
                    person_name.append('Софи Тернер')
                elif j == 9:
                    person_name.append('Арья Старк')
                    person_name.append('Мэйми Уильямс')
                elif j == 10:
                    person_name.append('Роберт Баратеон')
                    person_name.append('Статус: мертв')
                elif j == 11:
                    person_name.append('Джоффри Баратеон')
                    person_name.append('Джек Глисон')
                elif j == 12:
                    person_name.append('Кхад Дрого')
                    person_name.append('Джейсон Момоа')
                elif j == 13:
                    person_name.append('Бриенна Тарт')
                    person_name.append('Гвендалин Кристи')
                elif j == 14:
                    person_name.append('Петир Бейлиш')
                    person_name.append('Эйдан Гиллен')
                else:
                    person_name.append('Неизвестный')
                    person_name.append('Неизвестный')
                break
        if flag == [False]:
            person_name.append('Неизвестный')
            person_name.append('Неизвестный')

    return person_name


if __name__ == '__main__':
    file_name = "images/test7.jpg"
    person = face_rec(file_name)
    for i in range(0,len(person)-1,2):
        print(i//2+1, '   ', person[i],'\n',
              '     ', person[i+1],'\n')
