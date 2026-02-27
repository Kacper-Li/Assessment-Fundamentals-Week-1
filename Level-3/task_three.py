"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def get_both_VAT(total_price_string: str) -> tuple[str, str]:
    """Returns tuple of VAT and Total inc VAT as strings. Expects string."""
    try:
        total_price = float(total_price_string)
        vat_add_on = total_price * 0.20
        vat_included = total_price + vat_add_on
        vat = f"VAT: £{vat_add_on:.2f}\n"
        total_inc_vat = f"Total inc VAT: £{vat_included:.2f}"
        return str(vat), str(total_inc_vat)
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
        # print(line, "and", line[:6])
        # If first word of line is Total:
        if line[:6] == "Total:":
            #   Search the line for the total price: i.e. everything after £ on that line
            total_price = line[-4:]
            # print(total_price)
            #   Add new line to make a gap before total line displayed
            invoice_string += "\n" + line + "\n"
            # Convert the price to float, calculate VAT
            # Add -added- VAT and Total inc VAT as two lines on the end.
            added_VAT, total_with_VAT = get_both_VAT(total_price)
            invoice_string += added_VAT + total_with_VAT
        else:
            invoice_string += line + "\n"
    return invoice_string  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
