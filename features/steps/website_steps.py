from behave import given, when, then
from page import SearchPage


@given('зашли на сайт "{page}"')
def step_impl(context, page):
    context.gogl = SearchPage(context.browser, page)


@then('проверили, что появилось поле "{field}"')
def step_impl(context, field):
    context.gogl.check_field(field)
