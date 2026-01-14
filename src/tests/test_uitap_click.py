
from playwright.sync_api import sync_playwright
from src.pages.uitap_click_page import UITAPClickPage

def test_physical_click_changes_color_to_green(tmp_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(locale="pt-BR", viewport={"width": 1280, "height": 800})
        page = context.new_page()

        uitap = UITAPClickPage(page)
        uitap.goto()
        uitap.physical_click_button()
        uitap.assert_button_success_class()

        out = tmp_path / "btn_green.png"
        uitap.screenshot_after_click(str(out))
        assert out.exists(), "Screenshot não foi gerado."

        context.close()
        browser.close()
