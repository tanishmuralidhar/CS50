roic = int(input("Enter Return on Invested Capital Value (Linear Value): "))
# eg = earnings_growth
eg = int(input("Enter Earning Growth Percentage: "))
current_pe = int(input("Enter current pe of the stock: "))

if roic < 4:
    print("Can not compute")
    quit
elif 10<roic<=20:
    if eg == 4:
        intrinsic_pe = roic*0.95
        print(f"The intrinsic pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg == 6:
        intrinsic_pe = roic*1.061
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg == 8:
        intrinsic_pe = roic*1.21
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg == 10:
        intrinsic_pe = roic*1.41
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg > 10:
        intrinsic_pe = 0.2*(eg-10)+22.4
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    else:
        print("Choose a earnings growth of 6,8,10 or 10>")
elif 20<roic<=30:
    if eg == 4:
        intrinsic_pe = roic*0.67
        print(f"The intrinsic pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg == 6:
        intrinsic_pe = roic*1.061
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg == 8:
        intrinsic_pe = roic*1.21
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg == 10:
        intrinsic_pe = roic*1.41
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    elif eg > 10:
        intrinsic_pe = 0.2*(eg-10)+22.4
        print(f"The intric pe is {intrinsic_pe}, while the current pe is {current_pe}")
    else:
        print("Choose a earnings growth of 6,8,10 or 10>")
