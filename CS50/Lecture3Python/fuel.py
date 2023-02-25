while True:
    get_input = input("Fraction: ")
    try:
        numerator, denominator = get_input.split("/")
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        percentage = new_numerator / new_denominator
        if percentage <= 1:
            break
    except (ValueError, ZeroDivisionError):
        print("Enter a Fraction, ex) 3/4")
    else:
        break
percentage = percentage*100

if percentage < 1:
    print("E")
elif percentage > 99:
    print("F")
elif percentage == 0.01:
    print("E")
else:
    print(f"{round(percentage)}%")
