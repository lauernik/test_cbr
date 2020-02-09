from features.pages.basepage import BasePage
from datetime import datetime


class CbrPage(BasePage):

    def check_link_url(self, url):
        # Переходим в новую вкладку, т.к. страница открылась в новой
        self.browser.switch_to_window(self.browser.window_handles[-1])
        # Проверяем, что ссылки совпадают
        assert self.browser.current_url == url

    def open_text_link(self, text_link):
        self.click_element(
            self.browser.find_element_by_partial_link_text(text_link)
        )

    def enter_data_func(self, input_data):
        input_field = self.find_element(
            'textarea', 'id', 'MessageBody'
        )
        self.data_input(input_field, input_data)

    def fill_checkbox(self, text):
        self.click_element(self.browser.find_element_by_xpath(
            "//label[contains(text(),'{}')]".format(text)
        ))

    def take_screenshot(self, stage):
        now_time = datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
        self.browser.save_screenshot(
            f'screenshots/{stage}_{now_time}.png'
        )

    def click_ham_button(self):
        self.click_element(self.find_element(
            'span', 'class', 'burger'
        ))

    def check_warnings(self, check=False):
        find_element = self.browser.find_element_by_xpath(
            '//div[@id="content"]/p'
        ).text
        if check:
            assert find_element != self.warning_stored_ru
        else:
            self.warning_stored_ru = find_element
