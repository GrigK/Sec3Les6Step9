"""
pytest -s -v --tb=short test_parser.py
выдаст ошибку за неиспользуемый параметр

pytest -s -v --tb=short --browser_name=firefox test_parser.py
pytest -s -v --tb=short --browser_name=chrome test_parser.py
без ошибки
"""
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")