list = {

}

while True:
    try:
        item = input()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
    except EOFError:
        for x in sorted(list.xs()):
            print(list[x], x.upper())
        break
