"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    """Returns a formatted version of receipt_string, with VAT calculation included."""
    if not receipt_string:
        return "Receipt was empty"
    # Read line by line
    # If first word of line is Total:
    #   Add new line to make a gap before total line displayed
    #   Search the line for the total price: i.e. everything after £ on that line
    # Convert the price to float, calculate VAT
    # Add -added- VAT and Total inc VAT as two lines on the end.
    return "Not done yet :P"  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
    print(generate_invoice(""))
