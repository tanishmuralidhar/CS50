import random

def main():
    level = get_level()
    simulate_round(2,8)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def simulate_round(x,y):
    count_tries = 1
    while count_tries <= 1:
        try:
            answer = input(f"{x} + {y} = ")
            if answer == x+y:
                return True
            else:
                count_tries ++ 1
                print("EEE")
        except:
            pass
if __name__ == "__main__":
    main()
