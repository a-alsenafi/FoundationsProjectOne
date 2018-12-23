####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate",
                    "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Cup Cakez"  # complete me!
signature_flavors = ["super vanilla", "super chocolate"]  # complete me!
order_list = []
base = 5


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    for i in menu:
        print("-" + "\"" + str(i) + "\" " + "(KD " + (str(menu[i]) + ")"))

    # your code goes here!


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for i in (original_flavors):
        print("-"+"\""+str(i)+"\"")


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for i in signature_flavors:
        print("-"+"\""+str(i)+"\"")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    for x in menu:
        if x == order:
            return True


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    print("What\'s your order? (Enter the exact spelling of the item you want. Type \'Exit\' to end your order.)")
    x = "abc"
    order_list = []
    # your code goes here!
    while x != "Exit":
        x = input()
        if is_valid_order(x):
            order_list.append(x)
        else:
            print("Order not valid")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total > base:
        print("Sorry, your order is not eligible for credit card payment")
    else:
        print("This order is eligible for credit card payment")
        print("Thank you for shopping at "+cupcake_shop_name)


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for x in order_list:
        for y in menu:
            if x == y:
                total = total + menu[y]

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for x in order_list:
        print("-"+str(x))
    print("Your total is: " + str(get_total_price(order_list)))
    accept_credit_card(get_total_price(order_list))
