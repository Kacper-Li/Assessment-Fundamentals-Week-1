"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def get_original_price(item_price_string: str) -> str:
    """Returns the price without VAT added. i.e. 80%"""
    try:
        item_price = float(item_price_string)
        original_price = item_price * 0.80
        return f"{original_price:.2f}"
    except:
        raise "WRONG VALUE TYPE INPUT TO ORIGINAL PRICE GETTER"


def get_both_VAT(total_VAT_price_string: str) -> tuple[str, str]:
    """Returns tuple of original price and added VAT lines. Both have line break inc."""
    try:
        total_VAT_price = float(total_VAT_price_string)
        vat_add_on = total_VAT_price * 0.20
        vat_deducted = total_VAT_price - vat_add_on
        original_total = f"Total: £{vat_deducted:.2f}\n"
        vat = f"VAT: £{vat_add_on:.2f}\n"
        return str(original_total), str(vat)
    except:
        raise "WRONG VALUE TYPE INPUT TO VAT CALCULATOR"


def generate_invoice(receipt_string: str) -> str:
    """Returns a formatted version of receipt_string, with VAT calculation included."""
    if not receipt_string:
        return "Receipt was empty"
    # Read line by line
    receipt_lines = receipt_string.split("\n")
    invoice_string = "VAT RECEIPT\n\n"
    for line in receipt_lines:
        if line[:6] == "Total:":
            total_price = line[-4:]
            original_total, vat = get_both_VAT(total_price)
            invoice_string += "\n" + original_total
            invoice_string += vat
            invoice_string += f"Total inc VAT: £{total_price}"
        else:
            line_price_adjusted = line[:-4] + get_original_price(line[-4:])
            invoice_string += line_price_adjusted + "\n"
    return invoice_string  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
