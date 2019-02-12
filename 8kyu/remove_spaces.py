def remove_spaces(string):
    new_string = ""
    for char in string:
        if char != " ":
            new_string += char
    return new_string

if __name__ == "__main__":
    remove_spaces('8 j 8   mBliB8g  imjB8B8  jl  B') == '8j8mBliB8gimjB8B8jlB'
    remove_spaces('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd') == '88Bifk8hB8BB8BBBB888chl8BhBfd'
    remove_spaces('8aaaaa dddd r     ') == '8aaaaaddddr'
    remove_spaces('jfBm  gk lf8hg  88lbe8 ') == 'jfBmgklf8hg88lbe8'
    remove_spaces('8j aam') == '8jaam'