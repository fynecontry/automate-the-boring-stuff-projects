#!/usr/bin/env python3

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    '''Prints players amount of items in inventory'''
    print("Inventory:")
    item_total = 0
    
    # Display each items and the total of all
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v

    print("Total number of items: " + str(item_total))

def add_to_inventory(inventory, added_items):
    '''Update inventory with list of items'''
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1        # Add item if it does not exists

    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
