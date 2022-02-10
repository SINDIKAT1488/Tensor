from .base_page import BasePage
from .locators import PicturesPageLocators
from .test_data import PicturesPageTestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class PicturesPage(BasePage):
    def pictures_link_availability(self):
        with allure.step("Наличие ссылки на картинки"):
            self.pictures_link = self.browser.find_elements(
                *PicturesPageLocators.PICTURES_LINK)
            print(len(self.pictures_link))
            assert len(
                self.pictures_link) != 0, "Ссылка картинки не присутствует на странице"

    def pictures_link_click(self):
        with allure.step("Клик по ссылке с картинками"):
            if len(self.pictures_link) == 1:
                self.pictures_link[0].click()
            time.sleep(1)
            new_window = self.browser.window_handles[1]
            self.browser.switch_to.window(new_window)
            print(self.browser.current_url)
            assert self.browser.current_url == PicturesPageTestData.CURRENT_URL, "При нажатии на ссылку картинки не произошло перехода к соответствующему url"

    def select_first_category(self):
        with allure.step("Открытие первой категории с картинками"):
            first_category = self.browser.find_element(
                *PicturesPageLocators.FIRST_CATEGORY)
            first_category_text = first_category.get_attribute(
                PicturesPageLocators.FIRST_CATEGORY_TEXT)
            first_category_link = self.browser.find_element(
                *PicturesPageLocators.FIRST_CATEGORY_LINK)
            first_category_link.click()
            input_line = self.browser.find_element(
                *PicturesPageLocators.INPUT_LINE)
            print(input_line.get_attribute(
                PicturesPageLocators.INPUT_LINE_VALUE))
            assert first_category_text == input_line.get_attribute(
                PicturesPageTestData.INPUT_LINE), "При нажатии на 1 категорию в поиске не появился верный тест"

    def first_picture_click(self):
        with allure.step("Проверка открытия первой картинки"):
            first_picture = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(
                    PicturesPageLocators.FIRST_PICTURE)
            )
            first_picture.click()
            image_preview = self.browser.find_element(
                *PicturesPageLocators.IMAGE_PREVIEW)
            image = self.browser.find_element(*PicturesPageLocators.IMAGE)
            self.first_image_scr = image.get_attribute(
                PicturesPageLocators.FIRST_IMAGE_SCR)
            assert image_preview.is_displayed(), "Картинка не отображается при открытии"

    def next_picture_click(self):
        with allure.step("Проверка открыия следующей картинки"):
            self.browser.implicitly_wait(5)
            next_pictures_button = self.browser.find_element(
                *PicturesPageLocators.NEXT_PICTURES_BUTTON)
            next_pictures_button.click()
            next_picture = self.browser.find_element(
                *PicturesPageLocators.NEXT_PICTURE)
            next_picture_scr = next_picture.get_attribute(
                PicturesPageLocators.NEXT_PICTURE_SCR)
            print(self.first_image_scr)
            print(next_picture_scr)
            assert self.first_image_scr != next_picture_scr, "После нажатия кнопки вперед картинка не поменялась"

    def previous_picture_click(self):
        with allure.step("Проверка возврата к предыдущей картинке"):
            prev_pictures_button = self.browser.find_element(
                *PicturesPageLocators.PREV_PICTURES_BUTTON)
            prev_pictures_button.click()
            prev_picture = self.browser.find_element(
                *PicturesPageLocators.PREV_PICTURE)
            prev_picture_scr = prev_picture.get_attribute(
                PicturesPageLocators.PREV_PICTURE_SCR)
            print(self.first_image_scr)
            print(prev_picture_scr)
            assert self.first_image_scr == prev_picture_scr, "После нажатия кнопки назад отображается не изначальная картинка"
