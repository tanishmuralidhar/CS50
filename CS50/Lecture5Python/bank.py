def main():
    print(f"${value()}")
def value():
    answer = input("Greeting: ").upper().strip()
    if "hello" in answer:
        return 0
    elif "h" in answer:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()