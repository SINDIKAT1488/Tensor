from selenium.webdriver.common.by import By


class SearchPageLocators():
    SEARCH_AREA = (By.CSS_SELECTOR,
                   ".input__control.input__input.mini-suggest__input")
    HINT_TABLE = (By.CSS_SELECTOR, "div.mini-suggest__popup_visible")
    ENTER_BUTTON = (By.CSS_SELECTOR,
                    "button[type='submit'].mini-suggest__button")
    RESULT_TABLE = (By.CSS_SELECTOR, "ul#search-result")
    LINK = "text"


class PicturesPageLocators():
    PICTURES_LINK = (By.CSS_SELECTOR, "a[data-id='images']")
    FIRST_CATEGORY = (By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0")
    FIRST_CATEGORY_TEXT = "data-grid-text"
    FIRST_CATEGORY_LINK = (
        By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0 a")
    INPUT_LINE = (By.CSS_SELECTOR, "input.input__control")
    INPUT_LINE_VALUE = "value"
    FIRST_PICTURE = (
        By.CSS_SELECTOR, ".justifier__item_first.serp-item_pos_0 a")
    IMAGE_PREVIEW = (By.CLASS_NAME, "MMImage-Preview")
    IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    FIRST_IMAGE_SCR = "src"
    NEXT_PICTURES_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    NEXT_PICTURE = (By.CLASS_NAME, "MMImage-Origin")
    NEXT_PICTURE_SCR = "src"
    PREV_PICTURES_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")
    PREV_PICTURE = (By.CLASS_NAME, "MMImage-Origin")
    PREV_PICTURE_SCR = "src"
