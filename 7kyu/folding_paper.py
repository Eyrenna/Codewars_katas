def folding(a,b):
    squares = 1 # Al final habrá uno resultante de a = b
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
        squares += 1
    return squares

if __name__ == "__main__":
    assert folding(2,1) ==2
    assert folding(10,7) == 6
    assert folding(3,1) == 3
    assert folding(4,1) == 4
    assert folding(3,2) == 3
    assert folding(4,2) == 2
    assert folding(1000,700) == 6
    assert folding(1000,999) == 1000