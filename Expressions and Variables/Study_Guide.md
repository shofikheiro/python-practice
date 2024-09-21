# Study guide: Expressions and variables
### Terms
* **expression** - a combination of numbers, symbols, or other values that produce a result when evaluated
* **data types** - classes of data (e.g., string, int, float, Boolean, etc.), which include the properties and behaviors of instances of the data type (variables)
* **variable** - an instance of a data type class, represented by a unique name within the code, that stores changeable values of the specific data type
* **implicit conversion** - when the Python interpreter automatically converts one data type to another
* **explicit conversion** - when code is written to manually convert one data type to another using a data type conversion function:
    * str() - converts a value (often numeric) to a string data type
    * int() - converts a value (usually a float) to an integer data type
    * float() - converts a value (usually an integer) to a float data type

### Variables Annotated by Type
* Optional
* Make codes easier to read
* Help find error in during compilation
~~~python
import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}
~~~