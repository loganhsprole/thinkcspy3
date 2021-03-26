def dayname(daynum):
    if daynum == 0:
        print("Sunday")
    elif daynum == 1:
        print("Monday")
    elif daynum == 2:
        print("Tuesday")
    elif daynum == 3:
        print("Wednesday")
    elif daynum == 4:
        print("Thursday")
    elif daynum == 5:
        print("Friday")
    elif daynum == 6:
        print("Saturday")
    else:
        return


daynumber = int(input("Enter day number: "))
dayname(daynumber)
