
from playwright.sync_api import Page

class BadButtonPage:
    """Page Object para página com botão problemático (#badButton)."""

    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
        self.button = page.locator('#badButton')

    def goto(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state('domcontentloaded')

    def physical_click_button(self):
        self.button.scroll_into_view_if_needed()
        box = self.button.bounding_box()
        if not box:
            raise RuntimeError('Não foi possível obter bounding box do #badButton')
        x = box['x'] + box['width'] / 2
        y = box['y'] + box['height'] / 2
        self.page.mouse.click(x, y)

    def is_button_green(self) -> bool:
        color = self.page.evaluate("""
            () => {
                const el = document.querySelector('#badButton');
                if (!el) return null;
                const cs = window.getComputedStyle(el);
                return cs.backgroundColor; // 'rgb(0, 128, 0)'
            }
        """)
        return color == 'rgb(0, 128, 0)'
