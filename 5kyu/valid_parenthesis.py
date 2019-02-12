def valid_parentheses(string):
    if string.count("(") != string.count(")"):
        return False
    else:
        open = []
        for item in string:
            i =[]
            if item == "(":
                i = [string.find(item)]
                open = open + i
            elif item == ")":
                if open == []:
                    return False
                else:
                    open = open[:len(open)-1]
            else:
                pass
    if open == []:
      return True
if __name__ == "__main__":
    assert valid_parentheses("  (") == False
    assert valid_parentheses(")test") == False
    assert valid_parentheses("") == True
    assert valid_parentheses("hi())(") == False
    assert valid_parentheses("hi(hi)()") == True