def remove(string, number):
    new_string = ""
    counter = 0
    for char in string:
        if char != "!":
            new_string = new_string + char
        elif char == "!":
          counter += 1
          if counter > number:
              new_string = new_string + char
            
    return new_string

if __name__ == "__main__":
    assert remove("Hi!",1) == "Hi"
    assert remove("Hi!",100) == "Hi"
    assert remove("Hi!!!",1) == "Hi!!"
    assert remove("Hi!!!",100) == "Hi"
    assert remove("!Hi",1) == "Hi"
    assert remove("!Hi!",1) == "Hi!"
    assert remove("!Hi!",100) == "Hi"
    assert remove("!!!Hi !!hi!!! !hi",1) == "!!Hi !!hi!!! !hi"
    assert remove("!!!Hi !!hi!!! !hi",3) == "Hi !!hi!!! !hi"
    assert remove("!!!Hi !!hi!!! !hi",5) == "Hi hi!!! !hi"
    assert remove("!!!Hi !!hi!!! !hi",100) == "Hi hi hi"
   