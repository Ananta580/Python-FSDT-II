class IceShoppeOrder:
    def __init__(self, customer_name, flavor, size):
        self.customer_name = customer_name
        self.flavor = flavor
        self.size = size

# Create an array to store IceShoppeOrder objects
order_list = []

# Add orders to the array
order1 = IceShoppeOrder("Alice", "Chocolate", "Large")
order_list.append(order1)

order2 = IceShoppeOrder("Bob", "Vanilla", "Medium")
order_list.append(order2)

order3 = IceShoppeOrder("Eve", "Strawberry", "Small")
order_list.append(order3)

# Print the orders
for order in order_list:
    print(f"Customer: {order.customer_name}, Flavor: {order.flavor}, Size: {order.size}")