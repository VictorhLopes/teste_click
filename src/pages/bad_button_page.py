
from playwright.sync_api import Page, expect
from src.utils.mouse import physical_click_center

class BadButtonPage:
    """Page Object da página UITAP /click (botão que ignora click DOM)."""

    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
        self.button = page.locator('#badButton')

    def goto(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state('domcontentloaded')

    def physical_click_button(self):
        physical_click_center(self.page, self.button)

    def assert_button_success_class(self, timeout_ms: int = 5000):
        self.page.wait_for_function(
            """
            () => {
                const el = document.querySelector('#badButton');
                return el && el.classList.contains('btn-success');
            }
            """,
            timeout=timeout_ms
        )

    def assert_button_green(self):
        try:
            expect(self.button).to_have_css("background-color", "rgb(40, 167, 69)", timeout=3000)
        except AssertionError:
            expect(self.button).to_have_css("background-color", "rgb(33, 136, 56)", timeout=2000)
