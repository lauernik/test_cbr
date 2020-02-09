from features.pages.basepage import BasePage


class SearchPage(BasePage):

    def check_field(self, field):
        self.search_field = self.find_element(
            'input', 'title', field
        )

    def enter_data_func(self, input_data):
        self.data_input(self.search_field, input_data)

    def click_button(self, button_name):
        self.click_element(self.find_element(
            'input', 'value', button_name
        ))

    def find_link(self, link):
        self.finded_link = self.find_element(
            'a', 'href', link
        )

    def click_link(self):
        self.finded_link.click()
