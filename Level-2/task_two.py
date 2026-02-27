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
    """Return basket list with unique item appended.\n
    Duplicates increase tracked count in item_count dict"""
    if item in basket:
        item_count[item['name'], item['price']] += 1
    else:
        item_count[item['name'], item['price']] = 1
        basket.append(item)
    return basket


def generate_receipt(basket_given: list) -> str:
    """Returns a built string of each item in the basket_given."""
    if basket_given != []:
        total = 0.00
        receipt = ""
        for item in basket_given:
            number_of_item = item_count[item['name'], item['price']]
            price_of_item = item['price']
            collective_price = price_of_item * number_of_item
            total += collective_price

            if item['price'] == 0.00:
                receipt += f"{item['name']} x {number_of_item} - Free\n"
            else:
                receipt += f"{item['name']} x {number_of_item} - £{collective_price:.2f}\n"
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
