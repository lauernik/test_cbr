class SearchPage(object):
    def __init__(self, brow, page):
        self.browser = brow
        self.browser.get(page)

    def check_field(self, field):
        self.search_field = self.browser.find_element_by_xpath(
            '//input[@title="' + field + '"]')

    def enter_data_func(self, input_data):
        self.search_field.send_keys(input_data)

    def click_button(self, button_name):
        button = self.browser.find_element_by_xpath(
            '//input[@value="' + button_name + '"]')
        button.click()

    def find_link(self, link):
        self.finded_link = self.browser.find_element_by_xpath(
            '//a[@href="' + link + '"]')

    def click_link(self):
        self.finded_link.click()
