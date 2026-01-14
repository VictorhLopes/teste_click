
import os
from playwright.sync_api import Page, expect

class UITAPClickPage:
    """POM da página UITAP /click com clique físico e screenshot."""

    URL = "http://uitestingplayground.com/click"
    BUTTON_SELECTOR = "#badButton"

    def __init__(self, page: Page):
        self.page = page
        self.button = page.locator(self.BUTTON_SELECTOR)

    def goto(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def physical_click_button(self):
        # Garante visibilidade
        self.button.scroll_into_view_if_needed()
        box = self.button.bounding_box()
        if not box:
            raise RuntimeError("Não foi possível obter bounding box do #badButton")
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2
        # Clique físico
        self.page.mouse.move(x, y)
        self.page.mouse.click(x, y)
        # Pequena espera + remove :hover
        self.page.wait_for_timeout(150)
        self.page.mouse.move(x + 200, y)

    def assert_button_success_class(self, timeout_ms: int = 5000):
        # Espera até que 'btn-success' esteja aplicado (sem regex)
        self.page.wait_for_function(
            """
            () => {
                const el = document.querySelector('#badButton');
                return el && el.classList.contains('btn-success');
            }
            """,
            timeout=timeout_ms,
        )

    def assert_button_green(self):
        # Alternativa por cor: aceita ativo e final
        try:
            expect(self.button).to_have_css("background-color", "rgb(40, 167, 69)", timeout=3000)
        except AssertionError:
            expect(self.button).to_have_css("background-color", "rgb(33, 136, 56)", timeout=2000)

    def screenshot_after_click(self, path: str = "screenshots/btn_green.png"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Validação estável por classe antes de capturar
        self.assert_button_success_class()
        try:
            self.button.screenshot(path=path)
        except Exception:
            self.page.screenshot(path=path, full_page=False)
