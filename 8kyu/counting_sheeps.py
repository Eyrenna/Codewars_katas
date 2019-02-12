def count_sheeps(arrayOfSheeps):
  count = 0
  for item in arrayOfSheeps:
      if item == True:
          count += 1
  return count
    
if __name__ == "__main__":
    assert  count_sheeps(   [True,  True,  True,  False,
                            True,  True,  True,  True ,
                            True,  False, True,  False,
                            True,  False, False, True ,
                            True,  True,  True,  True ,
                            False, False, True,  True ]) == 17