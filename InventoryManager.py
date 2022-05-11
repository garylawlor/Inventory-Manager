from tabulate import tabulate
import datetime

#Dummy data
products = ["TV","Microwave","Dishwasher","Washing Machine","Fridge","Blender"]
prices = {"TV":210,"Microwave":150,"Dishwasher":450,"Washing Machine":390,"Fridge":610,"Blender":70}
IDs = {"TV":12001,"Microwave":12002,"Dishwasher":12003,"Washing Machine":12004,"Fridge":12005,"Blender":12006}
qtys = {"TV":12,"Microwave":19,"Dishwasher":10,"Washing Machine":54,"Fridge":62,"Blender":29}


class product_class():
    def __init__(self,product,price,ID,qty):
        self.product = product
        self.price = price
        self.ID = ID
        self.qty = qty
        
    def __str__(self):
        return f"PRODUCT:{self.product};\n price:{self.price};\n Id:{self.ID};\n Qty:{self.qty};"

    def __repr__(self):
        return self.product,self.price,self.ID,self.qty        
        
class inventory():
    def __init__(self):
        self.products = []
        for product in products:
            self.products.append(product_class(product,prices[product],IDs[product],qtys[product]).__repr__())
            
    def __str__(self):
        inv_str = ""
        for item in self.products:
            inv_str += "\n"+item.__str__()
        return "This is the inventory:\n" + inv_str
            

    
def create_table(inventory):
    data = inventory

    col_names = ["Product","Price","ID","Qty"]
    now = datetime.datetime.now()
    try:
        return print(tabulate(data, headers=col_names))
    except:
        print(now,"### ERROR ### Unable to output inventory table.")


def update_inventory(inv,product,price_change,ID_change,qty_change):
    global prices
    global IDs
    global qtys
    now = datetime.datetime.now()
    
    if product in products:
        prices[product] = price_change
        IDs[product] = ID_change
        qtys[product] = qty_change
    
        inv = inventory()
    
        create_table(inv.products)
    else:
        print(now,"### ERROR ### Provided product does not match database inventory. No changes made.")


my_inventory = inventory()
create_table(my_inventory.products)
update_inventory(my_inventory,"DVD",15,14001,45)
update_inventory(my_inventory,"TV",500,15001,11)