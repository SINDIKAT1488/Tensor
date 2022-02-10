from re import search
from select import select
from .base_page import BasePage
from .locators import SearchPageLocators
from .test_data import SearchPageTestData
from selenium.webdriver.common.by import By
import allure


class SearchPage(BasePage):
    def search_area_availability(self):
        with allure.step("Проверка наличия поля поиска"):
            self.search_area = self.browser.find_elements(
                *SearchPageLocators.SEARCH_AREA)
            print(len(self.search_area))
            assert len(self.search_area) != 0, "Отсутствует поле поиска"

    def enter_tensor(self):
        with allure.step("Ввод значения Тензор"):
            if len(self.search_area) == 1:
                self.search_area[0].send_keys(SearchPageTestData.SEARCH_AREA)

    def hint_table_availability(self):
        with allure.step("Проверка таблицы с подсказками"):
            self.browser.implicitly_wait(5)
            hint_table = self.browser.find_elements(
                *SearchPageLocators.HINT_TABLE)
            print(len(hint_table))
            assert len(hint_table) != 0, "Не появидась таблица с подсказками"

    def click_enter(self):
        with allure.step("Нажимаем Enter"):
            enter_button = self.browser.find_element(
                *SearchPageLocators.ENTER_BUTTON)
            enter_button.click()
            self.browser.implicitly_wait(5)
            self.result_table = self.browser.find_elements(
                *SearchPageLocators.RESULT_TABLE)
            print(len(self.result_table))
            assert len(
                self.result_table) != 0, "Не появилась таблица с результатами поиска"

    def check_tensor_in_result(self):
        with allure.step("Ищем tensor.ru"):
            result_list = []
            for i in range(5):
                self.browser.implicitly_wait(5)
                result = self.browser.find_element(
                    By.CSS_SELECTOR, f"li[data-cid='{str(i)}'] .Organic-Subtitle a")
                link = result.get_attribute(SearchPageLocators.LINK)
                result_list.append(link)
            print(result_list)
            assert SearchPageTestData.TENSOR in result_list, "В списке первых 5 результатов нет tensor.ru"
