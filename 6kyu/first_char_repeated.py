def first_dup(string):
    for char in string:
        if string.count(char) > 1:
            return char
    return None


test.assert_equals(first_dup('tweet'), 't')
test.assert_equals(first_dup('Ode to Joy'), ' ')
test.assert_equals(first_dup('ode to joy'), 'o')
test.assert_equals(first_dup('bar'), None)
test.assert_equals(first_dup('123123'), '1');
test.assert_equals(first_dup('!@#$!@#$'), '!');
test.assert_equals(first_dup('1a2b3a3c'), 'a');