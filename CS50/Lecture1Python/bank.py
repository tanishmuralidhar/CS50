answer_bank = input("Greeting: ")
new_answer = answer_bank.lower().strip()

if "hello" in new_answer:
    print("$0")

elif "h" in new_answer[0]:
    print("$20")

else:
    print("$100")
