from features.pages.basepage import BasePage


class CbrPage(BasePage):

    def check_link_url(self, url):
        # Переходим в новую вкладку, т.к. страница открылась в новой
        self.browser.switch_to_window(self.browser.window_handles[-1])
        # Проверяем, что ссылки совпадают
        assert self.browser.current_url == url
