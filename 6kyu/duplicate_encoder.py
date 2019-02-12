def duplicate_encode(word):
    word = word.lower()
    result = ""
    for char in word:
        if word.count(char) == 1:
            result += "("
        else:
            result += ")"
    return result

if __name__ == "__main__":
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("