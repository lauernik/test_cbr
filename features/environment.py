from selenium import webdriver
from features.pages.searchpage import SearchPage
from features.pages.cbrpage import CbrPage
from os import mkdir
from shutil import rmtree
from features.send_mail import send_email


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)
    context.browser.maximize_window()
    context.gogl = SearchPage(context.browser)
    context.cbr = CbrPage(context.browser)
    mkdir('screenshots')


def after_all(context):
    context.browser.quit()
    send_email('test@test.com')
    rmtree('screenshots')
