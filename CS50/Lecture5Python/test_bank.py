from bank import value

def  returns_100():
    assert value("sup") == "$100"
    assert value("123423") == "$100"

def  returns_20():
    assert value("h") == "$20"
    assert value("Hi it's Leonard") == "$20"

def  returns_0():
    assert value("hello") == "$0"
