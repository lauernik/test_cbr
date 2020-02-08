class SearchPage(object):
    def __init__(self, brow, page):
        self.browser = brow
        self.browser.get(page)

    def check_field(self, field):
        self.browser.find_element_by_xpath('//*[@title="'
                                           + field.lower().title() + '"]')
