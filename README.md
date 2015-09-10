# rewe_shopping_list_wrapper
A small wrapper to add and remove products from a rewe shopping list.

##Example Usage
```python
login(os.environ.get("rewe_user"), os.environ.get("rewe_password"))
shopping_list = ShoppingList.from_name("rewe_api", True)
onions_1kg = Product(1041138, 1)
shopping_list.add_product(onions_1kg)
```

1. We login to the rewe service
2. We get our shopping list ("rewe_api") we want to use if it doesnt exists we just create it
3. After that we create a Product in this case its a net of onions
4. We add it to the shopping list
