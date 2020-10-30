import sympy


def calc_val_IoF(quantity):
    """
    It reduces the quantity value to the correct modulus
    """
    quantity_i = quantity % (2 ** 32)

    if quantity_i < 2 ** 31:
        return quantity_i

    return -1 * (2 ** 32 - quantity_i)


def main():
    print("\n\tThis is the formula which is going to be solved - for quantity:")
    print("\n\t\t2^32 * n = 1500 * quantity + 1200 =>")
    print("\t\t=> quantity = (2^32 * n - 1200) / 1500 =>")
    print("\n\t\t=> quantity = (2^30 * n - 300) / 375")

    # Return the number c such that, (a * c) = 1 (mod m)
    #          (375 * inverse) = 1 (mod 2^32)
    inverse = sympy.mod_inverse(375, 2 ** 32)

    mod_i = 1  # Counter for the while which uses modular arithmetic to test different values

    while True:  # Calculate the desired value
        quantity = ((mod_i * (2 ** 30)) - 300) * inverse

        quantity_sol = calc_val_IoF(quantity)  # Calculate the candidate value for the quantity

        if quantity_sol > 0:  # Only positive quantities work for the c code
            print("\n\t\tThe result for quantity is {}".format(quantity_sol))
            exit(0)

        mod_i = mod_i + 1  # Update modulus counter


main()


