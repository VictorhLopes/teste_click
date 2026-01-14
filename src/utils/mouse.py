
# src/utils/mouse.py
from playwright.sync_api import Page

def physical_click_center(page: Page, locator):
    """Realiza clique físico no centro de um locator, com pequena espera e removendo :hover."""
    locator.scroll_into_view_if_needed()
    box = locator.bounding_box()
    if not box:
        raise RuntimeError("Sem bounding box disponível para clique físico.")
    x = box['x'] + box['width']/2
    y = box['y'] + box['height']/2
    page.mouse.move(x, y)
    page.mouse.click(x, y)
    page.wait_for_timeout(150)
    page.mouse.move(x + 200, y)
