answer_deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer_deep.strip() == "42":
    print("Yes")
elif answer_deep.strip().lower() == "forty-two":
    print("Yes")
elif answer_deep.strip().lower() == "forty two":
    print("Yes")
else:
    print("No")