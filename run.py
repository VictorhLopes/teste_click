
from playwright.sync_api import sync_playwright
from src.pages.uitap_click_page import UITAPClickPage

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(locale="pt-BR", viewport={"width": 1280, "height": 800})
        page = context.new_page()

        uitap = UITAPClickPage(page)
        uitap.goto()
        uitap.physical_click_button()
        uitap.assert_button_success_class()
        uitap.screenshot_after_click("screenshots/btn_green.png")
        print("✔ Screenshot salvo em: screenshots/btn_green.png")

        context.close()
        browser.close()

if __name__ == "__main__":
    main()