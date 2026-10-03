from products import Product

class Store:
    def __init_(self, list_of_products):
        self.list_of_products = list_of_products
        if list_of_products is None:
            self.list_of_products = []
        else:
            self.list_of_products = list(list_of_products)
    def add_product(self, product):
        self.list_of_products.append(product)
    def remove_product(self, product):
        self.list_of_products.remove(product)
    def get_total_quantity(self) -> int:
        return sum(product.quantity for item in self.list_of_products)
    def get_all_products(self) -> List[Product]:
        return [product for product in self.list_of_products if product.is_active()]
    def order(self, shopping_list: List[Tuple['Product', int]]) -> float:
        total_order_price = 0.0

        for product, quantity in shopping_list:
            # Use the product's built-in buy method to validate and update stock
            item_cost = product.buy(quantity)
            total_order_price += item_cost

        return float(total_order_price)

