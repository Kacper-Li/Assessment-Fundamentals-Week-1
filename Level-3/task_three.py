"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def get_original_price(item_price_string: str) -> str:
    """Returns the price without vat added. i.e. 80%"""
    try:
        item_price = float(item_price_string)
        original_price = item_price * 0.80
        return f"{original_price:.2f}"
    except:
        raise Exception("WRONG VALUE TYPE INPUT TO ORIGINAL PRICE GETTER")


def get_both_vat(total_vat_price_string: str) -> tuple[str, str]:
    """Returns tuple of original price and added vat lines. Both have line break inc."""
    try:
        total_vat_price = float(total_vat_price_string)
        vat_add_on = total_vat_price * 0.20
        vat_deducted = total_vat_price - vat_add_on
        original_total = f"Total: £{vat_deducted:.2f}\n"
        vat = f"VAT: £{vat_add_on:.2f}\n"
        return str(original_total), str(vat)
    except:
        raise Exception("WRONG VALUE TYPE INPUT TO vat CALCULATOR")


def generate_invoice(receipt_string: str) -> str:
    """Returns a formatted version of receipt_string, with vat calculation included."""
    if not receipt_string:
        return "Receipt was empty"
    receipt_lines = receipt_string.split("\n")
    invoice_string = "VAT RECEIPT\n\n"
    any_items_found = 0
    for line in receipt_lines:
        pound_index = line.rfind('£')
        line_without_price = line[:pound_index + 1]
        price = line[pound_index + 1:]

        if line[:6] == "Total:":
            if any_items_found:
                invoice_string += "\n"
            original_total, vat = get_both_vat(price)
            invoice_string += original_total + vat
            invoice_string += f"Total inc VAT: £{price}"
        else:
            any_items_found = 1
            line_adjusted = line_without_price + get_original_price(price)
            invoice_string += line_adjusted + "\n"
    return invoice_string  # return the invoice string


if __name__ == "__main__":
    RECEIPT_STRING_1 = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(RECEIPT_STRING_1))
    print("--------------------------------------------")
    RECEIPT_STRING_2 = """Total: £0.00"""
    print(generate_invoice(RECEIPT_STRING_2))
