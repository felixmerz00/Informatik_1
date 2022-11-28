from public.item import Item
from public.order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__name = restaurant_name
        self.__menu = menu_list
        self.__oders = []

    def get_restaurant_name(self):
        return self.__name

    def get_menu_list(self):
        return self.__menu.copy()
    
    def get_order_list(self):
        if len(self.__oders) != 0: 
            return self.__oders.copy()
        return "No order yet" 
    
    def set_order(self, item_list):
        valid_items = []
        for item in item_list:
            if item in self.__menu:
                valid_items.append(item)

        # If all ordered items are invalid, the list is empty now and no Order object should be created.
        if valid_items: 
            self.__oders.append(Order(valid_items))

    def get_revenue(self):
        revenue = 0
        for order in self.__oders: 
            revenue += order.get_bill_amount()
        return revenue


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish]
    # Create order list
    order_list = [steak, steak, salad, pizza]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
