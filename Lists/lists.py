'''# This exercise walks you through how to write a list comprehension # to create a 
# list of squared numbers (n*n or n**2). It needs to # return a list of squares 
# of consecutive numbers between “start” and “end” inclusively. For example, 
# squares(2, 3) should return a list containing [4, 9].
# 
# 1. The function receives the variables “start” and “end” through the function parameters. 
# 2. In the return line, start by entering the list brackets [ ] that will contain the list comprehension.
# 3. Between the brackets [ ]: 
#### a. Enter the arithmetic expression to square a variable “n”. 
#### b. To the right of the square expression, write a for loop that iterates over 
#       “n” in a range() from the “start” to “end” variables.
#### c. Ensure the “end” range value is included in the range() by adding 1 to it.
# 4. Run your code to see if it works!  If needed, the solution to this code is 
#    included in the “Study Guide: List Operations and Methods” reading under 
#    “Skill Group 2” (list comprehensions). 

def squares(start, end):
    return [x**2 for x in range(start,end+1)]


print(squares(2, 3))    # Should print [4, 9]
print(squares(1, 5))    # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))   # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''

def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for person in people:
        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"   
        name, age, profession = person
        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as {}.".format(name, age, profession))

# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])


# Click Run to submit code


# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer