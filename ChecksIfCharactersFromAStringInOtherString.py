# Finds product characters in debris. If all product characters are in debris, returns product. If all product characters are 
not in debris, returns a string.

def fix_machine(debris, product):
    container = ''
    i = 0
    while i < len(product):
        target = debris.find(product[i])
        container += debris[target]
        i = i + 1
        if target == -1:
            return "Give me something that's not useless next time."
    return container  
