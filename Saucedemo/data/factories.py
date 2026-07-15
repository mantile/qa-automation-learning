from data.test_data import TestData

class UserFactory:

    @staticmethod
    def standart() -> str:
        return TestData.USERS['standard']['username']
    
    @staticmethod
    def locked() -> str:
        return TestData.USERS['locked']['username']
    
    @staticmethod
    def problem() -> str:
        return TestData.USERS['problem']['username']
    
    @staticmethod
    def glitch() -> str:
        return TestData.USERS['glitch']['username']
    
    @staticmethod
    def error() -> str:
        return TestData.USERS['error']['username']
    
    @staticmethod
    def visual() -> str:
        return TestData.USERS['visual']['username']
    
    @staticmethod
    def password() -> str:
        return TestData.PASSWORDS
    
class ItemFactory:

    @staticmethod
    def backpack() -> str:
        return TestData.ITEMS['backpack']['item_id']
    
    @staticmethod
    def bike_light() -> str:
        return TestData.ITEMS['bike_light']['item_id']
    
    @staticmethod
    def t_shirt() -> str:
        return TestData.ITEMS['t_shirt']['item_id']
    
    @staticmethod
    def fleece() -> str:
        return TestData.ITEMS['fleece']['item_id']
    
    @staticmethod
    def onesie() -> str:
        return TestData.ITEMS['onesie']['item_id']
    
    @staticmethod
    def red_t_shirt() -> str:
        return TestData.ITEMS['red_t_shirt']['item_id']
    
    @staticmethod
    def all_items() -> list:
        return [item['item_id'] for item in TestData.ITEMS.values()]
    
    @staticmethod
    def random_item() -> str:
        import random
        return random.choice(ItemFactory.all_items())
    
class DataFactory:

    user = UserFactory
    item = ItemFactory