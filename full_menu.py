#Menu Dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

#Order List
order = []

#Greeting
print("Welcome to the variety food truck.")

#Order Loop
place_order = True
while place_order:
    print("From which menu would you like to order? ")
    
    i = 1
    menu_items = {}
    
    #Menu Options
    for key in menu.keys():
        menu_items[i] = key 
        i += 1
        
    #Customer Input
    menu_category = input("Type menu number: ")
    
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")
            
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
                    
            menu_selection = input("Enter the item number: ")
            
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)
                
                if menu_selection in menu_items.keys():
                    item_name = menu_items[menu_selection]["Item name"]
                    quantity = input(f"How many {item_name}s would you like? (Default is 1): ")
                    
                    if not quantity.isdigit():
                        print("Invalid input. Quantity set to 1 by default.")
                        quantity = 1
                    else:
                        quantity = int(quantity)
                        
                    order.append({
                            "Item name": item_name,
                            "Price": menu_items[menu_selection]["Price"],
                            "Quantity": quantity
                        })
                    
                else:
                    print("Invalid selection. Please choose a valid item number.")
            
            else:        
                print("Invalid input. Please enter a number.")
                
        else:
            print(f"{menu_category} was not a menu option.")
            
    else:
        print("You didn't select a number.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        
        