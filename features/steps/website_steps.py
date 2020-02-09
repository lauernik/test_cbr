from behave import given, when, then
from features.pages.searchpage import SearchPage


@given('зашли на сайт "{page}"')
def step_impl(context, page):
    context.gogl = SearchPage(context.browser)
    context.gogl.get_page(page)


@then('проверили, что появилось поле "{field}"')
def step_impl(context, field):
    context.gogl.check_field(field)


@when('ввели в поле поиск значение "{input_data}"')
def step_impl(context, input_data):
    context.gogl.enter_data_func(input_data)


@then('нажали на кнопку "{button_name}"')
def step_impl(context, button_name):
    context.gogl.click_button(button_name)


@when('нашли ссылку "{link}"')
def step_impl(context, link):
    context.gogl.find_link(link)


@then('нажали на ссылку "http://www.cbr.ru/"')
def step_impl(context):
    context.gogl.click_link()
