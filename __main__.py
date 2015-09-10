__author__ = 'fritz'
from shopping_list import ShoppingList
from product import Product
from utils import login
import os


def run():
    login(os.environ.get("rewe_user"), os.environ.get("rewe_password"))
    shopping_list = ShoppingList.from_name("rewe_api", True)
    shopping_list.set_active()
    onions_1kg = Product(1041138, 1)
    shopping_list.add_product(onions_1kg)



if __name__ == "__main__":
    run()



