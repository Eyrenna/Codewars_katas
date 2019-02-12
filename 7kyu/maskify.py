# return masked string
def maskify(cc):
    ocult = ""
    position = 0
    for char in cc:
        if len(cc) <= 4:
            return cc
        elif position < len(cc)-4:
            ocult = ocult + '#'
            position += 1
        else:
            ocult = ocult + char
    return ocult

if __name__ == "__main__":
    assert maskify(' ') == ' '
    assert maskify('123') == '123'
    assert maskify('SF$SDfgsd2eA') == '########d2eA'