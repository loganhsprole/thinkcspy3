def final_amt(p, r, n, t):
    """Apply the compound interest formula to p
        to produce the final amount.
    """

    a = p * (1 + r / n) ** (n * t)
    return a


toInvest = float(input("How much do you want to invest? "))
fnl = final_amt(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have", fnl)
