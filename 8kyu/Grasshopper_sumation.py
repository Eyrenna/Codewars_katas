def summation(num):
    add = 1
    result = 0
    while add <= num:
        result = result + add
        add += 1
    return result

if __name__ == "__main__":
    assert summation(1) == 1
    assert summation(8) == 36