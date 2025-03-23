stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    inventory_total = 0
    print("Inventory:")
    for item, amount in inventory.items():
        print(amount, item)
        inventory_total += amount
    print(f'Total number of items: {inventory_total}')

    
    


if __name__ == "__main__":
    displayInventory(stuff)
