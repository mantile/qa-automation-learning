import os

from PIL import Image, ImageChops
from pathlib import Path

class ImagesComporator:
    def __init__(self, screenshots_dir="data"):
        self.screenshots_dir = Path(screenshots_dir)
        self.screenshots_dir.mkdir(exist_ok=True)

    def get_etalon_path(self, page_name: str, element_name: str) -> Path:
        page_dir = self.screenshots_dir / page_name
        page_dir.mkdir(exist_ok=True)
        return page_dir / f"{element_name}.png"
    
    def compare(self, page, selector: str, page_name: str, element_name: str) -> bool:
        etalon_path = self.get_etalon_path(page_name, element_name)
        temp_path = self.screenshots_dir / f"temp_{element_name}.png"

        element = page.locator(selector)
        if element.count == 0:
            return False
        
        element.screenshot(path=str(temp_path))

        try:
            img1 = Image.open(etalon_path)
            img2 = Image.open(temp_path)

            if img1.size != img2.size:
                temp_path.unlink()
                return False
            
            diff = ImageChops.difference(img1, img2)
            
            is_same = diff.getbbox() is None
            
            temp_path.unlink()
            return is_same
            
        except Exception as e:
            temp_path.unlink()
            return False