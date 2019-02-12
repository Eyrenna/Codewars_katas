def generate_hashtag(s): 
    s = s.title()
    s = s.replace(" " , "")
    s = "#" + s
    if len(s) > 140 or s == "#":
        return False
    else:
        return s

if __name__ == "__main__":
    assert generate_hashtag('') == False
    assert generate_hashtag('Do We have A Hashtag')[0] == '#'
    assert generate_hashtag('Codewars') == '#Codewars'
    assert generate_hashtag('Codewars      ') == '#Codewars' 
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('CodeWars is nice') == '#CodewarsIsNice' 
    assert generate_hashtag('c i n') == '#CIN'
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False 