
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    if basket != []:
        total = 0.00
        receipt = ""
        for item in basket:
            total += item['price']
            if item['price'] == 0.00:
                receipt += f"{item['name']} - Free\n"
            else:
                receipt += f"{item['name']} - £{item['price']:.2f}\n"
        receipt += f"Total: £{total:.2f}"
        return receipt
    return "Basket is empty"  # return the receipt string


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
