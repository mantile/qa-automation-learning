import time

from playwright.sync_api import Page

class BasePage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.logger = None
        self._expected_elements: list[str] = []

    def navigate_to(self, url: str = None):
        if url is None:
            url = self.URL
        self.page.goto(url)
        return self
    
    def open_page(self):
        self.navigate_to()
        self.wait_for_page_load_with_retry()
        return self

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()
    
    def is_element_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
    
    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")
        return self
    
    def is_error_visible(self) -> bool:
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
    
    def wait_for_page_load_with_retry(
        self, 
        timeout: int = 30000,
        retry_interval: int = 1000
    ):
        if not self._expected_elements:
            return self
        
        start_time = time.time()
        last_error = None
        
        while time.time() - start_time < timeout / 1000:
            try:
                all_visible = True
                for selector in self._expected_elements:
                    if not self.is_element_visible(selector):
                        all_visible = False
                        break
                
                if all_visible:
                    return self
                
                time.sleep(retry_interval / 1000)
                
            except Exception as e:
                last_error = e
                time.sleep(retry_interval / 1000)
                continue
        
        raise TimeoutError(
            f"Page dont load for {timeout} ms. "
            f"Last error: {last_error}"
        )