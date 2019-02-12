def first_non_repeating_letter(string):
    lowstring = string.lower()
    non_repeat = False
    index = 0
    while non_repeat == False:
        if index == len(string):
            return ""
        elif lowstring.count(lowstring[index]) > 1:
            index += 1
        else:
            return string[index]
            non_repeat = True

if __name__ == "__main__":
    assert first_non_repeating_letter('a') =='a'
    assert first_non_repeating_letter('stress') =='t'
    assert first_non_repeating_letter('moonmen') =='e'

    assert first_non_repeating_letter('') ==''

    assert first_non_repeating_letter('abba') ==''
    assert first_non_repeating_letter('aa') ==''

    assert first_non_repeating_letter('~><#~><') =='#'
    assert first_non_repeating_letter('hello world ==eh?') =='w'

    assert first_non_repeating_letter('sTreSS') =='T'
    assert first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') ==','