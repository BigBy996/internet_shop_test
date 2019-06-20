link_template = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/"


def test_contains_add_to_basket_button(browser, request):
    language = request.config.getoption("language")
    browser.get(link_template.format(language))
    browser.find_element_by_class_name("btn-add-to-basket")
