class SearchPage(object):
    def __init__(self, brow, page):
        self.browser = brow
        self.browser.get(page)

    def check_field(self):
        pass
