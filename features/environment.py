from selenium import webdriver
from features.pages.searchpage import SearchPage
from features.pages.cbrpage import CbrPage


def before_all(context):
    context.browser = webdriver.Chrome()
    context.gogl = SearchPage(context.browser)
    context.cbr = CbrPage(context.browser)


def after_all(context):
    context.browser.quit()
