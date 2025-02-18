#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  # +++your code here+++
  # ['aba', 'xyz', 'aa', 'x', 'bbb']), 3
  print(f"words is: ", words)
  i = 0
  for var in words:
    #print(var)
    if len(var) >= 2:
      #print(len(var))
      if var[0:1] == var[-1]:
        i += 1
  #print(f"i is: ", i)
  #words.append(i)
  #print(f"words after append: ", words)
  return i


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 li['bbb', 'ccc', 'axx', 'xzz', 'xaa']sts and sorting each of them
# before combining them.
def front_x(words):
  # +++your code here+++
  #['bbb', 'ccc', 'axx', 'xzz', 'xaa']
  words_x = []
  words_no_x = []
  #print(words)
  for var in words:
    if var[0:1] == "x":
      letter_x = var[0:1]
      words_x.append(var)
      sorted_words_x = sorted(words_x)
      #print(f"sorted_words_x =: ", sorted_words_x)
    else:
      words_no_x.append(var)
      sorted_words_no_x = sorted(words_no_x)
      #print(f"sorted_words_no_x =: ", sorted_words_no_x)
  return sorted_words_x + sorted_words_no_x 



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  # +++your code here+++
  sorted_tuples = []
  print(f"tuples = : ", tuples)
  for var in tuples:
    print(f"var is: ", var)
    #len_var = len(var)
    #print(f"len_var is: ", len_var)
    #idx_num = len_var - 1
    #print(f"idx_num is: ", idx_num)
    #sorted_list_by_first = sorted(tuples)
    #print(sorted_list_by_first)
    sorted_list_by_second = sorted(tuples, key=lambda x: x[1])
    #print(sorted_list_by_second)
    
  return sorted_list_by_second


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print()
  print('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


  print()
  print('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
