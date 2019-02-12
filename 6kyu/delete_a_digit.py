def delete_digit(number):
    string_num = str(number)
    initial = int(string_num[1:])
    for digit in string_num:
        proof = int(string_num[:string_num.find(digit)] + string_num[string_num.find(digit)+1:])
        if proof > initial:
            initial = proof
        else:
            pass
    return initial

if __name__ == "__main__":
    assert delete_digit(152) ==52
    assert delete_digit(1001) == 101
    assert delete_digit(10) == 1