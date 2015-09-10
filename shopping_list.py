__author__ = 'fritz'
from utils import post, get


class ShoppingList():
    def __init__(self, identification, name=None):
        self.identification = identification
        self.name = name

    @classmethod
    def create(cls, name):
        payload = {"shoppingListName": name}
        url = "https://shop.rewe.de/shoppinglist/create/ajax"
        response = post(url, payload)
        return cls(response.get('model').get('identification'), name)

    @classmethod
    def from_name(cls, name, create=False):
        payload = {}
        url = "https://shop.rewe.de/shoppinglist/lists/ajax"
        response = post(url, payload)
        shopping_lists = response.get('model').get('shoppingLists')
        for shopping_list in shopping_lists:
            if shopping_list.get('name') == name:
                return cls(shopping_list.get('identification'))
        if create:
            return cls.create(name)
        return None

    def add_product(self, product):
        payload = {"shoppinglistIdentification": self.identification,
                   "nan": product.nan,
                   "quantity": product.quantity}
        url = "https://shop.rewe.de/shoppinglist/add-product"
        post(url, payload)

    def remove_product(self, product):
        payload = {"shoppinglistIdentification": self.identification,
                   "nan": product.nan,
                   "quantity": 0}
        url = "https://shop.rewe.de/shoppinglist/remove-item/submit"
        post(url, payload, False)

    def set_active(self):
        url = "https://shop.rewe.de/shoppinglist/selectActiveList?selectedShoppingListIdentification={}".format(self.identification)
        get(url)

    def remove(self):
        self.set_active()
        url = "https://shop.rewe.de/shoppinglist/delete"
        get(url)