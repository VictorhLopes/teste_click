
from playwright.sync_api import Page, expect
import os

class UITAPClickPage:
    """POM da página UITAP /click com clique físico e screenshot."""

    URL = "http://uitestingplayground.com/click"
    BUTTON_SELECTOR = "#badButton"  # seletor do botão problemático

    def __init__(self, page: Page):
        # Mantém referência para a página Playwright
        self.page = page
        # Cria um locator para o botão
        self.button = page.locator(self.BUTTON_SELECTOR)

    def goto(self):
        """Navega até a página e aguarda o DOM carregar."""
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def physical_click_button(self):
        """Executa clique físico: move e clica nas coordenadas do centro do botão."""
        # Garante visibilidade do elemento
        self.button.scroll_into_view_if_needed()
        # Obtém o bounding box (coordenadas e dimensões)
        box = self.button.bounding_box()
        if not box:
            raise RuntimeError("Não foi possível obter bounding box do #badButton")
        # Calcula o centro do botão
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2
        # Emula movimento e clique de mouse físico
        self.page.mouse.move(x, y)
        self.page.mouse.click(x, y)

    def assert_button_green(self):
        """Valida, via assertion, que o background ficou no verde esperado."""
        expect(self.button).to_have_css("background-color", "rgb(40, 167, 69)")

    def screenshot_after_click(self, path: str = "screenshots/btn_green.png"):
        """Tira screenshot do botão (ou da página se necessário) quando já estiver verde."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        expect(self.button).to_have_css("background-color", "rgb(40, 167, 69)")
        try:
            self.button.screenshot(path=path)
        except Exception:
            self.page.screenshot(path=path, full_page=False)
