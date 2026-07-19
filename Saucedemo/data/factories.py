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
    def backpack_id() -> str:
        return TestData.ITEMS['backpack']['id']
    
    @staticmethod
    def bike_light_id() -> str:
        return TestData.ITEMS['bike_light']['id']
    
    @staticmethod
    def t_shirt_id() -> str:
        return TestData.ITEMS['t_shirt']['id']
    
    @staticmethod
    def fleece_id() -> str:
        return TestData.ITEMS['fleece']['id']
    
    @staticmethod
    def onesie_id() -> str:
        return TestData.ITEMS['onesie']['id']
    
    @staticmethod
    def red_t_shirt_id() -> str:
        return TestData.ITEMS['red_t_shirt']['id']
    
    @staticmethod
    def all_items_names() -> list:
        return [item['item_id'] for item in TestData.ITEMS.values()]
    
    @staticmethod
    def all_items_id() -> list:
        return [item['id'] for item in TestData.ITEMS.values()]
    
    @staticmethod
    def random_item() -> str:
        import random
        return random.choice(ItemFactory.all_items_names())
    
    @staticmethod
    def random_items(count: int) -> list:
        import random
        all_items = ItemFactory.all_items_names()
        if count > len(all_items):
            return all_items
        return random.sample(all_items, count)
    
class DataFactory:

    user = UserFactory
    item = ItemFactory