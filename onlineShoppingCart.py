class ItemToPurchase:
    ''''
    Class to represent an item to purchase and print the purchase cost of the purchased item quantity
    '''
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    def print_item_cost(self):
        items_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${items_cost}')
        return items_cost
        

class ShoppingCart:
    '''
    Manager class to manage the shopping cart and purchase items
    '''
    duplicate_item_tracker = {} 
    purchased_items = []
    def __init__(self, default_items_count = 2, allow_more_items = True):
        self.default_items_count = default_items_count
        self.allow_more_items = allow_more_items
    
    def get_user_input(self):
        purchased_items_count = len(self.purchased_items)
        print(f"Item {purchased_items_count + 1}")
        item_name = input("Enter the item name: ")
        exisitng_item = self.fetch_item_by_name(item_name)
        if exisitng_item != None:
            print("Item already exists")
            exisitng_item.item_quantity += int(input("Enter the item quantity you want add:"))
        else:
            item_price = int(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            self.add_item(item_name, item_price, item_quantity)
            self.duplicate_item_tracker[item_name] = purchased_items_count
        
    def fetch_item_by_name(self, item_name):
        position = self.duplicate_item_tracker[item_name] if item_name in self.duplicate_item_tracker else -1
        if position > -1:
            return self.purchased_items[position]
        return None
    
    def add_item(self, item_name, item_price, item_quantity):
        item = ItemToPurchase(item_name=item_name, item_price=item_price, item_quantity=item_quantity)            
        self.purchased_items.append(item)
        
    def print_receipt(self):
        print("TOTAL COST")
        print()
        total_cost = 0
        for item in self.purchased_items:
            total_cost += item.print_item_cost()
        print()
        print(f'Total: ${total_cost}')
        
    
    def purchase_items(self):
        if self.default_items_count > 0:
            for i in range(self.default_items_count):
                self.get_user_input()
        else:
            self.get_user_input()
            
        if self.allow_more_items:
            while int(input("Do you want to add more items? (yes=1/no=0): ")) == 1:
                self.get_user_input()
            
        self.print_receipt()
        
# main
cart = ShoppingCart()
cart.purchase_items()
        
    

