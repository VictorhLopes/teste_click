
import os
from playwright.sync_api import sync_playwright
from src.pages.bad_button_page import BadButtonPage

def test_bad_button_click():
    test_url = os.getenv('TEST_URL')
    if not test_url:
        raise RuntimeError('Defina TEST_URL com a URL da página que possui #badButton')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(locale='pt-BR', viewport={"width": 1280, "height": 800})
        page = context.new_page()

        bad = BadButtonPage(page, test_url)
        bad.goto()
        bad.physical_click_button()

        assert bad.is_button_green(), 'O botão não ficou verde após clique físico.'

        context.close()
        browser.close()
