class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def get_page(self, page):
        self.browser.get(page)

    def find_element(self, element, attr, value):
        return self.browser.find_element_by_xpath(
            f'//{element}[@{attr}="{value}"]'
        )

    def click_element(self, locator):
        locator.click()

    def data_input(self, locator, data):
        locator.send_keys(data)
