from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = Page
        self.logger = None

    def navigate(self, url: str):
        self.oage.goto(url)
        return self
    
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()
    
    def is_element_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
    
    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")
        return self
