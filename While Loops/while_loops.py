# Disclaimer!! This is not my code, but I find it difficult to understand therefore I take notes of it.
# This function that takes an argument n and returns the sum of integers from 1 to n.
# For example, if n=5, your function should add up 1+2+3+4+5 and return 15.
def sum_of_integers(n):

  # This if condition is to show that there is no sum of integers if n is less than one
  if n < 1:
    return 0

  # I still have no idea what i means. But I think I roughly know why its value is 1. I think it's to show the lowest possible answer (maybe)
  # And the sum stands for the highest integer which is obviously n   
  i = 1
  sum = n

  # This while loop is for the integers in between 1 to n (again, I think)
  while i < n:
    sum +=  i
    i += 1

  return sum

print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15