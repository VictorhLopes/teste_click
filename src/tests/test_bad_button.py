
import os
from playwright.sync_api import sync_playwright
from src.pages.bad_button_page import BadButtonPage

def test_bad_button_click():
    # Usa TEST_URL se definida; senão, fallback para a página oficial do desafio
    test_url = os.getenv('TEST_URL', 'http://uitestingplayground.com/click')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(locale='pt-BR', viewport={"width": 1280, "height": 800})
        page = context.new_page()

        bad = BadButtonPage(page, test_url)
        bad.goto()
        bad.physical_click_button()
        bad.assert_button_success_class()

        context.close()
        browser.close()
