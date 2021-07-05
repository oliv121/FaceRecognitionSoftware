from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QScrollArea, QApplication,
                             QVBoxLayout, QMainWindow, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import face_recognition
from PIL import Image, ImageDraw


# Нахождение лиц на фото
def face_search(img_path):
    img = face_recognition.load_image_file(img_path)        # Изображение с которым мы будем работать
    faces_locations = face_recognition.face_locations(img)  # Список с координатами лиц
    pil_img = Image.fromarray(img)                          # Пиллоу изображения для дальнейшей работы с ним
    draw1 = ImageDraw.Draw(pil_img)

    for (top, right, bottom, left) in faces_locations:
        # Рисуем прямоугольник на найденных лицах
        draw1.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=2)

    del draw1
    pil_img.save("images/new_img.jpg")                      # Сохраняем новое изображение

    return faces_locations


# Обрезка лиц с изображения и их кодировка
def cut_face(faces_locations, img_path):
    img = face_recognition.load_image_file(img_path)        # Изображение с которым мы будем работать
    count = 0                                               # Количество лиц
    faces_encoding = []                                     # Список, где храняться кодировки лиц

    for face_location in faces_locations:
        top, right, bottom, left = face_location
        face_img = img[top:bottom, left:right]              # Новое изображение с вырезанным лицом
        pil_img = Image.fromarray(face_img)
        pil_img.save(f"images/{count}_face_img.jpg")
        img_face = face_recognition.load_image_file(f"images/{count}_face_img.jpg")
        faces_encoding.append(face_recognition.face_encodings(img_face)[0])  # Добавление в массив кодировку нового лица
        count += 1

    return count, faces_encoding


# Сравнение кодировок лиц
def face_compar(face1_encodings, face2_encodings):
    result = face_recognition.compare_faces([face1_encodings], face2_encodings) # Возвращает True или False

    return result


# Кодируем лица с которыми будем сравнивать
def encoding_database():
    faces_encoding = []                                     # Список с кодировками лиц
    for number in range(15):
        img = face_recognition.load_image_file(f"images/faces_database/face{number}.jpg")
        faces_encoding.append(face_recognition.face_encodings(img)[0])  # Добавление в массив кодировку нового лица

    return faces_encoding


# Основная функция распознавания
def face_rec(img_path):
    database_encoding = encoding_database()                                 # Кодируем лица с которыми будем сравнивать
    faces_locations = face_search(img_path)                                 # Список с координатами лиц на фото
    people_number, faces_encodings = cut_face(faces_locations, img_path)    # Ко-во лиц и список их кодировок
    person_info = []                                                        # Список с данными об найденными лицах
    for i in range(people_number):
        for j in range(15):
            chek_flag = face_compar(faces_encodings[i], database_encoding[j]) # Результат сравнивания лица с лицом из бд

            if chek_flag == [True]:
                if j == 0:
                    person_info.append('Дейенерис Таргариен')
                    person_info.append('Актер: Эмилия Кларк')
                    person_info.append('СПОЙЛЕР: умрет от рук Джона Сноу')
                elif j == 1:
                    person_info.append('Джон Сноу')
                    person_info.append('Актер: Кит Хэрингтон')
                    person_info.append('СПОЙЛЕР: жив')
                elif j == 2:
                    person_info.append('Серсея Ланнистер')
                    person_info.append('Актер: Лина Хиди')
                    person_info.append('СПОЙЛЕР: умрет вмсесте с братом Джейме')
                elif j == 3:
                    person_info.append('Тирион Ланнистер')
                    person_info.append('Актер: Питэр Динклэйдж')
                    person_info.append('СПОЙЛЕР: жив')
                elif j == 4:
                    person_info.append('Джейме Ланнистер')
                    person_info.append('Актер: Николай Костер-Вальдау')
                    person_info.append('СПОЙЛЕР: умрет вместе с сестрой Серсеей')
                elif j == 5:
                    person_info.append('Эддард Старк')
                    person_info.append('Актер: Шон Бин')
                    person_info.append('СПОЙЛЕР: умрет от рук Джоффри')
                elif j == 6:
                    person_info.append('Робб Старк')
                    person_info.append('Актер: Ричард Мэдден')
                    person_info.append('СПОЙЛЕР: умрет на крсаной свадьбе')
                elif j == 7:
                    person_info.append('Бран Старк')
                    person_info.append('Актер: Исаак Хемпсмид-Райт')
                    person_info.append('СПОЙЛЕР: жив')
                elif j == 8:
                    person_info.append('Санса Старк')
                    person_info.append('Актер: Софи Тернер')
                    person_info.append('СПОЙЛЕР: жива')
                elif j == 9:
                    person_info.append('Арья Старк')
                    person_info.append('Актер: Мэйми Уильямс')
                    person_info.append('СПОЙЛЕР: жива')
                elif j == 10:
                    person_info.append('Роберт Баратеон')
                    person_info.append('Актер: Статус: мертв')
                    person_info.append('СПОЙЛЕР: умрет из-за кабана')
                elif j == 11:
                    person_info.append('Джоффри Баратеон')
                    person_info.append('Актер: Джек Глисон')
                    person_info.append('СПОЙЛЕР: умрет из-за яда')
                elif j == 12:
                    person_info.append('Кхад Дрого')
                    person_info.append('Актер: Джейсон Момоа')
                    person_info.append('СПОЙЛЕР: умрет от рук Дейенерис')
                elif j == 13:
                    person_info.append('Бриенна Тарт')
                    person_info.append('Актер: Гвендалин Кристи')
                    person_info.append('СПОЙЛЕР: жива')
                elif j == 14:
                    person_info.append('Петир Бейлиш')
                    person_info.append('Актер: Эйдан Гиллен')
                    person_info.append('СПОЙЛЕР: умрет от рук Арьи')
                else:
                    person_info.append('Неизвестный')
                    person_info.append('Актер: Неизвестный')
                    person_info.append('СПОЙЛЕР: -')
                break
        if chek_flag == [False]:
            person_info.append('Неизвестный')
            person_info.append('Неизвестный')
            person_info.append('Спойлер - нет')

    return person_info


