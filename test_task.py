from .pages.main_page import SearchPage
from .pages.pictures_page import PicturesPage
import allure


@allure.feature('simbirsoft_task')
@allure.story('Авторизация на почте. Поиск и отправка письма')
def test_task_tensor(browser):
    link = "https://yandex.ru/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    search_page = SearchPage(browser, link)
    search_page.open()                      # открываем страницу
    search_page.search_area_availability()  # Проверка наличия поля поиска
    search_page.enter_tensor()              # Ввод значения Тензор
    search_page.hint_table_availability()   # Проверка таблицы с подсказками
    search_page.click_enter()               # Нажимаем Enter
    search_page.check_tensor_in_result()    # Ищем tensor.ru


def test_pictures_yandex(browser):
    link = "https://yandex.ru/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    pictures_page = PicturesPage(browser, link)
    pictures_page.open()                        # открываем страницу
    # проверяем наличие ссылки на картинки
    pictures_page.pictures_link_availability()
    pictures_page.pictures_link_click()         # клик по ссылке с картинками
    # открываем первую категорию с картинками
    pictures_page.select_first_category()
    pictures_page.first_picture_click()         # клик по первой картинке
    pictures_page.next_picture_click()          # клик по следующей картинке
    pictures_page.previous_picture_click()      # возврат к предыдущей картинке
