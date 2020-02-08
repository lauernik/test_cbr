from behave import given, when, then


@given('зашли на сайт "{page}"')
def step_impl(context, page):
    context.browser.get(page)
