"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []
item_count = {
    # "name": 0
}

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list:
    """Return basket list with item appended."""
    if item in basket:
        print("Copy add")
        item_count[item['name'], item['price']] += 1
        print(f"{item_count}")
    else:
        item_count[item['name'], item['price']] = 1
        basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    """Returns a built string of each item in the basket."""
    if basket != []:
        total = 0.00
        receipt = ""
        print(item_count)
        for item in basket:
            number_of_item = item_count[item['name'], item['price']]
            print(f"number of {item} is {number_of_item}")
            price_of_item = item['price']
            collective_price = price_of_item * number_of_item
            total += collective_price
            if item['price'] == 0.00:
                receipt += f"{item['name']} - Free\n"
            else:
                receipt += f"{item['name']} - £{collective_price:.2f}\n"
        receipt += f"Total: £{total:.2f}"
        return receipt
    return "Basket is empty"  # return the receipt string


#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####

if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.70
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(f"basket: {basket}\n\n")
    print(generate_receipt(basket))
