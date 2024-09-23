# Study Guide: for Loops
### ```for``` loops VS. ```while``` loops
> * ```while``` loops are used when a segment of code needs to execute repeatedly while a condition is true
> * ```for``` loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence
### Syntax
```python 
for variable in sequence: 
    body of loop
```
### Common ```for``` Loop Structure
#### ```for``` Loop with ```range()```
* ```x = Start``` - Starting index position of the range
    * Default index position is 0.
    * The starting index position is included in the range.
    * Example syntax: ```range(2, y, z)``` or ```range(x+3, y, z)``` 
* ```y = Stop``` - Ending index position of range
    * No default index position. Must include the ending index position in the ```range()``` parameters.
        * Example syntax: ```range(y)```
    * The value of the ending index position is excluded from the range.
    * To include the ending index number, use the expression: ```y+1 (index + 1)```
        * Example syntax: ```range(x, y+1, z)```
        * Alternatively, if ```y``` = 10, you can write: ```range(x, 11, z)```
* z = Step - Incremental value
### Common pitfalls when using ```the range()``` function:
* Forgetting that **the upper limit of a ```range()``` isn’t included** in the range.
* **Iterating over non-sequences**. For example, strings are iterable letter by letter, but not word by word. 
### Nested ```for``` Loops
```python
for x in sequence:
    # start of the outer loop body
    for y in sequence:
        # start of the inner loop body
        # end of of the inner loop body
    # continue body of the outer loop
    # end of the outer loop body
```
### ```for``` loop with nested if Statement
```python
for x in sequence:
    # start of body of for loop
    if condition is true:
        # start of body of if-statement
        # end of body of if-statement
    # continue body of for loop
    # end of body of for loop

# As a list comprehension:
[x for x in sequence if condition]
```
### List Comprehensions
It is important to know that loops can be avoided sometimes; as you progress, you will develop a sense of when and how to do so. The concepts ```for``` loops are similar between other languages, but in Python, **list comprehensions** provide a concise way to create lists based on existing lists or sequences. <br><br>
Here is a concrete example for better understanding. Let's say you have a sequence of number and you want to create a new list containing only the even numbers from the sequence.<br><br>
With traditional ```for``` Loop, you might write:
```python
sequance = range
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)
```
With a list comprehensions, you could achieve the same thing:
```python
sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]
```
Both of these pieces of code will create a list of even numbers from 1 to 10: [0, 2, 4, 6, 8].The list comprehension version does this in a single, compact line. These “one-liners” are very useful and dramatically reduce overhead.