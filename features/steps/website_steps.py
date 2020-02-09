from behave import given, when, then


# 1 шаг
@given('зашли на сайт "{page}"')
def step_impl(context, page):
    context.gogl.get_page(page)


# 2 шаг
@then('проверили, что появилось поле "{field}"')
def step_impl(context, field):
    context.gogl.check_field(field)


# 3 шаг
@when('ввели в поле поиск значение "{input_data}"')
def step_impl(context, input_data):
    context.gogl.enter_data_func(input_data)


# 4 шаг
@then('нажали на кнопку "{button_name}"')
def step_impl(context, button_name):
    context.gogl.click_button(button_name)


# 5 шаг
@when('нашли ссылку "{link}"')
def step_impl(context, link):
    context.link_cbr = link
    context.gogl.find_link(link)


# 6 шаг
@then('нажали на ссылку "http://www.cbr.ru/"')
def step_impl(context):
    context.gogl.click_link()


# 7 шаг
@then('проверили, что открыт нужный сайт')
def step_impl(context):
    context.cbr.check_link_url(context.link_cbr)


# 8 шаг
@then('нажали на ссылку "{text_link}"')
def step_impl(context, text_link):
    context.cbr.open_text_link(text_link)


# 9 шаг
@then('открыли раздел "{text_link}"')
def step_impl(context, text_link):
    context.cbr.open_text_link(text_link)


# 10 шаг
@when('в поле Ваша благодарность ввели значение "{input_data}"')
def step_impl(context, input_data):
    context.cbr.enter_data_func(input_data)


# 11 шаг
@when('поставили галочку "{text}"')
def step_impl(context, text):
    context.cbr.fill_checkbox(text)


# 12 шаг
@then('сделали скриншот')
def step_impl(context):
    context.cbr.take_screenshot('reception')


# 13 шаг
@when('нажали на кнопку "Три полоски"')
def step_impl(context):
    context.cbr.click_ham_button()


# 14 шаг
@when('нажали на раздел "{text_link}"')
def step_impl(context, text_link):
    context.cbr.open_text_link(text_link)


# 15 шаг
@when('нажали на ссылку "{text_link}"')
def step_impl(context, text_link):
    context.cbr.open_text_link(text_link)


# 16 шаг
@then('запомнили текст предупреждения')
def step_impl(context):
    context.cbr.check_warnings()


# 17 шаг
@when('сменили язык страницы на "{text_link}"')
def step_impl(context, text_link):
    context.cbr.open_text_link(text_link)


# 18 шаг
@then('проверили, что текст отличается от запомненного текста ранее')
def step_impl(context):
    context.cbr.check_warnings(check=True)


# 19 шаг
@then('сделали ещё скриншот')
def step_impl(context):
    context.cbr.take_screenshot('warning')
