# Create new class ItemToPurchase:
class itemtopurchase:
    # Initialize constructor to provide class attribute:
    def __init__(self,item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    # define print function:
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity:,} @ ${self.item_price:,.2f} = ${self.item_quantity*self.item_price:,.2f}")

# prompt the user to enter two items: 
print("ITEM 1")
itemname1 = input("Enter the item name: ")
itemprice1 = float(input("Enter the item price: "))
itemquantity1 = int(input("Enter the item quantity: "))
print("ITEM 2")
itemname2 = input("Enter the item name: ")
itemprice2 = float(input("Enter the item price: "))
itemquantity2 = int(input("Enter the item quantity: "))

item1 = itemtopurchase(itemname1, itemprice1, itemquantity1)
item2 = itemtopurchase(itemname2, itemprice2, itemquantity2)

#Print items and total cost:
print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${item1.item_quantity*item1.item_price + item2.item_quantity*item2.item_price:,.2f}")