"""module for pricing"""


def calculate_discount(price, discount_percentage):
    """calculate discount and price"""

    # validate price
    if not isinstance(price, (int, float)) or price < 0:
        return "Kindly use positive numbers"

    # validate discount
    if (
        not isinstance(discount_percentage, (int, float))
        or discount_percentage < 0
        or discount_percentage > 100
    ):
        return "Discount should be between 0 and 100"

    # calculate discoun and price
    if discount_percentage >= 20:
        discount = (discount_percentage / 100) * price
        final_price = price - discount
    else:
        final_price = price
    return final_price

    # get price and discount inputs


while True:
    try:
        price_input = float(input("Enter price of your commodity: "))
        discount_input = float(input("Enter discount to your price: "))
    except ValueError:
        print("Kindly use numbers.")

    # check that the inputs fall within the requirements of discount and price
    else:
        buying_price = calculate_discount(price_input, discount_input)
        if isinstance(buying_price, (int, float)):
            print(f"Your buying price is, Ksh {buying_price}")
        else:
            print(buying_price)

            #exiting or proceeding
        exiting=input('Press y if you wish to proceed: ')
        if exiting != 'y':
            break