# Первое окно
class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 200)
        self.setWindowTitle('Распознавание персонажев')

        # Тексты с критериями загрузки изображения
        self.lbl1 = QLabel("1. Лица на фотографии должны быть хорошо видны", self)
        self.lbl1.move(10, 10)
        self.lbl1.adjustSize()
        self.lbl2 = QLabel("2. Желательно не больше 3", self)
        self.lbl2.move(10, 30)
        self.lbl2.adjustSize()
        self.lbl3 = QLabel("3. Чем ниже качесто, тем быстрее обрабатывается фото", self)
        self.lbl3.move(10, 50)
        self.lbl3.adjustSize()

        self.btn = QPushButton(self)            # Кнопка для загрузки изображения
        self.btn.setText('Загрузить фото')
        self.btn.resize(150, 50)
        self.btn.move(175, 100)

        self.btn.clicked.connect(self.window2)

    def window2(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0] # Открывает диалоговое окно
        person_name = face_rec(self.file_name)                  # Вызов функции распознавания
        self.hide()                                             # Закрыть первое окно

        self.second_form = SecondWindow(person_name)            # Вызов вторго окна
        self.second_form.show()


# Второе окно
class SecondWindow(QMainWindow):

    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle('Персонажи и спойлеры')
        person_info = args[-1]

        self.scroll = QScrollArea()                                 # Область прокрутки
        self.widget = QWidget()                                     # Виджет, содержащий коллекцию Vertical Box
        self.vbox = QVBoxLayout()                                   # Вертикальное поле

        self.lbl_photo = QLabel("Найденные лица:\n", self)
        self.vbox.addWidget(self.lbl_photo)

        self.pixmap = QPixmap(f"images/new_img.jpg")                # Фото с найденными лицами
        self.main_image = QLabel(self)
        self.main_image.setPixmap(self.pixmap)
        self.vbox.addWidget(self.main_image)

        self.lbl_persons = QLabel("\nНайденные персонажи:", self)
        self.vbox.addWidget(self.lbl_persons)

        for i in range(0, len(person_info)-1, 3):
            object1 = QLabel(f"\n\n{person_info[i]}", self)         # Имя героя
            object2 = QLabel(f"{person_info[i + 1]}", self)         # Имя актера
            object3 = QLabel(f"{person_info[i + 2]}", self)         # Спойлер по герою
            self.vbox.addWidget(object1)
            self.vbox.addWidget(object2)
            self.vbox.addWidget(object3)
            self.pixmap = QPixmap(f"images/{i // 3}_face_img.jpg")  #
            self.image = QLabel(self)
            self.image.setPixmap(self.pixmap)
            self.vbox.addWidget(self.image)

        self.widget.setLayout(self.vbox)

        # Свойства области прокрутки
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)   # По вертикали
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # По горизонтали
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.show()

        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstWindow()
    ex.show()
    sys.exit(app.exec())
