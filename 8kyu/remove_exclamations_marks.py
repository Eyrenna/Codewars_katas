def remove_exclamation_marks(s):
    news = ""
    for char in s:
        if char != "!":
            news = news + char 
    return  news


if __name__ == "__main__":
    assert remove_exclamation_marks("Hello World!") == "Hello World"
    assert remove_exclamation_marks("Hello World!!!") == "Hello World"
    assert remove_exclamation_marks("Hi! Hello!") == "Hi Hello"
    assert remove_exclamation_marks("") == ""
    assert remove_exclamation_marks("Oh, no!!!") == "Oh, no"